# DOX tree convention

DOX remains a Markdown-first `AGENTS.md` framework. This convention is optional: it gives teams and tooling a small, machine-checkable shape without changing the copy-paste install path.

## Goals

- Keep the root `AGENTS.md` useful to humans and agents.
- Let repositories define local contracts close to the files they govern.
- Make child indexes checkable without requiring a package, database, service, or generated lockfile.
- Catch stale child indexes, missing child docs, and accidental deletion of the root framework block.

## Non-goals

- No heavy schema for all prose content.
- No mandatory runtime dependency.
- No central registry.
- No requirement that every folder has an `AGENTS.md`.
- No attempt to prove that a doc is semantically complete.

## Required shape

A repository that opts into this machine-checkable convention must have a root `AGENTS.md`.

The root `AGENTS.md` must contain:

1. A protected framework block, delimited by:
   - `<!-- DOX-CORE-START: ... -->`
   - `<!-- DOX-CORE-END: ... -->`
2. A `## Child DOX Index` section.
3. One bullet per direct child DOX file, using this form:

```markdown
- `path/to/AGENTS.md` — short description of the child scope.
```

Child `AGENTS.md` files must use this section order:

1. `# <scope name>`
2. `## Purpose`
3. `## Ownership`
4. `## Local Contracts`
5. `## Work Guidance`
6. `## Verification`
7. `## Child DOX Index`

A child index may say `No child DOX files yet.` when the scope has no nested DOX files.

## Parent-child rules

- A parent index entry must point to an existing `AGENTS.md` file.
- A child `AGENTS.md` must be inside the parent's subtree.
- A child may make local rules more specific, but must not weaken the root DOX contract.
- Parent docs should describe broad ownership. Child docs should hold concrete local rules.

## When to create a child AGENTS.md

Create one when a folder becomes a durable boundary with its own:

- purpose or product surface
- ownership/responsibility split
- local contracts or side effects
- workflow or verification rules
- durable assets, source materials, or generated outputs

Do not create child docs for temporary scratch folders or one-off files.

## Validation

This fork includes a small reference validator:

```bash
python3 scripts/dox_lint.py .
```

The validator checks:

- root `AGENTS.md` exists
- protected root DOX markers exist and are ordered correctly
- every `AGENTS.md` has a `## Child DOX Index`
- every child-index bullet pointing to an `AGENTS.md` resolves to a real file
- every non-root `AGENTS.md` includes the required child section set

Validation is intentionally structural. It cannot prove the prose is correct.

## Example

```text
repo/
  AGENTS.md
  backend/
    AGENTS.md
  frontend/
    AGENTS.md
  scripts/
    AGENTS.md
```

Root index:

```markdown
## Child DOX Index

- `backend/AGENTS.md` — API, persistence, jobs, and backend verification rules.
- `frontend/AGENTS.md` — UI, routing, design-system, and browser verification rules.
- `scripts/AGENTS.md` — maintenance scripts and operational checks.
```
