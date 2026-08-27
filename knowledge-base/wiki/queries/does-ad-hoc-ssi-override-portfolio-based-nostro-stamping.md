---
type: query
title: Does Ad Hoc SSI Override Portfolio-Based Nostro Stamping?
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, nostro, portfolio, rfi, ratan, controls, audit]
related: [portfolio-based-nostro-stamping, nostro-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/RFI Nostro stamping based on Portfolio - UAT.md"]
---
# Does Ad Hoc SSI Override Portfolio-Based Nostro Stamping?

## Open Question

When a user manually selects an RFI nostro for a non-RFI portfolio through ad hoc SSI, does that selection override automated portfolio-based nostro stamping?

## Current Evidence

UAT test 7 passed and confirms that the nostro type is visible in both list and form views and that a user can select an RFI nostro even for a non-RFI portfolio. The source does not show the post-release selected nostro, exception behavior, SWIFT output, EBBS accounting outcome, authorization requirement, or audit trail.

## Required Evidence

Confirm the precedence between manual SSI and the automated portfolio rule, then document:

- maker/checker or entitlement requirements;
- validation and SI mismatch handling;
- persistence through release, amendment, and restamping;
- SWIFT and EBBS accounting effects; and
- audit events identifying the manual override.