---
type: source
title: "Draft: Auto Aggregation Based on Normalized Payment Schedule"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, auto-aggregation, netting, ratan, fmrp, draft-requirement]
related: [2026-brp-q3-ratansett-product-agnostic-aggregation, normalized-payment-schedule, product-agnostic-cashflow-aggregation, fmrp-flow, what-are-the-normalized-payment-schedule-aggregation-keys, how-will-normalized-payment-schedule-aggregation-coexist-with-irs-and-ccs-auto-netting, what-is-the-historical-data-policy-for-normalized-payment-schedule-aggregation]
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Netting -- [Draft", "auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Netting -- [Draft] Auto Aggregation based on Normalized Payment Schedule.md"] Auto Aggregation based on Normalized Payment Schedule.md"] Auto Aggregation based on Normalized Payment Schedule.md"]
authors: []
year: 2026
url: ""
venue: "Internal functional requirement draft"
---
# Draft: Auto Aggregation Based on Normalized Payment Schedule

This draft functional requirement proposes a strategic [[product-agnostic-cashflow-aggregation]] capability in [[ratan]], driven by a proposed upstream [[normalized-payment-schedule]].

## Background and stated problem

The document states that [[murex-2-11]] aggregates cashflows under the same trade, while [[stella]], the cashflow generator for [[fmrp-flow]], does not implement that behavior.

RATAN introduced IRS Netting and [[ccs-auto-netting]] as supplementary auto-aggregation mechanisms. The draft characterizes those mechanisms as taxonomy-specific, limited respectively to IRS and CCS. It states that this approach will not satisfy requirements as more taxonomies enter FMRP Flow, citing `InterestRate:LoanDeposit` as an example.

The source also identifies an IRS model with multiple cashflows in the second leg that current IRS Netting does not support. The supporting work item is [ADO Story 15005868: FMRP 8.0 India Rates — IRS trade, second leg with multiple cashflows](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/15005868).

## Proposed direction

The upstream and data-modeling teams are stated to be working with RATAN stakeholders to introduce Normalized Payment Schedule as a basis for strategic product-agnostic aggregation.

The requirement is tracked as [ADO Story 14618546: 2026 BRP Q3 RatanSett Enhancement — Product Agnostic Aggregation based on Normalized Payment Schedule](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14618546), represented in this wiki by [[2026-brp-q3-ratansett-product-agnostic-aggregation]].

## Evidence limitations

The detailed requirement scenarios are not available as machine-readable text in this source. The document defers to `attachments/analysis.xlsx`, described as the newest version of user cases, and embedded screenshots.

Referenced user-case categories are:

- Happy User Cases
- Negative User Cases
- Historical Data-User Cases

Consequently, this draft does not establish the aggregation keys, eligibility conditions, schedule granularity, calculation method, error handling, historical-data policy, or acceptance criteria.

## Open requirement areas

The design requires resolution of:

- [[what-are-the-normalized-payment-schedule-aggregation-keys]]
- [[how-will-normalized-payment-schedule-aggregation-coexist-with-irs-and-ccs-auto-netting]]
- [[what-is-the-historical-data-policy-for-normalized-payment-schedule-aggregation]]

The source establishes a planned direction, not evidence that Normalized Payment Schedule aggregation has been approved, implemented, tested, or deployed.