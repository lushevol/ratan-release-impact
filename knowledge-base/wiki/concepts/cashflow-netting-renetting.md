---
type: concept
title: Cashflow Netting Re-netting
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, netting, recovery, reconciliation, resultant-cashflow]
related: [netting-service, cashflow-auto-netting, netting-resultant-cashflow, pending-auto-netting-state, resultant-cashflow-status-consistency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Refactor Netting Process.md"]
---
# Cashflow Netting Re-netting

Cashflow Netting Re-netting (`renet`) is the proposed Netting Service recovery operation for finding incomplete cashflow net requests and regenerating resultant cashflows.

## Intended Responsibility

The source assigns `renet` to [[netting-service]], alongside normal netting and unnetting. It is intended to address incomplete requests whose resultant cashflow was not successfully generated.

This makes re-netting a distinct recovery and reconciliation capability, rather than an implicit side effect of generic lifecycle status processing.

## Unspecified Behavior

The source does not define:

- how an incomplete net request is identified;
- whether re-netting is scheduled, manually initiated, or event-triggered;
- duplicate-resultant prevention;
- idempotency keys or request state transitions;
- handling where component statuses have already changed; or
- downstream publication and reconciliation behavior.

These details are necessary to ensure `renet` does not create duplicate resultant cashflows or leave component cashflows in inconsistent states.