---
type: query
title: What Controls Govern Manual RFI Nostro Selection for Non-RFI Portfolios?
tags: [RFI, Nostro, manual-override, SSI, authorization, maker-checker]
related: [nostro-static-popup, portfolio-based-rfi-nostro-stamping, rfi-nostro-account]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio.md"]
---

# What Controls Govern Manual RFI Nostro Selection for Non-RFI Portfolios?

Scenario 9 allows a user to manually select an RFI Nostro for a non-RFI portfolio through adhoc SSI selection. Because the RFI routing rule is justified by a regulatory settlement requirement, the override requires explicit control design.

The requirement does not define:

- User entitlement to select an RFI Nostro.
- Maker/checker approval requirements.
- Warning or confirmation behavior.
- Audit-trail fields and retention.
- Validation against portfolio classification.
- Downstream accounting and SWIFT consequences.
- Whether the override is permitted only for an exception or operational repair.
