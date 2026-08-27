---
type: query
title: What Is the Auto Netting Benefit Calculation?
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, metrics, operational-benefit, inter-entity-netting]
related: [inter-entity-netting-coverage-metrics, netting-eligibility-rules]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting/Inter entity Netting - Volume Tracker.md"]
---
# What Is the Auto Netting Benefit Calculation?

The Inter Entity Netting volume tracker reports `Auto netting benefit` separately from `Total Netted`, and the values differ on many dates. For example, on 26 June 2026 it reports 778 total netted but 416 auto-netting benefit; on 29 June it reports 1,462 and 973 respectively.

## Questions to Resolve

- What formula produces `Auto netting benefit`?
- What is its unit: cashflows, payments avoided, settlement instructions avoided, monetary amount, or another measure?
- What source system and processing stage provide the metric?
- Which populations, exclusions, grouping rules, or netting outcomes make it differ from `Total Netted`?
- Is it intended as an operational KPI, a financial benefit measure, or both?

Until these questions are answered, the field should be reported as an undefined tracker metric rather than interpreted as a payment-count reduction.

Related operational fields are described in [[inter-entity-netting-coverage-metrics]]. The primary evidence is [[26-auto-netting-page-md-files--176-cash-settlement-home-page-cash-settlement-home-page-functional-requirement-s--11suykf]].