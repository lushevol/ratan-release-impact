---
type: query
title: What Is the Authoritative SSI+ Inactivation and Reactivation Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [ssi-plus, ssi, dormancy, lifecycle-management, integration]
related: [ssi-plus, dormant-ssi-processing, does-created-at-filtering-correctly-implement-the-ssi-last-used-date-window]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Dormant SSI processing.md"]
---
# What Is the Authoritative SSI+ Inactivation and Reactivation Contract?

## Question

What contract governs SSI+ status updates for dormant SSIs, including inactivation, reactivation, idempotency, audit, and reconciliation?

## Evidence

The design states that SSIs unused for 24 months should have their last-used date recorded and be fed to SSI+ for inactive status updates. It defines neither an SSI+ interface nor the operational safeguards governing those updates.

The new BCS endpoint supplies daily use records, but it returns individual cashflow-ID and SSI-ID pairs and does not define downstream duplicate handling, status-update timing, or delivery semantics.

## Contract elements to define

- Canonical SSI identifier and cross-flow normalization.
- Business-effective date and 24-month cutoff calculation.
- Whether SSI+ receives incremental observations, a consolidated last-used-date feed, or explicit status-change commands.
- Idempotency key, retry classification, and terminal-failure handling.
- Audit trail and reconciliation controls.
- Override, appeal, and manual-recovery procedures.
- Reactivation or exception handling when an inactive SSI becomes used again.
- Controls preventing erroneous or premature inactivation.

The documented BCS API returns HTTP 500 for an invalid payment-date format, which should be classified appropriately by any automated consumer.