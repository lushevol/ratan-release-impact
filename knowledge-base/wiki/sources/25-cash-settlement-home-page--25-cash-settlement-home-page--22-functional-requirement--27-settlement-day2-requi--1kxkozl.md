---
type: source
title: Tranche 2 Manual-Entity Settlement UAT Tracking
authors: []
year: 2026
url: ""
venue: "Operational UAT tracking document"
created: 2026-08-23
updated: 2026-08-23
tags: [uat, settlement, manual-entities, tranche-2, swift, mx]
related: [manual-entity-settlement-enablement, manual-entity-settlement-onboarding, country-specific-settlement-uat-coverage, manual-entity-swift-mx-bifurcation, mt210-message-generation, cashflow-suppression-rule, cashflow-splitting, why-is-mt210-not-generated-in-bh-ng-and-ug-uat, was-gh-dvp-exception-case16-validly-executed, must-qatar-slate-one-cashflow-suppression-be-verified-in-uat, should-ug-split-cashflows-trigger-wht-nstp-rules]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/UAT testing checking-Tranche2.md"]
---
# Tranche 2 Manual-Entity Settlement UAT Tracking

## Scope

This document is an operational tracking sheet for Tranche 2 UAT scenarios supporting settlement enablement for manual entities. It covers BH, QA, QATAR SLATE ONE LLC*DOH, NG, GH, and UG scenarios involving MT103, MT202, MT202COV, MT202Flip, MT210, MX routing, withdrawal, DVP NSTP exceptions, netting, and split cashflows.

The sheet is not a formal test report. The `Test Report` column is blank throughout, and the entries do not consistently provide expected results, actual results, evidence, or approval status. Scenario listing must therefore be distinguished from verified execution.

## Recorded UAT Data

| Country | UAT scenario | UAT testcase | cashflow id | Comment | Test Report |
| --- | --- | --- | --- | --- | --- |
| BH | MT103/202COV/withdraw | case1 /case2/case3/case5/case12/case18 | M00127113543/N00000120435/ S00000120437 | 2026-08-06 No cancellation for MX covered No MT202FLip-MX | |
| MT103 external MX | case1 | M00127114900 | |
| MT103 cov external MT202 cov internal | case18 | S00000120436 | |
| MT103 internal MX | case20 | M00127115448 | |
| MT202& withdraw | case4/case11 | M00127113321 | |
| MT202Flip | case8 | M00126967696 | |
| MT202 | case9 | M00127114211 | |
| MT202 External MX | case9 | M00127114920 | |
| MT202 internal MX | case21 | M00127115452 | |
| MT103&Withdraw | case10 | M00127113942 | |
| MT210 | case6/case7/case13 | M00127052845/M00127113310 | 2026-08-06 Tested result is not matched with the expected result ,should generate MT210 ,but not generate | |
| BH-BH | | | 2026-08-14 Deepak will arrange to test it . 📎 [RE UAT testcase open questions for tranche2 -BH-BH RTGS.msg](attachments/RE UAT testcase open questions for tranche2 -BH-BH RTGS.msg) 2026-08-07 Need to follow up after CPT ![image-2026-8-10_16-22-53.png](attachments/image-2026-8-10_16-22-53.png) | |
| DVP NSTP exception | case19 | M00127114666 | | |
| QA | MT103/withdraw | case1 /case2/case3/case10 | M00127115369/M00127115463/M00127113745 | 2026-08-13 No cancellation for MT103/MT202 covered No MT202FLip-MX | |
| MT103 external MX | case1 | M00127115377 | |
| MT202 | case4 | M00127114408 | |
| MT202 external MX | case4/case9 | M00127114902 | |
| MT103 external MX MT202 internal MX | case5 | M00127115372 | |
| MT210&withdraw | case6/case7/case13 | M00127114702/M00127114701 | |
| MT202&withdraw | case8/case9 | M00127114668/M00127113370/M00127115459 | |
| MT103 cov external MX&withdraw MT202cov internal MX & withdraw | case12 | M00127114700 | |
| MT103 internal MX | case20 | M00127115371 | |
| MT202 internal MX | case21 | M00127114426 | |
| QA-QA MT | case9 | M00127115459 | 2026-08-06 ![image-2026-8-10_16-22-43.png](attachments/image-2026-8-10_16-22-43.png) | |
| DVP NSTP | case19 | N00000120444 | | |
| QATAR SLATE ONE LLC*DOH | | | Synthia mentioned this cashflow should be casfhflow suppressed and no need to setup ,if need to verify during UAT？ | |
| NG | MT103 | case1/case2/case3/case4/case5/case6 | M00126621544/M00126623229/M00127011525 | MX cancellation not covered MT202Flip -MX not covered | |
| MT103external MX | case1 | M00127115281 | |
| MT202 | case6/case7/case8/case9/case12 | M00127113641/M00127113558/M00126683225/M00127113579/M00127113533 | |
| MT103COV/202COV | case10 | M00126623229 | |
| MT202Flip | case11 | M00126683224 | |
| MT202 | case12 | M00127113533 | |
| MT103 | case14 | M00126621633 | |
| MT202 external MX | case15 | M00127115287 | |
| MT103&withdraw | case17 | M00126080077 | |
| MT202&withdraw | case18 | M00126026660 | |
| MT103COV/MY202COV/withdraw | case19 | M00126621523 | |
| MT103COV/MT202COV | casee24 | N00000120325 | |
| MT103 internal MX | casse30/case32 | M00127115444/M00127115547 | |
| MT202 intern MT202Flip al MX | case31/case33 | M00127115446/M00127115563 | |
| MT210 | case20 | M00126623233 | 2026-08-11 Tested result is not matched with the expected result ,should generate MT210 ,but not generate | |
| rounding precison to 0 | | | | |
| GH | MT103&withdraw | case1/case2/case3/case10 | M00127113614 | | |
| MT103 external MX | case1 | M00127115269 | |
| MT202 external MX | case1/case9 | M00127115272/M00127115275 | |
| MT202&withdraw | case4/case11 | M00127113755 | |
| MT103COV/MY202COV/withdraw | case5/case12 | M00127113575 | |
| MT210 | case6/case7 | 007408012777/007408012731 | |
| MT202&withdraw | case8/13 | M00127113379 | |
| MT202 | case9 | M00127114406/M00127115339 | |
| MT103-Netting | case15 | N00000120422 | |
| MT202 internal MX | case17 | M00127115443 | |
| MT103 internal MX | case18 | M00127115441 | |
| DVP exception | case16 | M00126097470/M00126080232 | 2026-08-11 This cashflow not hit DVP exception ,but the result is passed | |
| UG | MT103&withdraw | case1/case2/case3/case10 | M00127113599 | | |
| MT103 external MX | case1 | M00127115260 | | |
| MT202 | case4/case9 | M00126746157 | | |
| MT103COV/MY202COV/withdraw | case5/case12 | M00126413291 | | |
| MT202Flip | case8 | M00126669829 | | |
| MT202 external MX | case9 | M00127115263 | | |
| MT202&withdraw | case11 | M00127114293 | | |
| MT202 internal MX | case17 | S00000120443 | | |
| MT103 internal MX | case18 | S00000120442 | | |
| MT210 | case6/case13/case7 | M00127113688/M00127114179 | 2026-08-13 Tested result is not matched with the expected result ,should generate MT210 ,but not generate | |
| Split cash flow - Withholding TAX | case15 | S00000121068/S00000121067 | 2026-08-13 What does this mean ,need the split cashflow to hit WHT NSTP?but I didn't see the split cashflow hit any WHT NSTP rule | |
| DVP exception | case16 | M00127114567/M00127114566 | | |
| | | | | |
| | | | | |

