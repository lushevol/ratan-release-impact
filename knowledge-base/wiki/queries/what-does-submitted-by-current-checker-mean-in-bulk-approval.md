---
type: query
title: What Does “Submitted by Current Checker” Mean in Bulk Approval?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, bulk-approve, checker, maker-checker, open-question]
related: [cashflow-bulk-submit-and-approve, bulk-exception-preview-eligibility, swift-value-date-maker-checker-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Process for Multi Exceptions/Bulk UI Technical Design.md"]
---
# What Does “Submitted by Current Checker” Mean in Bulk Approval?

## Question

What precise maker/checker restriction is represented by the condition “checker stage, and is submitted by current checker”?

## Possible Interpretations

The condition may mean either:

- A checker cannot approve a cashflow that they previously submitted.
- A cashflow already submitted by the current checker is excluded from checker-stage bulk processing for another reason.

The source does not distinguish between these interpretations.

## Required Clarification

Define the relevant submission event, the identity used for comparison, the period for which submission history matters, and whether the restriction blocks the entire batch or only the affected cashflow. Also confirm whether the rule applies only to **Bulk Approve** or to other checker actions.