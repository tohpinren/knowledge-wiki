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
- `AGENTS.md` → rules for LLM behavior
- `index.md` → page directory
- `log.md` → history of updates

Ensures consistency as the wiki grows.

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
- LLM reads relevant pages and synthesizes answers across them
- raw sources are only used if the wiki is incomplete

Typical flow:
1. LLM reads `index.md` to locate relevant pages
2. LLM reads selected pages from `/wiki`
3. LLM synthesizes an answer

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

## Long-Term Vision

A system where:
- knowledge is structured, not scattered
- insights compound over time
- everything I’ve learned remains accessible

> a maintained, queryable representation of what I know
