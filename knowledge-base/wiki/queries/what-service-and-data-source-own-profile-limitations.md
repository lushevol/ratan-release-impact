---
type: query
title: What Service and Data Source Own Profile Limitations?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, profile-limitation, service-ownership, data-ownership, validation]
related: [profile-limitation-api, batch-profile-limitation-validation, which-service-owns-fields-validation-rules-and-profile-limitation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Batch Limitation Check API Doc.md"]
---
# What Service and Data Source Own Profile Limitations?

Which component owns the `/v1/profileLimitation` API domain and the authoritative profile/currency limitation data it checks?

## Evidence

The source defines `POST /v1/profileLimitation/checkLimitationsBatch` and shows an item failure when limitation data cannot be obtained for a profile and currency:

```text
cannot get limitation for profile: USER_A, currency: USD
```

It does not identify an implementation service, data store, rule engine, profile identity source, or operational owner.

## Questions to resolve

- Is the caller profile derived from the authenticated principal, a JWT claim, an HTTP header, or another context?
- Which service and dataset are authoritative for limitations?
- Is unavailable limitation data a conservative business rejection, missing configuration, or dependency error?
- Who governs limitation configuration and its audit trail?
- Are failure reasons stable codes or diagnostic text?

This extends [[which-service-owns-fields-validation-rules-and-profile-limitation]] with a concrete consumer-facing batch API. It does not establish that any named rule service implements the capability.