---
type: source
title: Cashflow Splitting Release
authors: []
year: 2025
url: ""
venue: "Settlement Day 2 functional requirement"
tags: [cashflow-splitting, settlement-day-2, release-management, rule-engine]
related: [cashflow-splitting, pending-nds-netting-splitting-rule, split-release-versus-uber-release, ratan-rule-service, ratanone-db-repository]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Release.md"]
---
# Cashflow Splitting Release

## Scope

This functional requirement records the release coordination for cashflow splitting in Settlement Day 2. It covers individual split releases, the integrated `feature/uber_split` release stream, and splitting-related rule changes.

The source provides strong evidence for branch names, release versions, pull requests, predicates, SQL lookup criteria, and the stated production rule identifier. It does not establish the complete runtime state model, rule precedence, test coverage, rollback behavior, or production rollout status.

## Relevant service release matrix

| Service | Split branch | Split release | Owner |
|---|---|---|---|
| `ratan-cashflow-lifecycle-service` | `feature/settlement-day2-split-common` | `release/v3.4.0`, PR 2016340 | Daiqi Wang |
| `ratan-cash-settlement-netting-service` | `feature/settlement-day2-split-common` | `release/v1.7.0`, PR 2016349; `release/v1.7.1`, PR 2161814 | Wen Hao |
| `ratan-cash-settlement-query-service` | `feature/settlement-day2-split-9939815` | `release/v3.2.0`, PR 2016321 | Daiqi Wang |
| `ratan-cash-settlement-orchestration` | `feature/settlement-day2-split-common` | `release/v3.4.0`, PR 2016326 | Daiqi Wang |
| `ratan-cash-settlement-accounting-service` | `feature/settlement-day2-split-common` | `release/v1.4.0`, PR 2055899 | Li1, Johnny |
| `ratan-cash-settlement-ssi-stamping-service` | `feature/split-with-ssi` | `release/v2.5.8`, PR 2055695 | Wen Hao |
| `ratan-cash-settlement-group-management-service` | `feature/settlement-day2-split-common` | `release/v2.2.0`, PR 2055909 | Li1, Johnny |
| `ratan-rule-service` | `feature/settlement-day2-split-common` | `release/v2.3.0`, PR 2016335 | Daiqi Wang |
| `ratanone-rule-service` | `feature/settlement-day2-split-common` | `release/v2.4.0`, PR 2016333 | Daiqi Wang |
| `ratanone-swift-service` | `feature/settlement-day2-split-common` | `release/v2.5.0`, PR 2134569 | Li1, Johnny |
| `ratanone-static-data-service` | `feature/settlement-day2-split-common` | `release/v3.7.0`, PR 2136962 | Pengpeng Li |
| `ratanone-db-repository` | `feature/bau-golive-15-nov-2025` replaced `feature/settlement-day2-split-common` | `develop`, PR 2146456 for splitting DML; prior PR 2056165 was struck through | Qingrong Zhao |
| `mfe-cashflow-blotter` | `feature/splitting_hold_bulk_fail` | `release/v1.38.7` | Zhonghui Feng |
| `mfe-admin-module` | Not specified | Not specified | Not specified |
| `ratanone-foundation` | Not specified | Not specified | Not specified |
| `ratan-cash-settlement-lms-service` | `feature/day2-split-common` | `release/v.2.2.5` | Wen Hao |

## Integrated `uber_split` release matrix

