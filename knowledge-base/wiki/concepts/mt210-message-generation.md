---
type: concept
title: MT210 Message Generation
created: 2026-08-23
updated: 2026-08-23
tags: [mt210, swift, message-generation, uat, settlement]
related: [settlement-acknowledgement-flow, manual-entity-swift-mx-bifurcation, tranche-2-manual-entity-settlement-uat, why-is-mt210-not-generated-in-bh-ng-and-ug-uat]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/UAT testing checking-Tranche2.md"]
---
# MT210 Message Generation

MT210 Message Generation is the expected production of an MT210 message during applicable manual-entity settlement scenarios. In the Tranche 2 UAT tracker, MT210 scenarios are listed for BH, QA, NG, GH, and UG.

## Observed UAT Issue

The tracker records an expected MT210 that was not generated for three scopes:

- BH cases 6, 7, and 13, cashflows `M00127052845/M00127113310`, observed 2026-08-06.
- NG case 20, cashflow `M00126623233`, observed 2026-08-11.
- UG cases 6, 13, and 7, cashflows `M00127113688/M00127114179`, observed 2026-08-13.

The source does not establish a shared root cause. Possible areas requiring evidence include message-generation rules, country or entity configuration, settlement-instruction data, test-data preconditions, and downstream routing.

## Required Investigation Evidence

Investigation should compare the affected scenarios with a known-good MT210 flow and capture:

1. The authoritative rule requiring MT210 generation.
2. Input cashflow and settlement-instruction data.
3. Application, RATAN, and FMSGW processing logs.
4. Message-queue or message-holding state.
5. Generated-message search results and timestamps.
6. Any formal defect identifier and retest evidence.

The QA and GH MT210 rows must not be classified as failures solely because they list MT210 scenarios; this source does not record the same non-generation observation for them.