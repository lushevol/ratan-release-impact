# Rebook duplicate-payment control: Payment Type impact analysis

Generated: 2026-08-25

## Executive verdict

**NO-GO for implementation or release; desired behavior is NOT PROVEN.**

**Analysis scope:** this repository is an impact-analysis harness. This exercise verifies whether the requirement-analysis workflow produces a correct, evidence-backed contract. It is not authorization to implement the Rebook change, and no production behavior is being changed.

The current repository contains two active Rebook decision paths that select candidate cashflows by original/trade ID and settlement currency, then tag the incoming `New` cashflow as `Rebook` when any selected history is within `incoming value date - 5 days` and belongs to the application's broader post-release status set. This reading is **CONFIRMED** by exact source and GitNexus call-graph evidence.

The proposed “limit to Payment Type” behavior is not present. The Wiki material inspected does not define Payment Type as the approved replacement predicate, its allowed values, null policy, or whether currency and the five-day window remain. Existing code parses SCBML `paymentType` into a field named `settlementType`, which raises a naming/contract risk. The relevant tests could not execute because the private parent POM `com.scb.ratan:ratanone-dependencies:8.0.2` is unavailable from the configured Maven repository.

## Normalized rules

### Current implementation (confirmed)

For an incoming event `n`, tag `Rebook` when all of the following hold:

1. `n.eventType == New`.
2. Candidate `o` shares `originatingTradeId` with `n` for Murex, otherwise shares `tradeId`.
3. `o.settlementCurrency == n.settlementCurrency`.
4. A history row for a candidate cashflow has `valueDate >= n.settlementDate - 5 calendar days`.
5. That history row maps to `CashflowStatus.getPostReleasedStatus()`.

This is not exactly the prose “any cashflow RELEASED in VD-5”: code includes the domain's broader post-release status set, and it applies a lower date bound without an observed upper bound. A future-dated candidate may therefore satisfy the repository query unless another invariant prevents it upstream.

### Desired rule (unresolved)

The narrowest plausible interpretation is to replace condition 3 with:

`o.paymentType == n.paymentType`

This is only a proposal. The following must be decided before coding:

- Does Payment Type replace currency only, replace the five-day rule, or add to both?
- Is the authoritative value SCBML `conf:paymentType`, the persisted `settlement_type`, settlement method, payment direction, or another business taxonomy?
- Are comparisons exact, normalized, hierarchical, or grouped by an approved taxonomy?
- What happens for blank, absent, unknown, or newly introduced values?
- Should the status predicate be exactly `RELEASED`, or the existing released/settled/netted/pending-ack combinations?
- Must the prior value date also be `<=` the incoming value date?
- Is matching by original/trade ID retained? Without it, unrelated payments of the same type would collide.

## Current execution flow

1. Camunda calls [`CashflowDuplicateCheckController.java`](../../repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/controller/CashflowDuplicateCheckController.java) through `POST /ratan/camunda/cashflow/preCheck` or `POST /v2/ratan/camunda/cashflow/preCheck`; the deprecated `/eventSplit` endpoint reaches the same legacy service path.
2. [`CashflowDuplicateCheckService.java`](../../repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/service/CashflowDuplicateCheckService.java) parses the incoming event and invokes its private `reversalOrRebook` implementation.
3. The lifecycle processor route independently invokes the protected implementation in [`AbstractCashflowActionProcessor.java`](../../repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/processor/AbstractCashflowActionProcessor.java) from the New/Withdrawal init and status-move processors.
4. [`RatanCashflowDetailsRepository.java`](../../repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/domain/repository/RatanCashflowDetailsRepository.java) selects cashflow IDs with the same original/trade ID and currency.
5. [`RatanHistoryRepository.java`](../../repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/domain/repository/RatanHistoryRepository.java) filters candidate history rows by value date and evaluates the post-release status set.
6. `Rebook` is written into the event reason. The legacy pre-check path also emits its audit event to Kafka.

## Impact surface

### Repository and components

- Primary repository: `repos/ratan-cashflow-lifecycle-service/` — **CONFIRMED**.
- API entrypoints: [`CashflowDuplicateCheckController.java`](../../repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/controller/CashflowDuplicateCheckController.java).
- Duplicate-check service: [`CashflowDuplicateCheckService.java`](../../repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/service/CashflowDuplicateCheckService.java).
- Lifecycle processors: [`lifecycle/processor/*NewAndWithdrawal*.java`](../../repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/processor/).
- Candidate and status repositories: [`lifecycle/domain/repository/Ratan*Repository.java`](../../repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/domain/repository/).
- Input/persistence model: [`RatanStellaMessageEvent.java`](../../repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/entity/RatanStellaMessageEvent.java) and [`XpathResult.java`](../../repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/feign/dto/XpathResult.java). SCBML `paymentType` maps to Java `settlementType`.
- No other repository is confirmed as requiring a code change. SDLC semantic expansion returned broad candidates, but no concrete cross-repository runtime edge established ownership of this decision.