| Service | Mix branch | Uber release |
|---|---|---|
| `ratan-cashflow-lifecycle-service` | `feature/uber_split` | `release/v4.0.0`, PR 2134796 |
| `ratan-cash-settlement-netting-service` | `feature/uber_split` | `release/v3.0.0`, PR 2140434 |
| `ratan-cash-settlement-query-service` | `feature/uber_split` | `release/v4.0.0`, PR 2140298 |
| `ratan-cash-settlement-orchestration` | `feature/uber_split` | `release/v4.0.0`, PR 2140289 |
| `ratan-cash-settlement-accounting-service` | `feature/uber_split` | `release/v2.0.0`, PR 2134809 |
| `ratan-cash-settlement-ssi-stamping-service` | `feature/uber_split` | `release/v3.1.2`, PR 2140267 |
| `ratan-cash-settlement-group-management-service` | `feature/uber_split` | `release/v3.0.0`, PR 2140318 |
| `ratan-rule-service` | `feature/uber_split` | `release/v3.1.0`, PR 2140326 |
| `ratanone-rule-service` | `feature/uber_split` | `release/v2.4.0` |
| `ratanone-swift-service` | `feature/uber_split` | `release/v4.0.0`, PR 2134804 |
| `ratanone-static-data-service` | `feature/uber_split` | `release/v4.0.2`, PR 2140338 |
| `ratanone-db-repository` | Not specified | Not specified |
| `mfe-cashflow-blotter` | Not specified | `release/v1.38.7` |
| `mfe-admin-module` | Not specified | Not specified |
| `ratanone-foundation` | `feature/uber_split` | `release/v7.0.4` |

The final “To uber Release PR” summary omits `ratanone-rule-service`, `ratanone-db-repository`, `mfe-cashflow-blotter`, and `ratanone-foundation`, even though some of them appear in the expanded matrix.

## Splitting rule predicates

```text
Cashflow__Splitting_Id != null && Cashflow__Splitting_Id != ""

Cashflow__Is_Split_Amend_Amount == true

Cashflow__Is_Cashflow_Unsplit == true

Cashflow__Is_Withdrawal_On_Split == true
```

The source does not state whether these are independent rules, event conditions, or flags used by a larger rule set.

## Pending NDS Netting predicate

```text
Instrument_Common__Murex_Product_Typology in ("NDS", "NDCF", "NDFRA", "ND CDS Fixing", "ND CDS", "ND-Convert", "NDS Fixing")
&& Cashflow__ND_Parent_Typology != "NDIRS"
&& Entity__Booking_Entity_SCI_FMID in ("10075222", "400041070", "400906330", "300011345", "10038345", "2", "300075472", "6", "4", "400960089", "9", "400093619", "300036368", "400452428", "400451508", "3", "10020899", "10032025", "10036642", "10062461", "10078716", "235003861", "400001378", "400054708", "400054737", "400054741", "400057714", "400075752", "400090093", "400095464", "400130178", "400130180", "400185419", "400193370", "400209000", "400218197", "400220273", "400229749", "400516442", "400516443", "400667486", "400677737", "400683682", "400798477", "400899993", "401053411")
&& Cashflow__Cashflow_Event_Reason not in ("Reversal", "Rebook")
&& (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")
&& ((Cashflow__Duplicate_NDS_FXD == null || Cashflow__Duplicate_NDS_FXD == ""))
&& (Cashflow__Splitting_Id == null || Cashflow__Splitting_Id == "")
```

The rule therefore requires an allowed NDS-related product typology, excludes `NDIRS`, restricts booking entity by an explicit SCI FMID allowlist, and excludes reversal, rebook, already-netted, duplicate NDS FXD, and already-split cashflows.

## Production rule lookup

```sql
SELECT * FROM ratanone_rule_service.ratan_rule_engine
where business_flow ='STRATEGIC_SETTLEMENT'
and status ='LIVE'
and rule_type ='NSTP'
and reason ='Pending NDS Netting';
```

The document states:

```text
prod rule id is: 7350773637874561024
```

The source does not provide the returned row, rule version, priority, effective date, or database schema.

## Related wiki context

Cashflow splitting intersects with [[concepts/cashflow-lineage-and-amendment-correlation]], [[concepts/ssi-stamping]], [[concepts/cashflow-aggregation-state-model]], and [[entities/ratan]]. Its release structure is summarized in [[comparisons/split-release-versus-uber-release]].

---

