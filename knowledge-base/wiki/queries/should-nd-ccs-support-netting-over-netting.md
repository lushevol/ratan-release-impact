---
type: query
title: Should ND CCS Support Netting over Netting?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, netting, nd-ccs, configuration, risk]
related: [netting-over-netting, auto-netting, irs-auto-netting, netting-key-selection, fmrp, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - FXO.md"]
---
# Should ND CCS Support Netting over Netting?

## Question

Should ND CCS be permitted to use netting over netting, and what approvals and controls are required?

## Evidence

The FXO checklist states that netting over netting is restricted to IRS and that ND IRS follows the same ISDA taxonomy. It then says configuration must be updated to allow ND CCS if the new product requires this capability.

This describes a current restriction and a proposed extension, not an implemented capability.

## Information Needed

- Business and legal justification.
- Applicable ISDA taxonomy.
- Eligibility and grouping rules.
- Use of NID and any secondary netting key.
- Component-to-resultant cashflow traceability.
- Accounting and SWIFT-message effects.
- Cancellation, unwind, and failure handling.
- Configuration ownership and approval.
- Regression and UAT evidence.

An authorized decision is required before ND CCS support can be documented as accepted.