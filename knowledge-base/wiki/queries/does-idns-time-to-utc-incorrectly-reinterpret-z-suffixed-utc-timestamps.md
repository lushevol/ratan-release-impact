---
type: query
title: Does IdnsTimeToUtc Incorrectly Reinterpret Z-Suffixed UTC Timestamps?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, utc, ui, timestamp-parsing, risk]
related: [ratan-indonesia-time-zone-contract, timestamp-semantic-and-format-consistency, 51358-ratan-cash-settlement-query-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UTC Time zone impact - Indonesia/Time Fields Summary.md"]
---
# Does IdnsTimeToUtc Incorrectly Reinterpret Z-Suffixed UTC Timestamps?

The documented conversion table maps both `2026-08-20T10:00:00` and `2026-08-20T10:00:00Z` to `2026-08-20T03:00:00Z`. This shows that the trailing `Z` is accepted but its usual UTC semantic meaning is not retained in that conversion path.

## Why this matters

If a `Z`-suffixed API response is a genuine UTC instant, treating it as an Indonesia UTC+7 wall-clock value shifts the instant by seven hours. The source contains multiple Local Time-labelled API values with `Z`, so field-by-field validation is required.

## Required validation

1. Locate `IdnsTimeToUtc` call sites and distinguish user-input processing from API-response processing.
2. Test offsetless, `Z`-suffixed, and `+00:00` inputs against expected displayed and transmitted instants.
3. Verify affected Cashflow History, static/history, rule-history, affirmation, and netting-preview screens.
4. Add regression tests proving that explicit UTC values are never shifted as local input.

This query informs the platform-wide [[ratan-indonesia-time-zone-contract]].