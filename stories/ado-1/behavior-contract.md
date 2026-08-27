# ADO-1 ReBook Payment Type Behavior Contract

Status: `BLOCKED ON REQUIREMENT DECISION`

Restarted at the requirement-grill gate: 2026-08-27

## Scope and Operating Constraints

- POC domains: ReBook (this story) and CCIL (outside this story).
- Execution mode: local simulation only.
- External authentication, remote APIs, database polling, and Kafka remain mocked.
- POC verification owner: project owner. Target SDLC verification owner: QA.
- Evidence model: capture `before` and `after` runs; do not overwrite a prior run.
- This gate may clarify the rule and design a target matrix. It must not change the
  ReBook simulator or target scenarios until the material decisions below are resolved.

## Requested Change

Requested-change source: `stories/ado-1/requirements.md:5-11`

The story describes the current control as a five-day, same-currency heuristic
and asks for an "additional limit to Payment Type." It also says a new cashflow
is tagged ReBook when "any cashflow RELEASED in VD-5" exists.

The word `additional` currently implies that currency remains a predicate. That
interpretation is not approved because it conflicts with a prior decision record.

## Evidence Retrieval Record

Retrieved: 2026-08-27

- Required OpenKB MCP retry: failed with `Transport closed`.
- Fallback used: `openkb --kb-dir knowledge-base status` plus exact local reads
  of previously discovered OpenKB pages.
- Citation classification for this restart: `openkb-cli/local-read`, not live
  OpenKB MCP retrieval.
- The CLI recognized `knowledge-base/` and reported the compiled wiki folders,
  but reported zero raw indexed documents. Therefore this restart uses exact
  page contents as evidence and does not claim that a fresh CLI search index was
  available.
- A search miss is not being used as proof that a Payment Type rule does not exist.

Exact business/design pages read:

- `knowledge-base/wiki/sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--1oyjh4.md:14-36`
  (`Ingenuine Rebook Exception in Ratan`) documents applicable Trade ID,
  Murex Original Trade ID, same currency, released or settled, and a five-day
  deployed proximity rule.
- `knowledge-base/wiki/concepts/rebook-exception.md:10-27` explains that ReBook
  detection is candidate selection, not authoritative amendment lineage.
- `knowledge-base/wiki/concepts/payment-date-proximity-matching.md:10-29`
  documents a configured five-day window but does not define calendar type,
  endpoint direction, or future-date behavior.
- `knowledge-base/wiki/queries/was-currency-validation-newly-enforced-in-the-may-30-2026-ratan-rebook-change.md:10-20`
  records historical uncertainty about when currency matching was enforced.
- `knowledge-base/wiki/queries/what-is-the-validated-precision-and-recall-of-the-five-day-ratan-rebook-rule.md:10-22`
  says lower exception volume is not validated precision or recall.

## Current Observed Behavior

The current implementation has two ReBook decision paths. Both select candidates
with the same identity and currency, then accept the new cashflow when any
candidate history row is at least `incoming value date - 5 calendar days` and
belongs to the code's post-release status set.

The date query has no upper bound. Static source therefore permits a comparator
whose value date is after the incoming value date. This is current code behavior,
not evidence that future-dated matching is intended or occurs in production.

### Current Predicate Table

| Field | Current operator | Value/source | Missing-data behavior | Evidence/owner |
|---|---|---|---|---|
| Event type | case-insensitive equality | `New` | Other event types do not enter ReBook matching | Current implementation |
| Identity for Murex | equality | `originatingTradeId` | Null behavior is not established by inspected tests | Business/design + current implementation |
| Identity for non-Murex | equality | `tradeId` | Blank Trade ID returns no candidates | Current implementation |
| Currency | equality | `settlementCurrency` | Null behavior depends on generated query semantics and is not proven | Business/design + current implementation |
| Comparator value date | `>=` | incoming settlement date minus 5 JVM-local calendar days | Missing incoming date can fail before query construction; exact failure contract is not established | Current implementation |
| Comparator status | membership | nine `getPostReleasedStatus()` triples | Unknown enum values are mapped before membership evaluation; exact failure/no-match behavior is not established | Current implementation |
| Payment Type | none | SCBML value is stored as Java `settlementType`, but is not used here | Missing value currently does not affect ReBook selection | Current implementation |
| Multiplicity | `anyMatch` | any qualifying comparator | No candidates means no ReBook | Requested change + current implementation |

Current status membership is:

