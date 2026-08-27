---
type: query
title: Does South Africa Use the Standard Auto DVP Value-Date Validation Window?
created: 2026-08-23
updated: 2026-08-23
tags: [south-africa, value-date, validation, dvp]
related: [auto-dvp, rta-cashflow-validation, auto-dvp-pilot-scope, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md"]
---
# Does South Africa Use the Standard Auto DVP Value-Date Validation Window?

RATAN's requirement applies the window `payment date <= RTA value date <= payment date + 2 business days`. Razor reference behavior says value date is not a matching criterion in some African countries because client-account debit may occur on a different date.

South Africa appears in the pilot scope. Confirm whether it is included in Day 1 and, if so, whether it follows the standard validation window or an approved country-specific exception.