---
type: concept
title: Trade and Cashflow SSI Linkage
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, trade-settlement, cashflow-settlement, data-boundary]
related: [trade-ssi-stamping, adhoc-ssi-workflow, ssi-stamping-notification, ratan, ssi]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade SSI Stamping - Product templates.md"]
---

# Trade and Cashflow SSI Linkage

Trade SSI stamping and cashflow SSI stamping are linked but are not an inheritance relationship.

## Boundary

- The cashflow process remains unchanged.
- A cashflow SSI must not automatically inherit the trade SSI.
- A later cashflow stamp may contain a different SSI from the trade stamp.
- CDUPS queries the latest cashflow SSI on demand when confirmation requires it.
- Fixing Notice responses prioritize the latest cashflow SSI result before the general SSI result.

This boundary prevents a claim about a trade-level SSI from being incorrectly applied to a cashflow-level SSI.