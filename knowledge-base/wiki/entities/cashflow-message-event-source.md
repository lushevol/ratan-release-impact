---
type: entity
title: CashflowMessageEventSource
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, event-source, lineage, Ratan, Stella]
related: [ratan, stella, cashflow-lifecycle-state-machine, business-versioned-cashflow-persistence]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Status Update API Tuning/lifecycle service - state machine.md"]
---
# CashflowMessageEventSource

`CashflowMessageEventSource` is the domain record associated with `ratan_stella_message_event_source`. In the design, it is the central event-source persistence model for cashflow lifecycle updates.

## Responsibilities

The record captures:

- Current and previous cashflow business versions and workflow statuses.
- Event and business-event lineage.
- Settlement amount, currency, date, method, and type.
- Trade, portfolio, product-taxonomy, and originating-system identifiers.
- Entity, payer, receiver, and counterparty information.
- Netting, un-netting, STP, fixing, commodity, and lien-monitor indicators.
- Murex classification and strategy metadata.
- Tracking identifiers and message-delivery attributes.

## Update behavior

For a new cashflow ID, the record is inserted. It is also inserted for business-version upgrades and downgrades. When the business version is unchanged, the design calls for an update rather than a new event-source insert.

This behavior is part of the [[business-versioned-cashflow-persistence]] model and feeds the [[cashflow-lifecycle-state-machine]]. The source does not specify database keys, indexes, immutable fields, or field-level overwrite rules.