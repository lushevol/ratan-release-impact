---
type: concept
title: Trade Validation Group Advancement
created: 2026-08-23
updated: 2026-08-23
tags: [RATAN, TDS3, trade-validation, group-advancement, event-driven-processing]
related: [tds3, ratan, cashflow-group, cashflow-group-lifecycle, trade-validated-event, group-ready-event]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter Detail.md"]
---
# Trade Validation Group Advancement

Trade validation is propagated at trade scope in the process described by the source. A trade message from [[entities/tds3]] causes all cashflow groups associated with the relevant `tradeId` to receive `isTradeValidated=true`.

## Processing paths

The behavior is specified for:

- `TDS3_Trade_Message_Process_In` through `tds3-trade-inbound`.
- `TDS3_Trade_Murex_Message_Process_In` through `tds3-trade-murex-inbound`.

For both paths:

1. Obtain `TradeInfo` from `scbml`.
2. Update `ratan_trade`.
3. Emit [[entities/trade-validated-event]].
4. Update all groups for the relevant `tradeId` with `isTradeValidated=true`.
5. Retrieve groups in `PENDING_TRADE_VALIDATION`.
6. Advance eligible groups to `READY`.
7. Publish [[entities/group-ready-event]] for downstream orchestration.

The claim is limited to groups associated with the processed `tradeId`; it does not establish equivalent behavior for unrelated trades or other message sources.

## Sequencing constraint

Trade validation alone does not necessarily make a group ready. The group must also satisfy the previous-group dependency represented by `PENDING_PRE_GROUP` and `noPreviousGroupPending`.

The source does not specify whether validation updates are idempotent, how conflicting validation messages are handled, or whether partial trade validation is possible.