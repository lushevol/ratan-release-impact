---
type: query
title: What Is the Authoritative Split-Child Lifecycle After Parent Withdrawal?
tags: [cashflow, splitting, withdrawal, lifecycle, cancellation]
related: [cashflow-splitting, split-cashflow-withdrawal-propagation, ratan-fail-and-autofail-status-transitions, cashflow-pre-fail-state-restoration]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT/Cashflow Splitting UAT For ASPIRE.md"]
---
# What Is the Authoritative Split-Child Lifecycle After Parent Withdrawal?

The ASPIRE UAT record reports passing withdrawal scenarios for split cashflows in HK, TW, and TH, including automatic cancellation of failed and SWIFT-suppressed children. It does not define the lifecycle contract needed to interpret those results.

## Questions to resolve

- What trigger, ordering, and timing apply when a split parent is withdrawn?
- Which child states are eligible for automatic cancellation?
- What is the required outcome for released, unreleased, failed, and SWIFT-suppressed children?
- Are child cancellations synchronous, asynchronous, and idempotent?
- Which final statuses and accounting events must be produced?
- Does the same contract apply to gross manual splits, gross automatic splits, and net-resultant automatic distribution?

## Evidence

[[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--6za5lq]] is UAT evidence that selected scenarios passed. It is not an authoritative transition specification.