### Database dependencies

These tables are established from runtime mappers/query clients, not migration SQL:

- `ratan_stella_message_event_source`: candidate selection by original/trade ID, currency today, and potentially persisted `settlement_type` for the future predicate. Runtime mapper: [`RatanStellaMessageEventMapper.xml`](../../repos/ratan-cashflow-lifecycle-service/src/main/resources/mapperxml/RatanStellaMessageEventMapper.xml).
- `ratan_cashflow_scbml_history`: value-date and post-release status lookup. Runtime MyBatis-Plus mapper/query: [`RatanCashflowScbmlHistoryMapper.xml`](../../repos/ratan-cashflow-lifecycle-service/src/main/resources/mapperxml/mybatisplus/RatanCashflowScbmlHistoryMapper.xml) and `RatanHistoryRepository`.

No schema migration is proven necessary: `settlement_type` is already represented and populated, but data completeness/cardinality must be profiled before relying on it as a control key.

### Kafka dependencies

- `Common_Event_Record_In`: configured as `kafka.eventRoute`; the legacy duplicate-check service publishes the pre-check audit event here. Source: [`application.yml`](../../repos/ratan-cashflow-lifecycle-service/src/main/resources/application.yml) and `CashflowDuplicateCheckService.publishEvent`.
- `Cash_Settlement_Orchestration_Process_In`: downstream STP trigger used by the lifecycle route. Source: [`CashflowStpHandler.java`](../../repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/domain/event/handler/CashflowStpHandler.java) and lifecycle configuration.

The Rebook predicate itself performs database reads and does not directly consume or produce Kafka. The topics above are surrounding transport dependencies; changing the predicate should not change their contracts unless the event-reason taxonomy is validated with consumers.

## GitNexus blast radius

The indexed root graph was at commit `3f2ac84`, so scores are strong code-structure evidence but not a fresh-index release gate.

- `getCashflowIdsUnderSameOriginalTradeIdAndSameCurrency`: **CRITICAL**, 50 impacted symbols, 12 direct, 2 processes, 5 modules.
- `existCashflowsPostReleasedWith5Days`: **CRITICAL**, 48 impacted symbols, 10 direct, 2 processes, 5 modules.
- `CashflowDuplicateCheckService.reversalOrRebook`: **HIGH**, 31 impacted symbols, 1 direct, 2 processes, 3 modules.
- `AbstractCashflowActionProcessor.reversalOrRebook`: **MEDIUM**, 10 impacted symbols, 7 direct, 2 modules.

The two detected processes are the controller/service `eventSplit` family and `initializeStellaEvent`. The duplicated Rebook implementations create divergence risk: changing only one route would produce inconsistent tagging.

## Proposed change shape (not authorization to implement)

1. Define a single domain-level Rebook candidate specification shared by legacy and lifecycle routes.
2. Rename or document the `paymentType` → `settlementType` mapping before using it as a control predicate; avoid introducing a second competing field.
3. Change candidate matching only after the business decisions above are approved. Prefer an explicit new repository method over silently changing a method whose name promises same currency.
4. Add observability that records which predicate matched without logging sensitive payment data.
5. Compare old and new decisions in shadow mode against labeled genuine-rebook/false-positive cases before enforcement.

## Verification matrix

At minimum, executable tests must cover:

| Case | Expected result |
|---|---|
| Same trade identity, same Payment Type, qualifying status, VD exactly -5 | Rebook, if boundary is inclusive |
| Same identity/type/status, VD -6 | Not Rebook, if five-day rule remains |
| Same identity/type/status, future value date | Not Rebook, unless explicitly approved |
| Same identity/status/window, different Payment Type | Not Rebook |
| Same identity/status/window/type, different currency | Decision required: proves whether CCY was removed |
| Same type/status/window, different trade identity | Not Rebook |
| Same identity/type/window, Projected/Queued only | Not Rebook |
| Released versus Settled/Netted/Pending Ack variants | Exact approved status matrix |
| Missing/blank Payment Type on new or prior cashflow | Explicit safe behavior; no accidental blank-to-blank match |
| Murex versus non-Murex identity selection | Correct original/trade ID key |
| Both legacy and lifecycle routes | Identical reason result |
| Database integration with real mapper criteria | Correct columns and date bounds |
| API-to-persistence-to-Kafka integration | Reason survives full transport without contract break |

