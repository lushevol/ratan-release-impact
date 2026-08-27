---
type: query
title: What Is the Authoritative Bulk Fail API and Approval Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, bulk-fail, api, approval, camunda]
related: [bulk-manual-fail-workflow, ratan-fail-and-autofail-status-transitions, what-are-the-authorization-controls-for-send-to-waiting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Bulk Fail/Bulk Fail Technical Design.md"]
---
# What Is the Authoritative Bulk Fail API and Approval Contract?

The source shows a Manual Fail API payload with `cashflowId`, `cashflowVersion`, `businessVersion`, and `minorVersion`, but the displayed URL combines inconsistent link targets and path suffixes. It does not show APIs for manual-fail approval or rejection.

## Questions to resolve

- What is the canonical Manual Fail URL and HTTP method?
- Which interfaces invoke `Approve`, `Reject`, and scheduled `AutoFail`?
- What authorization and maker/checker entitlement rules apply to each action?
- What are the batch-size, partial-success, retry, idempotency, and optimistic-locking contracts?
- What error codes and response semantics apply at item and batch level?
- Which audit, event, notification, and reconciliation records must be emitted?

This query is related to [[what-are-the-authorization-controls-for-send-to-waiting]] because manual `Fail` moves a cashflow to `WAITING / Pending Verification / Pending Manual Fail`.