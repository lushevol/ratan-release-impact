---
type: concept
title: Inter-Entity Netting Coverage Metrics
created: 2026-08-22
updated: 2026-08-22
tags: [inter-entity-netting, auto-netting, coverage, metrics, settlement-day-2]
related: [netting-eligibility-rules, auto-netting-rule-check, auto-netting-static-go-live-sequencing, what-is-the-auto-netting-benefit-calculation, what-caused-inter-entity-netting-coverage-to-drop-in-june-and-august-2026]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting/Inter entity Netting - Volume Tracker.md"]
---
# Inter-Entity Netting Coverage Metrics

Inter-entity netting coverage metrics distinguish the total observed cashflow population from the subset eligible for automatic netting under the volume tracker's reported `<=100K` threshold.

## Reported Measures

- **Total cashflow** is the daily population recorded by the tracker.
- **out of scope(>100K)** is the portion excluded by the reported threshold.
- **in Scope (<=100K)** is the population within the threshold.
- **Total Netted** is the reported number of cashflows netted.
- **Netted vs in scope** is the reported coverage rate for the in-scope population and broadly corresponds to `Total Netted / in Scope (<=100K)`, subject to rounding.
- **Netted vs Total** is the reported coverage rate across all recorded cashflows and broadly corresponds to `Total Netted / Total cashflow`, subject to rounding.
- **Auto netting benefit** is a separate reported metric. It cannot be assumed to equal payment-count reduction, avoided operational work, or any other specific measure because the tracker provides no formula or unit.

## Interpretation

A high `Netted vs in scope` result indicates strong coverage within the tracker's measured eligible population. It does not establish high coverage of all cashflows: a substantial `>100K` population can keep `Netted vs Total` materially lower.

For example, the tracker records 99% in-scope coverage on 17 June 2026, while only 33% of total cashflows were netted because 674 of 1,008 cashflows were out of scope. The threshold is evidence of the tracker’s measured population, not proof of a universal eligibility policy across products, entities, currencies, or netting rules.

## Operational Signals

The tracker records a sharp fall in in-scope coverage on 22–25 June 2026, recovery to generally 98–100% from 26 June to 30 July, and a further decline in the records from 31 July onward. These signals require operational investigation; coverage data alone does not establish a configuration, batch, data, or rule-evaluation cause.

This metric model supplements [[netting-eligibility-rules]] and provides monitoring evidence relevant to [[auto-netting-static-go-live-sequencing]]. The formula and intended meaning of the benefit field remain tracked in what is the auto netting benefit calculation.