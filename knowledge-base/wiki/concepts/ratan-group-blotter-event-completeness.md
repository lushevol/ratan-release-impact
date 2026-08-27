---
type: concept
title: RATAN Group Blotter Event Completeness
created: 2026-08-24
updated: 2026-08-24
tags: [RATAN, group-blotter, event-completeness, reversal-rebook, non-economic-amendment]
related: [ratan, cashflow-event-control, cashflow-batch-control, non-economic-cashflow-amendment-handling, six-attribute-cashflow-equivalence, trade-validation-cashflow-gating, manual-cashflow-blotter-push-exception]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/RATAN Settlement Control on Trade Validation.md"]
---
# RATAN Group Blotter Event Completeness

RATAN group blotter event completeness is the control that verifies whether the cashflows associated with a market event have arrived as a complete group.

## Covered event relationships

The source identifies groups involving:

- Reversal and rebook events.
- CCS interest pay and receive flows.
- CCS initial notional payments.
- Initial notional payments and first-period interest payments.

The blotter can hold a cashflow while waiting for a related event. This is distinct from the trade-validation gate described in [[concepts/trade-validation-cashflow-gating]].

## Non-economic amendment comparison

After the full group arrives, RATAN compares withdrawals and new cashflows to identify non-economic amendments. The intended outcome is to ignore non-economic changes where appropriate and reduce manual effort for reversal and rebook processing.

The source reports 200 Murex 2.11 non-economic amendments for SG, MY, IN, and CN over three months, and 2,000 for all entities over three months. These figures are operational indicators rather than formally defined metrics because the source provides no extraction or reconciliation method.

## Operational dependency

If an expected cashflow is stuck in Murex or cancelled before feeding to RATAN, the group may remain incomplete. The documented response is manual monitoring and, in specified cases, a manual push to the cashflow blotter. See [[concepts/manual-cashflow-blotter-push-exception]].