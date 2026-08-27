---
type: query
title: What Is the Reinstate Exception Lifecycle for Held Cashflows?
tags: [cashflow, reinstate, exception-lifecycle, hold, waiting]
related: [held-cashflow-reinstatement, ssi-exception-state-model, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Actions on Hold.md"]
created: 2026-08-23
updated: 2026-08-23
---
# What Is the Reinstate Exception Lifecycle for Held Cashflows?

The requirement states that **Send to WAITING** sets a held cashflow to `WAITING` with a `Reinstate` exception and records `Reinstate` in history. It does not define the exception lifecycle.

## Questions to resolve

- Does `Reinstate` block release until an operator takes an explicit action?
- Which actions clear, resolve, or retain the exception: SSI amendment, release, cashflow suppression, SWIFT suppression, or netting?
- Is the exception retained as historical audit evidence after the cashflow reaches its terminal state?
- What happens when the same cashflow is held and reinstated multiple times?
- Which service owns exception creation and state transitions, and what idempotency behavior applies?

This must be resolved before treating `Reinstate` as part of the authoritative [[ssi-exception-state-model]].