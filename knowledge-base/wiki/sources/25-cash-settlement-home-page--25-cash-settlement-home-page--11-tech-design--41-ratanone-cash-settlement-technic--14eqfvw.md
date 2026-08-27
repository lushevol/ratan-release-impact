---
type: source
title: Uber Development Testing
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, uber, integration-testing, api-migration, netting, schema-evolution]
related: [uber, scbml, uber-restructured-workflow-integration, uber-restructured-flow-vs-scbml-legacy-flow, what-is-the-authoritative-uber-lifecycle-api-routing-contract, does-netnew-automatically-publish-to-process-in-for-uber, which-cash-settlement-actions-publish-domain-events-versus-process-messages, what-is-the-authoritative-uber-schema-compatibility-policy, which-service-owns-the-fail-action-for-uber-cashflows]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing.md"]
authors: []
year: 2025
url: ""
venue: ""
---
# Uber Development Testing

This document is an integration-test plan and issue record for Uber adoption of the restructured RATAN cash-settlement workflow. It covers environment allocation, lifecycle API migration, schema compatibility, planned business cases, ownership of user actions, and unresolved routing responsibilities.

The document is not a complete acceptance record: detailed execution evidence is present for only selected cases. Proposed API behaviour marked “Need confirm” remains unapproved.

## Environment allocation

| Ratan Env | VPN | Blade | TDS3 index |
| --- | --- | --- | --- |
| DEV | QA2 | **Dev3** | sit |
| UAT4 | QA1 | **Dev7: Markets** | fmrp1 |

The source identifies `q-51358-ratanone-uber-msg` as the relevant queue. Internal dashboard URLs and password-access instructions are intentionally not reproduced here; they belong in access-controlled operational documentation.

## Workflow API integration inventory

| Service / old URL | New URL | Notes |
| --- | --- | --- |
| `51358-ratan-cashflow-lifecycle-service` — `/v1/ratan/cashflow/query` | Keep Same | NA, lifecycle need enhance |
| `/v1/ratan/camunda/lifecycle/update/status`; `/v2/ratan/lifecycle/update/status/batch/transactional`; `/v1/ratan/cashflow/user/status/update` | `/v2/ratan/camunda/lifecycle/status/move` | Need confirm: user actions such as `ResendToRazor`, `ReGenerateSwift`, and `EarlyRelease` cause lifecycle to publish no data except a domain event. |
| `/v1/ratan/lifecycle/update/status` | `/v2/ratan/camunda/lifecycle/status/move` | Consolidate this to the only API for Camunda request. |
| `/v1/ratan/lifecycle/update/status/batch` | Removed | |
| `/v1/cashflow/holding/disable` | Keep same | NA |
| `/ratan/camunda/cashflow/preCheck` | `/v2/ratan/camunda/cashflow/preCheck` | Need confirm: do not calculate cutoff; do not auto-materialize; do not publish to `process_in`; validate mandatory fields and persist data if validation passes. |
| `/v1/cashflow/cutoffs/calculate` | Removed | |
| `/v1/ratan/camunda/lifecycle/msgEventCheck` | Removed | |
| `/v1/ratan/camunda/cashflow/stamp` | `/v2/ratan/camunda/cashflow/stamp` | Need confirm whether stamping runs when mandatory fields are missing, returns the remaining-mandatory-field result, and causes `TechFail` when fields remain missing. |
| `/v1/cashflow/camunda/holding-check` | `/v1/cashflow/camunda/holding` | Need confirm whether workflow releases directly through a subflow or saves a holding record through lifecycle. |
| `/v2/ratan/lifecycle/update/status/batch/transactional` | `/v2/ratan/cashflow/init/move/status` | Used by [[netting-service]]. |
| `51358-ratan-rule-service` — `/v1/nstpException/batchClose` | Removed | |
| `/v1/nstpException/close` | Keep Same | |
| `/v1/suppressionRule/check` | Keep Same | |
| `/v1/swiftSuppressionRule/check` | Keep Same | |
| `/v1/netting/rules/checkIrsRule` | Keep Same | |
| `/v1/netting/rules/checkNettingRule` | Keep Same | |
| `/v1/nstpRule/check` | Keep Same | |
| `51358-ratan-cash-settlement-ssi-stamping-service` — `/v1/stamping/cashflow/exception/batchClose` | Keep Same | |
| `/v1/stamping/cashflow/exception/close` | `/v2/stamping/cashflow/exception/close` | |
| `/v1/stamping/cashflow/enrich` | `/v2/stamping/cashflow/accounting/enrich` | |
| `51358-ratan-cash-settlement-netting-service` — `/v1/netting/camunda/autoUnNet` | Keep Same | |
| `/v1/netting/camunda/checkPaymentDateForIRS` | Keep Same | |
| `/v1/netting/camunda/netForIRS` | Keep Same | |
| `51358-mfe-cashflow-blotter` — `/v1/ratan/cashflow/user/status/update` | `/v2/ratan/cashflow/move/status/user` | |

