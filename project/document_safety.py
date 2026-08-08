"""Repository-local safety checks for DOCX/OOXML processing.

The limits in this module were measured against the repository's publication
corpus. They are deliberately small enough to reject abusive packages while
remaining above every legitimate document observed during the Phase 3 review.
"""

from __future__ import annotations

import re
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit
from zipfile import BadZipFile, ZipFile

from lxml import etree


MAX_OOXML_FILE_BYTES = 1 * 1024 * 1024
MAX_ZIP_ENTRIES = 128
MAX_TOTAL_COMPRESSED_BYTES = 1 * 1024 * 1024
MAX_TOTAL_UNCOMPRESSED_BYTES = 8 * 1024 * 1024
MAX_PACKAGE_COMPRESSION_RATIO = 50
MAX_ENTRY_COMPRESSION_RATIO = 100
MAX_XML_PART_BYTES = 2 * 1024 * 1024

HYPERLINK_RELATIONSHIP_TYPE = (
    "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink"
)
RELATIONSHIP_NAMESPACE = (
    "http://schemas.openxmlformats.org/package/2006/relationships"
)
REQUIRED_DOCX_PARTS = {"[Content_Types].xml", "_rels/.rels", "word/document.xml"}
MACRO_CONTENT_TYPE_MARKERS = (
    b"application/vnd.ms-word.document.macroEnabled.main+xml",
    b"application/vnd.ms-word.template.macroEnabledTemplate.main+xml",
    b"application/vnd.ms-office.vbaProject",
)
DISALLOWED_RELATIONSHIP_TYPES = (
    "/oleObject",
    "/package",
)


class DocumentSafetyError(ValueError):
    """Raised when a document or path violates the repository safety policy."""


def resolve_repository_path(
    path: str | Path,
    repository_root: str | Path,
    *,
    allowed_extensions: set[str] | None = None,
    must_exist: bool = True,
    expect_directory: bool = False,
) -> Path:
    """Resolve a path and require its effective location to remain in the repository.

    ``strict=False`` permits new destination files and directories. Existing
    symlinks and Windows junctions/reparse points are resolved before the
    containment check. Empirical Windows reparse-point testing remains deferred
    until a suitable test environment is available.
    """

    root = Path(repository_root).resolve(strict=True)
    candidate = Path(path).expanduser()
    if not candidate.is_absolute():
        candidate = root / candidate
    resolved = candidate.resolve(strict=False)
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise DocumentSafetyError("Path resolves outside the repository root") from exc

    if allowed_extensions is not None:
        allowed = {extension.lower() for extension in allowed_extensions}
        if resolved.suffix.lower() not in allowed:
            raise DocumentSafetyError(
                "Unsupported file extension; allowed extensions: " + ", ".join(sorted(allowed))
            )
    if must_exist and not resolved.exists():
        raise DocumentSafetyError("Required repository path does not exist")
    if must_exist and expect_directory and not resolved.is_dir():
        raise DocumentSafetyError("Expected a directory")
    if must_exist and not expect_directory and not resolved.is_file():
        raise DocumentSafetyError("Expected a regular file")
    return resolved


def safe_xml_parser() -> etree.XMLParser:
    """Return an XML parser that does not load DTDs, entities, or network data."""

    return etree.XMLParser(
        resolve_entities=False,
        load_dtd=False,
        no_network=True,
        huge_tree=False,
        recover=False,
    )


def parse_xml_part(data: bytes, part_name: str) -> etree._Element:
    """Parse a size-bounded XML part using the repository's defensive settings."""

    if len(data) > MAX_XML_PART_BYTES:
        raise DocumentSafetyError(f"XML part exceeds the size limit: {part_name}")
    upper = data.upper()
    if b"<!DOCTYPE" in upper or b"<!ENTITY" in upper:
        raise DocumentSafetyError(f"DTD or entity declaration rejected: {part_name}")
    try:
        return etree.fromstring(data, parser=safe_xml_parser())
    except etree.XMLSyntaxError as exc:
        raise DocumentSafetyError(f"Invalid XML part: {part_name}") from exc


def _entry_ratio(uncompressed: int, compressed: int) -> float:
    if compressed:
        return uncompressed / compressed
    if uncompressed == 0:
        return 0.0
    raise DocumentSafetyError("Non-empty ZIP entry has zero compressed size")


