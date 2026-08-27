---
type: entity
title: ratan-cash-settlement-netting-service
created: 2026-08-22
updated: 2026-08-24
tags: ["microservice", "netting", "settlement", "hard-blocker", "ratan", "service", "cashflow-splitting", "cash-settlement", "backend-service", "resultant-cashflow", "un-netting"]
related: ["ratan-one", "netting-service", "swap-agent-coupon-interim-mtm-hard-blocker", "resultant-hard-blocker-stamping", "auto-netting-rule-check", "splitting-cashflow", "cashflow-splitting", "split-cashflow-persistence-and-lineage", "ratan-cashflow-lifecycle-service", "ratan", "hard-blocker-exception", "hard-blocker-go-live-checklist", "resultant-cashflow-hard-blocker-propagation", "swap-agent-hard-blocker", "ratanone-rule-service", "uber", "ratan-cash-settlement-orchestration", "automatic-un-netting-error-handling", "product-agnostic-cashflow-aggregation", "process-in-topic"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker Tech Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Tech Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker go live checklist.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/[Deprecated", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/Uber Dev Testing Question.md"] Hard Blocker Tech Analysis.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/Uber Dev Testing Question.md"]
---
# ratan-cash-settlement-netting-service

`ratan-cash-settlement-netting-service` is a Ratan microservice. The Hard Blocker Tech Design describes it as responsible for validating and executing specified Ratan cashflow netting requests. The deprecated Hard Blocker Tech Analysis describes it as responsible for enriching resultant cashflow data during netting. The Splitting Tech Design names it as a split-processing component, and the Hard Blocker go-live checklist identifies it as the Ratan cash-settlement netting service.

For the Uber integration, the Uber Dev Testing Question describes the service as the netting service involved in automatic un-netting.

## Hard-blocker request validation

For the `SWAP_AGENT` hard-blocker design, the service receives `murexProductStrategy` and `paymentType` in `NettingRequest`. According to the Hard Blocker Tech Design, it validates the combination before retrieving cashflow information from Lifecycle and rejects prohibited combinations with:

```java
NET_CASHFLOW_NOT_MATCH_RULE_ERROR(422, "700400422")
```

The Hard Blocker Tech Design attributes the implementation to:

- `HardBlockerProperties.java`
- `NettingRequest.java`
- `NettingService.java`
- `NettingDomainService.java`
- `new-cashflow.xml`
- `StampingCashFlowEntity.java`
- `NettingError.java`
- `application.yml`

It also stamps resultant cashflows with the hard-blocker marker described in [[resultant-hard-blocker-stamping]]. Source references to releases, pull requests, and pipelines provide implementation traceability but do not establish deployment or enablement.

## Deprecated resultant-cashflow enrichment analysis

The deprecated Hard Blocker Tech Analysis describes a separate expected role for the deprecated Swap Agent hard-blocker implementation: placing component-derived data onto resultant cashflows so [[ratanone-rule-service]] could evaluate the resulting hard-blocker rule.

The analysis references these SCBML fields:

```xml
<scb:hardBlockerComponentMurexStrategy th:text="${CashFLowInfo.Instrument_Common__Component_Murex_Product_Strategy}"></scb:hardBlockerComponentMurexStrategy>
<scb:hardBlockerComponentPaymentType th:text="${CashFLowInfo.Cashflow__Component_Payment_Type}"></scb:hardBlockerComponentPaymentType>
<scb:hardBlockerComponentType th:text="${CashFLowInfo.Cashflow__Component_Strategy_Payment_Hard_Blocker}"></scb:hardBlockerComponentType>
```

That source also associates the enrichment work with:

- `NettingDomainService.java`
- `StampingCashFlowEntity.java`

The final schema contract is unresolved. The final rule uses `Cashflow__Component_Strategy_Payment_Hard_Blocker`, while the recorded database migration maps the two separate component attributes. See [[resultant-cashflow-hard-blocker-propagation]].

## Go-live checklist requirements

The Hard Blocker go-live checklist requires deployment of the following version:

| Service | Version |
| --- | --- |
| `ratan-cash-settlement-netting-service` | `1.5.7` |

The checklist also requires searching `cash_netting_service.t_cashflow` for messages containing `hardBlockerComponentType` after `2025-09-27`:

```sql
select * from cash_netting_service.t_cashflow tc where tc.message like '%hardBlockerComponentType%' and tc.created_at > '2025-09-27';
```

No query result or deployment sign-off is included in the checklist source.

## Cashflow-splitting design

The Splitting Tech Design lists version `1.7.0` on branch `feature/settlement-day2-split-common`.

In the documented manual-split timeout test, this service:

1. Called Lifecycle status updates for parent and child cashflows.
2. Received a timeout and logged an error.
3. Resumed child processing after Lifecycle processing completed, through consumption of the parent cashflow domain event.

The Splitting Tech Design associates the service with the `cash_netting_service.splitting_cashflow` persistence schema. It does not explicitly assign database-write ownership or define transactional boundaries.

## Uber automatic un-netting

### Observed endpoint failure

The Uber Dev Testing Question records the following automatic un-netting endpoint:

```text
POST http://ratan-cash-settlement-netting-service/v2/netting/camunda/autoUnNet
```

The endpoint returned HTTP 500 with:

```json
{"status":500,"message":"No static resource v2/netting/camunda/autoUnNet.","data":null}
```

A separate execution reached `UnNettingService` and failed with `Payload must not be null`. The Uber Dev Testing Question treats these as distinct endpoint/routing and payload-validation failure modes.

### Scope

The Uber Dev Testing Question associates the automatic un-netting failures with:

- `N00000062630`
- `C06810140005`
- `C06810141005`

According to that source, manual un-netting is a separate flow and was reported as missing a Query Service call.