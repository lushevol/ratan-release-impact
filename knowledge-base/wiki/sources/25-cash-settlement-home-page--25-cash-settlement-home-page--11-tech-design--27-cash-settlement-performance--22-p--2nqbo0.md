---
type: source
title: PostgreSQL Explain and Query Performance
authors: []
year: 2025
url: ""
venue: "Cash Settlement technical design"
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, explain, query-performance, cash-settlement, query-planner]
related: [postgresql, explain, postgresql-query-lifecycle, postgresql-explain-plan-reading, postgresql-index-bitmap-sequential-scan-selection, postgresql-sequential-scan-triage, pg-hint-plan, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/PostgreSQL Explain.md"]
---
# PostgreSQL Explain and Query Performance

## Scope

This internal technical design document introduces PostgreSQL query planning and `EXPLAIN` output in the context of recurring slow SQL in the Cash Settlement production environment. It covers the query lifecycle, planner cost estimates, scan strategies, memory settings, and practical plan-reading guidance.

The document is useful as architectural and diagnostic guidance. Its empirical scan-selection results come from a Ratan DEV test and must not be treated as universal PostgreSQL thresholds.

## PostgreSQL query lifecycle

The document describes five stages:

1. **Parser:** Converts SQL text into a parse tree and validates grammar.
2. **Analyzer:** Performs semantic analysis and produces a `Query` tree.
3. **Rewriter:** Applies PostgreSQL rules, including view-related transformations.
4. **Planner:** Converts the query tree into a cost-based `Plan` tree.
5. **Executor:** Executes the selected plan through table, index, buffer-manager, memory, and temporary-file operations.

The source identifies the following PostgreSQL structures.

```cpp
typedef struct SelectStmt
{
        NodeTag         type;

        /*
         * These fields are used only in "leaf" SelectStmts.
         */
        List       *distinctClause;     /* NULL, list of DISTINCT ON exprs, or
                                         * lcons(NIL,NIL) for all (SELECT DISTINCT) */
        IntoClause *intoClause;         /* target for SELECT INTO */
        List       *targetList;         /* the target list (of ResTarget) */
        List       *fromClause;         /* the FROM clause */
        Node       *whereClause;        /* WHERE qualification */
        List       *groupClause;        /* GROUP BY clauses */
        List       *havingClause;       /* HAVING conditional-expression */
        List       *windowClause;       /* WINDOW window_name AS (...), ... */

        /*
         * In a "leaf" node representing a VALUES list, the above fields are all
         * null, and instead this field is set.  Note that the elements of the
         * sublists are just expressions, without ResTarget decoration. Also note
         * that a list element can be DEFAULT (represented by a SetToDefault node),
         * regardless of the context of the VALUES list. It's up to parse analysis
         * to reject that where not valid.
         */
        List       *valuesLists;        /* untransformed list of expression lists */

        /*
         * These fields are used in both "leaf" SelectStmts and upper-level
         * SelectStmts.
         */
        List       *sortClause;         /* sort clause (a list of SortBy's) */
        Node       *limitOffset;        /* # of result tuples to skip */
        Node       *limitCount;         /* # of result tuples to return */
        List       *lockingClause;      /* FOR UPDATE (list of LockingClause's) */
        WithClause *withClause;         /* WITH list */

        /*
         * These fields are used only in upper-level SelectStmts.
         */
        SetOperation op;                /* type of set op */
        bool            all;            /* ALL specified? */
        struct SelectStmt *larg;        /* left child */
        struct SelectStmt *rarg;        /* right child */
        /* Eventually add fields for CORRESPONDING spec here */
} SelectStmt;
```

```cpp
typedef struct Query
{
	NodeTag		type;

	CmdType		commandType;	/* select|insert|update|delete|merge|utility */

	/* where did I come from? */
	QuerySource querySource pg_node_attr(query_jumble_ignore);

	uint64		queryId pg_node_attr(equal_ignore, query_jumble_ignore, read_write_ignore, read_as(0));

	bool		canSetTag pg_node_attr(query_jumble_ignore);

	Node	   *utilityStmt;

	int			resultRelation pg_node_attr(query_jumble_ignore);

	bool		hasAggs pg_node_attr(query_jumble_ignore);
	bool		hasWindowFuncs pg_node_attr(query_jumble_ignore);
	bool		hasTargetSRFs pg_node_attr(query_jumble_ignore);
	bool		hasSubLinks pg_node_attr(query_jumble_ignore);
	bool		hasDistinctOn pg_node_attr(query_jumble_ignore);
	bool		hasRecursive pg_node_attr(query_jumble_ignore);
	bool		hasModifyingCTE pg_node_attr(query_jumble_ignore);
	bool		hasForUpdate pg_node_attr(query_jumble_ignore);
	bool		hasRowSecurity pg_node_attr(query_jumble_ignore);
	bool		isReturn pg_node_attr(query_jumble_ignore);

	List	   *cteList;
	List	   *rtable;
	List	   *rteperminfos;
	FromExpr   *jointree;
	List	   *mergeActionList;
	bool		mergeUseOuterJoin;
	List	   *targetList;
	OverridingKind override;
	OnConflictExpr *onConflict;
	List	   *returningList;
	List	   *groupClause;
	bool		groupDistinct;
	List	   *groupingSets;
	Node	   *havingQual;
	List	   *windowClause;
	List	   *distinctClause;
	List	   *sortClause;
	Node	   *limitOffset;
	Node	   *limitCount;
	LimitOption limitOption;
	List	   *rowMarks;
	Node	   *setOperations;
	List	   *constraintDeps;
	List	   *withCheckOptions;
	int			stmt_location;
	int			stmt_len pg_node_attr(query_jumble_ignore);
} Query;
```

```cpp
typedef struct PlannedStmt
{
	pg_node_attr(no_equal, no_query_jumble)

	NodeTag		type;

	CmdType		commandType;	/* select|insert|update|delete|merge|utility */

	uint64		queryId;		/* query identifier (copied from Query) */

	bool		hasReturning;
	bool		hasModifyingCTE;
	bool		canSetTag;
	bool		transientPlan;
	bool		dependsOnRole;
	bool		parallelModeNeeded;
	int			jitFlags;

	struct Plan *planTree;
	List	   *rtable;
	List	   *permInfos;
	List	   *resultRelations;
	List	   *appendRelations;
	List	   *subplans;
	Bitmapset  *rewindPlanIDs;
	List	   *rowMarks;
	List	   *relationOids;
	List	   *invalItems;
	List	   *paramExecTypes;
	Node	   *utilityStmt;
	int			stmt_location;
	int			stmt_len;
} PlannedStmt;
```

## Reading `EXPLAIN`

An `EXPLAIN` result is a tree of plan nodes. Each node reports a node type and planner estimates, commonly including:

- Startup cost
- Total cost
- Estimated output rows
- Additional properties such as `Index Cond`, `Filter`, and scan details

Startup cost represents work before the first tuple is returned. Run cost represents the work required to fetch all tuples. Total cost is startup cost plus run cost.

Planner costs are arbitrary relative units, conventionally based on disk-page fetches. They are not elapsed time, and they do not include client-side result transmission. A parent node's cost includes the costs of its child nodes. The `rows` value is the number of rows emitted by a node, not necessarily the number of rows physically scanned.

Plain `EXPLAIN` reports estimates. Production investigations should compare those estimates with actual execution using a controlled `EXPLAIN (ANALYZE, BUFFERS)` workflow, taking care because `ANALYZE` executes the statement.

## Scan strategies

- **Sequential scan:** Reads table pages and evaluates predicates against rows.
- **Index scan:** Uses an index to locate qualifying rows and fetches table tuples individually.
- **Bitmap index scan and bitmap heap scan:** Builds tuple locations from an index and fetches heap pages in physical order to reduce random I/O.
- **Sort:** Adds a plan node when the required ordering is not supplied by an existing access path.

A predicate shown as `Index Cond` constrains index-driven retrieval. A predicate shown as `Filter` is evaluated after candidate rows have been retrieved. A filter can reduce emitted rows without substantially reducing the scan work.

Bitmap structures can become lossy when they exceed available memory, retaining page-level rather than tuple-level information. PostgreSQL must then recheck conditions, which can increase CPU work and latency. This makes `work_mem` relevant to large bitmap scans.

## Cost parameters

The source lists these PostgreSQL planner defaults:

| Parameter | Default stated | Meaning |
|---|---:|---|
| `seq_page_cost` | `1.0` | Estimated cost of sequential page fetches |
| `random_page_cost` | `4.0` | Estimated cost of non-sequential page fetches |
| `cpu_tuple_cost` | `0.01` | Cost of processing each row |
| `cpu_index_tuple_cost` | `0.005` | Cost of processing each index entry |
| `cpu_operator_cost` | `0.0025` | Cost of evaluating an operator or function |
| `shared_buffers` | Not numerically specified | Shared database buffer memory |
| `temp_buffers` | Not numerically specified | Per-session temporary-table buffers |
| `work_mem` | Not numerically specified | Memory available to an individual query operation |

The source gives this sequential-scan estimate:

```text
run cost = cpu run cost + disk run cost
         = (cpu_tuple_cost + cpu_operator_cost) × N_tuple
           + seq_page_cost × N_page
```

It also gives this `tenk1` example:

```text
total cost = (358 × 1.0) + (10000 × 0.01)
           = 458
```

The numerical examples contain inconsistencies that require correction before operational use. In particular, one example uses `0.001` where the stated `cpu_tuple_cost` is `0.01`, and an index startup calculation uses `0.00025` where the stated `cpu_operator_cost` is `0.0025`.

## Ratan DEV empirical test

The test used:

```sql
select *
from cash_settlement_query_cn.cashflow_data
where created_at < '2024-02-27 08:35:40';
```

The table contained 124,635 records and had a B-tree index on `created_at`.

| Estimated or returned records | Approximate share of table | Observed plan |
|---:|---:|---|
| Less than 2,010 | Less than approximately 1.6% | Index scan |
| Approximately 2,006–17,161 | Approximately 1.6%–13.7% | Bitmap index scan / bitmap heap scan |
| More than 17,214 | More than approximately 13.8% | Sequential scan |

These observations are local to the tested table, data distribution, statistics, PostgreSQL configuration, hardware, cache state, and query shape. The approximately 13.8% transition must not be generalized as a PostgreSQL-wide rule.

## Practical guidance

- Inspect whether important predicates appear as `Index Cond` rather than only as `Filter`.
- Design indexes around actual query predicates, ordering, selectivity, write overhead, and column order; more indexed columns are not automatically better.
- Use an index whose order satisfies `ORDER BY` when that is beneficial and supported by the query shape.
- Use `LIMIT` when the application genuinely needs a bounded result set. Pair it with deterministic `ORDER BY` for stable results.
- Investigate `work_mem` and lossy bitmap behavior for large result sets.
- Compare estimated rows with actual rows and validate changes under representative volume, cache state, and concurrency.
- Treat the tested scan thresholds as workload-specific baselines.
- Distinguish core PostgreSQL, which has no native optimizer hints, from the external `pg_hint_plan` extension.

## References

- [PostgreSQL Documentation: Using EXPLAIN](https://www.postgresql.org/docs/14/using-explain.html)
- [PostgreSQL Documentation: EXPLAIN](https://www.postgresql.org/docs/14/sql-explain.html)
- [The Internals of PostgreSQL](https://www.interdb.jp/pg/pgsql03.html)
- [PostgreSQL planner cost constants](https://www.postgresql.org/docs/14/runtime-config-query.html)
- [Pg-Hint-Plan](https://pg-hint-plan.readthedocs.io/_/downloads/en/pg15/pdf/)
- [TidBitmap in PostgreSQL](https://blog.51cto.com/frankiewb/1603921)