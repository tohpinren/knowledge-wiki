# Knowledge Wiki

A long-term, LLM-maintained knowledge system built from my university notes, projects, and readings.

Inspired by Andrej Karpathy’s idea on “LLM Wikis”:
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

---

## Motivation

Over the past few years, I’ve accumulated a large amount of material:
- lecture slides (PDFs)
- assignments and reports
- Notion notes
- project work (especially FYP)

All of this is currently scattered and poorly connected. After graduation, I know I won’t realistically revisit or reuse most of it in its current form.

This project is an attempt to:
- preserve what I’ve learned
- make it actually usable in the future
- turn fragmented notes into structured knowledge

---

## Idea

Instead of treating documents as something to retrieve from (RAG), this system **compiles them into a persistent wiki**.

Core idea:
> Use an LLM to incrementally build and maintain a structured, interlinked knowledge base from raw sources.

- sources are read and integrated once
- knowledge is stored as structured markdown pages
- connections and synthesis are preserved over time

The wiki becomes a **compounding artifact**:
- more sources → richer structure
- more queries → more useful pages
- more links → easier navigation

---

## Goals

### Long-term retention
Keep everything I’ve learned in a form that is still usable years later.

### Structured knowledge (not notes)
- unify concepts across courses
- remove duplication
- make relationships explicit

### Queryable system
Be able to ask:
- how does X work?
- where did I use Y?
- compare A vs B across courses/projects

### Practical reuse
Serve as a reference for:
- system design
- ML concepts
- databases / infra
- past project decisions

---

## Architecture

### Raw sources (`/raw`)
- PDFs, notes, assignments, reports
- immutable
- source of truth

---

### Wiki (`/wiki`)
LLM-generated markdown pages:
- concepts
- courses
- projects
- syntheses

This is the main interface for knowledge.

---

### System (`/system`)
- canonical policy and lightweight state
- manifests, layouts, evidence, graph, metrics, and logs live here
- only a small subset belongs in git

This keeps the published wiki readable while still giving the tooling a place for operational metadata.

---

## Workflow

### Ingest
- add source to `/raw`
- LLM reads and integrates it into the wiki
- updates multiple pages and links

---

### Query (LLM Interface)

The LLM is the primary interface for interacting with the wiki.

- questions are answered using `/wiki`, not raw documents
- the index is the navigation layer for locating relevant pages
- LLM reads full relevant wiki pages and synthesizes answers across them
- if the published wiki does not contain enough information, query says so instead of falling back to raw sources

Typical flow:
1. LLM reads `index.md` to locate relevant pages
2. LLM reads selected pages from `/wiki`
3. LLM synthesizes an answer
4. LLM may suggest a reusable synthesis page, but does not auto-save it

---

### Write-back (Knowledge Compounding)

High-value outputs from queries are persisted back into the wiki.

Examples:
- comparisons across courses/projects
- summaries and abstractions
- insights discovered during querying

Workflow:
1. ask a question
2. LLM generates an answer
3. decide if the answer is worth keeping
4. save it as a new page (e.g. `/wiki/syntheses/`)

Both ingested sources and generated insights become part of the knowledge base.

---

### Lint
- detect contradictions
- find missing concepts/pages
- suggest new connections or sources

---

## Why not just RAG?

RAG:
- retrieves raw fragments
- recomputes synthesis every time

This system:
- stores synthesized knowledge
- builds persistent structure
- improves over time instead of resetting per query

The LLM operates over **compiled knowledge (wiki)** rather than raw documents.

---

## Tools

- Obsidian (navigation + visualization)
- LLM agent (query + maintenance)
- Markdown + Git (storage)

---

## Status

Initial setup. Starting with:
- exporting existing notes
- ingesting course-by-course
- defining schema

---

## Current Scaffold

The repository now includes a working v1 base implementation:

- `raw/` for immutable source material
- `wiki/` for canonical markdown pages and generated index
- `system/` for rules, manifests, review artifacts, graph data, metrics, and logs
- `system/graph/` for the internal knowledge graph and report
- `src/knowledge_wiki/` for the Python package
- `tests/` for unit, integration, and acceptance coverage

Implemented workflows:

- recursive course ingest from directories like `raw/Y1S1/CS1231S`
- per-file source manifests and evidence artifacts
- provider-side PDF and Office file upload for extraction when an OpenAI-compatible provider is configured
- LLM-planned course layouts under `system/reviews/layouts/`
- layout approval auto-publishes canonical course pages
- feedback-driven layout revision via reprompt
- post-publish page revision via `revise-page`
- wiki-first query via structured index + full page reading
- optional synthesis suggestions from query output
- internal graph sidecar for query expansion and lint
- semantic linting
- CLI entrypoint via `kwiki`
- optional Gradio UI for query and review
- repo-local Obsidian vault scaffold under `.obsidian/`

