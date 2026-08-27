---
type: source
title: UAT Testing Checking — Tranche 1 Manual-Entity Settlement
authors: []
year: 2026
url: ""
venue: Internal UAT coverage tracker
created: 2026-08-23
updated: 2026-08-23
tags: [uat, manual-entities, settlement, tranche-1, swift, mx]
related: [manual-entity-settlement-enablement, country-specific-settlement-uat-coverage, manual-entity-swift-mx-bifurcation, murex, scb-kenya-b, tanzania-scb-dar, vietnam-scb-hanoi-hni-gbs, zambia-scb-zambia-lus-gbs, what-is-the-authoritative-mt210-eligibility-rule-for-manual-entities, what-is-the-approved-tanzania-dfcc-uat-scenario-and-murex-dependency, is-bangladesh-mt202flip-formally-descoped, have-all-tranche-1-business-rule-changes-been-verified]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/UAT testing checking-Tranche1.md"]
---
# UAT Testing Checking — Tranche 1 Manual-Entity Settlement

This operational tracker records Tranche 1 UAT scenarios, cashflow identifiers, automated-report references, coverage gaps, and open expected-result issues for manual-entity settlement. It is point-in-time evidence, not a final acceptance or sign-off record.

The tracker demonstrates uneven documented coverage. It distinguishes scenarios with recorded evidence from scenarios that are uncovered, blocked by dependencies, explicitly descoped, or affected by disputed expected results. Country-specific conditions must not be interpreted as authoritative routing rules for other entities.

## Key findings

- Kenya has automated-report links for one MX-routing scenario, but the DFCC variant has no recorded case and several cover, withdrawal, and MT202Flip variants remain open.
- Tanzania has evidence only for its first listed scenario. Its DFCC scenario is blocked pending trade booking in [[murex]].
- Kenya and Vietnam each record an MT210 expected-result mismatch for a named cashflow. The tracker does not define a general MT210 eligibility rule.
- Bangladesh records broad internal MT coverage and one external MX case, while cancellation is pending. Its MT202Flip scope changed from a requested test to “no need to test,” without a cited formal decision.
- Pakistan explicitly records MT103COV, MT202COV, MT202Flip, and withdrawal as not covered.
- The final tracker question asks whether new or updated business rules have been verified for all Tranche 1 entities.

## Coverage tracker

