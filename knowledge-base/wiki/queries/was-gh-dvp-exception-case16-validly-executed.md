---
type: query
title: Was GH DVP Exception Case16 Validly Executed?
created: 2026-08-23
updated: 2026-08-23
tags: [uat, ghana, dvp, nstp, test-validity]
related: [tranche-2-manual-entity-settlement-uat, ghana-scb-ghana-acc-gbs, country-specific-settlement-uat-coverage]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/UAT testing checking-Tranche2.md"]
---
# Was GH DVP Exception Case16 Validly Executed?

## Question

Can GH DVP exception case16 be accepted when the recorded cashflows did not hit the DVP exception path but the result was marked as passed?

## Evidence

The tracker records GH DVP exception case16 with cashflows `M00126097470/M00126080232` and the comment dated 2026-08-11: “This cashflow not hit DVP exception ,but the result is passed.”

## Required Clarification

Confirm the intended preconditions and assertions for case16, identify whether entering the DVP exception path was mandatory, and explain the pass criterion. The associated workflow, rule evaluation, NSTP status, and test evidence should be attached before the result is treated as valid.

## Status

Open. The source establishes a test-validity concern but does not prove that the pass was incorrect.