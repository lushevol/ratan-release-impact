---
type: query
title: What Are the TLM, LMS, and CIS Impacts of IRS Cashflow Aggregation?
tags: [irs, cashflow, aggregation, integration, tlm, lms, cis]
related: [irs-cashflow-aggregation, tlm, lms, cis, cashflow-aggregation-state-model]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Aggregation.md"]
---
# What Are the TLM, LMS, and CIS Impacts of IRS Cashflow Aggregation?

## Question

How do [[tlm]], [[lms]], and [[cis]] consume or respond to aggregated, waiting, unaggregated, and dead cashflow states?

## Evidence

The source marks TLM impact as TBC. It identifies a possible LMS impact if `WAITING` cashflow feeds are sent and a possible CIS impact for PM currency. No interface specifications, ownership decisions, event contracts, or message mappings are supplied.

## Required resolution

For each downstream system, confirm:

- Whether it receives relevant cashflow events or feeds.
- Whether `AGGREGATED` and `DEAD` are accepted statuses.
- Whether aggregation changes event timing, payloads, identifiers, or reconciliation behavior.
- Required schema, operational, and testing changes.
- The accountable downstream owner and sign-off criteria.