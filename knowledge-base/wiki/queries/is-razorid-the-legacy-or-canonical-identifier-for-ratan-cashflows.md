---
type: query
title: Is razorID the Legacy or Canonical Identifier for RATAN Cashflows?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, razor, fmrp, identifier, terminology, open-question]
related: [fmrp, razor, ratan-murex-211-cashflow-integration, what-replaced-the-legacy-fmrp-inbound-acknowledgement-status-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0118.md"]
---
# Is razorID the Legacy or Canonical Identifier for RATAN Cashflows?

The source calls the inbound task “RATAN-MUREX cashflow inbound” and labels inbound documents `RATAN_CASHFLOW`. However, legacy formulas and fields use `client.scb.fmrp.inbound.razorID` and `M_RATAN_ID`, while MQ queue names contain `MLS`.

The source does not define whether RAZOR is:

- a former name for RATAN;
- a separate upstream or intermediary system;
- a retained technical identifier in a RATAN integration; or
- an unrelated component.

The final RATAN-10822 revision deletes `razorID`, making terminology resolution necessary for interpreting historical records and ensuring future interface documentation uses the correct identifier.