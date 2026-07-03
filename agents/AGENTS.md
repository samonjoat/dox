# Agent templates DOX

## Purpose

Owns reusable agent prompt templates for maintaining DOX trees.

## Ownership

- `orchestrator.md` describes the coordination role for scanning candidate files and delegating documentation work.
- `documenter.md` describes the focused role for inspecting one path and updating the nearest owning `AGENTS.md` when required.

## Local Contracts

- Templates must remain harness-portable. Name common capabilities instead of hard-coding one tool stack unless a section is explicitly adapter-specific.
- Templates must not require DOX users to install a runtime.
- Documenter guidance may edit `AGENTS.md` files only; source-file edits belong to the caller's coding agent.

## Work Guidance

- Keep outputs concise and deterministic so orchestrators can parse them.
- Include adapter notes for Codex, Claude Code, OpenCode, and Hermes-style subagents only as examples.

## Verification

- Run `python3 scripts/dox_lint.py .` after changing this folder or its child index.

## Child DOX Index

No child DOX files yet.
