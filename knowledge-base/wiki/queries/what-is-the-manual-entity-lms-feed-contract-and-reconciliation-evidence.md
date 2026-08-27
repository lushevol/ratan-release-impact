---
type: query
title: What Is the Manual-Entity LMS Feed Contract and Reconciliation Evidence?
created: 2026-08-23
updated: 2026-08-23
tags: [LMS, manual-entities, integration-contract, reconciliation, UAT]
related: [manual-entity-lms-reference-data-feed, lms, manual-entity-settlement-onboarding, cross-border-debit-lms-feed-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/019 Feed Manual Entities to LMS.md"]
---
# What Is the Manual-Entity LMS Feed Contract and Reconciliation Evidence?

## Question

What is the authoritative integration contract and completion evidence for feeding the 13 manual-entity records to LMS?

## Specific Unknowns

- Which system publishes the manual-entity roster to LMS?
- What payload, file, API, or message schema is authoritative?
- Are `FMID`, `COUNTRY CODE`, `FMCODE`, and `BRANCH CODE` mandatory LMS fields?
- Are alphabetic branch codes `UG` and `QA` valid by design?
- What response or audit evidence confirms acceptance of each record?
- How are rejected, duplicated, amended, or removed records handled?
- What reconciliation proves that LMS contains the intended 13 records?
- Does the manual-entity feed share any contract or processing rules with [[cross-border-debit-lms-feed-contract]]?

## Current Evidence

[[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--1mr6oix]] provides the roster and establishes intended scope. It does not contain an interface specification, execution log, test results, reconciliation output, or approval.

## Resolution Needed

Obtain the LMS integration specification, source-to-target mapping, feed execution evidence, record-level acknowledgements, and reconciliation or UAT approval artefacts before treating the roster as a completed onboarding event.