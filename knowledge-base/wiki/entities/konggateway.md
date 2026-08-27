---
type: entity
title: KongGateway
created: 2026-08-25
updated: 2026-08-25
tags: [konggateway, api-gateway, rdm, pct2, ratan]
related: [rdm, ratan-rdm-reference-data-integration, rat-pct2-refresh]
sources: ["RATAN/RATAN -Interfaces/Ratan and RDM 38430.md"]
---
# KongGateway

## Role in the RDM interface

**KongGateway** is identified as the API delivery channel for PCT2 portfolio data in the RDM-to-RATAN interface inventory.

The scheduled job **`RAT_PCT2_REFRESH`** is stated to obtain or refresh PCT2 portfolio data through an API via KongGateway.

## Known limitations

The source does not specify:

- The API endpoint or route.
- Authentication and authorisation requirements.
- Request and response schemas.
- Refresh schedule or triggering conditions.
- Timeout, retry, reconciliation, or failure behaviour.
- KongGateway or API ownership.

This page records only the stated architectural role and should not be treated as an API contract.