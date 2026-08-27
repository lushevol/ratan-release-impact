---
type: concept
title: SSI SWIFT Field Enrichment
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, swift, scbml, settlement-instruction, vostro, nostro]
related: [trade-ssi-stamping, ssi-product-template-mapping, ratan, cdups]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade SSI Stamping - Product templates.md"]
---

# SSI SWIFT Field Enrichment

SSI SWIFT Field Enrichment embeds Vostro and Nostro results into the SCBML response returned to [[cdups]].

## Mapping

| SWIFT field | SCBML or response role | Typical source |
|---|---|---|
| Field 53 | Sender’s correspondent or booking-entity correspondent; sometimes account | SCB Nostro or combined client Vostro and SCB Nostro |
| Field 54 | Receiving correspondent in Fixing-related examples | SCB Nostro |
| Field 56 | Intermediary institution | Client Vostro |
| Field 57 | Account-with-institution or client receiving correspondent | Client Vostro |
| Field 58 | Beneficiary customer | Client Vostro |

The response also returns names, addresses, account numbers, BICs, and per-leg `vostroResult` and `nostroResult` values. Sample account numbers and names are fixtures and are not business rules.