1. `RELEASED / NA / NA`
2. `SETTLED / NA / NA`
3. `NETTED / NA / Pending_Ack`
4. `NETTED / NA / Released`
5. `NETTED / NA / Settled`
6. `READY / NA / Pending_Ack`
7. `NOSTRO_MATCHED / NA / NA`
8. `NETTED / NA / NostroMatched`
9. `SPLIT / NA / NostroMatched`

### Current Implementation Evidence

- `repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/processor/AbstractCashflowActionProcessor.java:710-732`,
  symbol `AbstractCashflowActionProcessor.reversalOrRebook`.
- `repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/service/CashflowDuplicateCheckService.java:699-721`,
  symbol `CashflowDuplicateCheckService.reversalOrRebook`.
- `repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/domain/repository/RatanCashflowDetailsRepository.java:829-849`,
  symbol `getCashflowIdsUnderSameOriginalTradeIdAndSameCurrency`.
- `repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/domain/repository/RatanHistoryRepository.java:780-803`,
  symbol `existCashflowsPostReleasedWith5Days`.
- `repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/domain/status/CashflowStatus.java:301-308`,
  symbol `getPostReleasedStatus`.
- `repos/ratan-cashflow-lifecycle-service/src/main/java/com/scb/ratan/cashflow/lifecycle/feign/dto/XpathResult.java:163-180`
  maps SCBML `conf:paymentType` to the Java `settlementType` extraction field.

GitNexus `context` confirmed that both ReBook paths call the same candidate and
history predicates. This establishes duplicated callers and current static flow;
it does not establish business intent or production outcomes.

## Before Evidence

Immutable artifact: `test-engine/evidence/ado-1/before/run.json`

- Captured: `2026-08-27T11:50:24.303657+00:00`.
- Evidence mode: `observed_in_test_engine_simulation`.
- Result: 14 passed, 0 failed.
- Relationship: all 14 mappings are `EXERCISES/supported`; approval to promote
  them to `VERIFIES` is pending.
- External boundaries are mocked and production code was not executed.
- The local simulator currently keys release markers by
  `(original_trade_id, currency)` and applies `date difference <= 5`; Payment
  Type is emitted as test data but is not a matching predicate.

Relevant inspected executable tests:

- `CN-API-Rebook-001-001` and `CN-API-Rebook-001-002` assert the Murex +5/+6
  day boundary.
- `CN-API-Rebook-001-003` asserts no ReBook for different currency.
- `CN-API-Rebook-001-005` and `CN-API-Rebook-001-006` assert the Stella +5/+6
  day boundary; `CN-API-Rebook-001-007` covers different currency.
- `CN-API-Rebook-001-008`, `CN-API-Rebook-001-009`, and
  `CN-API-Rebook-001-010` exercise equivalent Uber-style boundary/currency cases.
- Source: `test-engine/suites/rebook/CN-API-ReBook.robot`.
- These tests were executed in the recorded local baseline, but they are not
  business authority and do not cover Payment Type, null handling, business-day
  calendars, reverse/future date direction, or the full Java status set.

Inspected Java tests named `*PostReleasedWith30Days` call the five-day method and
mock key predicates. They show asserted status examples but were not executed in
this restart and do not prove boundary SQL semantics.

## Desired Behavior: Confirmed vs Unresolved

Confirmed facts:

- ReBook remains a heuristic because no original-to-replacement linkage exists.
- Existing identity matching remains in scope unless the owner explicitly changes it.
- Payment Type exists in SCBML and is represented in Java as `settlementType`.
- The POC must produce local `before` and `after` evidence with mocked boundaries.

Inference requiring approval:

- `additional limit to Payment Type` most naturally means
  `identity AND currency AND Payment Type AND date AND status`.

Contradictions and gaps:

- The story says Payment Type is additional, while
  `reports/requirement-impact/rebook-payment-type.md:163-169` records an unnamed
  earlier requirement-owner decision that Payment Type replaces currency.
- The story says `RELEASED`; OpenKB says released or settled; current code accepts
  nine status triples.
- Neither the story nor exact OpenKB pages define calendar versus business days,
  both endpoints, timezone, or future-dated comparators.
- Neither the story nor exact OpenKB pages define Payment Type taxonomy,
  normalization, or missing/blank/unknown behavior.
- OpenKB evidence discusses Murex and Stella; the local suite also exercises an
  Uber-style flow. The target source-system scope is not explicit.

## Clarification Ledger

