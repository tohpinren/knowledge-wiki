# System

Operational metadata for the knowledge wiki lives here. This directory mixes canonical policy files with generated runtime state, so only a small subset should be tracked in git.

Tracked:

- `AGENTS.md` defines maintenance rules
- `README.md` files document the layout
- `manifests/modules/` stores lightweight module-level state

Generated and typically untracked:

- `index.md` summarizes runtime state
- `log.md` records workflow events
- `manifests/sources/` stores per-source ingest state
- `evidence/` stores per-file evidence summaries
- `reviews/` stores layout reviews and internal generated publish plans
- `graph/` stores graph payloads and reports
- `metrics/` stores usage and cost accounting
- `cache/` stores transient artifacts
