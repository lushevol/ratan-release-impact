---
type: query
title: What Is the Authoritative NDS Cashflow Processing State Machine?
tags: [cashflow, nds, lifecycle, orchestration, state-machine]
related: [nds-cashflow-processing, ratan-cash-settlement-orchestration, lifecycle-service, nstp-and-ndirs-rule-routing, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--30-nds-cashflow-processing-design--yw8sda]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NDS Cashflow Processing Design.md"]
created: 2026-08-24
updated: 2026-08-24
---
# What Is the Authoritative NDS Cashflow Processing State Machine?

The source records a new node immediately after Pre-check in `ratan-cash-settlement-orchestration` and a lifecycle-service separation between persistence and attribute stamping. It does not specify the full ordered flow.

## Questions to Resolve

- What is the new post-Pre-check node named, and which service owns it?
- Does it execute persistence, stamping, rule evaluation, or another NDS-specific activity?
- What are the success, failure, retry, and terminal-state transitions?
- Are persistence and stamping atomic, eventually consistent, or compensated after partial failure?
- Which design is authoritative for lifecycle stamping and its reconciliation behavior?

The referenced Confluence page, *Cashflow Lifecycle Stamping Logic*, should be ingested before this query is resolved.