---
type: concept
title: Reinstatement Domain Event and History
created: 2026-08-24
updated: 2026-08-24
tags: [reinstatement, cashflow, Camunda, domain-events, UI-history]
related: [cashflow-status-restoration, cash-settlement-cashflow-domain-events, camunda]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/Uber Dev Testing Question.md"]
---
# Reinstatement Domain Event and History

Reinstatement domain-event history is the end-to-end behavior connecting a UI reinstatement or task-failure action to Camunda execution, domain-event serialization, and visible UI history.

The tested reinstatement flow used:

```text
/v2/ratan/cashflow/move/status/user
```

The UI was also expected to remove the SCBML field. For `C06810142009`, the fail action called:

```text
https://fmo-mfe-dev.uk.dev.net:8453/api/ratan/v1/camunda/task/fail
```

However, UI history missed the event because of a message-format error on `cash_settlement_cashflow_domain_events`. The source marks the issue fixed but does not document the corrected event schema or proof that the history projection was repaired.