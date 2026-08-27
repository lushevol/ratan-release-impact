---
type: entity
title: Netting Service
created: 2026-08-22
updated: 2026-08-24
tags: ["service", "cashflow-auto-netting", "rat​​an", "rest-api", "application-service", "cashflow-netting", "resultant-cashflow", "component-cashflow", "netting", "cash-settlement", "CCIL", "IRS", "fixing-flag", "RATANONE", "cashflow", "aggregation", "settlement"]
related: ["ratan", "cashflow-auto-netting", "auto-netting-rule-check", "auto-netting-persistence-model", "control-m", "rule-service", "netting-and-lifecycle-service-separation", "netting-resultant-cashflow", "netting-un-net-lifecycle", "pending-auto-netting-state", "event-driven-component-cashflow-status-management", "ccil-netting", "settlement-method-driven-netting", "cash-settlement-platform", "batch-service", "lifecycle-service", "fixing-flag-notification-processing", "pending-fixing-and-waiting-another-leg", "ratan-cash-settlement-orchestration", "cashflow-netting", "resultant-cashflow-generation", "netting-eligibility", "maker-checker-netting", "cashflow", "normalized-payment-schedule", "product-agnostic-cashflow-aggregation", "normalized-payment-schedule-completeness-check", "what-is-the-authoritative-auto-aggregation-completeness-and-idempotency-contract", "what-is-the-canonical-fee-and-asgross-exclusion-semantics-for-auto-aggregation"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Technical Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Refactor Netting & Status Move Process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/CCIL Netting Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Fixing flag notification.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Product Agnostic Aggregation Design.md"]
---

# Netting Service

## Role and Status

Netting Service is described as the application-service entry point for cashflow netting and as the service owning auto-netting workflow integration.

The **Netting Service Design** source describes it as a proposed RATANONE service for controlled cashflow netting, unnetting, validation, and splitting. Its focus is netting operations rather than the full cash-settlement orchestration domain, although it is adjacent to [[ratan-cash-settlement-orchestration]].

The **Refactor Netting & Status Move Process** source presents Netting Service as a proposed responsibility boundary and does not confirm deployment or implementation status. The **CCIL Netting Design** source likewise describes it as the proposed execution and review layer for CCIL netting.

The **Product Agnostic Aggregation Design** source separately describes Netting Service as the proposed owner of automatic cashflow aggregation processing. That draft-specific aggregation responsibility should not be treated as confirmation that the broader service boundary has been implemented.

The service manages relationships between resultant cashflows and their component cashflows.

The **Fixing flag notification** source separately describes Netting Service as a proposed component that evaluates whether an IRS cashflow satisfies the waiting-fixing-flag rule. This source-specific role concerns IRS rule evaluation and does not establish that the service owns the resulting lifecycle-state transition.

## Core Responsibilities and Functions

Across the sources, the proposed responsibilities include:

- Accept `NET`, `UNNET`, and `SPLIT` operations.
- Perform manual or automatic netting.
- Generate resultant cashflows by aggregating component amounts.
- Manage relationships between component and resultant cashflows.
- Validate proposed requests and check netting eligibility.
- Apply status and sub-status changes.
- Enforce a maker/checker control.
- Write status updates back to STELLA.
- Update component-cashflow status following netting or unnetting.
- Support recovery of incomplete netting requests.
- Integrate with auto-netting rules, workflows, scheduling, and persistence.

The **Refactor Netting & Status Move Process** source specifically identifies the following functions:

| Function | Responsibility |
|---|---|
| `net` | Perform manual or automatic netting, generate a resultant cashflow, and update component-cashflow status. |
| `unnet` | Unnet a resultant cashflow and update component-cashflow status. |
| `manageComponentCashflowStatus` | Consume `cash_settlement_cashflow_domain_events` and update component-cashflow status when required. |
| `netRuleCheck` | Check whether a cashflow matches netting rules. |
| `renet` | Find incomplete cashflow net requests and regenerate resultant cashflows. |

The **Auto Netting Technical Design** source assigns the following workflow-integration responsibilities:

- Interact directly with the Rule Engine API for auto-netting rule management.
- Provide the Auto Netting Rule Check API used by Camunda.
- Provide the scheduled auto-netting job endpoint triggered by Control-M.
- Refresh cashflows after an auto-netting rule changes.
- Persist proposed auto-netting cashflow and configuration records.

## Domain Scope

A netting operation combines two or more component cashflows into a resultant cashflow. After successful netting, component cashflows become `netted` and stop flowing independently, while the resultant cashflow continues until settlement.

The **Refactor Netting & Status Move Process** source assigns both netting orchestration and component-status management to Netting Service, while [[lifecycle-service]] owns generic individual-cashflow status transitions.

The **Netting Service Design** source additionally proposes splitting as an accepted operation. The available sources do not define how `SPLIT` operates, its resulting cashflow relationships, or its status-transition behavior.

## Product-Agnostic Automatic Aggregation

The following behavior is described specifically in the **Product Agnostic Aggregation Design** draft.

For each candidate cashflow, Netting Service is intended to:

1. Derive an expected eligible-leg count from [[normalized-payment-schedule]].
2. Fetch cashflows by `tradeId`.
3. Filter the fetched cashflows by currency and payment date.
4. Exclude `"AsGross"` cashflows from the received-leg count.
5. Move processing to “pending another leg” when the expected count exceeds the received count.
6. Otherwise perform automatic aggregation.

Fee cashflows are separately said to bypass aggregation, while Fee schedule entries are excluded from the expected count. The complete predicates and exact Fee matching semantics are not specified.

This draft states that Netting Service is the proposed owner of this automatic aggregation processing. It does not establish that this product-agnostic aggregation flow is identical to the auto-netting `netRuleCheck` flow described in the **Auto Netting Technical Design**. The sources do not state whether the two flows use the same API, rule engine, persistence model, or implementation.

### Draft Contract Gaps

The **Product Agnostic Aggregation Design** is draft design intent only. It does not define:

- Persistence behavior.
- Idempotency.
- Concurrency control.
- An over-count path.
- Error recovery.
- The exact transition represented by “pending another leg.”

These gaps are tracked in [[what-is-the-authoritative-auto-aggregation-completeness-and-idempotency-contract]] and [[what-is-the-canonical-fee-and-asgross-exclusion-semantics-for-auto-aggregation]].

## IRS Waiting-Fixing-Flag Evaluation

According to the **Fixing flag notification** source, Netting Service must:

- Call an IRS check API.
- Determine whether an IRS cashflow matches the waiting-fixing-flag rule.

The result is associated with the distinction between `PendingFixing` and `WaitingAnotherLeg`. The source does not establish whether Netting Service owns the final lifecycle-state decision or only supplies a rule-evaluation result to [[lifecycle-service]].

This IRS check responsibility is described separately from the auto-netting `netRuleCheck` function. The sources do not state whether they use the same API, rule engine, or implementation.

For the IRS check API, the **Fixing flag notification** source does not provide:

- API signature.
- Request or response schema.
- Error behavior.
- Timeout policy.
- Ownership of state mutation.

## CCIL Netting

According to the **CCIL Netting Design** source, CCIL settlement-method cashflows may allow different counterparties to participate in a netting operation. The resultant cashflow should use settlement method `CASH` rather than `CCIL`.

That design calls for a new controller supporting both CCIL netting execution and preview, while reusing existing service-layer netting functionality rather than building a separate netting engine.

The **CCIL Netting Design** source does not specify backend safeguards to prevent invalid mixing of normal and CCIL cashflows. It also does not specify controls for cross-counterparty authorization, auditability, reconciliation, or provenance.

## Design Considerations and Unresolved Contracts

Netting Service has a broad proposed scope covering:

- Netting orchestration and resultant-cashflow generation.
- Reversal through `unnet`.
- Splitting operations.
- Validation and netting-eligibility checks.
- Maker/checker control.
- Status and sub-status changes, including updates written back to STELLA.
- Rule evaluation.
- Recovery through `renet`.
- Event-driven synchronization of component-cashflow status.
- Auto-netting workflow integration.
- Persistence of proposed auto-netting cashflow and configuration records.
- Product-agnostic automatic aggregation as described in the separate draft.
- CCIL netting execution and preview through a new controller that reuses existing service-layer netting functionality.
- IRS waiting-fixing-flag rule evaluation through an IRS check API.

The sources do not state whether these functions should remain together or be decomposed into separate services.

The **Netting Service Design** source does not define the service API, package structure, transaction boundaries, authorization model, idempotency contract, or event-processing semantics. It should therefore be treated as a proposed component rather than an established production boundary.

Other unspecified netting behaviors include:

- Duplicate-resultant prevention.
- `renet` idempotency.
- Event retry and replay.
- Failure handling when resultant and component updates do not complete together.
- `SPLIT` request semantics and resulting cashflow lifecycle.

The **Auto Netting Technical Design** source states that the relationship between Netting Service and [[rule-service]] should be clarified if they represent separate components or different names for the same Rule Engine integration.

The **Product Agnostic Aggregation Design** source leaves the completeness, counting, exclusion, transition, persistence, idempotency, concurrency, and recovery contracts unresolved for its aggregation flow.

## Related Pages

- [[ratan-cash-settlement-orchestration]]
- [[netting-and-lifecycle-service-separation]]
- [[event-driven-component-cashflow-status-management]]
- [[netting-resultant-cashflow]]
- [[resultant-cashflow-generation]]
- [[netting-un-net-lifecycle]]
- [[netting-eligibility]]
- [[maker-checker-netting]]
- [[pending-auto-netting-state]]
- [[ccil-netting]]
- [[settlement-method-driven-netting]]
- [[cash-settlement-platform]]
- [[fixing-flag-notification-processing]]
- [[pending-fixing-and-waiting-another-leg]]
- [[normalized-payment-schedule]]
- [[product-agnostic-cashflow-aggregation]]
- [[normalized-payment-schedule-completeness-check]]
- [[what-is-the-authoritative-auto-aggregation-completeness-and-idempotency-contract]]
- [[what-is-the-canonical-fee-and-asgross-exclusion-semantics-for-auto-aggregation]]