---

## Git Boundary

This private repo tracks the software and the published wiki, not the raw source dump or every generated runtime artifact.

Tracked:

- `src/`, `tests/`, `README.md`, `pyproject.toml`, `uv.lock`, `.env.example`
- shared `.obsidian/` config
- canonical wiki pages under `wiki/`
- minimal `system/` state such as `AGENTS.md`, README files, and module manifests

Ignored:

- `raw/` source files
- `personal/` notes
- generated `system/evidence/`, `system/reviews/`, `system/metrics/`, `system/manifests/sources/`
- generated `system/index.md`, `system/log.md`, and graph payloads
- local workspace files such as `.obsidian/workspace.json`

---

## Quick Start

Install the package in editable mode:

```bash
pip install -e .
```

Create a repo-local `.env` from the example and set your provider settings:

```bash
cp .env.example .env
```

Then edit `.env`:

```dotenv
GEMINI_API_KEY=...
KWIKI_INGEST_PROVIDER=gemini
KWIKI_INGEST_MODEL=gemini-2.5-flash-lite
KWIKI_QA_PROVIDER=gemini
KWIKI_QA_MODEL=gemini-2.5-flash
KWIKI_INGEST_CONCURRENCY=4
```

`Settings.from_root()` now loads `.env` automatically, so this is the main place to change providers and models.

Open the repository root in Obsidian, not just `wiki/`. The bootstrap now creates a minimal `.obsidian/` vault config and uses `raw/assets/` for downloaded attachments.

Provider/model selection is split by task:

- ingest uses `KWIKI_INGEST_PROVIDER` and `KWIKI_INGEST_MODEL`
- query/revision uses `KWIKI_QA_PROVIDER` and `KWIKI_QA_MODEL`
- `KWIKI_PROVIDER` and `KWIKI_MODEL` still work as global fallbacks for backward compatibility

The default configuration now assumes Gemini:

- ingest defaults to `gemini` + `gemini-2.5-flash-lite`
- Q&A defaults to `gemini` + `gemini-2.5-flash`
- `KWIKI_INGEST_CONCURRENCY` defaults to `4`

To switch either path back to OpenAI, set the task-specific provider/model and provide `OPENAI_API_KEY`:

```dotenv
KWIKI_INGEST_PROVIDER=openai_compatible
KWIKI_INGEST_MODEL=gpt-5.4-mini
KWIKI_QA_PROVIDER=openai_compatible
KWIKI_QA_MODEL=gpt-5.4-mini
OPENAI_API_KEY=...
```

Ingest prefers the configured provider, with bounded retries and timeouts:

- supported files are sent to the configured ingest provider when file inputs are available
- PDF and Office extraction can fall back locally when provider-side extraction fails
- completed per-file extraction results are persisted incrementally during course ingest

Create the scaffold if needed:

```bash
kwiki init
```

Put a course under `raw/`, for example:

```text
raw/
  Y1S1/
    CS1231S/
      lectures/
      tutorials/
      labs/
```

Run a recursive course ingest:

```bash
kwiki ingest-course raw/Y1S1/CS1231S
```

Ingest extraction and page drafting run in parallel with bounded concurrency controlled by `KWIKI_INGEST_CONCURRENCY`.

Inspect and approve the planned layout:

```bash
kwiki layouts
kwiki approve-layout layout-y1s1-cs1231s-<batch>
```

If the layout is wrong, revise it with feedback instead of starting from scratch:

```bash
kwiki revise-layout layout-y1s1-cs1231s-<batch> --feedback "Split the topic tree more clearly and keep proofs separate from worked artifacts."
```

Approving the layout publishes the canonical pages immediately:

```bash
kwiki approve-layout layout-y1s1-cs1231s-<batch>
```

If a published page needs another pass:

```bash
kwiki revise-page wiki/courses/y1s1/cs1231s/topics/core-concepts.md --feedback "Be more concise and keep only the most reusable ideas."
```

Published pages land under:

```text
wiki/courses/y1s1/cs1231s/
  index.md
  topics/
```

Ask a question against the published wiki:

```bash
kwiki query "How does normalization compare across courses?"
```

Run lint:

```bash
kwiki lint
```

Launch the local review UI:

```bash
pip install .[ui]
kwiki ui
```

---

## Long-Term Vision

A system where:
- knowledge is structured, not scattered
- insights compound over time
- everything I’ve learned remains accessible

> a maintained, queryable representation of what I know
