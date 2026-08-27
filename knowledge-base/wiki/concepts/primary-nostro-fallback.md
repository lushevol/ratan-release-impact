---
type: concept
title: Primary Nostro Fallback
created: 2026-08-23
updated: 2026-08-23
tags: [primary-Nostro, SSI-stamping, fallback, static-data]
related: [ssi-stamping-service, ccy-pair-based-nostro-selection, ssi-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Compatibility design for multiple entities.md"]
---
# Primary Nostro Fallback

Primary Nostro fallback is the proposed path for SSI stamping when a cashflow has missing or multiple Vostro records.

The design proposes querying primary Nostro using `CCY Pair` when the pair exists; otherwise, the existing CN logic should be followed. It does not confirm whether `CCY Pair` is valid for primary Nostro queries, nor whether a failed pair-specific query should fall back to a query without the pair.

This unresolved behavior affects account-selection safety, exception handling, and replay design.