---FILE: wiki/concepts/cashflow-splitting.md---
---
type: concept
title: Cashflow Splitting
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-splitting, cash-settlement, settlement-day-2, lifecycle, release-management]
related: [cashflow-lineage-and-amendment-correlation, cashflow-aggregation-state-model, split-release-versus-uber-release, pending-nds-netting-splitting-rule, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Release.md"]
---
# Cashflow Splitting

Cashflow splitting is the Settlement Day 2 processing area in which a cashflow is associated with split-specific lifecycle behavior, including split identification, split amount amendment, unsplitting, and withdrawal on split.

The source documents splitting as a coordinated change rather than an isolated transformation. The implementation spans lifecycle, netting, query, orchestration, accounting, SSI stamping, group management, rule, SWIFT, static-data, database, and cashflow blotter components.

## Documented split-related fields

| Field or predicate | Documented meaning |
|---|---|
| `Cashflow__Splitting_Id != null && Cashflow__Splitting_Id != ""` | The cashflow has a splitting identifier. |
| `Cashflow__Is_Split_Amend_Amount == true` | The cashflow is associated with a split amount amendment. |
| `Cashflow__Is_Cashflow_Unsplit == true` | The cashflow is marked for or associated with an unsplit operation. |
| `Cashflow__Is_Withdrawal_On_Split == true` | The cashflow is associated with withdrawal on split. |

These predicates are recorded as source facts. The source does not define their lifecycle transitions, precedence, mutual exclusivity, or whether they are separate rules or conditions within a composite rule.

## Service impact

The release matrices associate splitting with:

- Cashflow lifecycle handling
- Netting eligibility and exclusions
- Cashflow querying and presentation
- Workflow orchestration
- Accounting
- SSI stamping
- Group management
- Rule evaluation and static functions
- SWIFT processing
- Rule-service database DML
- Cashflow blotter behavior

The integrated rollout uses the `feature/uber_split` branch for most listed backend services. See [[comparisons/split-release-versus-uber-release]] for the distinction between the initial split releases and the integrated release stream.

## Relationship to other cashflow behavior

Splitting should be considered alongside [[concepts/cashflow-lineage-and-amendment-correlation]] because the source includes split identifiers and amendment-related predicates. It may also interact with [[concepts/cashflow-aggregation-state-model]] and [[concepts/ssi-stamping]], but this source does not establish the exact runtime interaction.

## Known limitations

The source does not specify:

- The canonical split state machine
- How split, amend, unsplit, and withdrawal events transition cashflow status
- Whether split identifiers are generated, copied, or replaced
- Rule ordering or precedence
- Rollback and failure handling
- Test or UAT evidence
- Production rollout status
---

---FILE: wiki/concepts/pending-nds-netting-splitting-rule.md---
---
type: concept
title: Pending NDS Netting Splitting Rule
created: 2026-08-23
updated: 2026-08-23
tags: [pending-nds-netting, cashflow-splitting, ndf, rule-engine, nstp]
related: [cashflow-splitting, ratan-rule-service, ratanone-db-repository, cashflow-lineage-and-amendment-correlation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Release.md"]
---
# Pending NDS Netting Splitting Rule

The `Pending NDS Netting` rule is documented as an `NSTP` rule for the `STRATEGIC_SETTLEMENT` business flow. It selects eligible NDS-related cashflows while excluding cashflows that are already netted, duplicated, split, reversed, or rebooked.

## Authoritative predicate recorded by the source

```text
Instrument_Common__Murex_Product_Typology in ("NDS", "NDCF", "NDFRA", "ND CDS Fixing", "ND CDS", "ND-Convert", "NDS Fixing")
&& Cashflow__ND_Parent_Typology != "NDIRS"
&& Entity__Booking_Entity_SCI_FMID in ("10075222", "400041070", "400906330", "300011345", "10038345", "2", "300075472", "6", "4", "400960089", "9", "400093619", "300036368", "400452428", "400451508", "3", "10020899", "10032025", "10036642", "10062461", "10078716", "235003861", "400001378", "400054708", "400054737", "400054741", "400057714", "400075752", "400085753", "400090093", "400095464", "400130178", "400130180", "400185419", "400193370", "400209000", "400218197", "400220273", "400229749", "400516442", "400516443", "400667486", "400677737", "400683682", "400798477", "400899993", "401053411")
&& Cashflow__Cashflow_Event_Reason not in ("Reversal", "Rebook")
&& (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")
&& (Cashflow__Duplicate_NDS_FXD == null || Cashflow__Duplicate_NDS_FXD == "")
&& (Cashflow__Splitting_Id == null || Cashflow__Splitting_Id == "")
```

## Eligibility and exclusions

A cashflow must satisfy all of these conditions:

1. `Instrument_Common__Murex_Product_Typology` is one of `NDS`, `NDCF`, `NDFRA`, `ND CDS Fixing`, `ND CDS`, `ND-Convert`, or `NDS Fixing`.
2. `Cashflow__ND_Parent_Typology` is not `NDIRS`.
3. `Entity__Booking_Entity_SCI_FMID` is in the explicit allowlist in the predicate.
4. `Cashflow__Cashflow_Event_Reason` is not `Reversal` or `Rebook`.
5. `Cashflow__Netting_Id` is null or empty.
6. `Cashflow__Duplicate_NDS_FXD` is null or empty.
7. `Cashflow__Splitting_Id` is null or empty.

## Production lookup

```sql
SELECT * FROM ratanone_rule_service.ratan_rule_engine
where business_flow ='STRATEGIC_SETTLEMENT'
and status ='LIVE'
and rule_type ='NSTP'
and reason ='Pending NDS Netting';
```

The stated production rule ID is `7350773637874561024`.

The source does not establish the rule's priority, version, effective date, complete database row, or whether the listed predicate is the currently deployed expression.
---

---FILE: wiki/entities/ratan-cashflow-lifecycle-service.md---
---
type: entity
title: ratan-cashflow-lifecycle-service
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, service, cashflow-splitting, lifecycle, settlement-day-2]
related: [cashflow-splitting, split-release-versus-uber-release, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Release.md"]
---
# ratan-cashflow-lifecycle-service

`ratan-cashflow-lifecycle-service` is the service identified in the Settlement Day 2 cashflow-splitting release matrix as responsible for lifecycle-related splitting changes.

## Release records

- Split branch: `feature/settlement-day2-split-common`
- Split release: `release/v3.4.0`
- Split release pull request: 2016340
- Uber branch: `feature/uber_split`
- Uber release: `release/v4.0.0`
- Uber release pull request: 2134796
- Listed owner: Daiqi Wang

The source establishes release provenance but does not describe the service API, event contract, state transitions, or deployment status.
---

---FILE: wiki/entities/ratan-rule-service.md---
---
type: entity
title: ratan-rule-service
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, service, rule-engine, cashflow-splitting, nstp]
related: [pending-nds-netting-splitting-rule, cashflow-splitting, ratanone-db-repository]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Release.md"]
---
# ratan-rule-service

`ratan-rule-service` is the rule-service component listed in the cashflow-splitting release matrices. It is associated with the splitting rule release and the integrated `feature/uber_split` rollout.

## Release records

- Split branch: `feature/settlement-day2-split-common`
- Split release: `release/v2.3.0`
- Split release pull request: 2016335
- Uber branch: `feature/uber_split`
- Uber release: `release/v3.1.0`
- Uber release pull request: 2140326
- Listed owner: Daiqi Wang

The source also identifies `ratanone_rule_service.ratan_rule_engine` as the table queried to locate the live `Pending NDS Netting` rule. The source does not state whether `ratan-rule-service` or `ratanone-rule-service` is the runtime authority for the returned rule.
---

---FILE: wiki/entities/ratanone-db-repository.md---
---
type: entity
title: ratanone-db-repository
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, database, repository, rule-engine, cashflow-splitting, dml]
related: [pending-nds-netting-splitting-rule, cashflow-splitting, ratan-rule-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Release.md"]
---
# ratanone-db-repository

`ratanone-db-repository` is the database repository identified as containing splitting-related DML and rule-service database changes.

## Release records

The initial matrix shows `feature/settlement-day2-split-common` struck through and replaced by `feature/bau-golive-15-nov-2025`. It lists `develop` as the target and pull request 2146456 for adding splitting DML:

```text
feature/bau-golive-15-nov-2025
develop
Pull request 2146456: add splitting dml
```

The earlier split pull request 2056165 is also shown but struck through.

The expanded `uber_split` matrix lists the repository with `feature/settlement-day2-split-common`, target `develop`, and pull request 2056165, but does not provide an Uber release. The conflicting records mean that the authoritative database branch and pull request for the final rollout remain unresolved.
---

---FILE: wiki/comparisons/split-release-versus-uber-release.md---
---
type: comparison
title: Split Release Versus Uber Release
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-splitting, release-management, uber-split, settlement-day-2]
related: [cashflow-splitting, ratan-cashflow-lifecycle-service, ratan-rule-service, ratanone-db-repository]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Release.md"]
---
# Split Release Versus Uber Release

