---
type: query
title: How Are Duplicate or Multi-Matching Schedule Events Counted?
created: 2026-08-22
updated: 2026-08-22
tags: [payment-schedules, cashflows, deduplication, expected-payment-count]
related: [schedule-to-cashflow-matching, expected-payment-count-for-auto-netting, irs, ccs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Product Agnostic model to identify all cashflows for a specific value date to support Auto Aggregation.md"]
---
# How Are Duplicate or Multi-Matching Schedule Events Counted?

The source says that an IRS or CCS payment is eligible for Expected Payment Count if any first-leg or second-leg schedule matches its date and currency. It does not define multiplicity.

## Questions

- Is a cashflow that matches schedules on both legs counted once or twice?
- Do multiple schedule entries with the same date and currency represent separate expected payments?
- What schedule-event identifier distinguishes legitimate repeated payments from duplicates?
- At which stage are duplicate schedule records or duplicate cashflows excluded?

## Impact

An undefined counting rule can overstate or understate Expected Payment Count, causing premature or permanently blocked Auto Netting.