# GitHub automation DOX

## Purpose

Owns GitHub-native automation for this repository.

## Ownership

- `workflows/dox-lint.yml` runs the optional DOX structural validator in GitHub Actions.

## Local Contracts

- Workflows must use repository-local scripts where possible.
- CI must not require secrets for documentation validation.
- Workflow names should describe the check they run.

## Work Guidance

- Keep workflow permissions minimal.
- Prefer standard GitHub-hosted runners and stock actions for portability.

## Verification

- Run `python3 scripts/dox_lint.py .` locally before relying on the workflow.

## Child DOX Index

No child DOX files yet.
