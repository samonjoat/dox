# Scripts DOX

## Purpose

Owns optional local tooling for checking or maintaining DOX structure.

## Ownership

- `dox_lint.py` validates the structural DOX convention without external dependencies.

## Local Contracts

- Scripts must run with Python standard library only unless the README and this file explicitly document a dependency.
- Scripts must not modify repository files unless their name and help text clearly identify them as fixers.
- Validation output must be deterministic and CI-friendly.

## Work Guidance

- Prefer explicit error messages with file paths.
- Keep checks structural; do not pretend to validate whether prose is semantically complete.

## Verification

- Run `python3 scripts/dox_lint.py .` from the repository root.

## Child DOX Index

No child DOX files yet.
