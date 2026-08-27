---
type: concept
title: Withdrawal-New Cashflow and Razor-Release Check
tags: [cashflow, lifecycle, stella, scbml, razor, validation]
related: [irs-cashflow-processing, lifecycle-service, razor, scbml]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/IRS Cashflow Processing Design.md"]
---
# Withdrawal-New Cashflow and Razor-Release Check

The withdrawal-new cashflow and Razor-release check is a pending lifecycle API proposed for the IRS flow.

## Stated Detection Inputs

The API is intended to:

1. Query the Stella message table for a withdrawal-and-new cashflow condition.
2. Require event `Withdrawal_New`.
3. Require `pre_cashflow_id` to be non-null.
4. Query SCBML history to determine whether the cashflow has previously been released to [[razor]].

## Status and Limits

This API is marked Pending in the source. The design does not define the Stella-to-SCBML correlation key, the exact meaning of prior release, behavior when records are missing or inconsistent, or the response model.

The Razor-release check applies only to this proposed lifecycle API in the cited IRS design. It is not evidence of a general Razor-release rule for all lifecycle or netting operations.

See [[how-is-prior-razor-release-determined-for-withdrawal-new-cashflows]].