| ID | Unresolved decision | Why it changes delivery | Precise sources | Evidence gap | Owner | Resolution |
|---|---|---|---|---|---|---|
| Q1 | Retain or replace currency | Changes candidate query and currency-negative tests | Requested change `requirements.md:7-11`; prior decision `reports/requirement-impact/rebook-payment-type.md:163-169`; test `CN-API-Rebook-001-003` | Current story and prior decision conflict | POC owner | Pending |
| Q2 | Payment Type comparison and invalid-data policy | Defines data contract, candidate key, failures, and target matrix | Requested change `requirements.md:10-11`; current mapping `XpathResult.java:163-180` | No authoritative taxonomy or normalization rule was found | POC owner, later QA approval | Pending |
| Q3 | Exact comparator status set | Changes which historical rows can trigger ReBook | Requested change `requirements.md:6`; OpenKB source lines 27-35; current `CashflowStatus.getPostReleasedStatus` | Three different status interpretations exist | POC owner | Pending |
| Q4 | Exact five-day interval | Changes query operators and boundary/future-date tests | Requested change `requirements.md:6-9`; OpenKB proximity page lines 14-25; current `existCashflowsPostReleasedWith5Days`; tests `001-001`, `001-005`, `001-006` | Calendar, direction, upper bound, and timezone are unspecified | POC owner | Pending |
| Q5 | Capture-system scope | Determines scenario matrix and rollout consistency | OpenKB source lines 38-51; current Murex/non-Murex branch; tests `001-001`, `001-005`, `001-008` | Story does not name source systems | POC owner | Pending |

## Clarifications Required

### Q1 - Predicate Combination

Question: Must Payment Type be added alongside same-currency matching, or replace
same-currency matching?

Why this matters: The two answers select different comparator populations, require
different repository criteria, and reverse the expected outcome of the existing
different-currency scenarios.

Evidence:

- [Requested change] `stories/ado-1/requirements.md:7-11` says current behavior
  includes same currency and future behavior is an "additional" Payment Type limit.
- [Prior decision] `reports/requirement-impact/rebook-payment-type.md:163-169`
  records an unnamed earlier owner answer that Payment Type replaces currency.
- [Current implementation] `RatanCashflowDetailsRepository.getCashflowIdsUnderSameOriginalTradeIdAndSameCurrency`
  requires currency equality today.
- [Executable test] `CN-API-Rebook-001-003` was executed and passed as
  `EXERCISES/supported`; it asserts that different currency does not ReBook.

Conflict or gap: The current story and prior decision record prescribe mutually
exclusive future predicates; the prior record is historical evidence, not current approval.

Decision needed: Choose exactly one:

1. `identity AND currency AND Payment Type AND date AND status`.
2. `identity AND Payment Type AND date AND status` (currency removed).

### Q2 - Payment Type Contract

Question: What exact Payment Type comparison and invalid-data contract should the
ReBook control enforce?

Why this matters: Field selection, normalization, valid values, and null behavior
change the candidate query, exception path, backward compatibility with existing
rows, and the positive/negative test matrix.

Evidence:

- [Requested change] `stories/ado-1/requirements.md:10-11` names Payment Type but
  provides no field path or comparison semantics.
- [Current implementation] `XpathResult.java:163-180` reads SCBML
  `scb:payment/conf:paymentType` into the Java `settlementType` field; presence of
  that field proves availability only, not that it is the approved discriminator.
- [Business/design] The exact OpenKB pages listed above define no Payment Type
  taxonomy, normalization, or missing-data rule.
- [Prior decision] `reports/requirement-impact/rebook-payment-type.md:163-169`
  records SCBML Payment Type and "throw an exception" for missing, blank, or
  unknown values, but does not name the exception/control outcome and is not
  current approval.

Conflict or gap: A field exists, but authoritative comparison and invalid-data
semantics are absent.

Decision needed: Specify all of the following:

1. Confirm the source as SCBML `conf:paymentType` / Java `settlementType`, or name another field.
2. Define equality: exact, trimmed, case-normalized, or mapped through a taxonomy.
3. Provide the allowed values and aliases, or name their authoritative reference.
4. For missing, blank, malformed, or unknown values on either cashflow, choose
   `no match`, `data-quality exception`, or another exact outcome; if exception,
   name its type/reason and whether processing stops.

### Q3 - Comparator Status

Question: Which exact comparator status triples qualify for ReBook?

Why this matters: Selecting literal `RELEASED`, released-or-settled, or the current
nine-state set changes false positives, affected repository behavior, and status tests.

Evidence:

- [Requested change] `stories/ado-1/requirements.md:6` says `RELEASED`.
- [Business/design] `Ingenuine Rebook Exception in Ratan`, lines 27-35, says
  released or settled.
