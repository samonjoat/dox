# Docs DOX

## Purpose

Owns human-readable DOX specifications, validation conventions, and evidence notes.

## Ownership

- `spec.md` defines the optional machine-checkable convention for DOX trees.
- `evidence.md` records claims, caveats, and interpretation boundaries for reported DOX outcomes.

## Local Contracts

- Keep DOX Markdown-first. Specs may define optional validation, but must not imply users need a package or service to use DOX.
- Separate normative requirements from recommendations and examples.
- Evidence notes must distinguish reported third-party observations from verified guarantees.

## Work Guidance

- Prefer short, operational sections over broad essays.
- Use RFC-style words only when useful: required, recommended, optional.
- Do not overclaim empirical impact without methodology, raw data, or reproducible analysis.

## Verification

- Run `python3 scripts/dox_lint.py .` from the repository root after changing docs structure or child indexes.

## Child DOX Index

No child DOX files yet.
