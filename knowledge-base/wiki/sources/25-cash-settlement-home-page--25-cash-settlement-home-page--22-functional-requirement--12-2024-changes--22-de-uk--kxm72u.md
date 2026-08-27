---
type: source
title: "Cash Settlement Home Page — 2024 DE and UK Release Tracking"
tags: [cash-settlement, auto-netting, UK-release, DE-release, release-tracking, production-issues]
related: [uk-cash-settlement-release, ratan, murex, nds-auto-netting, lms, production-scale-performance-testing, settlement-rule-replay, cash-settlement-release-incident-management, what-is-the-authoritative-uk-go-live-and-evidence-date, are-nds-fixing-waiting-states-expected]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/DE UK release tracking.md"]
authors: []
year: 2024
url: ""
venue: ""
---

# Cash Settlement Home Page — 2024 DE and UK Release Tracking

## Summary

This document records lessons from the UK Cash Settlement release and references a DE technical release on 13 October 2024. It covers production performance, auto-netting, settlement-instruction (SSI) controls, downstream integration, payment-message generation, business-rule validation, and go-live recovery activities.

The document includes operational records published between 11 and 19 January 2025. Their relationship to the October 2024 DE release and the UK business go-live is not explained. The January 2025 records should therefore be treated as associated production evidence rather than definitive evidence of the October release timeline.

Related system pages include [[entities/ratan]], [[entities/murex]], [[entities/nds-auto-netting]], and [[entities/lms]].

## Major issues and improvements

