---
type: query
title: Why Did the Kenya DVP NSTP Test Pass Without Matching the Stated Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [kenya, dvp, nstp, uat, test-oracle]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--obojum, scb-kenya-b, tranche-1-uat-coverage-status]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/UAT testing checking-Tranche1.md"]
---
# Why Did the Kenya DVP NSTP Test Pass Without Matching the Stated Rule?

For Kenya, the tracker states on 2026-08-05 that cashflow `M00127114078` passed a DVP strategy NSTP exception result despite not meeting the stated DVP exception condition. It specifically notes that `Entity__Counterparty_SCI_FMID` was not in scope and that CPTY did not meet the rule condition.

Required resolution evidence includes the approved DVP NSTP rule, the cashflow attributes used during evaluation, the executed assertion, and the definition of the recorded pass criterion.