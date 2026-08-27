---
type: project
title: Cash Settlement 2.0 Technical Debt Remediation
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, technical-debt, lifecycle, workflow, scbml]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--13iana4, cashflow-lifecycle-state-machine-restructuring, cashflow-stamping-domain-ownership, eventual-consistency-for-cashflow-exceptions-and-swift-status, what-is-the-scbml-decommission-target-format-and-migration-plan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement 2.0 Technical Design.md"]
status: planned
owner: Xinmiao Huang
start_date: 2026-08-24
target_date: ""
---
# Cash Settlement 2.0 Technical Debt Remediation

A proposed multi-topic remediation initiative for Strategic Cash Settlement. The source assigns owners for architecture topics but does not demonstrate that implementation has started; therefore the project is recorded as planned.

## Scope

- Restructure the cashflow lifecycle state machine and persistence approach.
- Simplify workflow responsibilities and clarify service boundaries.
- Move default cashflow stamping to Standardization Service.
- Decommission SCBML.
- Address distributed-lock, Strategic SSI, and OpenSearch topics.

## Proposed ownership

[[xinmiao-huang|Xinmiao Huang]] owns the first four listed topics. [[chen-yang|Chen Yang]] owns distributed-lock issues, [[quill-li|Quill Li]] owns Strategic SSI, and [[ruiheng-cao|Ruiheng Cao]] owns OpenSearch integration.

## Risks

The proposal does not define a migration plan, canonical state-transition contract, target SCBML format, transactional semantics, or compensating controls for asynchronous exception closure and lock removal. These gaps should be resolved before delivery commitments are made.