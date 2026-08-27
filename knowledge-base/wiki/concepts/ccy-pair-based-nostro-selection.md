---
type: concept
title: CCY Pair-Based Nostro Selection
created: 2026-08-23
updated: 2026-08-23
tags: [CCY-Pair, Nostro, SSI-stamping, static-data]
related: [ssi-stamping, ssi-stamping-service, scbml, tds3, primary-nostro-fallback]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Compatibility design for multiple entities.md"]
---
# CCY Pair-Based Nostro Selection

`CCY Pair`-based Nostro selection uses a currency-pair value such as `EGOUSD` to identify the expected settlement account.

The proposed behavior is:

- Single Vostro plus settlement means `FXBRREC`: query Nostro with `CCY Pair` when present.
- Missing or multiple Vostro: query primary Nostro with `CCY Pair` when present.
- Missing `CCY Pair`: follow existing CN logic.

The source does not resolve whether a failed pair-specific lookup should retry without the pair or how the primary Nostro query is defined.