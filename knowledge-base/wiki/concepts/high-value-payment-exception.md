---
type: concept
title: High Value Payment Exception
tags: [cash-settlement, risk, fx-conversion, exception-management]
related: [ratan, fx-conversion-service, cashflow-multi-exception-generation]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions.md"]
---
# High Value Payment Exception

High Value Payment is a checker-only cashflow exception in [[ratan]]. It must be generated when a payment amount is above USD 100 million after conversion to USD through the [[fx-conversion-service]].

The requirement specifies a strict “above 100 million” threshold, implying that exactly USD 100 million does not meet the stated condition.

## Unspecified controls

The source does not define:

- FX rate source, type, or valuation timestamp.
- Rounding and precision rules.
- Conversion behavior when the source payment currency is USD.
- Fallback behavior for an unavailable or invalid conversion response.
- Treatment of stale FX data.

These controls are necessary for deterministic implementation and auditability.