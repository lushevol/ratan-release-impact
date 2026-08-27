---
type: concept
title: Cashflow Cutoff Static Data
created: 2026-08-23
updated: 2026-08-23
tags: [cutoff, static-data, cashflow, ratan, razor]
related: [ratan, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data.md"]
---
# Cashflow Cutoff Static Data

Cashflow cutoff static data controls the date and time at which a cashflow is considered for release processing. The primary key is the combination of Legal Entity and Currency.

## Fields

- **Cutoff shifter and cutoff shifter unit:** A backward shift used to calculate the cutoff date. The source gives `0` and `-1` as examples.
- **Cutoff time:** A GMT time applied directly to the individual cashflow without calculation.
- **Queue shifter:** Produces the Ratan-to-Razor release cutoff time from the calculated cutoff date and cutoff time.

The requirement references a calculation result sample and Day 1 cutoff records, but those records are not present in the supplied text. The exact queue-shifter formula and holiday-calendar interaction therefore remain unspecified.