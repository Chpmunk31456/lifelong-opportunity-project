# Portuguese Localization Helper — pt-BR

## Mission
Produce a complete, natural professional Brazilian Portuguese edition from the frozen English source while preserving controlled meaning.

## Required inputs
- Frozen English source and freeze record.
- Project terminology rules/glossary.
- English traceability/evidence records.

## Required checks
- Complete section, heading, list, table, warning, link, citation, number, date, and callout parity.
- Natural pt-BR terminology and grammar.
- Preserve product names, standards, identifiers, URLs, commands, code, file paths, and formal credential names unless an established localized name is documented.
- Preserve legal/jurisdictional caveats and non-guarantee language.
- Check untranslated English leakage except proper nouns/technical terms.
- Check numeric/date/currency/unit fidelity.

## Required output
Create the pt-BR working master plus a Portuguese localization/parity QA record documenting source commit, terminology decisions, parity checks, unresolved ambiguities, and status.

## PASS conditions
PASS only when the Portuguese edition is complete, structurally faithful, meaning-preserving, and has no unresolved material translation ambiguity.

## Blocking conditions
- Missing content or warning.
- Changed numeric/date/legal meaning.
- Translation implies certification, guarantee, licensing transferability, or availability not present in English.
