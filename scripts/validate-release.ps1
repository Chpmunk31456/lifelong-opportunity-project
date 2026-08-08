$ErrorActionPreference = "Stop"

Write-Host "=== Lifelong Opportunity Release Validation ==="
Write-Host ""

$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Push-Location $RepoRoot

try {
    Write-Host "[1/6] Git status"
    git status --short
    if ($LASTEXITCODE -ne 0) {
        throw "git status failed"
    }

    Write-Host ""
    Write-Host "[2/6] Git whitespace check"
    git diff --check
    if ($LASTEXITCODE -ne 0) {
        throw "git diff --check failed"
    }

    Write-Host ""
    Write-Host "[3/6] Python syntax validation"

    $PythonFiles = @(
        "project\document_safety.py",
        "project\translate_missing_spanish.py",
        "project\translate_missing_ptbr.py",
        "project\qa-ptbr\render_docx.py"
    )

    foreach ($File in $PythonFiles) {
        if (-not (Test-Path $File)) {
            throw "Missing required file: $File"
        }

        python -m py_compile $File

        if ($LASTEXITCODE -ne 0) {
            throw "Python syntax validation failed: $File"
        }

        Write-Host "PASS: $File"
    }

    Write-Host ""
    Write-Host "[4/6] Required repository files"

    $RequiredFiles = @(
        "SECURITY.md",
        "SECURITY_CONTROLS.md",
        "RELEASE_SECURITY_CHECKLIST.md",
        "requirements.txt",
        "TOOL_VERSIONS.md",
        "project\document_safety.py"
    )

    foreach ($File in $RequiredFiles) {
        if (-not (Test-Path $File)) {
            throw "Missing required repository file: $File"
        }

        Write-Host "PASS: $File"
    }

    Write-Host ""
    Write-Host "[5/6] DOCX security validation"

    $PythonCode = @"
from pathlib import Path
import sys

repo = Path(r'''$RepoRoot''').resolve()
project = repo / "project"
sys.path.insert(0, str(project))

from document_safety import validate_docx

docx_files = sorted(repo.rglob("*.docx"))

passed = 0
failed = []

for path in docx_files:
    try:
        validate_docx(path)
        passed += 1
    except Exception as exc:
        failed.append((path, str(exc)))

print(f"DOCX discovered: {len(docx_files)}")
print(f"PASS: {passed}")
print(f"FAIL: {len(failed)}")

for path, error in failed:
    print(f"FAIL: {path.relative_to(repo)}")
    print(f"      {error}")

if failed:
    raise SystemExit(1)
"@

    # Do not pipe the Python program through stdin. On Windows PowerShell 5.1,
    # native-command stdin handling can terminate the surrounding script before
    # the next PowerShell statements execute. A temporary script keeps stdin
    # independent and guarantees that stage 6 is reached after Python returns.
    $TempPython = Join-Path ([System.IO.Path]::GetTempPath()) ("lifelong-validator-{0}.py" -f [guid]::NewGuid())

    try {
        Set-Content -LiteralPath $TempPython -Value $PythonCode -Encoding UTF8
        python $TempPython

        if ($LASTEXITCODE -ne 0) {
            throw "DOCX security validation failed"
        }
    }
    finally {
        Remove-Item -LiteralPath $TempPython -Force -ErrorAction SilentlyContinue
    }

    Write-Host ""
    Write-Host "[6/6] Repository completeness validation"

    $Guides = @(
        Get-ChildItem -Directory |
            Where-Object { $_.Name -match '^\d+-' }
    )

    if ($Guides.Count -ne 101) {
        throw "Expected 101 numbered guide folders (00-100), found $($Guides.Count)"
    }

    $GuideIds = @(
        $Guides | ForEach-Object {
            if ($_.Name -match '^(\d+)-') {
                [int]$matches[1]
            }
        }
    )

    $MissingGuideIds = @(0..100 | Where-Object { $_ -notin $GuideIds })

    if ($MissingGuideIds.Count -gt 0) {
        throw "Missing guide numbers: $($MissingGuideIds -join ', ')"
    }

    Write-Host "PASS: 101 numbered guides present (00-100)"

    $PairingErrors = @()

    foreach ($Guide in $Guides) {
        foreach ($Language in @('english','spanish','portuguese')) {
            $LanguagePath = Join-Path $Guide.FullName $Language

            if (-not (Test-Path $LanguagePath)) {
                continue
            }

            $DocxCount = @(
                Get-ChildItem $LanguagePath -Recurse -File -Filter *.docx -ErrorAction SilentlyContinue
            ).Count

            $PdfCount = @(
                Get-ChildItem $LanguagePath -Recurse -File -Filter *.pdf -ErrorAction SilentlyContinue
            ).Count

            $KnownException =
                ($Guide.Name -eq '70-travel-agent-and-travel-coordinator' -and
                 $Language -eq 'english' -and
                 $DocxCount -eq 0 -and
                 $PdfCount -eq 1) -or
                ($Guide.Name -eq '74-ecommerce-specialist-and-marketplace-coordinator' -and
                 $Language -eq 'english' -and
                 $DocxCount -eq 0 -and
                 $PdfCount -eq 1)

            if ($KnownException) {
                Write-Host "WARNING: Known missing English DOCX source: $($Guide.Name)"
            }
            elseif ($DocxCount -ne $PdfCount) {
                $PairingErrors += [PSCustomObject]@{
                    Guide    = $Guide.Name
                    Language = $Language
                    DOCX     = $DocxCount
                    PDF      = $PdfCount
                }
            }
        }
    }

    if ($PairingErrors.Count -gt 0) {
        $PairingErrors | Format-Table -AutoSize
        throw "Unexpected DOCX/PDF pairing defects found"
    }

    $MissingSpanish = @(
        $Guides | Where-Object {
            -not (Test-Path (Join-Path $_.FullName 'spanish'))
        }
    )

    Write-Host "Spanish folders present: $(101 - $MissingSpanish.Count)"

    if ($MissingSpanish.Count -gt 0) {
        Write-Host "WARNING: Missing Spanish folders: $($MissingSpanish.Count)"

        foreach ($Guide in $MissingSpanish) {
            Write-Host "WARNING: Missing Spanish: $($Guide.Name)"
        }
    }
    else {
        Write-Host "PASS: Missing Spanish folders: 0"
    }

    Write-Host "PASS: No unexpected DOCX/PDF pairing defects found"
    Write-Host "RELEASE BASELINE VALIDATION PASSED"
    Write-Host "No files were committed or pushed."
    Write-Host "============================================"
}
finally {
    Pop-Location
}
