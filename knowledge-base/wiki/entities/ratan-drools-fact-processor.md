---
type: entity
title: ratan_drools_fact_processor
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, drools, fact-processing, ratan, archived-design]
related: [ratan-rule, ratan-drools-rule, drools-based-nstp-rule-evaluation, should-drools-eval-perform-external-http-calls]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Tech Design.md"]/Rule Service Tech Design.md"]/Rule Service Tech Design.md"]
---
# ratan_drools_fact_processor

> [!warning]
> This is a proposed historical schema from an archived Rule Service design, not a confirmed current table.

`ratan_drools_fact_processor` was intended to register named custom fact processors. A processor names the produced fact and stores DRL fact-expression fragments for conditions that rely on externally obtained data.

The archived design gives GSAM-client lookup by FMID as an example of a custom processor use case. It does not specify processor ownership, invocation timing, timeout, retry, caching, idempotency, or failure behavior. These unresolved operational concerns are tracked by [[should-drools-eval-perform-external-http-calls]].