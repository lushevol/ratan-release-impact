---
type: concept
title: Trade SSI Stamping
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, trade-settlement, ratan, cdups, lookup, enrichment]
related: [ratan, ssi, cdups, fmrp, trade-cashflow-ssi-linkage, ssi-best-match-rule, ssi-product-template-mapping, ssi-swift-field-enrichment, ssi-stamping-retry-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade SSI Stamping - Product templates.md"]
---

# Trade SSI Stamping

Trade SSI stamping is the process of resolving settlement instructions from trade attributes and returning an enriched trade response to [[cdups]].

## Flow

1. CDUPS submits trade identity, version, temporal, entity, counterparty, CFI, settlement, and leg information.
2. [[ratan]] validates the request and locates the relevant trade context.
3. RATAN extracts product-specific currencies and party references from SCBML or the applicable Fixing Notice structure.
4. Vostro and Nostro instructions are selected using CFI, settlement-method, direction, currency, entity, and counterparty conditions.
5. The response returns per-leg result states and an SSI-enriched SCBML message.
6. CDUPS retries only the specified infrastructure and internal-error conditions.

The service is designed as a central SSI stamping capability, but it does not make cashflow SSI inherit trade SSI values.