| Major Issue/Problem | Impact | Root Cause | Lesson Learn & Improvement |
| --- | --- | --- | --- |
| Dashboard Performance Issue | Service restart & settlement BAU is blocked for a few hours | 1. Performance testing was not performed with actual production volume. 2. Design is not properly reviewed( dashboard calculation is done in memory) | 1. More clear baseline of performance testing scope & data volume. 2. Design tuning |
| Netting API timeout | User get timeout error from GUI but | 1. Performance testing was not performed with actual production volume( taking reference to Murex netting volume but it's not exactly same with RATAN process). | 1. Can have more clear agreement with business on the netting volume as the benchmark of our performance testing 2. Our design should have more buffer to support the BAU |
| Netting Cashflow not feed to LMS | Failure of cash balance projection in LMS | 1. Not all UAT test cases were performed as E2E until LMS | 1. Improve the E2E test case coverage until all downstream |
| NDS Auto Netting unknown cases happen in production | Some NDS cashflows( new cases)can't be auto netted | 1. UAT test cases quality: No clear responsibility on the UAT test case complication, responsibility on every team means no responsibility | 1. More clear responsibility that settlement team should take responsibility of business case definition, they should approach MO team to define the E2E business cases |
| SSI+ Best Matching logic | Later requirement and team stretch to design a tactical solution to meet the UK release | Settlement team didn't seriously review the SSI stamping difference between Murex & RATAN in earlier stage | 1. Follow more close with PO & BAU team to get these reviewed in detail level & get clear signoff in earlier stage. |
| Different Murex SSI between CURRFXD & CURROPT | Wrong payment can happen if the Vostro SSI is not correct | 1. SSI recon review were not properly done by settlement team | 1. Run the SSI recon with more production data |
| Business Rules are not correctly setup on day 1 | 1. Unexpected STP: Settlement risk 2. Unexpected Gross: Clearing team need to recall the funds | 1. Business rule requirement collection & review was not completed 2. Only one round of data replay to verify the business rules | Replay more production data for settlement team to review the business rule result. |
| MT605 82A BIC is populated with dummy BIC | Payment Failure | This is new user case. - Common logic provided by ops/PO: Map the ordering customer info to 82A of MT605 - There's special case for some client the ordering customer info are their agent info | 1. Issue had been reported in UAT as part of 2 weeks data comparation. 2. Ops team is taking the action to review & advise the difference, but the review is not that accurate. |

## DE technical release

The document identifies a 13 October 2024 DE technical release with the following CPT bookings:

```text
98587988
98588010
98588032
```

## UK business go-live issue register

| Issue NO. | Description | Status | Comment |
| --- | --- | --- | --- |
| 1 | NDS Auto Netting | | 1. Clearing Client Portfolio - Murex picking up 2. NDIRS not STP - RATAN to be fixed 3. Netting rule clean up - **Done** 4. NID difference - To be discussed with Murex |
| 2 | FMSGW Error | | Original FMSGW error message ‘SCB Invalid - For Message type=103 and Currency=MXN; Account field for Beneficiary customer (59) must present‘, |
| 3 | Murex Metal Payments stuck in grouping blotter | | Adhoc Murex issue which happen only in the go live which their CPN jobs were not ran with proper sequence. |
| | LMS Feeding failure | | **N00000013011 ** |
| | Cashflow stuck in swift generation | | M00114289625, M00114289206, need to regenerate the swift message from GUI. |
| | NSTP Exception is blank | | N00000013347,M00114292534,M00114315716,M00114294044,M00114292381,M00114274380,M00114269381,M00114269368,M00114290810 |
| | Cashflow Data can't load with API 500 error | | Manual cashflows by Oscar due to RATAN downtime M00111244743 - AUD, M00113836067, M00112645079 - JPY |

## First ten intended releases

The source labels the following records as “The first 10 payments we intend to release.” Their publication dates are in January 2025.

| **Data Publication Date Time** | **Original Trade ID** | **Trade ID** | **Cashflow Id** | **Cashflow Event Type** | **Cashflow State** | **Counterparty BIC CODE** | **Payment Date** | **CCY** | **Amount** | **Cashflow Swift Status** | **Cashflow Swift Reason** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-01-16T12:23:26Z | 98017564 | 98017564 | M00114223342 | New | SETTLED | SCBLDEFXXXX | 2025-01-20 | EUR | 5772 | Released by AMH | {1:F21SCBLGB2LATSY4868907242}{4:{177:2501190625}{451:0}{108:RXA1901250224316}} |
| 2025-01-13T17:19:42Z | 80317631 | 91277635 | M00114066178 | New | SETTLED | SCBLDEFXXXX | 2025-01-20 | GBP | 537552.74 | Released by AMH | {1:F21SCBLGB2LATSY4867979150}{4:{177:2501190625}{451:0}{108:RXA1901250224320}} |
| 2025-01-11T04:07:09Z | 95895538 | 95895538 | M00113164317 | New | SETTLED | SCBLDEFXXXX | 2025-01-20 | AUD | 2700.82 | Released by AMH | {1:F21SCBLGB2LCTSY0190703786}{4:{177:2501190612}{451:0}{108:RXA1901250224318}} |
| 2025-01-11T04:07:09Z | 90023111 | 90136776 | M00113072833 | New | SETTLED | SCBLUS33XXX | 2025-01-20 | AUD | 4158.64 | Released by AMH | {1:F21SCBLGB2LCTSY0190703785}{4:{177:2501190612}{451:0}{108:RXA1901250224322}} |
| 2025-01-11T04:07:09Z | 93703288 | 93703288 | M00111245670 | New | SETTLED | SCBLIDJXXXX | 2025-01-20 | JPY | 66726736 | Released by AMH | {1:F21SCBLGB2LATSY4867979117}{4:{177:2501190612}{451:0}{108:RXA1901250224324}} |
| 2025-01-11T04:07:09Z | 98017564 | 98017564 | M00111243957 | New | SETTLED | SCBLDEFXXXX | 2025-01-20 | PLN | 751072.88 | Released by AMH | {1:F21SCBLGB2LDTSY0176804680}{4:{177:2501190612}{451:0}{108:RXA1901250224321}} |
| 2025-01-11T04:07:09Z | 81080770 | 81280059 | M00111243614 | New | SETTLED | SCBLDEFXXXX | 2025-01-20 | EUR | 13402.21 | Released by AMH | {1:F21SCBLGB2LATSY4867979149}{4:{177:2501190625}{451:0}{108:RXA1901250224315}} |
| 2025-01-11T04:07:09Z | 73355912 | 98327695 | M00111243188 | New | SETTLED | SCBLHKHHXXX | 2025-01-20 | AUD | 826699.61 | Released by AMH | {1:F21SCBLGB2LDTSY0176804679}{4:{177:2501190612}{451:0}{108:RXA1901250224319}} |
| 2025-01-11T04:07:09Z | 81376394 | 81453110 | M00111205142 | New | SETTLED | SCBLSG22XXX | 2025-01-20 | EUR | 740288.89 | Released by AMH | {1:F21SCBLGB2LATSY4868907243}{4:{177:2501190625}{451:0}{108:RXA1901250224323}} |
| 2025-01-11T04:07:09Z | 98021220 | 98055576 | M00111204830 | New | SETTLED | SCBLDEFXXXX | 2025-01-20 | EUR | 13442 | Released by AMH | {1:F21SCBLGB2LATSY4868907241}{4:{177:2501190625}{451:0}{108:RXA1901250224317}} |

## SSI-refresh-triggered cashflows

The source labels this section “The 3 cashflow which were triggered by the SSI refresh,” but it contains eight rows.

| Data Publication Date Time | Original Trade ID | Trade ID | Cashflow Id | Cashflow Event Type | Cashflow State | Counterparty BIC CODE | Payment Date | CCY | Amount | Cashflow Swift Status | Cashflow Swift Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-01-17T08:28:36Z | 100228832 | 100228832 | M00114264086 | New | RELEASED | SBILGB2LXXX | 2025-01-21 | USD | 10000000 | Pending FMSGW Disp | Message is received |
| 2025-01-17T08:28:36Z | 100228827 | 100228827 | M00114264073 | New | RELEASED | SBILGB2LXXX | 2025-01-21 | USD | 30000000 | Pending FMSGW Disp | Message is received |
| 2025-01-17T08:28:36Z | 100226568 | 100226568 | M00114260321 | New | RELEASED | SBILGB2LXXX | 2025-01-21 | USD | 37000000 | Pending FMSGW Disp | Message is received |
| 2025-01-17T08:28:36Z | 100226581 | 100226581 | M00114260338 | New | RELEASED | SBILGB2LXXX | 2025-01-21 | USD | 20000000 | Pending FMSGW Disp | Message is received |
| 2025-01-17T08:28:36Z | 100226572 | 100226572 | M00114260328 | New | SETTLED | SBILGB2LXXX | 2025-01-21 | USD | 10000000 | Auto Settled by Ratan | |
| 2025-01-17T08:28:36Z | 100226579 | 100226579 | M00114260324 | New | SETTLED | SBILGB2LXXX | 2025-01-21 | USD | 20000000 | Auto Settled by Ratan | |
| 2025-01-16T04:17:24Z | 100181916 | 100181916 | M00114195651 | New | SETTLED | WFBIUS6WFFX | 2025-01-21 | USD | 202000000 | Auto Settled by Ratan | |
| 2025-01-11T04:07:09Z | 78057806 | 78074690 | M00111246979 | New | SETTLED | SBILGB2LXXX | 2025-01-21 | USD | 20000000 | Auto Settled by Ratan | |

## NDS issue data

| Issue | Identifiers / examples |
|---|---|
| NDS & NDS Fixing different NID | `M00114151898`, `M00114273743` |
| Picking up Razor typology | `M00114270111` — Outright, `M00114270311` — FX Swap |
| NDS Fixing stopped by netting rule | `M00114149131`, `M00114273761` |

## OIS records

| Data Publication Date Time | Original Trade ID | Trade ID | ND Parent Trade Id | ND Parent Typology | Murex Product Typology | Cashflow Id | Cashflow Event Type | Cashflow State |
|---|---:|---:|---:|---|---|---|---|---|
| 2025-01-19T11:03:06Z | 100222795 | 100222795 | 98198861 | OIS | NDS Fixing | M00114253610 | New | WAITING |
| 2025-01-19T11:03:06Z | 100222794 | 100222794 | 95430083 | OIS | NDS Fixing | M00114253608 | New | WAITING |
| 2025-01-19T11:03:06Z | 100222792 | 100222792 | 94779277 | OIS | NDS Fixing | M00114253604 | New | WAITING |
| 2025-01-19T11:03:07Z | 100222797 | 100222797 | 100216964 | OIS | NDS Fixing | M00114253614 | New | WAITING |
| 2025-01-19T11:03:06Z | 100222790 | 100222790 | 92170030 | OIS | NDS Fixing | M00114253601 | New | WAITING |
| 2025-01-19T11:03:09Z | 100222784 | 100222784 | 91349794 | OIS | NDS Fixing | M00114253593 | New | WAITING |
| 2025-01-19T11:03:06Z | 100222787 | 100222787 | 92109900 | OIS | NDS Fixing | M00114253597 | New | WAITING |
| 2025-01-19T11:03:06Z | 100222793 | 100222793 | 95430069 | OIS | NDS Fixing | M00114253606 | New | WAITING |
| 2025-01-19T11:03:07Z | 100222796 | 100222796 | 100210091 | OIS | NDS Fixing | M00114253612 | New | WAITING |
| 2025-01-19T11:03:06Z | 100222788 | 100222788 | 92169950 | OIS | NDS Fixing | M00114253599 | New | WAITING |
| 2025-01-19T11:02:32Z | 100238706 | 100238706 | 100215240 | OIS | NDS Fixing | M00114277268 | New | WAITING |
| 2025-01-19T11:03:07Z | 100222804 | 100222804 | 92109901 | OIS | NDS Fixing | M00114253632 | New | WAITING |
| 2025-01-19T11:03:07Z | 100222819 | 100222819 | 92170031 | OIS | NDS Fixing | M00114253651 | New | WAITING |
| 2025-01-19T11:03:07Z | 100222823 | 100222823 | 95430084 | OIS | NDS Fixing | M00114253666 | New | WAITING |
| 2025-01-19T11:03:07Z | 100222822 | 100222822 | 95430070 | OIS | NDS Fixing | M00114253664 | New | WAITING |
| 2025-01-19T11:03:07Z | 100222821 | 100222821 | 94779278 | OIS | NDS Fixing | M00114253662 | New | WAITING |
| 2025-01-19T11:03:07Z | 100222825 | 100222825 | 98198862 | OIS | NDS Fixing | M00114253669 | New | WAITING |
| 2025-01-19T11:03:07Z | 100222828 | 100222828 | 100216965 | OIS | NDS Fixing | M00114253674 | New | WAITING |
| 2025-01-19T11:03:07Z | 100222813 | 100222813 | 92169951 | OIS | NDS Fixing | M00114253643 | New | WAITING |
| 2025-01-19T11:03:07Z | 100222800 | 100222800 | 91349795 | OIS | NDS Fixing | M00114253618 | New | WAITING |
| 2025-01-19T11:03:07Z | 100222827 | 100222827 | 100210092 | OIS | NDS Fixing | M00114253672 | New | WAITING |
| 2025-01-19T11:02:32Z | 100238707 | 100238707 | 100215241 | OIS | NDS Fixing | M00114277270 | New | WAITING |

The `WAITING` state is observed but not interpreted as a defect because the expected lifecycle transition is not documented.

## Operational findings

- Performance testing used Murex volume as a reference even though the source states that Murex volume is not equivalent to the RATAN process.
- Dashboard calculations were performed in memory, and a service restart blocked settlement BAU for several hours.
- The RATAN netting API produced GUI timeout errors.
- Incomplete E2E UAT coverage allowed a cashflow feed failure to LMS and caused cash-balance projection failure.
- NDS Auto Netting had unknown production cases, NID differences, Razor typology selection, and fixing cashflows stopped by netting rules.
- SSI+ Best Matching was addressed late, without sufficiently early review of Murex/RATAN SSI-stamping differences.
- Differences between Murex `CURRFXD` and `CURROPT` SSI values created a material incorrect-payment risk for Vostro SSI selection.
- Only one production-data replay was used to verify settlement business rules.
- The MT605 `82A` mapping did not handle clients for whom ordering-customer information represented an agent.
- UK go-live required manual Swift regeneration, manual cashflow creation, and operational handling of blank NSTP exceptions and API 500 errors.

## Evidence limitations

The document does not provide complete issue statuses, exact performance targets, interface-level LMS diagnostics, authoritative NID mappings, expected OIS/NDS fixing state transitions, or confirmed payment losses resulting from SSI or MT605 mapping risks.

---

---FILE: wiki/projects/uk-cash-settlement-release.md---
---
type: project
title: UK Cash Settlement Release
tags: [cash-settlement, UK, release, go-live, auto-netting]
related: [26-auto-netting-page-md-files--122-cash-settlement-home-page-cash-settlement-home-page-functional-requirement-20--gwcnbq, ratan, murex, nds-auto-netting, lms, production-scale-performance-testing, settlement-rule-replay, cash-settlement-release-incident-management, go-live-decision-criteria]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- 2024 changes -- DE UK release tracking.md"]
status: active
owner: ""
start_date: 2024-10-13
target_date: ""
---

# UK Cash Settlement Release

## Purpose

The release introduced or changed Cash Settlement Home Page, RATAN auto-netting, SSI handling, settlement rules, downstream cashflow feeds, and payment-message processing for the UK business. The source also records a DE technical release on 13 October 2024.

## Scope

The release evidence covers:

- Cash Settlement Home Page dashboard performance and netting API behavior.
- RATAN settlement and auto-netting.
- Murex-to-RATAN SSI and business-rule alignment.
- NDS and NDS Fixing cases.
- LMS downstream cashflow feeding.
- FMSGW validation and Swift dispatch.
- NSTP exception diagnostics.
- Manual recovery during production incidents.

## Status

The source records operational progress but does not provide a complete closure status for the issue register. The project is therefore marked active pending confirmation of the authoritative UK go-live date, issue closure evidence, and the relationship between the 2024 release and January 2025 production records.

## Lessons

1. Performance benchmarks must use agreed RATAN production volumes and include capacity buffer.
2. UAT ownership must explicitly assign responsibility for business-case definition and E2E scenarios.
3. SSI reconciliation must compare Murex and RATAN behavior using sufficient production data.
4. Settlement rules require multiple rounds of production-data replay.
5. Release runbooks must cover Swift regeneration, manual cashflow creation, blank NSTP exceptions, downstream-feed failures, and API recovery.

## Retrospective questions

- Which date is the authoritative UK business go-live date?
- Which January 2025 records belong to this release?
- Were all FMSGW, LMS, NSTP, Swift-generation, and API incidents permanently resolved?
- What controls were added after the release?

---

---FILE: wiki/entities/fmsgw.md---
---
type: entity
title: FMSGW
tags: [messaging, payments, cash-settlement, swift]
related: [ratan, settlement-message-routing, swift-mt-mx-integration, uk-cash-settlement-release]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- 2024 changes -- DE UK release tracking.md"]
---

# FMSGW

FMSGW is the messaging gateway or downstream messaging component referenced in the UK Cash Settlement go-live issue register.

## Evidence from the release

The source records an FMSGW validation error:

```text
SCB Invalid - For Message type=103 and Currency=MXN; Account field for Beneficiary customer (59) must present
```

The source also records cashflows in `RELEASED` state with `Pending FMSGW Disp` status and the reason `Message is received`. The records are associated with SSI-refresh-triggered cashflows, but the source does not establish whether the pending dispatch state was expected or defective.

## Operational relevance

FMSGW is part of the path from RATAN cashflow release to payment-message dispatch. Failures or ambiguous pending states require reconciliation between cashflow state, Swift-message state, and downstream dispatch status.

---

---FILE: wiki/entities/cash-settlement-home-page.md---
---
type: entity
title: Cash Settlement Home Page
tags: [cash-settlement, dashboard, GUI, netting, operations]
related: [ratan, auto-netting, cashflow-monitoring, production-scale-performance-testing, cash-settlement-release-incident-management]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- 2024 changes -- DE UK release tracking.md"]
---

# Cash Settlement Home Page

Cash Settlement Home Page is the operational dashboard and GUI referenced in the UK release tracking document.

## Observed behavior

The source attributes a production performance incident to dashboard calculations being performed in memory. A service restart blocked settlement BAU for several hours. The GUI also returned timeout errors when users attempted netting operations, and an API 500 error prevented cashflow data from loading in another incident.

Manual recovery included regenerating Swift messages from the GUI. The source does not identify the exact endpoint, latency target, resource metrics, or API implementation.

## Release-control implications

Cash Settlement Home Page should have:

- Production-scale performance benchmarks.
- Capacity buffer beyond the agreed BAU volume.
- Monitoring for timeout and API 500 responses.
- A documented fallback for message regeneration and manual cashflow recovery.
- Clear linkage between GUI actions and resulting cashflow, Swift, and settlement states.

---

---FILE: wiki/entities/currfxd.md---
---
type: entity
title: CURRFXD
tags: [murex, product-classification, SSI, cash-settlement]
related: [murex, curr-opt, ssi-selection-hierarchy, nostro-vostro-settlement-controls]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- 2024 changes -- DE UK release tracking.md"]
---

# CURRFXD

CURRFXD is a Murex product or processing classification referenced in an SSI comparison with `CURROPT`.

The source states that different Murex SSI values between `CURRFXD` and `CURROPT` could result in an incorrect Vostro SSI and therefore an incorrect payment. It presents this as a material payment risk, not as a confirmed payment loss.

---

---FILE: wiki/entities/curropt.md---
---
type: entity
title: CURROPT
tags: [murex, product-classification, SSI, cash-settlement]
related: [murex, currfxd, ssi-selection-hierarchy, nostro-vostro-settlement-controls]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- 2024 changes -- DE UK release tracking.md"]
---

# CURROPT

CURROPT is a Murex product or processing classification referenced in an SSI comparison with `CURRFXD`.

The source identifies different SSI values between the two classifications as a potential cause of incorrect Vostro SSI selection and incorrect payment. The document recommends running SSI reconciliation with more production data.

---

---FILE: wiki/concepts/production-scale-performance-testing.md---
---
type: concept
title: Production-Scale Performance Testing
tags: [performance-testing, production-volume, capacity, cash-settlement, release-readiness]
related: [cash-settlement-home-page, ratan, auto-netting, go-live-decision-criteria, production-release-management]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- 2024 changes -- DE UK release tracking.md"]
---

# Production-Scale Performance Testing

Production-scale performance testing validates that a settlement platform and its operational interfaces remain usable at agreed production volumes, with sufficient capacity buffer.

## Release evidence

The UK release tracking document attributes a dashboard service restart, several hours of blocked settlement BAU, GUI netting timeouts, and an API 500 cashflow-loading incident to inadequate performance validation. Murex netting volume was used as a reference, but the source explicitly states that Murex volume is not equivalent to the RATAN process.

## Required controls

A release should define and approve:

- The data volume used as the benchmark.
- Expected concurrency and workload shape.
- Dashboard response-time and API response-time targets.
- Capacity buffer above normal BAU volume.
- Resource and memory limits for in-memory calculations.
- Restart, degradation, and recovery procedures.

The source does not provide numerical performance targets, throughput results, or concurrency measurements.

---

---FILE: wiki/concepts/settlement-rule-replay.md---
---
type: concept
title: Settlement Rule Replay
tags: [settlement-rules, replay, production-data, STP, gross-settlement, UAT]
related: [ratan, auto-netting, straight-through-processing, settle-as-gross, go-live-decision-criteria, pre-rule-migration]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- 2024 changes -- DE UK release tracking.md"]
---

# Settlement Rule Replay

Settlement rule replay is the repeated execution of settlement business rules against production-like trades or cashflows to verify the resulting settlement classification and operational outcome.

## Why it matters

The UK release tracking document states that only one round of production-data replay was used to verify business rules. Incomplete requirement collection and review then created a risk of incorrectly configured day-one rules.

The identified failure modes were:

- Unexpected STP, creating settlement risk.
- Unexpected gross settlement, requiring the clearing team to recall funds.
- NDS cases that could not be auto-netted.
- Rule outcomes inconsistent with SSI or product classifications.

## Recommended control

Settlement teams should review multiple replay rounds using broader production data before go-live. Each replay should record:

- Input trade and cashflow population.
- Applied rule and rule version.
- Expected and actual STP/NSTP or gross outcome.
- SSI and product-classification inputs.
- Exceptions and their owners.
- Signoff and remediation evidence.

---

---FILE: wiki/concepts/cash-settlement-release-incident-management.md---
---
type: concept
title: Cash Settlement Release Incident Management
tags: [cash-settlement, incident-management, go-live, recovery, operations]
related: [uk-cash-settlement-release, ratan, fmsgw, cash-settlement-home-page, settlement-message-routing, swift-mt-mx-integration, post-implementation-testing, release-rollback-readiness]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- 2024 changes -- DE UK release tracking.md"]
---

# Cash Settlement Release Incident Management

Cash settlement release incident management covers detection, containment, recovery, reconciliation, ownership, and closure of production issues affecting cashflow netting and payment settlement.

## Incidents recorded by the source

The UK go-live register includes:

- NDS Auto Netting unknown cases and NID differences.
- An FMSGW MXN validation error.
- Murex metal payments stuck in the grouping blotter because CPN jobs ran in the wrong sequence.
- An LMS feeding failure identified as `N00000013011`.
- Cashflows stuck in Swift generation, including `M00114289625` and `M00114289206`.
- Blank NSTP exceptions, including `N00000013347`, `M00114292534`, `M00114315716`, `M00114294044`, `M00114292381`, `M00114274380`, `M00114269381`, `M00114269368`, and `M00114290810`.
- Cashflow data unavailable because of an API 500 error, followed by manual cashflow creation during RATAN downtime. The cited records are `M00111244743`, `M00113836067`, and `M00112645079`.

## Minimum closure evidence

Each incident should record:

1. A named owner and severity.
2. Affected trades, cashflows, messages, or downstream consumers.
3. Immediate containment and any manual intervention.
4. Reconciliation confirming that no duplicate, missing, or incorrect payment remains.
5. Permanent corrective action.
6. Regression or post-implementation test evidence.
7. Explicit closure status.

The source has a status column, but most issue statuses are blank. “Netting rule clean up — Done” appears only in a comment.

---

---FILE: wiki/queries/what-is-the-authoritative-uk-go-live-and-evidence-date.md---
---
type: query
title: What Is the Authoritative UK Go-Live and Evidence Date?
tags: [query, UK-release, go-live, chronology, production-evidence]
related: [uk-cash-settlement-release, 26-auto-netting-page-md-files--122-cash-settlement-home-page-cash-settlement-home-page-functional-requirement-20--gwcnbq, production-release-management]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- 2024 changes -- DE UK release tracking.md"]
---

# What Is the Authoritative UK Go-Live and Evidence Date?

## Question

Which date is the authoritative UK business go-live date, and why does a document referring to a 13 October 2024 DE technical release contain production records published between 11 and 19 January 2025?

## Evidence

- The source explicitly identifies a 13 October 2024 DE technical release.
- A separate section is titled “UK Business Go Live,” but it does not state the go-live date.
- The section describing the first ten intended releases contains records published on 11, 13, and 16 January 2025.
- SSI-refresh-related records are dated 16 and 17 January 2025.
- OIS/NDS Fixing records are dated 19 January 2025.

## Required resolution

Confirm whether the January 2025 records are:

- Delayed post-go-live validation evidence.
- Evidence from a later release or migration.
- Appended operational records unrelated to the October 2024 release.
- A documentation or date-labeling error.

Until resolved, the records should not be used to establish the October release timeline.

---

---FILE: wiki/queries/are-nds-fixing-waiting-states-expected.md---
---
type: query
title: Are NDS Fixing WAITING States Expected?
tags: [query, NDS, OIS, fixing, cashflow-state, auto-netting]
related: [nds-auto-netting, pending-fixing, settlement-rule-replay, uk-cash-settlement-release]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- 2024 changes -- DE UK release tracking.md"]
---

# Are NDS Fixing WAITING States Expected?

## Question

Do the OIS cashflows classified as Murex `NDS Fixing` and observed in `WAITING` state represent an expected lifecycle state, or do they indicate a fixing or netting defect?

## Evidence

The source contains 23 OIS records published on 19 January 2025. Each has:

- `ND Parent Typology = OIS`
- `Murex Product Typology = NDS Fixing`
- `Cashflow Event Type = New`
- `Cashflow State = WAITING`

The source separately identifies NDS Fixing cashflows stopped by a netting rule:

```text
M00114149131
M00114273761
```

## Required investigation

Confirm:

1. The expected lifecycle for an OIS `NDS Fixing` cashflow.
2. Whether `WAITING` means pending fixing, pending enrichment, pending netting, or an exception.
3. Whether the 23 records later transitioned to `RELEASED`, `SETTLED`, or another state.
4. Which netting rule affected the two cited cashflows.
5. Whether the state behavior differs between NDS and NDS Fixing.

No defect should be inferred from `WAITING` alone without the expected state transition and processing timestamps.

---

---FILE: wiki/log.md---
## 2026-08-22 ingest | Cash Settlement Home Page — 2024 DE and UK Release Tracking
- Ingested the source summary, UK release project page, key release entities, production-scale performance-testing concept, settlement-rule replay concept, cash-settlement incident-management concept, and chronology and NDS fixing queries.