The source distinguishes an initial split release stream from a later integrated Uber release stream.

| Dimension | Split release | Uber release |
|---|---|---|
| Primary branch pattern | `feature/settlement-day2-split-common` or service-specific split branches | `feature/uber_split` |
| Purpose | Deliver service-specific splitting implementation | Integrate splitting across multiple services |
| Example lifecycle service version | `release/v3.4.0` | `release/v4.0.0` |
| Example netting service version | `release/v1.7.0` and `release/v1.7.1` | `release/v3.0.0` |
| Example rule service version | `release/v2.3.0` | `release/v3.1.0` |
| Database treatment | Includes branch and DML changes, with conflicting records | No unambiguous Uber release is listed |
| Evidence status | Explicitly documented in the first matrix | Explicitly documented for most backend services, but the final summary is incomplete |

## Interpretation

The split release establishes service-level implementation baselines. The Uber release combines those changes into a coordinated rollout. Release numbers should be treated as provenance for the implementation record, not as proof of production deployment.

The source does not establish whether `ratanone-rule-service` was included in the final Uber release summary, why `ratan-cash-settlement-lms-service` is absent from the Uber matrix, or which database change is authoritative.
---

---FILE: wiki/queries/what-is-the-authoritative-cashflow-splitting-state-model.md---
---
type: query
title: What Is the Authoritative Cashflow Splitting State Model?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-splitting, state-model, settlement-day-2, open-question]
related: [cashflow-splitting, cashflow-lineage-and-amendment-correlation, cashflow-aggregation-state-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Release.md"]
---
# What Is the Authoritative Cashflow Splitting State Model?

The source lists predicates for split identification, split amount amendment, unsplitting, and withdrawal on split, but it does not define their state transitions or precedence.

The investigation should determine:

- Whether the predicates are separate rules, event conditions, or UI/filter flags
- Whether they can be true simultaneously
- How split, amend, unsplit, and withdrawal operations change cashflow status
- How `Cashflow__Splitting_Id` is created, retained, or cleared
- How splitting interacts with netting, aggregation, accounting, and SSI stamping
- What happens when a split operation fails or is reversed
---

---FILE: wiki/queries/which-services-are-in-the-final-cashflow-splitting-release.md---
---
type: query
title: Which Services Are in the Final Cashflow Splitting Release?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-splitting, release-management, deployment, open-question]
related: [cashflow-splitting, split-release-versus-uber-release, ratanone-db-repository]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Release.md"]
---
# Which Services Are in the Final Cashflow Splitting Release?

The release matrices do not agree completely. `ratanone-rule-service` appears in the expanded Uber matrix but is absent from the final Uber release summary. `ratan-cash-settlement-lms-service` appears in the initial service matrix but not in the Uber matrix. `ratanone-db-repository` has conflicting branch and pull-request records, and no Uber release is listed.

This query should establish:

- The authoritative final service inventory
- Whether each listed release reached production
- The final database branch and DML pull request
- Whether accounting and static-data repository links are documentation errors
- Whether `mfe-cashflow-blotter`, `ratanone-foundation`, and `mfe-admin-module` were release dependencies
---

---FILE: wiki/log.md---
## 2026-08-23 ingest | Cashflow Splitting Release

- Ingested the Settlement Day 2 cashflow-splitting release record, including service release matrices, `feature/uber_split` integration records, splitting predicates, the `Pending NDS Netting` rule predicate, SQL lookup, and production rule ID `7350773637874561024`.
- Added source, concept, entity, comparison, and open-question pages for cashflow splitting and its release coordination.