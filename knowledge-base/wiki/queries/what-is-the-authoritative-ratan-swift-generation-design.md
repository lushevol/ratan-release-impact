---
type: query
title: What Is the Authoritative RATAN SWIFT Generation Design?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, swift, documentation-governance, open-question]
related: [5-ratan--25-ratan-core-function-copy--23-ratan-settlement-6swift--1r9j1mr, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technica--v54z3s, swift-generation, ratan-settlement]
sources: ["RATAN/RATAN -Core Function copy/RATAN-Settlement  6_SWIFT.md"]
---
# What Is the Authoritative RATAN SWIFT Generation Design?

## Question

Is [[sources/5-ratan--25-ratan-core-function-copy--23-ratan-settlement-6swift--1r9j1mr]] the authoritative functional or technical definition for RATAN SWIFT generation, or is authority held by [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technica--v54z3s]]?

## Why this is unresolved

The available ingest context contains only the filename and path for the RATAN Settlement SWIFT document. It does not include revision metadata, authorship, document identifiers, message specifications, workflow details, or implementation contracts. Consequently, the two sources cannot be classified as duplicates, complementary specifications, or conflicting versions.

## Required evidence

Resolve this question by comparing the documents':

- document identifiers, revision dates, and authorship;
- supported SWIFT message types and versions;
- input data and field-mapping rules;
- generation triggers and preconditions;
- validation, approval, release, and dispatch controls;
- duplicate prevention, retry, repair, and reconciliation behavior;
- ownership, dependencies, and operational requirements.

Until that comparison is completed, claims from either source should remain attributed to the specific document rather than merged into [[concepts/swift-generation]].