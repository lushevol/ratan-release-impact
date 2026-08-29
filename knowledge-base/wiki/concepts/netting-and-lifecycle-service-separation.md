---
type: concept
title: Netting and Lifecycle Service Separation
created: 2026-08-22
updated: 2026-08-22
tags: [service-boundaries, cashflow-lifecycle, cashflow-netting, architecture]
related: [cashflow-auto-netting, ratan-cashflow-lifecycle-state-machine, netting-resultant-cashflow, netting-un-net-lifecycle, lifecycle-service, netting-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Refactor Netting & Status Move Process.md"]
---
# Netting and Lifecycle Service Separation

## Definition

Netting and lifecycle service separation is the proposed architectural boundary between:

- Maintaining the lifecycle status of an individual cashflow.
- Orchestrating netting operations that create or reverse resultant cashflows and manage their component cashflows.

The boundary is intended to prevent generic status transitions from implicitly performing netting-specific business logic.

## Proposed Ownership

### Lifecycle Service

The [[lifecycle-service]] is proposed to own:

- `initializeCashflow`, including generation of the cashflow Stella message event.
- `updateStatus`, which changes an individual cashflow status from X to Y.

### Netting Service

The [[netting-service]] is proposed to own:

- `net` for manual and automatic netting.
- Resultant-cashflow generation.
- Component-cashflow status updates.
- `unnet` for reversing a resultant cashflow.
- `netRuleCheck`.
- `renet` for incomplete net requests.
- Event-driven component-cashflow status management.

## Rationale

The source identifies the existing update cashflow status API as complex, slow in production incidents, and responsible for multiple concerns. Separating responsibilities is intended to support:

- Smaller and more targeted transactions.
- Easier understanding of individual status transitions.
- More isolated testing.
- Lower regression impact when netting logic changes.
- Action-specific status behavior through a template-mode design.

The source does not establish that the proposed architecture has achieved these outcomes.

## Domain Relationship

A netting operation combines component cashflows into a resultant cashflow. The resultant continues through settlement, while component cashflows become `netted` and stop flowing independently. This relationship means that service separation must define how lifecycle transitions and netting side effects remain coordinated.

The proposal does not specify whether resultant and component updates are atomically consistent or intentionally eventually consistent.

## Limitations

The service boundary is clearer than the legacy arrangement, but the Netting Service still contains several independently changing responsibilities: orchestration, reversal, rule checking, recovery, and event-driven status synchronization. Further decomposition may be appropriate if operational or ownership boundaries diverge.

The source also omits API contracts, transaction scopes, invalid-transition behavior, idempotency, retry handling, and failure compensation.

## Related Concepts

- [[concepts/cashflow-auto-netting]]
- ratan cashflow lifecycle state machine
- [[concepts/netting-resultant-cashflow]]
- [[concepts/netting-un-net-lifecycle]]
- [[concepts/pending-auto-netting-state]]