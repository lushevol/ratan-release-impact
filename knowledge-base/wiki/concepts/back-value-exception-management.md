---
type: concept
title: Back Value Exception Management
tags: [cash-settlement, value-date, maker-checker, exception-management]
related: [ratan, cashflow-multi-exception-generation, ssi-dual-blind-remediation, maker-checker-settlement-control]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions.md"]
---
# Back Value Exception Management

Back Value is a maker/checker exception for a cashflow whose payment date is in the past, or whose same-day payment is beyond the GMT release cutoff.

## Generation sequence

Back Value is evaluated after SSI stamping or SSI checker approval:

1. If Vostro settlement means is `Over Account`, the source says to end exception checking.
2. Otherwise, generate Back Value when `Cashflow.Payment_Date` is before the physical server date.
3. For a payment date equal to the server date, generate it when current GMT time is after the release cutoff.

The scope of the `Over Account` short-circuit is not explicit: it may apply only to Back Value evaluation or to the remaining multi-exception process.

## Dual entry and resolution

A maker selects a replacement date and Ratan stores it. The checker independently selects a date:

- Matching dates permit exception closure.
- Different dates cause SSI and other completed exceptions to close while Back Value remains open and the mismatch is highlighted.
- The checker may add a rejection comment and return the Back Value item to the maker.
- During rework, SSI and Cashflow Affirmation are read-only; the maker can update the preloaded prior value date.
- The checker later confirms the maker's revised date to close the remaining exception.

The release cutoff value, holiday treatment, time-source ownership, and date comparison normalization are not specified.