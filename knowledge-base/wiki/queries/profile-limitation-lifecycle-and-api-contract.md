---
type: query
title: What Is the Authoritative Profile Limitation Lifecycle and Check API Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, profile-limitation, maker-checker, state-machine, api-contract, open-question]
related: [profile-limitation, profile-limitation-maker-checker-workflow, profile-limitation-check-api, ratanone-rule-service, maker-checker-configuration-governance, pending-configuration-change-isolation, what-is-the-authoritative-static-configuration-maker-checker-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Rule Service Technical Design/Profile Limitation Maker Checker Design.md"]
---
# What Is the Authoritative Profile Limitation Lifecycle and Check API Contract?

The available design defines a profile-limitation workflow but leaves implementation-critical lifecycle and API details unresolved.

## Questions

1. Is `ADD_CONFIRMED` a typo for `ADD_PENDING`, or a valid omitted lifecycle state?
2. When an addition is rejected, is the record deleted, retained as `ADD_REJECTED`, or written to an audit/history store?
3. How are confirmed and pending values stored so an edit or deletion can be rejected and restored?
4. Is `CONFIRMED` with `is_delete = true` the canonical terminal deleted state, and should such records be excluded from all runtime reads?
5. Which records are visible to `GET /v1/staticLimitation/checkLimitation/{profile}/{currency}/{amount}` during pending add, edit, and delete operations?
6. What are the identity key, amount precision, currency validation, limit-boundary, error-response, and authorization rules for the API?
7. Is the workflow implemented by [[ratanone-rule-service]] independently or through the shared mechanism described by [[shared-static-configuration-maker-checker-engine]]?

## Evidence

[[profile-limitation-maker-checker-workflow]] documents the operation-specific state transitions and audit requirements. [[profile-limitation-check-api]] preserves the endpoint and its minimal response contract.

The broader configuration question is also related to [[what-is-the-authoritative-static-configuration-maker-checker-state-machine]].