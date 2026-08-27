---
type: concept
title: Cashflow Settlement-Method Event Consistency
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, settlement-method, events, withdrawal, projection]
related: [gross-util-settlement-method-transition, cashflow-data, denormalized-cashflow-query-read-model, what-is-the-authoritative-current-and-history-lifecycle-for-cashflow-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/Draft Design For Phase2.md"]
---
# Cashflow Settlement-Method Event Consistency

The FXU draft states that a `Withdrawal` event's settlement-method value must be overwritten by the settlement-method field value of the latest `New` event after a manual settlement-method change. The stated purpose is to keep settlement method consistent after the change action.

This language can be interpreted as a read-model or projection rule rather than mutation of immutable event history. The source does not clarify whether event records are overwritten, whether the rule applies only to a derived view, or how the latest `New` event is selected when events are delayed or out of order.

This requirement affects the consistency of [[cashflow-data]] and potentially the [[denormalized-cashflow-query-read-model]]. It should not be treated as evidence for SSI event contracts.