Observed test attempt:

```text
mvn -Dtest=RatanHistoryRepositoryTest,RatanCashflowDetailsRepositoryTest,CashflowNewAndWithdrawalActionStatusMoveProcessorTest,CashflowNewAndWithdrawalActionInitProcessorTest test
```

Result: **not executed**. Maven could not resolve private parent POM `com.scb.ratan:ratanone-dependencies:8.0.2` from Central. Existing tests also mock the two repository predicates in processor tests and are named “30Days” while invoking the five-day method, reducing their value as proof of date and matching semantics.

## Evidence ledger

| Assertion | Grade | Evidence | Limitation |
|---|---|---|---|
| Current match uses original/trade ID + currency | CONFIRMED | `RatanCashflowDetailsRepository` exact query builder; GitNexus callers | No production data sample |
| Current window is incoming VD minus five days | CONFIRMED | `RatanHistoryRepository` exact query builder; Wiki deployment note | No observed upper bound; timezone uses JVM default |
| Current status is broader than literal RELEASED | CONFIRMED | `CashflowStatus.getPostReleasedStatus()` call and repository tests | Full business approval of set not established |
| Payment Type is available in input/persistence model | CONFIRMED | `XpathResult.paymentType` XPath stored as `settlementType`; mapper/entity | Completeness and taxonomy unmeasured |
| Payment Type is the approved future discriminator | UNRESOLVED | User requirement only | Wiki search found no authoritative definition/approval |
| Lower exception volume proves better accuracy | UNRESOLVED | Wiki reports volume reduction after five-day change | No labeled false-positive/false-negative ground truth |
| Future behavior works | UNRESOLVED / NOT PROVEN | No implementation; tests unavailable | Private build dependency and missing acceptance decisions |

## Evidence required for GO

1. Product/control-owner approval of the normalized predicate, including whether currency and five-day limits remain and the exact status/date semantics.
2. Authoritative Payment Type taxonomy and source-of-truth field, plus null and normalization policy.
3. Data-quality profile for `ratan_stella_message_event_source.settlement_type` and labeled original/replacement samples.
4. Corporate Maven repository access and a green execution of the matrix above at unit, database-integration, and API/transport layers.
5. A fresh GitNexus index and `detect_changes` result for the implementation commit.
6. Shadow-run precision/recall against labeled outcomes, with rollback thresholds and monitoring ownership.

## Requirement-grill restart (2026-08-25)

LLM Wiki was queried first using the supplied requirement. The authoritative background pages are `wiki/concepts/rebook-exception.md` and `wiki/concepts/payment-date-proximity-matching.md`, sourced from the Settlement Day 2 functional requirement. They establish that the deployed control is a heuristic for a possible amendment rebook, not proof of original-to-replacement lineage.

The Wiki baseline is more precise than the supplied wording:

- candidate identity is the applicable Trade ID, with Murex using Original Trade ID;
- candidate currency must match;
- the prior cashflow is documented as **released or settled**, not strictly `RELEASED`;
- the deployed window is five **business-calendar days**, after a prior 15-day window;
- endpoint inclusivity is not documented;
- no authoritative Payment Type taxonomy or currency-to-Payment-Type migration rule was found.

The requirement owner has resolved the material decisions for this analysis:

- comparator status: `RELEASED` or `SETTLED`;
- window: five business days, inclusive at both endpoints;
- future discriminator: Payment Type replaces same-currency matching;
- source of truth: SCBML Payment Type;
- missing, blank, or unknown Payment Type: throw an exception.

The resulting contract is clear enough for impact analysis. It remains intentionally **not an implementation authorization**.

### SDLC Graph position

SDLC Graph was used as a bounded architecture cross-check. Its requirement search produced many lexical false positives and unresolved external frontiers, so its broad candidate count is not evidence that all returned repositories are impacted. Its service picture and dependency queries did provide useful corroboration for the lifecycle service, the two runtime tables, Kafka surroundings, and resolved calls to orchestration/netting/stamping services.

For this requirement, SDLC Graph is **secondary but useful**: retain it for cross-repository boundary discovery and dependency corroboration; do not use its semantic candidate list as the exact impact result. GitNexus must target the actual repository under `repos/`; the root harness index is not business-code evidence. In this run, the live GitNexus MCP did not have `ratan-cashflow-lifecycle-service` indexed, so no root-level blast-radius score is treated as authoritative.