## Schema-change compatibility cases

The stated upgrade principle is: **Only need to upgrade if any required fields change.** The source also states that Group Management Service and lifecycle service upgrades are required for every schema change, while other upgrades are on demand.

| Case No. | Flow | Data Model | Case Description | Downstream Behavior | Downstream upgrade required | Core Logic |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | TDSX → Ratan | Proto Buffer → JSON | Upstream(TDSX) add new attribute `testField` and upgrade schema V2; downstream(Ratan) still uses V1 | miss information in V1 processing no exceptions | If field is required then yes, otherwise nice to have | `TDSXUberMessage tdsxUberMessage = TDSXUberMessage.parseFrom(byteArr);` `String json = ProtobufUtils.toJson(tdsxUberMessage);` |
| 2 | TDSX → Ratan | Proto Buffer → JSON | Upstream(TDSX) remove `Netting_Id` and upgrade schema V2; downstream(Ratan) still uses V1 | upstream will not send this information no exceptions | No need | |
| 3 | TDSX → Ratan | Proto Buffer → JSON | Change attribute type from String to Integer | miss information in V1 processing no exceptions | If field is required then yes, otherwise nice to have | |
| 4 | TDSX → Ratan | Proto Buffer → JSON | Change attribute type from Integer to String | miss information in V1 processing; Int value will change to `0` (default) | If field is required then yes, otherwise nice to have | |
| 5 | TDSX → Ratan | Proto Buffer → JSON | Change attribute type from Array to Single | No information loss; old-schema array size is always 1 | No need | |
| 6 | TDSX → Ratan | Proto Buffer → JSON | Change attribute type from Single to Array | Might have information loss; if array size is greater than 1, only the last element will be picked, with no exceptions | If field is required then yes, otherwise nice to have | |
| 7 | Ratan → Ratan | JSON → Proto Object → JSON | Upstream producer adds `testField` and upgrades schema V2; downstream consumer remains V1 | miss information in V1 processing no exceptions | If field is required then yes, otherwise nice to have | `Cashflow cashflowV1 = ProtobufUtils.toProtobuf(json, Cashflow.class);` `String jsonV1 = ProtobufUtils.toJson(cashflowV1);` |
| 8 | Ratan → Ratan | JSON → Proto Object → JSON | Upstream removes `Netting_Id` and upgrades schema V2; downstream remains V1 | downstream will not send this information no exceptions | No need | |
| 9 | Ratan → Ratan | JSON → Proto Object → JSON | Change attribute type from String to Integer | No information loss | No need | |
| 10 | Ratan → Ratan | JSON → Proto Object → JSON | Change attribute type from Integer to String | miss information in V1 processing no exceptions | If field is required then yes, otherwise nice to have | |
| 11 | Ratan → Ratan | JSON → Proto Object → JSON | Change attribute type from Array to Single | No information loss; old-schema array size is always 1 | No need | |
| 12 | Ratan → Ratan | JSON → Proto Object → JSON | Change attribute type from Single to Array | If array size is 1, no information loss; if greater than 1, exception: `Array must have size 1, but has size 2` | Required | |

These behaviours are source assertions that require test validation before being treated as a production compatibility policy. See [[what-is-the-authoritative-uber-schema-compatibility-policy]].

## Evidenced test cases and defects

### Case 1: Pending Another Leg and IRS netting

| Step | Action | Expected | Cashflow Id |
| --- | --- | --- | --- |
| 1 | Publish JSON to `Cash_Settlement_Orchestration_Inbound_Uber_1` | `WAITING + Pending Operator + Pending Another Leg` | `CH6800724451` |
| 2 | Publish another JSON with the same trade ID; automatic netting occurs | `NETTED + NA + NA` | `CH6800724450`, `CH6800724451`, `N00000003845` |
| 3 | Check the netting resultant | `SETTLED + NA + NA` | `N00000003845` |

**Critical issue:** the `NetNew` message requires manual publication to a Kafka topic. The source records this as a gap, but does not include a trace, offset, or root-cause analysis. See [[does-netnew-automatically-publish-to-process-in-for-uber]].

### Case 2: Maker-checker with `MISSING_VOSTRO_ERRO` and Pending Affirmation

| Step | Description | Expected | Cashflow Id |
| --- | --- | --- | --- |
| 1 | Cashflow inbound and hits SSI and NSTP rule | `WAITING + Pending Exception + Pending Operator` | `C06810144246` |
| 2 | Maker submit | `WAITING + Pending Exception + Pending Verification` | `C06810144246` |
| 3 | Checker reject | `WAITING + Pending Exception + Pending Operator` | `C06810144246` |

