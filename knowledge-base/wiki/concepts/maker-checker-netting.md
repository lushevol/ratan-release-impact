---
type: concept
title: Maker/Checker Netting
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, netting, maker-checker, operational-control]
related: [netting-service, cashflow-netting, netting-eligibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design.md"]
---

# Maker/Checker Netting

Maker/checker netting is an operational control in which one user or process creates a netting request and another authorized party validates or approves it before execution.

The source explicitly requires a maker/checker process and separately requires an interface for netting validation. The request schema includes `process_type` values of `MANUAL` and `AUTO`, `updated_by`, `fmo_comments`, timestamps, and a `group_id`, which suggests audit and workflow context.

No approval states, role definitions, segregation-of-duties rules, rejection behavior, authorization policy, or automatic-processing exception are defined. These omissions prevent the source from serving as a complete approval contract.

See what are the netting maker checker approval semantics.