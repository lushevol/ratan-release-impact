---
type: concept
title: PostgreSQL Query Lifecycle
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, query-lifecycle, parser, planner, executor]
related: [postgresql, explain, postgresql-explain-plan-reading, pg-hint-plan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/PostgreSQL Explain.md"]
---
# PostgreSQL Query Lifecycle

PostgreSQL processes a SQL statement through a sequence of representations and execution stages. Understanding the stage at which a problem arises helps separate syntax, semantics, rewrite behavior, planning estimates, and runtime execution.

## Stages

1. **Parser:** Converts SQL text into a parse tree and performs grammar validation. The source identifies `SelectStmt` as a representative parse-tree structure.
2. **Analyzer:** Performs semantic analysis, resolves names and expressions, and converts the parse tree into a `Query` tree.
3. **Rewriter:** Applies rules stored in PostgreSQL's rule system, including transformations associated with views.
4. **Planner:** Converts the `Query` tree into a cost-based plan tree headed by `PlannedStmt`. Core PostgreSQL does not provide native optimizer hints; [[pg-hint-plan]] is an extension that adds hint-like behavior.
5. **Executor:** Requests tuples through the plan nodes and accesses tables and indexes through the buffer manager. It may use `temp_buffers`, `work_mem`, and temporary files.

## Diagnostic implication

The SQL text received by the database is not necessarily the same representation that reaches planning or execution. `EXPLAIN` reveals the selected plan, while `EXPLAIN (ANALYZE, BUFFERS)` provides measured execution and buffer information when used in an appropriate test environment.

The executor is demand-driven: upper plan nodes request tuples from child nodes. Describing execution simply as proceeding from the bottom of the plan tree to the root is a useful intuition for a single-table plan, but it is not a universal execution-order rule.

## Relevance to Cash Settlement

Recurring slow SQL in Cash Settlement is often associated with PostgreSQL access paths and planner decisions. The lifecycle provides the framework for investigating whether the cause is query shape, rewrite behavior, inaccurate estimates, unsuitable scan selection, memory pressure, or runtime I/O.

See [[postgresql-sequential-scan-triage]] for operational triage and [[lifecycle-precheck-database-performance]] for an application-specific performance context.