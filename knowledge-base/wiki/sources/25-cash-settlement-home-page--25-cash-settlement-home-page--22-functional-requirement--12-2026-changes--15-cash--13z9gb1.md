---
type: source
title: Copy of Cash Settlement Migration - Korea Test Cases
authors: []
year: 2026
url: ""
venue: Internal UAT test-case tracker
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, korea, cash-settlement, migration, uat, testing]
related: [ratan-settlement-korea, korea-ratan-uat-coverage, korea-manual-payment-integration, maker-checker-settlement-controls, did-korea-ratan-production-data-dump-and-swift-reconciliation-pass, should-korea-enable-inter-entity-bic-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/Copy of Cash Settlement Migration - Korea Test cases.md"]
---
# Copy of Cash Settlement Migration - Korea Test Cases

This internal tracker records 171 RATAN and MX2.11 Korea cash-settlement migration test cases executed primarily from May through July 2026. It is execution evidence for [[projects/ratan-settlement-korea]], rather than a signed production-readiness decision or authoritative functional specification.

## Test Result Summary

| Result | Cases |
|---|---:|
| PASS | 119 |
| DESCOPED | 48 |
| PENDING-Dump data | 3 |
| WIP | 1 |
| FAIL | 0 |

The passed cases cover RATAN user access, Korea data entitlement, cashflow search and export, settlement fields, SSI stamping, Main Nostro processing, netting and splitting, event handling, exception controls, selected NDS CCS netting, manual payments, SWIFT/MX generation, dashboards, EOD checks, reporting, and static-data maintenance.

The absence of recorded failures does not establish complete readiness: three production-data validations remain pending and inter-entity auto-netting remains WIP.

## Tested Korea Scope

The tracker supports Korea-specific evidence for:

- Country-based access restrictions, including a Korea user being unable to retrieve an LDN cashflow.
- SSI selection using exact product CFI, related Rates CFI, `MXBLANK`, Global fallback, and a tested Korea-entity preference over Global product-specific SSI.
- Main Nostro payment and receipt processing, including receipt processing without a Missing Vostro exception when Main Nostro is stamped.
- Maker/checker controls for manual SI input, netting, processing, suppression, and static-data changes.
- Manual and automated netting, gross override, splitting, un-splitting, and recovery from amendments or cancellations.
- Selected NDS CCS auto-netting: USD/INR, USD/BRL, and USD/KRW, including re-fixing and automatic un-netting/re-netting for USD/KRW.
- RATAN-to-OLTP-TIS manual-payment flows for KRW and FCY.
- MT103, MT202, MT103+202COV, MT210, MT192, MT292 and corresponding MX message scenarios, with ENISIS and/or SWIFT SAA acknowledgements.
- EOD accounting-error checks and Korea cashflow reporting through SSDR.

Korea exclusions include Fedwire payments, RATAN Over-Account processing, LIEN scenarios, precious-metal settlement, CNY ND CCS, ND-Bond, and several NDS variants. These exclusions are Korea scope boundaries and should not be interpreted as global RATAN capability limits.

## Outstanding Validation

The following cases are explicitly incomplete:

- Dashboard SWIFT and accounting-error validation against two days of production dump data.
- Dashboard sequence validation for cashflows stuck in Group Pending, using two days of production dump data.
- Three-day MX2.11-to-RATAN SWIFT reconciliation and one-day RATAN payment-type reconciliation with ENISIS.

See [[did-korea-ratan-production-data-dump-and-swift-reconciliation-pass]].

## Work in Progress

Inter-entity auto-netting was recorded as WIP. The tracker states that Deepak must configure a BIC netting rule and that business use of the rule requires discussion. See [[should-korea-enable-inter-entity-bic-netting]].

## Evidence and Limitations

Many PASS entries cite screenshots and cashflow identifiers. The supporting archives referenced by the tracker are:

- `REST_UAT_codeversion2.zip`
- `RETEST_UAT_codeversion1.zip`
- `KR_ENISI_UAT.zip`

The document is labelled “Copy of,” so its version authority relative to those archives is not established.

Several manual-payment cases are marked PASS while their expected RATAN status remains `TBC`; this demonstrates flow execution and OLTP-TIS retrieval, but not a confirmed intended final RATAN state.

---

---FILE: wiki/concepts/korea-ratan-uat-coverage.md---
---
type: concept
title: Korea RATAN UAT Coverage
created: 2026-08-22
updated: 2026-08-22
tags: [korea, ratan, uat, test-coverage, cash-settlement]
related: [ratan-settlement-korea, korea-ssi-onboarding, korea-manual-payment-integration, maker-checker-settlement-controls, reconciliation, swift-status-reconciliation, did-korea-ratan-production-data-dump-and-swift-reconciliation-pass, should-korea-enable-inter-entity-bic-netting]
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- 2026 Changes -- Cash Settlement -- Korea Migration -- Copy of Cash Settlement Migration - Korea Test cases.md"]
---
# Korea RATAN UAT Coverage

Korea RATAN UAT coverage is the documented functional-test evidence for migrating Korea cash-settlement operations from [[murex-2-11]] into [[ratan]].

## Recorded Outcome

The tracker records 119 PASS results out of 171 cases, with 48 DESCOPED cases, three production-data cases pending, one inter-entity netting case WIP, and no recorded FAIL results.

Passed coverage includes:

- RATAN access, user entitlement, search, filtering, export, audit trail, and dashboard functions.
- SSI selection, Main Nostro stamping, and manual SI controls.
- Netting, splitting, gross override, suppression, hold, fail, reinstate, and bulk processing.
- Event lifecycle handling for amendments, cancellations, value-date changes, fixing, netting changes, and split cashflows.
- Selected NDS CCS netting, Korea manual-payment integration, SWIFT/MX generation, reporting, EOD checks, and static-data maintenance.

## Readiness Boundary

This evidence supports functional UAT execution, not unconditional migration readiness. The outstanding production-data dashboard checks and SWIFT reconciliation remain material evidence gaps. Inter-entity BIC netting also requires both configuration and a business decision.

Korea-specific descopes, including Fedwire, LIEN, precious-metal settlement, and selected NDS flows, must remain scoped to Korea rather than being generalized to all RATAN deployments.

## Related Controls

Key controls evidenced by the test record include [[maker-checker-settlement-controls]], [[korea-ssi-onboarding]], [[straight-through-processing]], [[cashflow-suppression]], and [[swift-mt-mx-integration]].

---

---FILE: wiki/concepts/korea-manual-payment-integration.md---
---
type: concept
title: Korea Manual Payment Integration
created: 2026-08-22
updated: 2026-08-22
tags: [korea, ratan, oltp-tis, manual-payments, settlement]
related: [ratan-settlement-korea, maker-checker-settlement-controls, cashflow-status-handling]
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- 2026 Changes -- Cash Settlement -- Korea Migration -- Copy of Cash Settlement Migration - Korea Test cases.md"]
---
# Korea Manual Payment Integration

Korea Manual Payment Integration is the RATAN-to-OLTP-TIS handling of Korea cashflows that require manual-payment processing rather than standard RATAN settlement-message handling.

## UAT-Tested Flows

The source records PASS results for the following flows:

- `5318` — KRW credit to Over Account client.
- `5319` — FCY credit to Over Account client.
- `5323` — Another Bank (IRN), KRW.
- `5324` — Bank of Korea settlement payment to beneficiary bank, KRW.
- `5325` — Bank of Korea payment to final beneficiary, KRW.
- `3013` — Direct debit to client account, FCY.
- `0201` — Direct debit to client account, KRW.
- `5338` — Internal transfer to another branch, KRW.
- `5339` — Internal transfer to another branch, FCY.

For the relevant scenarios, the test record shows maker/checker execution and retrieval of cashflow information in OLTP-TIS.

## Event Handling

The source also marks PASS for post-processing amendment and cancellation tests. These results indicate that RATAN amendments and cancellations did not affect the OLTP-TIS process in the tested scenarios.

## Open Requirement Detail

Several flow cases are marked PASS even though their expected RATAN cashflow status is stated as `TBC`. The test evidence confirms flow execution, but does not establish the intended final RATAN state. This should be resolved before using these cases as complete operational acceptance criteria.

---

---FILE: wiki/concepts/maker-checker-settlement-controls.md---
---
type: concept
title: Maker/Checker Settlement Controls
created: 2026-08-22
updated: 2026-08-22
tags: [maker-checker, segregation-of-duties, settlement-controls, ratan, korea]
related: [korea-ratan-uat-coverage, korea-manual-payment-integration, cashflow-suppression, manual-failure-and-reinstatement, nostro-static-management]
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- 2026 Changes -- Cash Settlement -- Korea Migration -- Copy of Cash Settlement Migration - Korea Test cases.md"]
---
# Maker/Checker Settlement Controls

Maker/checker settlement controls enforce segregation between the user initiating a settlement-related action and the user approving it.

## Korea UAT Evidence

The Korea RATAN test tracker records passed maker/checker scenarios for:

- Dual-blind manual SI input, including prevention of a maker approving their own entry and mismatch validation.
- Manual netting for netting-defined and ad hoc clients.
- Bulk processing of eligible cashflow exceptions.
- Manual failure and subsequent processing of reinstated cashflows.
- Manual SWIFT and cashflow suppression.
- Korea manual-payment flows sent to OLTP-TIS.
- Creation and modification of NSTP rules, SWIFT suppression rules, cashflow suppression rules, Nostro static data, bilateral netting static data, and auto-distribution rules.

## Control Boundary

Some actions are explicitly single-level in the tested process, including early release, hold, and reinstate. The control model should therefore be assessed by action type rather than assumed to be uniformly dual-controlled.

The tracker also records that users with Cashflow Blotter access could search and export data while being unable to perform settlement actions, supporting a separation between inquiry and operational permissions.

---

---FILE: wiki/queries/did-korea-ratan-production-data-dump-and-swift-reconciliation-pass.md---
---
type: query
title: Did Korea RATAN Production Data Dump and SWIFT Reconciliation Pass?
created: 2026-08-22
updated: 2026-08-22
tags: [korea, ratan, reconciliation, production-data, swift, open-question]
related: [ratan-settlement-korea, korea-ratan-uat-coverage, reconciliation, swift-status-reconciliation]
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- 2026 Changes -- Cash Settlement -- Korea Migration -- Copy of Cash Settlement Migration - Korea Test cases.md"]
---
# Did Korea RATAN Production Data Dump and SWIFT Reconciliation Pass?

## Question

Were the pending Korea RATAN production-data validations completed, and did they pass?

## Evidence

The source marks three cases as `PENDING-Dump data`:

- Two-day production-dump review confirming no SWIFT or accounting errors.
- Two-day production-dump review confirming cashflows are not improperly stuck in Group Pending, or documenting valid stuck scenarios.
- Three-day SWIFT-data reconciliation between [[murex-2-11]] and [[ratan]], plus one-day RATAN payment-type reconciliation with ENISIS.

## Why It Matters

These controls are not covered by the passed functional UAT cases. They are necessary evidence for operational behavior over production-like data volumes and for cross-system message completeness.

## Needed Resolution

Obtain the completed dump-data reports, reconciliation output, exception disposition, and formal owner sign-off. If evidence does not exist, record this as a residual release or post-release control risk for [[ratan-settlement-korea]].

---

---FILE: wiki/queries/should-korea-enable-inter-entity-bic-netting.md---
---
type: query
title: Should Korea Enable Inter-Entity BIC Netting?
created: 2026-08-22
updated: 2026-08-22
tags: [korea, ratan, inter-entity, bic-netting, netting, open-question]
related: [ratan-settlement-korea, korea-ratan-uat-coverage, netting-key-selection]
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- 2026 Changes -- Cash Settlement -- Korea Migration -- Copy of Cash Settlement Migration - Korea Test cases.md"]
---
# Should Korea Enable Inter-Entity BIC Netting?

## Question

Should Korea use RATAN inter-entity auto-netting based on BIC netting logic?

## Evidence

The inter-entity auto-netting test case is marked `WIP`. The tracker states that Deepak must configure the BIC netting rule and that use of the rule requires discussion.

Other Korea netting scenarios, including client auto-netting, manual netting, clearing settlement, and selected NDS CCS netting, are marked PASS. Those outcomes do not confirm inter-entity BIC-netting eligibility.

## Decision Needed

Confirm:

1. The intended Korea business scope for inter-entity BIC netting.
2. The required BIC netting static-data configuration.
3. Ownership for configuration, testing, approval, and operational monitoring.
4. Whether enabling the rule introduces settlement, accounting, or reconciliation impacts.

Until resolved, inter-entity auto-netting should be treated as outside the demonstrated Korea UAT scope.

---

---FILE: wiki/log.md---
## 2026-08-22 ingest | Copy of Cash Settlement Migration - Korea Test Cases

- Added UAT evidence summary, Korea manual-payment and maker/checker control concepts, and open queries for pending production-data reconciliation and inter-entity BIC netting.