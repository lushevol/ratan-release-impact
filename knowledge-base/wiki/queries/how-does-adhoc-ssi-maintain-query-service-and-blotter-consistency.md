---
type: query
title: How Does Adhoc SSI Maintain Query Service and Blotter Consistency?
tags: [adhoc-ssi, query-service, cashflow-blotter, notifications, read-model-consistency]
related: [ssi-stamping-service, adhoc-ssi-maker-checker-workflow, query-service, cashflow-blotter, cashflow-notification-and-auto-refresh, cash-settlement-query-service-graphql-read-model]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/SSI Stamping Service Design/SSI Stamping Design.md"]
---
# How Does Adhoc SSI Maintain Query Service and Blotter Consistency?

The design’s BAU-difference table explicitly states that the Adhoc SSI cashflow status-update mechanism does not send a notice to [[query-service]].

## Open questions

- Is notification suppression intentional for all Maker, approval, and rejection outcomes?
- What event, polling, refresh, or direct-read mechanism keeps [[cashflow-blotter]] and the query read model current?
- What temporary divergence is acceptable, and how is it communicated to users?
- Does the suppression affect [[cashflow-notification-and-auto-refresh]] behavior or entitlement-aware notifications?
- How are failed or delayed compensating updates detected and reconciled?

No rationale, consistency mechanism, or service-level expectation is defined in the source.