---
type: query
title: Should SSI Stamping Fall Back to Nostro Without CCY Pair?
created: 2026-08-23
updated: 2026-08-23
tags: [query, SSI-stamping, Nostro, fallback, CCY-Pair]
related: [ssi-stamping-service, ccy-pair-based-nostro-selection, primary-nostro-fallback]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Compatibility design for multiple entities.md"]
---
# Should SSI Stamping Fall Back to Nostro Without CCY Pair?

The source asks whether SSI stamping should query Nostro without `CCY Pair` when a pair-specific query returns no result.

This requires a decision because fallback may improve resilience but could select an unintended settlement account. The answer should define lookup precedence, acceptable ambiguity, exception behavior, and replay safety.