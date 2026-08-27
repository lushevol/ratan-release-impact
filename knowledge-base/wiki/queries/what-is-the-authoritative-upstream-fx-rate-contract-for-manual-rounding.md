---
type: query
title: What Is the Authoritative Upstream FX Rate Contract for Manual Rounding?
created: 2026-08-23
updated: 2026-08-23
tags: [manual-rounding, fx-rate, upstream, authorization-limit]
related: [manual-cashflow-rounding, usd-equivalent-cashflow-adjustment-limit]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Manual Rounding.md"]
---
# What Is the Authoritative Upstream FX Rate Contract for Manual Rounding?

Manual Rounding must use an exchange rate from upstream to determine whether the adjustment is below the USD 1 limit. The source does not identify the upstream provider or the exact existing authorization-limit process to reuse.

## Required resolution

Determine the authoritative system, rate type, timestamp, precision, conversion direction, fallback behavior, and error handling. Confirm whether the threshold is a strict `< USD 1.00` comparison and whether it applies to the absolute or cumulative adjustment.

The decision should also specify when the rate is captured and whether maker entry and checker approval use the same rate.
