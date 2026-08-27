---
type: concept
title: Non-Economic Amendment Cashflow Replacement
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, amendment, non-economic-amendment, settlement, auditability, RATAN]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--34-trade-validation-cashf--mg1utu, released-settled-amendment-control, cashflow-version-concurrency-control, trade-event-undo-semantics, trade-validation-gated-cashflow-visibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process.md"]
---
# Non-Economic Amendment Cashflow Replacement

## Definition

Non-economic amendment cashflow replacement is the rule for deciding whether an amended trade's withdrawal and replacement events can substitute for an original cashflow. The decision depends on the original cashflow's historical user actions and release or settlement state.

## Untouched original cashflow

If the original cashflow has no in-scope manual action and has not been released or settled, RATAN may replace it with the latest cashflow event sequence after the amended trade is validated. The latest cashflow ID is then reflected in the cashflow blotter.

## Protected original cashflow

If a user has acted on the original cashflow, or if it has been released or settled, RATAN must not silently replace it. The original operational decision and its audit trail take precedence over automatic substitution. The source describes `HOLD-NONECO` for withdrawal and replacement events in this path.

The protected-action list includes:

- Exception Fix/Reject, including affirmation, SSI key-in, SWIFT value-date key-in, approve, and reject.
- Settle as Gross.
- Netting or un-netting.
- Hold or unhold.
- Manual fail.
- Re-instate.
- FM Comment.
- Manual Cashflow Suppression.
- Manual Swift Suppression.
- Early materialization.

## Control gaps

The requirement does not define the authoritative audit table, action precedence, partial-settlement behavior, or idempotency rules. It also does not establish whether every listed action, including hold or unhold, has the same protection semantics.

This concept complements [[concepts/released-settled-amendment-control]] and should not be interpreted as a finalized implementation contract.