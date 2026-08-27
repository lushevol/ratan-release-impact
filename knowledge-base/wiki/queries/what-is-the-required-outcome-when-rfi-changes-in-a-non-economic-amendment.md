---
type: query
title: What Is the Required Outcome When RFI Changes in a Non-Economic Amendment?
created: 2026-08-23
updated: 2026-08-23
tags: [rfi, nostro, amendments, group-management, open-question]
related: [rfi-nostro-stamping-based-on-portfolio, ratan-cash-settlement-group-management-service, dedicated-nostro-selection, amendment-driven-cashflow-correlation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Change List and API.md"]
---
# What Is the Required Outcome When RFI Changes in a Non-Economic Amendment?

The requirement says that, for an amendment meeting a non-economic condition, group management must further consider whether RFI changed between the old and new states.

The requirement does not define either the qualifying condition or the consequence of identifying an RFI change.

## Information required

- The authoritative definition of a non-economic amendment.
- The before-and-after fields used to establish an RFI change.
- Whether a changed `nostroId`, portfolio, or both is material.
- Required downstream action: restamping, regrouping, reapproval, exception handling, lifecycle event publication, or notification.
- Idempotency, audit, and reversal behavior.
- Whether active or historical cashflows are refreshed.

This gap affects amendment processing and is distinct from the underlying matching algorithm in [[what-is-the-authoritative-rfi-nostro-selection-and-fallback-rule]].