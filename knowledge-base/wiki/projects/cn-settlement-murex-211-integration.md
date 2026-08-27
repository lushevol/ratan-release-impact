---
type: project
title: CN Settlement Murex 2.11 Integration
status: on-hold
owner: ""
start_date: 2023-01-01
target_date: 2023-12-31
created: 2026-08-24
updated: 2026-08-24
tags: [china-settlement, murex-211, ratan, cashflow-integration]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--30-surrounding-system-in--19ui3cd, murex-ratan-bidirectional-cashflow-integration, china-cashflow-payment-stp-exclusion, murex-ratan-cashflow-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 Delivery Plan.md"]
---
# CN Settlement Murex 2.11 Integration

## Purpose

This planned delivery stream integrates [[murex-211]] cashflows with [[ratan]] for China settlement. The available evidence is a delivery plan rather than an implementation or release record. Accordingly, the project status is recorded as **on-hold** pending evidence of its final outcome.

## Planned delivery phases

1. **Q4 foundation:** integration strategy, scheduled publication, payment queues, processing scripts, staging-table capture, MQ connectivity, outbound workflow, message enrichment, and common-case amendment design.
2. **Q1 2023 lifecycle and control:** RATAN ACK and Release consumption, China payment-STP and BAU-queue exclusion, monitoring, reconciliation, exception analysis, and FMO hard-block scope.
3. **Q1 2023 assurance and go-live:** reverse ACK and Release testing, end-to-end SIT, SIT/UAT test-pack design, DPS approval, and a cashflow migration to be agreed near go-live.
4. **Contingent scope:** accounting/reporting work depends on [[razor]] accounting design; workflow optimization depends on an unspecified MSRB condition.

## Constraints and risks

- Development inbound/outbound MQ connectivity states that two MQ sets are required but only one is applicable.
- Amendment support was limited to a common case; `SN7` required further scenario testing.
- The exact definition and disposition of China cashflows excluded from payment STP are absent.
- The plan contains no confirmation of SIT, UAT, migration, DPS approval, or production deployment.

## Related pages

- [[murex-ratan-bidirectional-cashflow-integration]]
- [[china-cashflow-payment-stp-exclusion]]
- [[murex-ratan-cashflow-reconciliation]]
- [[what-are-the-murex-ratan-ack-and-release-message-contracts]]