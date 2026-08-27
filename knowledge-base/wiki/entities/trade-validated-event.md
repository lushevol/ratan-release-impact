---
type: entity
title: TradeValidatedEvent
created: 2026-08-23
updated: 2026-08-23
tags: [RATAN, TDS3, domain-event, trade-validation]
related: [tds3, ratan, cashflow-group, trade-validation-group-advancement, group-ready-event]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter Detail.md"]
---
# TradeValidatedEvent

`TradeValidatedEvent` is the domain event emitted after `TradeInfo` is obtained from `scbml` and `ratan_trade` is updated.

## Effect on groups

For the relevant `tradeId`, the event flow:

1. Updates all associated cashflow groups with `isTradeValidated=true`.
2. Retrieves groups in `PENDING_TRADE_VALIDATION`.
3. Advances groups that satisfy previous-group and message-completeness conditions.
4. Publishes [[entities/group-ready-event]] when a group becomes `READY`.

The source documents this behavior for both `tds3-trade-inbound` and `tds3-trade-murex-inbound`.