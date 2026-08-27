---
type: query
title: What Is the Authoritative Murex Cashflow Publication Window?
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, cashflow, value-date, scheduling, reconciliation]
related: [murex-to-ratan-cashflow-interface, murex-flow-group-batch-handling, auto-netting-datetime-calculation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Ratan MxML- SCBML Adaptor ( Entity CN, SG, IN, MY).md"]
---
# What Is the Authoritative Murex Cashflow Publication Window?

The source defines three incompatible eligibility statements for Murex 2.11 publication to Ratan:

- next nine calendar days, with no holiday or weekend consideration;
- next seven business days;
- value date from `mxSystemDate` through `mxSystemDate + 9Day`.

The answer must establish the authoritative rule, relevant calendar, treatment of holidays and weekends, applicable entities, and whether real-time new-booking publication uses the same window as scheduled feeding.

This affects [[murex-to-ratan-cashflow-interface]], [[murex-flow-group-batch-handling]], reconciliation expectations, and missing-message controls.