**Critical issue:** Swift service calls a legacy lifecycle API that is not Uber-supported and must call an appropriate lifecycle API.

### Other recorded case-level issues

| Case | Subject | Recorded issue |
| --- | --- | --- |
| 2.1 and 2.2 | Early and auto release | Holding-check API issue; Query Service UI-display issue; a maker can still edit after submit. |
| 3 | Bilateral netting | UI calls an old netting API that supports only SCBML. |
| 4 | Manual UnNetting | UI calls an old UnNetting API that supports only SCBML; Query Service component cashflow query returns empty results. |
| 5.1 | Auto UnNetting | Withdrawal inbound on netting resultant is not post-released. |
| 6 | Cashflow suppress / manual unsuppress | Unsuppress does not publish to `process_in`. |
| 7 | Swift suppress / manual Swift unsuppress | Unsuppress does not publish to `process_in`; passed value-date accounting is not sent and UI does not display it. |
| 8 | Manual Fail / Reinstate | Orchestration status-update API needs change. |
| 9 | Trade validation | Trade ID: `CH6672555548`. |

## Action ownership inventory

| Cashflow Action | Domain Client/UI | API provider | Comments |
| --- | --- | --- | --- |
| Comment | UI | lifecycle | |
| EarlyRelease | UI | lifecycle | |
| Hold | UI | lifecycle | |
| UnHold | UI | lifecycle | |
| ReGenerateSwift | UI | lifecycle | |
| ReInstate | UI | lifecycle | |
| ReplayStatusWriteBack | UI | lifecycle | |
| ResendToRazor | UI | lifecycle | |
| ManualAffirmed | UI | lifecycle | |
| ManualSuppress | UI | lifecycle | |
| ManualSwiftSuppress | UI | lifecycle | |
| ManualSwiftUnSuppress | UI | lifecycle | |
| ManualUnSuppress | UI | lifecycle | |
| Materialize | UI | lifecycle | Early materialize / Auto materialize |
| SettleAsGross | UI | lifecycle | |
| Submit | UI | orchestration | |
| ApproveOnlyMaker | UI | orchestration | |
| Approve | UI | orchestration | Suppress, Unsuppress verify Multi exception approve |
| Reject | UI | orchestration | |
| Fail | UI | ?? | ?? |
| Net | UI netting | Netting | |
| UnNet | UI netting | Netting | |
| GenerateSwift | orchestration | | |
| CashflowStamped | orchestration | | |
| IsNettingEligible | orchestration | | |
| IsNstp | orchestration | | |
| IsNstpChecker | orchestration | | |
| NetNew | netting | | |
| New | lifecycle | | |
| NostroStamped | ssi stamping | | |
| PaymentDateUpdate | rule service | | |
| Release | swift lifecycle | | |
| RevertToQueued | orchestration group | | |
| SentToRazor | orchestration | | |
| Settle | swift lifecycle | | |
| SsiStamped | ssi stamping | | |
| Suppress | orchestration | | |
| SwiftSuppress | orchestration | | |
| SwiftUpdate | swift | | |
| TechFail | orchestration lifecycle | | |
| ValidateDirect | orchestration | | |
| VostroStamped | ssi stamping | | |
| WaitingAnotherLeg | netting | | |
| Withdrawal | lifecycle | | |
| AccountingUpdate | accounting service | | |
| Affirmed | rule netting | | |

The inventory identifies intended ownership, not verified implementation status. In particular, `Fail` has no identified API provider.

## Open items

1. Determine handling of `Cash_Settlement_Ssi_Notify_Orchestration_In` and `Cash_Settlement_User_Task_Orchestration_In`.
2. Determine whether `RevertToQueued` and `Reinstate` publish to `process_in` through the Uber or legacy flow.
3. Determine how a new UI flow routes SCBML traffic to the legacy flow while preserving transactional operations such as manual netting.
4. Determine whether Query Service needs domain-event-specific logic.
5. Determine how batch jobs such as materialize and release select Uber/restructured versus legacy processing.
6. The source includes an image-only item without sufficient textual detail to classify.

## Related pages

- [[uber-restructured-workflow-integration]]
- [[uber-restructured-flow-vs-scbml-legacy-flow]]
- [[cashflow-lifecycle-state-machine-restructuring]]
- [[schema-evolution-for-cash-settlement]]
- [[netting-service]]
- [[what-is-the-authoritative-uber-lifecycle-api-routing-contract]]
- [[does-netnew-automatically-publish-to-process-in-for-uber]]
- [[which-cash-settlement-actions-publish-domain-events-versus-process-messages]]
- [[what-is-the-authoritative-uber-schema-compatibility-policy]]
- [[which-service-owns-the-fail-action-for-uber-cashflows]]