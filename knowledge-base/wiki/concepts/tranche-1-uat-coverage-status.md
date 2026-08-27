---
type: concept
title: Tranche 1 UAT Coverage Status
created: 2026-08-23
updated: 2026-08-23
tags: [uat, test-coverage, manual-entities, settlement, tranche-1]
related: [country-specific-settlement-uat-coverage, manual-entity-settlement-enablement, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--obojum]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/UAT testing checking-Tranche1.md"]
---
# Tranche 1 UAT Coverage Status

A UAT tracker should separate scenario status from acceptance status. The Tranche 1 tracker provides evidence for the following distinct states:

- **Evidenced:** a test case, cashflow identifier, report link, screenshot, or attachment is recorded.
- **Uncovered:** the tracker explicitly says no case is covered or asks whether required variants need coverage.
- **Blocked:** execution cannot proceed because of a stated dependency, such as Tanzania DFCC trade booking in [[murex]].
- **Descoped or not applicable:** the tracker states that a scenario is not required; this remains country-specific unless supported by a formal cross-country rule.
- **Disputed expected result:** a test outcome is recorded but conflicts with the stated expected behavior, as for the Kenya and Vietnam MT210 rows and the Kenya DVP NSTP row.

Evidence of individual execution does not demonstrate full acceptance. Completion requires an agreed scenario matrix, traceable results, resolution of disputed outcomes, and confirmation that country-specific scope decisions are approved.