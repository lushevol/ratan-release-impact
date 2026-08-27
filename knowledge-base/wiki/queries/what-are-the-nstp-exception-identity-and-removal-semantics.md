---
type: query
title: What Are the NSTP Exception Identity and Removal Semantics?
created: 2026-08-24
updated: 2026-08-24
tags: [NSTP, exceptions, lifecycle, audit, query]
related: [hot-nstp-rule-exception-reconciliation, nstp-rules]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Hot NSTP Rule Exception Generation.md"]
---
# What Are the NSTP Exception Identity and Removal Semantics?

## Question

How is an NSTP exception identified, and what should happen when the rule that caused it is removed or no longer applies?

## Why It Matters

The source requires exceptions to be generated and removed accordingly, but does not define whether an exception belongs to one rule, multiple rules, or a broader cashflow condition. Blind deletion could remove an exception still supported by another rule or erase a manually modified workflow record.

## Required Resolution

Define:

- The exception-to-cashflow and exception-to-rule relationship.
- The deduplication key.
- Rule and exception version provenance.
- Behavior for multiple supporting rules.
- Treatment of manual edits, resolution, and overrides.
- Whether removal means delete, cancel, close, or mark obsolete.
- Audit and retention requirements.