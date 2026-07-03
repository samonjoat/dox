# Tests DOX

## Purpose

Owns regression tests for optional DOX tooling.

## Ownership

- `test_dox_lint.py` verifies structural validator behavior and edge cases.

## Local Contracts

- Tests must use Python standard library only.
- Tests should build temporary repositories rather than mutating the real repository.
- Each bug fixed from review feedback should get a focused regression test when practical.

## Work Guidance

- Keep fixtures small and explicit.
- Test validator semantics, not Markdown rendering.

## Verification

- Run `python3 -m unittest discover -s tests` from the repository root.
- Run `python3 scripts/dox_lint.py .` from the repository root.

## Child DOX Index

No child DOX files yet.
