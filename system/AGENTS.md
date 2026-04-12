# Knowledge Wiki Agent Rules

1. Prefer compiled wiki pages over raw sources when answering questions.
2. Query by reading `wiki/index.md` first, then opening the most relevant wiki pages.
3. Do not write directly to canonical wiki pages outside the review workflow.
4. Every synthesized section should carry stable source tokens such as `[source:ml-notes#overview]`.
5. Publishing generated pages must update the wiki index, graph, and system log together.
6. Preserve raw sources as immutable inputs.
