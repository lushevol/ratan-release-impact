---
type: source
title: Cashflow Data Provider Query with Multiple Versions
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow-data, query-performance, multi-version-query, performance-test]
related: [cashflow-data-provider, cashflow-data, cashflow-data-history, multi-version-cashflow-query, cashflow-data-provider-query-performance, cash-settlement-performance-and-stress-testing, what-is-the-performance-scaling-behaviour-of-the-multi-version-cashflow-query]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume/Cashflow data provider query with multiple versions.md"]
---
# Cashflow Data Provider Query with Multiple Versions

## Summary

This performance test note evaluates a cashflow data provider query against multiple versions of cashflow data at two reported volumes. The test records a runtime of `55s` for `uat1` at `42w` and `133s` for `fmrp1` at `120w`.

The source does not define the units of `w`, the exact meaning of `cost`, the query or schema, the indexing strategy, the version-selection logic, the environment configuration, the concurrency level, or the acceptance threshold. The results should therefore be treated as environment- and workload-specific observations rather than as a general performance guarantee.

## Recorded Test Results

The following table is preserved from the source document:

```text
| env | count | cost | comments |
| --- | --- | --- | --- |
| uat1 | 42w | 55s | ![image-2026-4-8_11-33-4.png](attachments/image-2026-4-8_11-33-4.png) |
| fmrp1 | 120w | 133s | ![image-2026-4-9_10-27-20.png](attachments/image-2026-4-9_10-27-20.png) |
```

The source references two attachments:

- `attachments/image-2026-4-8_11-33-4.png`
- `attachments/image-2026-4-9_10-27-20.png`

Their contents are not available in the supplied source text.

## Observations

- The `fmrp1` test has both a larger reported count and a longer reported runtime than the `uat1` test.
- The reported runtime increases from `55s` to `133s`, approximately `2.42×`.
- The reported count increases from `42w` to `120w`, approximately `2.86×`.
- The two tests do not isolate volume from environment because `uat1` and `fmrp1` were tested at different counts.
- The measurements are insufficient to establish linear or nonlinear scaling behavior.
- The source does not state whether `cost` is wall-clock duration, database execution time, end-to-end latency, or another metric.

## Evidence Boundaries

These measurements apply only to the tested cashflow data provider query in the named environments. They should not be transferred directly to [[entities/cashflowsnew]], [[entities/ultra-cashflow-query]], [[entities/legacy-cashflow-query]], [[entities/cashflow-blotter]], or the general [[entities/query-service]] without evidence that those systems use the same query path, schema, indexes, and execution conditions.

The results do not establish:

- compliance with a production service-level objective;
- that `fmrp1` is intrinsically slower than `uat1`;
- the effectiveness of any index;
- the scalability of a specific version-selection algorithm; or
- whether the query returns every version, the latest version, or a deduplicated version-aware result.

## Follow-up Information Required

Further testing should record the meaning and units of `42w` and `120w`, the exact query and predicates, the version-selection semantics, schema and indexes, database and host configuration, cache state, concurrency, repetition count, and the target production volume and latency threshold. Query plans and execution statistics from the referenced attachments should also be extracted if available.

## Source Context

The source is located in the Cash Settlement System Design under Expose The Cashflow Data Design and the cashflow data provider query solution for big volume.