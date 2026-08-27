---
type: entity
title: GroupReadyEvent
created: 2026-08-23
updated: 2026-08-23
tags: [RATAN, domain-event, orchestration, cashflow-groups]
related: [cashflow-group, cashflow-group-lifecycle, trade-validated-event, group-completed-event]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter Detail.md"]
---
# GroupReadyEvent

`GroupReadyEvent` signals that a cashflow group has reached `READY` and can enter downstream orchestration.

## Downstream flow

The source associates the event with:

```text
group.status=READY
=> publish GroupReadyEvent
=> cashflowGroupMessage.status=END
=> send group message to topic:
   Cash_Settlement_Orchestration_Inbound
```

The exact transaction boundary between publishing the event, updating the message status, and sending the group message is not defined.