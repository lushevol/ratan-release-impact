---
type: query
title: What Does Top-Level Success Mean for Batch Limitation Checks?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, api-contract, batch-processing, validation-results]
related: [profile-limitation-api, batch-profile-limitation-validation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Batch Limitation Check API Doc.md"]
---
# What Does Top-Level Success Mean for Batch Limitation Checks?

Does response-level `success` mean that the batch request was processed, that every item passed, or another outcome?

## Evidence

The response field table describes top-level `success` as “Whether check is passed.” However, the mixed-result example contains a failed item with `success: false` and still returns top-level `success: true`.

For null parameters, the API returns `results: null`, top-level `success: false`, and the reason `"Request items cannot be empty"`.

## Required resolution

Define the response semantics explicitly:

- whether top-level `success` represents request validity or processing completion;
- whether an all-items-pass indicator is required;
- how clients should distinguish invalid requests, partial business failures, and dependency failures;
- whether `reason` is stable machine-readable contract data or display text.

This distinction is central to [[batch-profile-limitation-validation]] for bulk submit, approve, and reject flows.