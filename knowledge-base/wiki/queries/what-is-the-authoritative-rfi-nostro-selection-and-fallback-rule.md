---
type: query
title: What Is the Authoritative RFI Nostro Selection and Fallback Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, rfi, portfolio, selection, open-question]
related: [rfi-nostro-stamping-based-on-portfolio, dedicated-nostro-selection, ratanone-static-data-service, ratan-cash-settlement-ssi-stamping-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Change List and API.md"]
---
# What Is the Authoritative RFI Nostro Selection and Fallback Rule?

The requirement mandates portfolio-dedicated RFI Nostros and type-aware querying but does not define the selection algorithm.

## Questions to resolve

- Which cashflow or trade field supplies the portfolio, and which service owns it?
- Is portfolio matching exact, normalized, hierarchical, and/or effective-dated?
- Which other attributes form the lookup key?
- Does a matching `RFI` Nostro take precedence over `DEFAULT`?
- What occurs when no RFI Nostro matches?
- What occurs when multiple RFI Nostros match?
- What static-data uniqueness constraints prevent ambiguity?

This contract is required for deterministic SSI stamping and safe operational fallback.