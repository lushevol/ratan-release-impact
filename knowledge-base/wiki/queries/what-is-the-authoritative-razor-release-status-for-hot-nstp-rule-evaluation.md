---
type: query
title: What Is the Authoritative Razor Release Status for Hot NSTP Rule Evaluation?
created: 2026-08-24
updated: 2026-08-24
tags: [Razor, NSTP, release-status, workflow, query]
related: [razor-release-boundary-for-hot-rule-evaluation, hot-nstp-rule-exception-reconciliation, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Hot NSTP Rule Exception Generation.md"]
---
# What Is the Authoritative Razor Release Status for Hot NSTP Rule Evaluation?

## Question

Which field, status, event, or downstream acknowledgement definitively proves that a cashflow has been released to Razor and is therefore excluded from hot NSTP-rule reconciliation?

## Why It Matters

The source requires processing only cashflows that have not been released to Razor, but it does not define the authoritative status or its owner. The answer must also establish whether the eligibility check is atomic with exception mutation and Razor release.

## Evidence

The source states that changed NSTP rules should be applied to cashflows “not release[d] to Razor yet.” It provides no status values, API, schema, event contract, or concurrency behavior.

## Required Resolution

Document the canonical status contract, transition timing, data owner, read path, and race-handling strategy.