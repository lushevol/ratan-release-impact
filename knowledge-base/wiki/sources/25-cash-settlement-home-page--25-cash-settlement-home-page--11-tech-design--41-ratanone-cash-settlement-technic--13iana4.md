---
type: source
title: Cash Settlement 2.0 Technical Design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, technical-debt, lifecycle, workflow, scbml, strategic-cash-settlement]
related: [cashflow-lifecycle-state-machine-restructuring, cashflow-stamping-domain-ownership, eventual-consistency-for-cashflow-exceptions-and-swift-status, cash-settlement-2-0-technical-debt-remediation, what-is-the-authoritative-cashflow-lifecycle-state-transition-and-persistence-contract, what-is-the-scbml-decommission-target-format-and-migration-plan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement 2.0 Technical Design.md"]
authors: []
year: 2025
url: ""
venue: Internal technical design
---
# Cash Settlement 2.0 Technical Design

This internal design identifies technical debt in Strategic Cash Settlement after nearly two years in production and proposes a remediation programme. It is a high-level proposal rather than a complete implementation design: several topics have only titles or owners, and referenced state-machine and workflow diagrams are not available as text.

## Background

The source identifies four principal concerns:

- Lifecycle status-machine logic is difficult and risky to extend, and does not adequately support transactional status updates.
- Microservice responsibilities are deeply coupled, especially between `orchestration-service` and `lifecycle-service`.
- Intermittent performance issues require bottleneck analysis.
- Dependence on SCBML/XML introduces verbosity, parsing complexity, limited readability and flexibility, performance concerns, and limited data-type support.

## Main topics and assigned owners

| | Topic | Owner | Problem Statement |
| --- | --- | --- | --- |
| 1 | State machine Restructure | @Xinmiao Huang | |
| 2 | Workflow optimization | @Xinmiao Huang | |
| 3 | Function Domain segregation | @Xinmiao Huang | |
| 4 | SCBML Decommission | @Xinmiao Huang | |
| 5 | Distributed lock issues | @Chen Yang | |
| 6 | Strategic SSI | @Quill Li | |
| 7 | Open search Integration | @Ruiheng Cao | |

## State-machine restructuring proposals

| Task No. | Description |
| --- | --- |
| 1 | Restructuring lifecycle service |
| 2 | Remove all useless table and clean up the related code |
| 3 | isBeforeValueDate is useless, can be removed and use isAfterValueDate instead |
| 4 | |
| | |

The source proposes that:

- Closure of all NSTP and SSI exceptions need not be synchronous; workflow may close exceptions when a cashflow arrives or is reinstated.
- The Auto Release job can leave lifecycle status as `released2Razor` even when workflow did not successfully consume its message.
- Cashflow stamping should move to [[cashflow-stamping-domain-ownership|Standardization Service]] by default; on reinstatement, lifecycle-service requests only specific fields.
- STP actions are mostly command-driven, while manual actions are generally command-plus-handler driven.
- Persistence should occur in `postprocess`, allowing `process` methods to run in parallel.
- Netting, UnNetting, and component-status changes should use `JdbcTemplate` batch updates for status and netting ID; “Net New” performs inserts only.

The source references table-analysis and state-machine diagrams but provides no textual transition model.

## Workflow optimization proposals

The proposed workflow changes are:

- Restrict precheck to data validation and persistence.
- Move workflow status to `TechFail` after validation failure.
- Move cutoff calculation to the beginning of “2-1,” an undefined flow label, to avoid missing cutoff data after `TechFail`.
- Move Auto Materialization/direct materialization checks from lifecycle precheck into workflow.
- Remove “Publish Post Process” from the sent-to-Razor flow.
- Remove the Swift Service distributed lock for SWIFT generation, accepting eventually consistent status write-back to lifecycle-service.
- Move Auto UnNet checking from lifecycle-service to Netting Service.

## Domain segregation and SCBML

The only detailed domain-segregation proposal is moving cashflow stamping to Standardization Service. SCBML decommissioning is named as a major topic but has no target format, consumer inventory, migration sequence, compatibility plan, or retirement criteria in this source.

## Limitations and follow-up

The source establishes strategic intent but does not define APIs, schemas, event contracts, transaction boundaries, retry or idempotency rules, reconciliation targets, migration sequencing, rollback, operational controls, or test evidence. In particular, the eventual-consistency and distributed-lock-removal proposals require additional safety controls before implementation.

Related investigation is tracked in [[what-is-the-authoritative-cashflow-lifecycle-state-transition-and-persistence-contract]], [[what-controls-make-swift-generation-safe-without-a-distributed-lock]], [[what-are-the-transaction-and-concurrency-rules-for-batch-cashflow-status-updates]], and [[what-is-the-scbml-decommission-target-format-and-migration-plan]].