- [Current implementation] `CashflowStatus.getPostReleasedStatus`, lines 301-308,
  accepts nine main/sub/sub-type combinations, including pending-ack and
  nostro-matched forms.
- [Executable test] Java tests
  `testExistCashflowsPostReleasedWith30Days`,
  `testExistCashflowsPostReleasedNettedReleasedWith30Days`, and
  `testExistCashflowsPostReleasedNettedSettledWith30Days` were inspected but not
  executed in this restart. Their names are stale and they assert only examples.

Conflict or gap: Requested change, business documentation, and current code each
describe a different set.

Decision needed: Provide the complete allowed list of
`main status / sub-status / sub-status event type` triples. At minimum, state
whether the target is literal `RELEASED`, `RELEASED + SETTLED`, or the current
nine-state set.

### Q4 - Five-Day Interval

Question: What exact date interval qualifies a comparator?

Why this matters: The current code uses calendar subtraction, includes the lower
endpoint, has no upper bound, and uses the JVM default timezone. Different answers
change database operators and require different boundary tests.

Evidence:

- [Requested change] `stories/ado-1/requirements.md:6-9` says `VD-5` and "limit to 5 days."
- [Business/design] `Payment-Date Proximity Matching`, lines 14-25, says within
  the configured five-day window but does not define its calendar or direction.
- [Current implementation] `RatanHistoryRepository.existCashflowsPostReleasedWith5Days`,
  lines 780-803, implements only `comparator VD >= incoming VD - 5 calendar days`.
- [Executable test] `CN-API-Rebook-001-001`, `CN-API-Rebook-001-005`, and
  `CN-API-Rebook-001-006` were executed and passed as `EXERCISES/supported`; they
  cover incoming dates +5 and +6 days after a comparator, not reverse/future
  direction, weekends, holidays, or timezone boundaries.

Conflict or gap: The available evidence does not establish calendar versus
business days, an upper bound, future-date policy, or timezone.

Decision needed: Confirm or replace this complete rule:

`incoming VD - 5 <= comparator VD <= incoming VD`, with both endpoints inclusive,
using either calendar days or a named business calendar and a named timezone.

### Q5 - Source-System Scope

Question: Which capture systems must apply the Payment Type rule in this story?

Why this matters: A shared rule requires equivalent behavior and tests across all
in-scope paths; a limited rollout requires explicit branching and prevents the
local simulator from claiming unsupported coverage.

Evidence:

- [Business/design] `Ingenuine Rebook Exception in Ratan`, lines 38-51, reports
  Murex and Stella outcomes; it discusses Uber only as a possible future source
  of authoritative trade-event lineage.
- [Current implementation] `getCashflowIdsUnderSameOriginalTradeIdAndSameCurrency`
  has a Murex branch and a shared non-Murex branch.
- [Executable test] `CN-API-Rebook-001-001` (Murex), `001-005` (Stella), and
  `001-008` (Uber-style) were executed and passed as `EXERCISES/supported`.
- [Requested change] `stories/ado-1/requirements.md` does not name a source system.

Conflict or gap: Current evidence covers more paths than the story explicitly scopes.

Decision needed: Name the target set, for example `Murex + Stella + Uber`, or list
the excluded systems and their retained behavior.

## Target Examples Pending Approval

| Example | Current observed result | Target result |
|---|---|---|
| Same identity/currency/type, qualifying status, comparator exactly incoming VD - 5 | ReBook under current status set | Pending Q2-Q4 |
| Same identity/currency/type, comparator incoming VD - 6 | No ReBook | Pending Q4 |
| Same identity/type/window/status, different currency | No ReBook | Pending Q1 |
| Same identity/currency/window/status, different Payment Type | Payment Type ignored | Must be no ReBook if Q2 approves type equality |
| Matching fields with missing Payment Type | Payment Type ignored | Pending Q2 |
| Comparator after incoming VD | Can qualify in current static code | Pending Q4 |
| `SETTLED`, `NETTED/Released`, or `NOSTRO_MATCHED` comparator | Can qualify under current set | Pending Q3 |

## Next Gate

Verdict: `BLOCKED ON REQUIREMENT DECISION`

After Q1-Q5 are answered:

1. Record the owner decisions in this contract and complete the target predicate table.
2. Run requirement impact analysis and GitNexus impact before any business symbol edit.
3. Modify or add local simulation tests for the approved target rule.
4. Capture a new immutable `after` evidence run without overwriting `before`.
5. Compare `before` and `after`; the POC owner decides whether mappings may move
   from `EXERCISES` to `VERIFIES`. In the target operating model, QA owns that approval.