## Findings

### Repeated MT210 non-generation

BH, NG, and UG each record an observed mismatch in which MT210 was expected but was not generated. The affected cashflows are:

- BH: `M00127052845/M00127113310`, cases 6, 7, and 13; observation dated 2026-08-06.
- NG: `M00126623233`, case 20; observation dated 2026-08-11.
- UG: `M00127113688/M00127114179`, cases 6, 13, and 7; observation dated 2026-08-13.

The source does not identify whether the common cause is a shared rule, entity configuration, test-data issue, or message-generation defect. See [[queries/why-is-mt210-not-generated-in-bh-ng-and-ug-uat]] and [[concepts/mt210-message-generation]].

### Explicitly incomplete MX coverage

BH, QA, and NG contain notes excluding some MX cancellation and MT202Flip-MX scenarios. These entries establish recorded scope limitations, but do not establish that the exclusions were formally approved or intentionally de-scoped. They should not be treated as successful test results.

### Outstanding BH-BH testing

BH-BH testing remained subject to follow-up. The notes reference Deepak arranging a test on 2026-08-14 and a follow-up after CPT. The attached message file and image are evidence references, not execution results.

### GH DVP exception validity concern

The GH DVP exception case16 cashflows reportedly did not hit the DVP exception, while the result was marked as passed. The scenario’s expected assertion and pass criteria require confirmation. See [[queries/was-gh-dvp-exception-case16-validly-executed]].

### Open configuration and rule questions

The QATAR SLATE ONE LLC*DOH note says the cashflow should be cashflow suppressed and may not require setup, but asks whether it should be verified during UAT. See [[queries/must-qatar-slate-one-cashflow-suppression-be-verified-in-uat]].

The UG split-cashflow Withholding TAX case asks whether split cashflows should hit a WHT NSTP rule. The source does not define the rule’s eligibility conditions or expected result. See [[queries/should-ug-split-cashflows-trigger-wht-nstp-rules]].

## Evidence Limitations

- All `Test Report` fields are blank.
- Formal approval, release readiness, and UAT completion cannot be inferred.
- Several rows appear shifted or malformed relative to the table header.
- The source contains apparent typographical inconsistencies, including `casee24`, `casse30/case32`, `MT202 intern MT202Flip al MX`, `rounding precison`, and `casfhflow`.
- Expected results and actual results are generally not recorded.
- Some cashflow IDs are associated with multiple cases without an explanation of the traceability model.
- The source does not provide logs, timestamps beyond comments, queue states, defect identifiers, or formal evidence links for the reported mismatches.

## Related Pages

This tracker extends [[concepts/manual-entity-settlement-enablement]], [[concepts/manual-entity-settlement-onboarding]], and [[concepts/country-specific-settlement-uat-coverage]]. Its message-path entries relate to [[concepts/manual-entity-swift-mx-bifurcation]], while the Slate One note relates to [[entities/qatar-slate-one-llc-doh-gbs]] and [[concepts/cashflow-suppression-rule]]. The UG split-cashflow question relates to [[concepts/cashflow-splitting]].