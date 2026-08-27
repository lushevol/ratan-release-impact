---
type: query
title: What Is the Authoritative MT210 Eligibility Rule for Manual Entities?
created: 2026-08-23
updated: 2026-08-23
tags: [mt210, uat, expected-result, manual-entities, settlement]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--obojum, manual-entity-settlement-enablement, tranche-1-uat-coverage-status]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/UAT testing checking-Tranche1.md"]
---
# What Is the Authoritative MT210 Eligibility Rule for Manual Entities?

The tracker records conflicting MT210 expectations for two country-specific UAT cashflows:

- Kenya cashflow `M00127115427` reportedly generated MT210 `M00127115486`, although the tracker says it should not generate MT210.
- Vietnam cashflow `M00127113939` reportedly did not generate MT210, although the tracker says that result does not match expectation. A possible currency change was being investigated.

The source does not supply the MT210 eligibility rule, message payloads, cashflow attributes, currency conditions, or approved expected-result definitions. Determine whether each mismatch is caused by product behavior, test data, currency eligibility, or an incorrect test oracle.