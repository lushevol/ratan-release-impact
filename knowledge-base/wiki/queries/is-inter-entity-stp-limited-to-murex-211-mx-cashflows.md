---
type: query
title: Is Inter-Entity STP Limited to Murex 2.11 MX Cashflows?
tags: [cash-settlement, settlement-day-2, STP, Murex, MX, SWIFT]
related: [inter-entity-cashflow-stp, murex-2-11, manual-entity-swift-mx-bifurcation, settlement-day-2]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity STP.md"]
---
# Is Inter-Entity STP Limited to Murex 2.11 MX Cashflows?

The source records agreement with Prakash and Amol that the requirement will apply only to MX cashflows from Murex 2.11. It does not show a formal approval record or explain the treatment of other flow types.

## Questions

1. Is the MX-only limitation an approved release boundary for Story 6473009?
2. Are SWIFT and other non-MX inter-entity cashflows unsupported, manually processed, or covered by another requirement?
3. Does the restriction apply only to Murex 2.11, or also to later Murex versions?
4. Must both the Murex version and MX classification be validated before STP eligibility is granted?
5. What UAT cases and operational metrics demonstrate correct exclusion of non-eligible flows?

The answer should be reconciled with [[manual-entity-swift-mx-bifurcation]] without generalizing this narrow requirement to the wider settlement architecture.