| Country | UAT scenario | UAT testcase | Cashflow ID | Comment | Test report |
| --- | --- | --- | --- | --- | --- |
| KE | 1. Sender BIC starts with SCBLKE and Receiver BIC does not start with SCBLKE, Settlement Account does not end with DFCC and does not equal KES MAIN — MX | case1, case6, case22, case23 | M00127114316 MT103 → internal MX; M00127114906 MT202 → external MX; M00127114904 MT103 external MX cancellation; M00127114906 MT202 external MX cancellation | Open coverage question: MT103 external MX, MT202 internal MX, withdrawal, MT103COV/MT202COV MX, and MT202Flip generating MX. | EG UBER: https://ratan-dev.uk.dev.net:9002/test-reports/auto-test/regression/1785480514603/report.html; EG SCBXML: https://ratan-dev.uk.dev.net:9002/test-reports/auto-test/regression/1785480531062/report.html; US: https://ratan-dev.uk.dev.net:9002/test-reports/auto-test/regression/1785481840724/report.html; IN: https://ratan-dev.uk.dev.net:9002/test-reports/auto-test/regression/1785481883308/report.html; UK: https://ratan-dev.uk.dev.net:9002/test-reports/auto-test/regression/1785488818490/report.html; KR: https://ratan-dev.uk.dev.net:9002/test-reports/auto-test/regression/1785480466729/report.html; withoute2e: https://ratan-dev.uk.dev.net:9002/test-reports/auto-test/regression/1785480671544/report.html; https://ratan-dev.uk.dev.net:9002/test-reports/auto-test/regression/1785482774494/report.html; https://ratan-dev.uk.dev.net:9002/test-reports/auto-test/regression/1785483623093/report.html |
| KE | 2. Sender BIC starts with SCBLKE and Receiver BIC does not start with SCBLKE, Settlement Account ends with DFCC — MT |  |  | No case covered. Open coverage question: MT103/MT202, MT103COV/MT202COV, withdrawal, and MT202Flip. |  |
| KE | 3. Sender BIC starts with SCBLKE and Receiver BIC does not start with SCBLKE, Settlement Account equals KES MAIN — MT | case6, case12, case13, case18 | M00126080255/N00000119666/M00126080100 MT202; M00126138908 MT103 and withdrawal | Open coverage question: MT103COV/MT202COV, withdrawal, and MT202Flip. |  |
| KE | 4. Sender BIC starts with SCBLKE and Receiver BIC starts with SCBLKE, Settlement Account does not end with DFCC and does not equal KES MAIN — MT | case1, case6, case11 | M00126080096 MT103; M00126080207/M00126097489 MT202 | Open coverage question: MT103COV/MT202COV, withdrawal, and MT202Flip. |  |
| KE | DVP NSTP exception | case13 | M00126080100; M00127114078 | 2026-08-05: M00127114078 hit DVP strategy NSTP exception. The cashflow did not hit the DVP exception, but the result passed. `Entity__Counterparty_SCI_FMID` was not in scope and CPTY did not meet the rule condition. |  |
| KE | MT210 | case21 | M00127115427 | 2026-08-05: New cashflow tested and generated MT210 M00127115486. The cashflow should not generate MT210; result does not match expectation. |  |
| TZ | 1. Sender BIC starts with SCBLTZ and Receiver BIC does not start with SCBLTZ, Nostro static BIC does not equal TANZTZTXXXX, Settlement Account does not end with DFCC — MX | case5, case6 | M00127115006; M00127115361 | MT202Flip and withdrawal not covered. |  |
| TZ | 2. Sender BIC starts with SCBLTZ and Receiver BIC starts with SCBLTZ, Nostro static BIC does not equal TANZTZTXXXX, Settlement Account does not end with DFCC — MT |  |  | No case covered. Potential scope: MT103, MT202, MT202Flip, MT103COV, MT202COV, withdrawal. |  |
| TZ | 3. Sender BIC starts with SCBLTZ and Receiver BIC does not start with SCBLTZ, Nostro static BIC equals TANZTZTXXXX, Settlement Account does not end with DFCC — MT |  |  | No case covered. Potential scope: MT103, MT202, MT202Flip, MT103COV, MT202COV, withdrawal. |  |
| TZ | 4. Sender BIC starts with SCBLTZ and Receiver BIC does not start with SCBLTZ, Nostro static BIC does not equal TANZTZTXXXX, Settlement Account ends with DFCC — MT |  |  | No case covered. Potential scope: MT103, MT202, MT202Flip, MT103COV, MT202COV, withdrawal. |  |
| TZ | DFCC case |  |  | 2026-08-13: Waiting for Murex to book trade. 2026-08-06: Waiting for user information to book trade. 2026-08-03: DFCC is new and no DFCC case appears reflected on the page. Attachment: `RE DFCC Payments - Nostro to be set up in RATAN. .msg`. |  |
| VN | Internal MT | case1, case11, case12, case13, case14 | N00000119447/M00127113940/M00127113940/M00125707258 MT202; M00127022151 MT103 |  |  |
| VN | MT202Flip | case19 | N00000119447 |  |  |
| VN | MT103 withdrawal | case21 | M00126565385 |  |  |
| VN | MT202 withdrawal | case22 | M00127030961 |  |  |
| VN | External MX | case25 | M00126791213 MT103 → external MX | Open coverage question: MT202 generating MX, MT103COV, MT202COV, MT202Flip, and withdrawal. |  |
| VN | MT210 | case24 | M00127113939 | 2026-08-05: Deepak is checking whether another currency can be used. This is not a priority and can proceed in parallel. The cashflow should not generate MT210; result does not match expectation. |  |
| BD | Internal MT | case2, case3, case16, case19, case20, case21, case22, case9, case10, case11, case18, case23 | M00127113409/M00127113407/M00127113405/M00127114719/M00127114725/M00127114721/M00127114412 MT103 and withdrawal; M00127114444/M00127114728/M00127114730/M00127114420/M00127114416 MT202 and two withdrawals | 2026-08-04: Deepak states one external case is covered; cancellation will be tested after Tanzania and other open cases complete. |  |
| BD | External MX |  | M00127114713 MT202 external MX | 2026-08-05: Deepak confirms M00127114713 covers external MX generation. |  |
| BD | MT202Flip |  |  | 2026-08-05: No such scenario; no need to test. 2026-08-03: MT202Flip was requested to verify `58BIC` in SWIFT static data, but no case was reflected on the page. |  |
| BD | Auto cashflow suppressed | case1 |  | No such scenario; descoped. |  |
| PK | Internal MT | case5 | 007373362592 | MT103COV, MT202COV, MT202Flip, and withdrawal not covered. |  |
| PK | External MX | case4 | M00127115297 |  |  |
| LK | Internal MT | case10 | M00127114526 | 2026-08-05 supporting screenshot recorded. |  |
| LK | External MX | case33 | M00127114897 |  |  |
| LK | Flip |  | M00127115505 | 2026-08-05 attachment: `RE LK nostro static followup call-3.msg`; supporting screenshot recorded. |  |
| ZM | Internal MT | case8 | M00127114168 |  |  |
| ZM | External MX | case9 | M00126097498 |  |  |
| Tranche 1 countries | Business rules |  |  | Open question: whether newly created or updated business rules are verified for these entities. |  |

## Interpretation constraints

The report links and attachments are evidence references, but the tracker does not provide an unambiguous pass/fail mapping between every report, test case, and cashflow. A recorded “passed” result does not establish complete country-level acceptance where the same tracker marks required scenarios as uncovered or blocked.

The BIC-prefix, settlement-account, and Nostro-static conditions are UAT scenario definitions. They are not sufficient evidence of an authoritative [[manual-entity-swift-mx-bifurcation]] specification.