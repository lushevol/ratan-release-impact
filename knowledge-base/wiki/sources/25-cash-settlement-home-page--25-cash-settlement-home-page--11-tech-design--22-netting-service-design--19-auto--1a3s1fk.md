---
type: source
title: Auto Netting Design
created: 2026-08-24
updated: 2026-08-24
tags: [netting, auto-netting, cashflow, technical-design]
related: [netting-service, t-auto-netting-task, auto-netting, amendment-cashflow-exclusion-from-auto-netting, what-is-the-authoritative-auto-netting-task-and-amendment-exclusion-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design/Auto Netting design.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Auto Netting Design

This source provides a minimal process outline for automated netting in the [[netting-service]].

## Documented process

```text
1. collect auto-netting tasks
2. remove amendment cashflow from auto-netting tasks
3. do auto-netting
```

The stated ordering requires amendment-cashflow removal after task collection and before auto-netting execution.

## Named database table

```text
t_auto_netting_task
```

[[t-auto-netting-task]] is the only database artifact named by the source. No DDL, columns, keys, indexes, constraints, ownership, retention policy, or task lifecycle is supplied.

## Scope and limitations

The source establishes that [[auto-netting]] is staged and that [[amendment-cashflow-exclusion-from-auto-netting]] is a pre-execution rule. It does not define task eligibility, amendment identification, netting calculations, persistence, idempotency, locking, error handling, retries, recovery, audit records, or outcomes for removed tasks.

Open design questions are tracked in [[what-is-the-authoritative-auto-netting-task-and-amendment-exclusion-contract]].