---
type: concept
title: Stella Cashflow Status Synchronization
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, status, stella, integration]
related: [strategic-cashflow, ratan-cashflow-lifecycle-service, ratanone-stella-ambassador, stella-batch-and-single-status-updates, cashflow-lifecycle-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Strategic Cashflow Stella Ambassandor.md"]
---
# Stella Cashflow Status Synchronization

Stella cashflow status synchronization propagates significant CN Settlement lifecycle actions from `ratan-cashflow-lifecycle-service` through [[ratanone-stella-ambassador]] to [[stella]].

The observed normal progression is:

```text
PROJECTED --Net--> NETTED
NETTED --Unnet--> PROJECTED
PROJECTED --Release--> RELEASED
RELEASED --Settle--> SETTLED
```

The source additionally records that Stella does not allow a direct cross-status `PROJECTED` to `SETTLED` update. It does not establish whether Ratan must reject that command before invoking Stella.