---
type: concept
title: Dedicated Nostro Selection
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, rfi, portfolio, selection, ssi]
related: [rfi-nostro-stamping-based-on-portfolio, ratanone-static-data-service, ratan-cash-settlement-ssi-stamping-service, what-is-the-authoritative-rfi-nostro-selection-and-fallback-rule, what-are-the-finddedicated-and-finddedicateds-api-contracts]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Change List and API.md"]
---
# Dedicated Nostro Selection

Dedicated Nostro selection is the intended type-aware lookup of an `RFI` Nostro using its associated portfolio information.

The requirement assigns this capability to [[ratanone-static-data-service]] through `findDedicated` and `findDedicateds`, and requires [[ratan-cash-settlement-ssi-stamping-service]] to account for trade-stamp compatibility while querying Nostro data.

The documented model does not define the operational selection algorithm. Open elements include:

- the source and ownership of the cashflow or trade portfolio;
- whether matching is exact and date-effective;
- matching attributes beyond portfolio;
- precedence between a matching `RFI` and `DEFAULT` Nostro;
- zero-match and multiple-match outcomes; and
- uniqueness constraints for eligible dedicated Nostros.

These omissions are delivery-critical because they determine which settlement account is stamped. They are tracked in [[what-is-the-authoritative-rfi-nostro-selection-and-fallback-rule]].