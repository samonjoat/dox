# DOX orchestrator agent template

## Purpose

Coordinate DOX maintenance across a repository without letting one agent mutate the whole tree blindly.

The orchestrator scans candidate paths, selects the paths that may affect durable documentation, delegates one path at a time to a documenter agent, collects compact results, and reports the final DOX maintenance summary.

## Inputs

- Repository root path.
- Changed paths, selected paths, or a user request such as `Initialize DOX tree for this project now.`
- Access to a documenter subagent or an equivalent isolated worker.

## Workflow

1. Read root `AGENTS.md`.
2. Build a concise repository map, excluding generated/vendor/cache folders such as `.git/`, `node_modules/`, `.venv/`, `dist/`, `build/`, and coverage outputs.
3. Identify candidate files or directories that may affect durable project structure, ownership, contracts, workflows, verification, or child indexes.
4. For each candidate path, launch a documenter worker with:
   - repository root
   - absolute or root-relative target path
   - the current DOX chain that applies to that path, if already known
5. Require the documenter to return one result line:

```text
PATH <path> | ACTION <updated|created|skipped|error> | DOX <path|none> | DETAIL <brief reason>
```

6. Continue after errors, but include them in the final report.
7. After all workers finish, run the available DOX validation command if one exists.
8. Report:
   - total paths processed
   - updated/created/skipped/error counts
   - `AGENTS.md` files touched
   - validation result

## Constraints

- Do not edit source files. The orchestrator coordinates documentation only.
- Prefer changed paths over a full repository scan when the caller provides a diff.
- Do not create child `AGENTS.md` files for temporary or generated folders.
- Do not weaken the protected root DOX framework block.
- Keep final output short enough for a caller to act on.

## Adapter notes

Different agent harnesses expose different tool names:

| Capability | Examples |
|---|---|
| Spawn worker | `task`, `delegate_task`, subagent, child process |
| Ask user | `question`, `clarify`, chat prompt |
| Read file | `read`, `read_file`, filesystem tool |
| Run command | `bash`, `terminal`, shell tool |

Use the capability, not the literal tool name, unless you are writing for one specific harness.
