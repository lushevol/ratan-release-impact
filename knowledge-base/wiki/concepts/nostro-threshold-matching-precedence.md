---
type: concept
title: Nostro Threshold Matching Precedence
created: 2026-08-22
updated: 2026-08-22
tags: [nostro-threshold, static-data, matching, settlement]
related: [split-child-threshold-redistribution, cashflow-splitting, auto-netting-rule-management]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT.md"]
---

# Nostro Threshold Matching Precedence

Nostro threshold static data determines whether a cashflow is automatically distributed when its amount exceeds a configured threshold.

The UAT configured three records for the same currency:

```text
1. Currency only
2. Booking entity + currency
3. Nostro BIC + currency
```

In the tested setup, the record matching booking entity plus currency controlled the distribution. This establishes an observed matching outcome, not a complete precedence specification.

The source does not state how a nostro-BIC-plus-currency match compares with a booking-entity-plus-currency match in all cases, nor does it document fallback behavior when multiple records match. The full precedence should therefore be confirmed before being treated as authoritative.