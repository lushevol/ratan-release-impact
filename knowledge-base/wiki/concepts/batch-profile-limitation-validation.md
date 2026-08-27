---
type: concept
title: Batch Profile Limitation Validation
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, batch-processing, profile-limitation, validation, api-design]
related: [profile-limitation-api, what-does-top-level-success-mean-for-batch-limitation-checks, what-is-the-canonical-batch-limitation-check-identifier-field, cn-rule-prevalidation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Batch Limitation Check API Doc.md"]
---
# Batch Profile Limitation Validation

Batch profile limitation validation checks multiple cashflow amount requests against profile and currency limitations in a single operation. The documented API shape accepts a collection of identifier, currency, and `BigDecimal` amount values.

## Two-level outcome model

The proposed [[profile-limitation-api]] distinguishes request processing from individual business outcomes:

- Top-level `success` is `false` for an empty or null item request, with `results: null`.
- A non-empty request may return top-level `success: true` while individual result records contain `success: false`.
- Each result carries a `reason`, allowing an item to fail without invalidating processing of the entire batch.

The source's mixed-result example makes item-level inspection mandatory for bulk-action clients. The formal description of top-level `success` is nevertheless ambiguous because it says “Whether check is passed,” which conflicts with the example. This ambiguity is tracked in [[what-does-top-level-success-mean-for-batch-limitation-checks]].

## Identifier correlation

Each item and result includes a cashflow-correlating identifier. However, the source uses both `referenceId` and `cashflowId` in incompatible payload examples. No canonical member name or aliasing approach is defined. See [[what-is-the-canonical-batch-limitation-check-identifier-field]].

## Scope limits

The source documents validation results but does not specify the profile derivation mechanism, rule evaluation method, limitation-data ownership, error taxonomy, or whether unavailable limitation data is a business denial, configuration failure, or dependency failure.

This is adjacent to [[cn-rule-prevalidation]], but there is no evidence that the CN Rule Service performs this validation.