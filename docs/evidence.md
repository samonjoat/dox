# DOX evidence notes

This page records reported evidence and caveats. It is not a benchmark certificate.

## Reported external observation

GitHub issue #3 reported an analysis of 9,911 Claude Code session logs comparing sessions with custom agent rulesets such as `AGENTS.md`/DOX against sessions without them.

Reported figures:

| Metric | With DOX / AGENTS.md | Without DOX / AGENTS.md | Reported difference |
|---|---:|---:|---:|
| Average human turns per session | 4.87 | 1.66 | +193% |
| Average prompt input tokens | 73,097.8 | 16,537.6 | Larger context navigation |
| Average tool errors per session | 0.68 | 0.37 | Higher, not automatically better |
| Average API cost per session | $10.48 | $2.09 | Higher, not automatically better |

## Interpretation boundaries

The data suggests that structured agent instructions may correlate with longer, deeper agent sessions. It does not, by itself, prove that DOX causes better outcomes.

Important caveats:

- Longer sessions can mean harder tasks, better persistence, or inefficient loops.
- Higher token use and cost can mean deeper work, or waste.
- Higher tool errors are not inherently positive.
- Public issue text does not provide raw data, sampling rules, or reproducible analysis.
- `AGENTS.md` usage may correlate with more sophisticated users or larger repositories.

## Responsible claim

Safe wording:

> DOX gives agents a durable local context structure. Third-party users have reported longer and deeper agent sessions with AGENTS.md-style rulesets, but those reports should be treated as observational rather than causal proof.

Avoid wording like:

> DOX proves agents are 193% better.

That claim is not supported by the available public evidence.
