---
type: concept
title: Cashflow Lifecycle State-Machine Restructuring
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, lifecycle, state-machine, persistence, technical-debt]
related: [cashflow-status-restoration, manual-cashflow-holding, eventual-consistency-for-cashflow-exceptions-and-swift-status, what-is-the-authoritative-cashflow-lifecycle-state-transition-and-persistence-contract, what-are-the-transaction-and-concurrency-rules-for-batch-cashflow-status-updates]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement 2.0 Technical Design.md"]
---
# Cashflow Lifecycle State-Machine Restructuring

A proposed redesign of lifecycle-service status handling intended to make changes safer and support transactional updates more effectively.

## Proposed changes

The proposal includes lifecycle-service restructuring, removal of unused tables and related code, and replacement of `isBeforeValueDate` with `isAfterValueDate`. It also proposes persisting data in `postprocess` while allowing `process` methods to execute in parallel.

A documented failure scenario is that an Auto Release message may not be consumed successfully by workflow even though lifecycle state has already become `released2Razor`. The source identifies this divergence but does not specify a durable event-delivery, retry, or reconciliation mechanism.

## Transactional batch updates

For netting, UnNetting, and component-status updates, the proposal calls for `JdbcTemplate` batch updates of status and netting ID. “Net New” is described as insert-only. It does not define transaction demarcation, isolation, optimistic locking, partial-failure handling, idempotency, or audit requirements.

## Status

This is a design proposal, not evidence of deployed state-machine behavior. The source’s UML and table-analysis diagrams are referenced but unavailable in textual form. Canonical states, guards, transition ownership, and concurrency controls remain open.