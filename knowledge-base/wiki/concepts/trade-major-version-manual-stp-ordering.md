---
type: concept
title: Trade Major-Version Manual STP Ordering
created: 2026-08-23
updated: 2026-08-23
tags: [trade-lifecycle, major-version, sequencing, manual-stp, dependency-control]
related: [bulk-manual-stp-group-blotter, group-blotter, allocation-cashflow-state-handling, murex-reversal-and-new-cashflow-matching]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter.md"]
---
# Trade Major-Version Manual STP Ordering

## Definition

Trade major-version manual STP ordering is the rule that groups for the same trade are evaluated and executed in ascending major-version order. A group key such as `T1_G2_V2` identifies the trade, group, and major-version sequence.

## Dependency Rule

An unresolved earlier major version blocks a later major version. The source demonstrates that selecting only `T1_G2_V2` or `T1_G3_V3` produces `N/A` when `T1_G1_V1` still contains pending cashflows.

Once the remaining pending cashflow in an earlier group is selected and processed, that group can complete. Later groups are not automatically completed unless their own eligibility and validation conditions also pass.

## Trade Partitioning

The ordering rule applies within a trade. Groups belonging to different trades may be processed independently in one bulk request, as shown by the scenario containing `T1_G1_V1` and `T2_G1_V1`.

## Qualification

The source does not specify whether ordering constrains only eligibility, execution start, commit order, or completion order when multiple threads are used. It also does not define whether a precheck failure causes rollback of earlier successful groups. These questions are tracked in [[queries/is-bulk-manual-stp-atomic-per-trade]].