---
type: query
title: What Is the Canonical Batch Limitation Check Identifier Field?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, api-contract, profile-limitation, identifier]
related: [profile-limitation-api, batch-profile-limitation-validation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Batch Limitation Check API Doc.md"]
---
# What Is the Canonical Batch Limitation Check Identifier Field?

Should clients use `referenceId` or `cashflowId` in requests and responses for `POST /v1/profileLimitation/checkLimitationsBatch`?

## Evidence

The request and response field tables, together with the initial JSON examples, use `referenceId` and describe it as `cashflowId`. The supplied HTTP request and response examples instead use `cashflowId`.

Both names appear to identify the same cashflow value, but they are incompatible JSON contracts for serialization and response correlation.

## Required resolution

Confirm:

1. the canonical field name for the external API;
2. whether the alternative name is accepted as a backward-compatible alias;
3. whether responses always echo the submitted field name or use one canonical member;
4. whether a versioned endpoint is required if consumers already depend on either form.

Until resolved, consumers should not infer a contract from example frequency. See [[profile-limitation-api]] and [[batch-profile-limitation-validation]].