---
type: query
title: How Is Prior Razor Release Determined for Withdrawal-New Cashflows?
tags: [razor, scbml, stella, lifecycle, cashflow, validation]
related: [withdrawal-new-cashflow-and-razor-release-check, irs-cashflow-processing, lifecycle-service, razor, scbml]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/IRS Cashflow Processing Design.md"]
---
# How Is Prior Razor Release Determined for Withdrawal-New Cashflows?

The proposed lifecycle API identifies withdrawal-and-new cashflows using Stella event `Withdrawal_New` and a non-null `pre_cashflow_id`, then checks SCBML history for prior release to Razor.

## Questions to Resolve

- What keys correlate the cashflow, Stella message record, and SCBML history record?
- Are `Withdrawal_New` and non-null `pre_cashflow_id` sufficient conditions?
- What event, status, or payload field in SCBML history constitutes release to Razor?
- How should missing, duplicate, or inconsistent records be handled?
- What response fields and error behavior does the lifecycle API expose?
- Is the lookup required synchronously in the IRS orchestration path?

The capability is marked Pending in the cited source.