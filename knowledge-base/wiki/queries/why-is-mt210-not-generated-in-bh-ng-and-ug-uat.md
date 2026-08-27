---
type: query
title: Why Is MT210 Not Generated in BH, NG, and UG UAT?
created: 2026-08-23
updated: 2026-08-23
tags: [uat, mt210, message-generation, defect-investigation, settlement]
related: [mt210-message-generation, tranche-2-manual-entity-settlement-uat, bahrain-scb-bahrai-man-gbs, scb-nigeria-lag-gbs, uganda-scb-uganda-kam-gbs, settlement-acknowledgement-flow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/UAT testing checking-Tranche2.md"]
---
# Why Is MT210 Not Generated in BH, NG, and UG UAT?

## Question

What rule, configuration, or processing condition caused MT210 not to be generated when the UAT tracker states that it should have been generated for BH, NG, and UG?

## Evidence

- BH: cases 6, 7, and 13; cashflows `M00127052845/M00127113310`; observation dated 2026-08-06.
- NG: case 20; cashflow `M00126623233`; observation dated 2026-08-11.
- UG: cases 6, 13, and 7; cashflows `M00127113688/M00127114179`; observation dated 2026-08-13.

The observations are repeated across three scopes, but the source contains no logs, expected-rule definition, queue evidence, formal defect reference, or populated test report.

## Investigation Tasks

Confirm the applicable MT210 generation contract, compare entity configuration and settlement instructions, verify test-data preconditions, inspect application and FMSGW/RATAN processing, and attach retest evidence. Do not infer that the issue has a single shared cause until those comparisons are complete.

## Status

Open. The source demonstrates an operational mismatch, not a confirmed defect diagnosis or release blocker.