def _validate_member_name(name: str) -> None:
    parts = PurePosixPath(name).parts
    if (
        not name
        or name.startswith(("/", "\\"))
        or "\\" in name
        or re.match(r"^[A-Za-z]:", name)
        or ".." in parts
    ):
        raise DocumentSafetyError("Unsafe archive member path")


def _validate_relationships(data: bytes, part_name: str) -> None:
    root = parse_xml_part(data, part_name)
    relationship_tag = f"{{{RELATIONSHIP_NAMESPACE}}}Relationship"
    for relationship in root.iter(relationship_tag):
        relationship_type = relationship.get("Type", "")
        if any(relationship_type.endswith(suffix) for suffix in DISALLOWED_RELATIONSHIP_TYPES):
            raise DocumentSafetyError("Embedded or externally attached OOXML content rejected")
        if relationship.get("TargetMode") != "External":
            continue
        target = relationship.get("Target", "")
        parsed = urlsplit(target)
        if (
            relationship_type != HYPERLINK_RELATIONSHIP_TYPE
            or parsed.scheme.lower() != "https"
            or not parsed.hostname
        ):
            raise DocumentSafetyError("Disallowed external OOXML relationship")


def validate_docx(path: str | Path) -> Path:
    """Validate a DOCX package before it is parsed, converted, or published."""

    document = Path(path)
    if document.suffix.lower() != ".docx":
        raise DocumentSafetyError("Only non-macro-enabled .docx input is allowed")
    if not document.is_file():
        raise DocumentSafetyError("DOCX input is not a regular file")
    if document.stat().st_size > MAX_OOXML_FILE_BYTES:
        raise DocumentSafetyError("DOCX file exceeds the size limit")

    try:
        with ZipFile(document, "r") as archive:
            entries = archive.infolist()
            if len(entries) > MAX_ZIP_ENTRIES:
                raise DocumentSafetyError("DOCX exceeds the ZIP entry-count limit")

            names = {entry.filename for entry in entries}
            if not REQUIRED_DOCX_PARTS.issubset(names):
                raise DocumentSafetyError("DOCX is missing required OOXML parts")

            total_compressed = sum(entry.compress_size for entry in entries)
            total_uncompressed = sum(entry.file_size for entry in entries)
            if total_compressed > MAX_TOTAL_COMPRESSED_BYTES:
                raise DocumentSafetyError("DOCX exceeds the compressed-size limit")
            if total_uncompressed > MAX_TOTAL_UNCOMPRESSED_BYTES:
                raise DocumentSafetyError("DOCX exceeds the uncompressed-size limit")
            if _entry_ratio(total_uncompressed, total_compressed) > MAX_PACKAGE_COMPRESSION_RATIO:
                raise DocumentSafetyError("DOCX exceeds the package compression-ratio limit")

            for entry in entries:
                _validate_member_name(entry.filename)
                if entry.flag_bits & 0x1:
                    raise DocumentSafetyError("Encrypted ZIP entries are not allowed")
                if _entry_ratio(entry.file_size, entry.compress_size) > MAX_ENTRY_COMPRESSION_RATIO:
                    raise DocumentSafetyError("DOCX entry exceeds the compression-ratio limit")

                lower_name = entry.filename.lower()
                if lower_name.endswith("vbaproject.bin"):
                    raise DocumentSafetyError("VBA content is not allowed")
                if lower_name.startswith("word/activex/"):
                    raise DocumentSafetyError("ActiveX content is not allowed")
                if lower_name.startswith("word/embeddings/"):
                    raise DocumentSafetyError("Embedded files or OLE objects are not allowed")
                if lower_name.startswith("customui/") or "/customui/" in lower_name:
                    raise DocumentSafetyError("Custom Office UI content is not allowed")

                if lower_name.endswith((".xml", ".rels")):
                    data = archive.read(entry)
                    parse_xml_part(data, entry.filename)
                    if lower_name.endswith(".rels"):
                        _validate_relationships(data, entry.filename)

            content_types = archive.read("[Content_Types].xml")
            if any(marker in content_types for marker in MACRO_CONTENT_TYPE_MARKERS):
                raise DocumentSafetyError("Macro-enabled OOXML content type is not allowed")
    except BadZipFile as exc:
        raise DocumentSafetyError("Invalid DOCX ZIP package") from exc

    return document
