# DOX documenter agent template

## Purpose

Inspect one target path and update the nearest owning `AGENTS.md` only when DOX requires a durable documentation change.

## Inputs

- Repository root path.
- One target file or directory path.
- Optional changed-file diff or summary from the caller.

## Workflow

1. Read the root `AGENTS.md`.
2. Walk from the repository root to the target path.
3. Read every `AGENTS.md` on that route.
4. Use the nearest `AGENTS.md` as the local contract and parent docs for broader rules.
5. Inspect the target path enough to understand whether it changes:
   - purpose, scope, ownership, or responsibilities
   - durable structure, contracts, workflows, or operating rules
   - required inputs, outputs, permissions, constraints, side effects, or artifacts
   - verification or quality expectations
   - child `AGENTS.md` index contents
6. If the target creates a durable boundary, create a child `AGENTS.md` with the standard section shape.
7. If the nearest owning doc is stale, update it concisely.
8. If no durable contract changed, leave docs untouched.
9. Return exactly one result line:

```text
PATH <path> | ACTION <updated|created|skipped|error> | DOX <path|none> | DETAIL <brief reason>
```

## Constraints

- Edit only `AGENTS.md` files.
- Do not edit source files, README prose, specs, or scripts unless the caller explicitly assigned that documentation file as the target.
- Do not weaken or remove the protected root DOX framework block.
- Do not duplicate broad parent rules in child docs.
- Delete stale contradictions instead of preserving historical notes.
- Keep `DETAIL` under 100 characters.

## Decision guide

Update docs when the answer is yes:

- Would a future agent need to know this to edit safely?
- Did ownership, workflow, verification, side effects, or durable structure change?
- Did a parent child-index become wrong?
- Did a new folder become a stable boundary?

Skip docs when the answer is yes:

- Is this a one-off content edit with no durable process impact?
- Is the target generated, cached, vendored, or temporary?
- Is the existing `AGENTS.md` already accurate?

## Example results

```text
PATH src/api/server.py | ACTION updated | DOX src/api/AGENTS.md | DETAIL added streaming endpoint contract
PATH docs/spec.md | ACTION skipped | DOX docs/AGENTS.md | DETAIL existing docs contract already covers spec prose
PATH src/payments | ACTION created | DOX src/payments/AGENTS.md | DETAIL new durable payment boundary
PATH missing.py | ACTION error | DOX none | DETAIL target path not found
```
