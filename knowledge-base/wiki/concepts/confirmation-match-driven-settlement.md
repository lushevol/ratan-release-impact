---
type: concept
title: Confirmation-Match-Driven Settlement
created: 2026-08-22
updated: 2026-08-22
tags: [confirmation, settlement, FMRP, STP, NSTP]
related: [fmrp, straight-through-processing, high-risk-nstp-rule, cashflow-status-and-substate-model, f2b]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list.md"]
---
# Confirmation-Match-Driven Settlement

Confirmation-match-driven settlement uses confirmation match status as an input to determine whether an FMRP event or cashflow may proceed to settlement.

## Checklist context

The F2B onboarding checklist identifies confirmation match status as a settlement control for new FMRP events and products. It appears alongside payment-duplication control, undo support, and STP/NSTP control.

## Onboarding requirements

For each new event or product, onboarding should document:

- The confirmation statuses that permit settlement.
- The statuses that hold or route a flow to NSTP.
- Behavior for amendments, fixing, refixing, novation, close out, undo, maturity, and expiry.
- Interaction with payment status and migration cutover.
- FMMIS actions required for STP/NSTP calculation.

The source does not define the status model or acceptance criteria.
