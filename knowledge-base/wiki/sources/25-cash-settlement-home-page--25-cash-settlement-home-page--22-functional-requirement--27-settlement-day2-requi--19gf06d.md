---
type: source
title: Inter-Entity Netting Design
authors: []
year: 0
url: "https://confluence.global.standardchartered.com/display/DSP/Inter+Entity+Netting"
venue: "Confluence"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, settlement-day-2, auto-netting, inter-entity-netting]
related: [inter-entity-netting, direction-dependent-prematch-key, ratanone-foundation, ratan-cash-settlement-netting-service, ratan-cash-settlement-group-management-service, ratan-rule-service, auto-netting-rule-check, settlement-day-2, is-inter-entity-netting-resultant-counterparty-selection-deterministic]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting/Inter Entity Netting Design.md"]
---
# Inter-Entity Netting Design

## Summary

This functional requirement and technical design note describes changes for Settlement Day 2 inter-entity netting. The design identifies two cashflow-processing nodes requiring changes:

1. **Cashflow Enrichment**, which sets the USD transferred amount into the cashflow.
2. **Auto Netting Job**, which creates direction-dependent matching maps and determines whether reciprocal cashflows match.

The design matches reciprocal `Pay` and `Receive` cashflows using a composite `PreMatchKey` containing the entity identifiers and amount. It does not establish production deployment, release completion, downstream resultant behavior, or the deterministic rule for selecting among duplicate keys.

## Cashflow Matching Samples

The source provides the following sample data:

| CashflowId | Entity FMID | Direction | Counterparty FMID | Amount | PreMatchKey | Currency | VD | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 400906330 | Pay | 7 | 100 | 400906330-7-100 | USD | 2026-03-01 | Match |
| 2 | 400906330 | Receive | 7 | 200 | 7-400906330-200 | USD | 2026-03-01 | Match |
| 3 | 400906330 | Receive | 7 | 600 | 7-400906330-600 | USD | 2026-03-01 | Not Match |
| 4 | 7 | Receive | 400906330 | 100 | 400906330-7-100 | USD | 2026-03-01 | Match |
| 5 | 7 | Pay | 400906330 | 200 | 7-400906330-200 | USD | 2026-03-01 | Match |
| 6 | 7 | Pay | 400906330 | 200 | 7-400906330-200 | USD | 2026-03-01 | Not Match |
| 7 | 10075222 | Pay | 400906330 | 200 | 10075222-400906330-200 | USD | 2026-03-01 | Not Match |

## Direction-Dependent Mapping Rules

The source defines the mapping rules as follows:

| Map Type (according to direction) | PreMatchKey Format | PreMatchKey | CashflowId(Match Result) |
| --- | --- | --- | --- |
| **Pay Map ** | **EntityFMID-CounterPartyFMID-Amount** | 400906330-7-100 | 1 (match) |
| 7-400906330-200 | 5 (match) 6 (not match) |
| 10075222-400906330-200 | 7 (not match) |
| **Receive Map** | **CounterPartyFMID-EntityFMID-Amount** | 7-400906330-200 | 2 (match) |
| 7-400906330-600 | 3 (not match) |
| 400906330-7-100 | 4 (match) |

For `Pay` cashflows:

```text
PreMatchKey = EntityFMID-CounterPartyFMID-Amount
```

For `Receive` cashflows:

```text
PreMatchKey = CounterPartyFMID-EntityFMID-Amount
```

This causes reciprocal records to resolve to the same key when entity direction and amount are aligned.

## Participating Services

All listed services use the shared feature branch `feature/autonetting-interEntity`. No release versions are populated in the source.

| service | feature branch | release version |
| --- | --- | --- |
| ratanone-foundation | feature/autonetting-interEntity | |
| ratan-cash-settlement-netting-service | feature/autonetting-interEntity | |
| ratan-cash-settlement-group-management-service | feature/autonetting-interEntity | |
| ratan-rule-service | feature/autonetting-interEntity | |

See [[entities/ratan-cash-settlement-netting-service]], [[entities/ratan-rule-service]], [[entities/ratanone-foundation]], and [[entities/ratan-cash-settlement-group-management-service]].

## Findings and Limitations

Cashflows 1 and 4 match because their reciprocal entity directions and amounts produce `400906330-7-100`. Cashflows 2 and 5 match because they produce `7-400906330-200`. Cashflows 3 and 6 do not match: cashflow 3 has a different amount, while cashflow 6 duplicates the key used by cashflow 5.

The duplicate example suggests one-to-one consumption or allocation, but the source does not define the tie-breaker. It is also unclear whether `Currency` and `VD` are independent eligibility filters because they appear in the sample data but not in the displayed key format.

The source does not specify the exact persisted field name or type for “USD Transfered Amount,” whether amounts are normalized to USD, what happens after a record is marked `Match`, or whether a successful match creates a resultant cashflow. These questions remain relevant to [[queries/is-inter-entity-netting-resultant-counterparty-selection-deterministic]].

## Related Wiki Topics

This design provides a concrete implementation example for [[concepts/inter-entity-netting]] and [[concepts/direction-dependent-prematch-key]]. It should be considered alongside [[concepts/auto-netting-rule-check]], [[concepts/netting-resultant-cashflow]], [[concepts/netting-type-derivation]], [[concepts/cross-rule-netting-isolation]], and [[concepts/settlement-day-2]].