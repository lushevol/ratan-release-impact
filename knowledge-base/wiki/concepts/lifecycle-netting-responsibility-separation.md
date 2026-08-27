---
type: concept
title: Lifecycle–Netting Responsibility Separation
created: 2026-08-22
updated: 2026-08-22
tags: [architecture, cashflow, lifecycle, netting, separation-of-concerns, refactoring]
related: [lifecycle-service, netting-service, cashflow-auto-netting, netting-resultant-cashflow, ratan-cashflow-lifecycle-state-machine, event-driven-component-cashflow-status-management]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Refactor Netting Process.md"]
---
# Lifecycle–Netting Responsibility Separation

Lifecycle–Netting Responsibility Separation is the proposed architectural boundary between generic cashflow status transitions and netting-specific domain operations.

## Proposed Allocation

[[lifecycle-service]] owns lifecycle initialization and status changes for an individual cashflow. [[netting-service]] owns operations that establish, reverse, recover, or maintain the relationship between resultant and component cashflows:

- `net`
- `unnet`
- `netRuleCheck`
- `renet`
- `manageComponentCashflowStatus`

Under this model, creating a [[netting-resultant-cashflow]] is a netting operation rather than a side effect embedded in a generic status-update API.

## Rationale

The source reports that the existing update-status API contains extensive unrelated business logic, operates as a large transaction, and has experienced production issues associated with long execution time. The separation is intended to:

- reduce transaction scope;
- make action-specific behavior easier to understand;
- isolate netting changes from ordinary lifecycle changes;
- make maintenance and targeted testing more practical; and
- align the design with SRP, separation of concerns, OCP, KISS, DIP, and LKP.

## Limitation

The proposed services remain coupled through lifecycle domain events: Netting Service reacts when a resultant cashflow reaches `released` or `settled`. The event contract, consistency model, and failure recovery must be explicitly designed; separation of implementation responsibility does not itself establish transactional correctness.