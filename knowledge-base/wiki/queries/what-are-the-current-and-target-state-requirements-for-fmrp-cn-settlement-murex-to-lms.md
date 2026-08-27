---
type: query
title: What Are the Current and Target State Requirements for FMRP CN Settlement Murex to LMS?
created: 2026-08-24
updated: 2026-08-24
tags: [cn-settlement, fmrp, murex-2-11, lms, requirements-gap, surrounding-system-integration]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--30-surrounding-system-in--1xh1k97, fmrp, lms, murex-211, cn-settlement-murex-211-integration, surrounding-system-integration, lms-cashflow-feed-eligibility, lms-event-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/FMRP CN Settlement - Murex Cashflow to LMS.md"]
---
# What Are the Current and Target State Requirements for FMRP CN Settlement Murex to LMS?

## Question

What are the authoritative current-state and target-state requirements for the apparent CN Settlement integration topic involving [[fmrp]], [[murex-211]], and [[lms]]?

## Evidence gap

[[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--30-surrounding-system-in--1xh1k97]] contains only the headings `Current State` and `Target State`. It does not answer this question.

## Information required

An authoritative requirements source should establish:

- the participating systems and system-of-record responsibilities;
- message direction, triggers, cashflow eligibility, lifecycle states, and sequencing;
- transport and payload contracts, including identifiers and mappings;
- error handling, retry, reconciliation, monitoring, and operational ownership;
- delivery scope, migration assumptions, testing, and acceptance criteria.

Existing pages on [[lms-cashflow-feed-eligibility]] and [[lms-event-contract]] are related knowledge but cannot be assumed to govern this integration without direct evidence.

## Next step

Locate a completed version of the requirements artifact or a formally approved design, interface specification, delivery record, or test evidence for the [[cn-settlement-murex-211-integration]] project.