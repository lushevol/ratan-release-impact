---
type: entity
title: t_auto_netting_task
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, netting, auto-netting, cashflow]
related: [netting-service, auto-netting, amendment-cashflow-exclusion-from-auto-netting, what-is-the-authoritative-auto-netting-task-and-amendment-exclusion-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design/Auto Netting design.md"]
---
# t_auto_netting_task

`t_auto_netting_task` is a database table named in the Auto Netting design as an artifact supporting [[auto-netting]] in the [[netting-service]].

The source does not provide a schema definition. Its columns, keys, relationships, indexes, constraints, ownership, retention requirements, and lifecycle semantics are unknown.

The documented workflow collects auto-netting tasks, excludes amendment cashflows, and then performs netting. It does not establish whether `t_auto_netting_task` stores all tasks, only eligible tasks, or task-processing outcomes.

See [[what-is-the-authoritative-auto-netting-task-and-amendment-exclusion-contract]] for unresolved data-model and lifecycle questions.