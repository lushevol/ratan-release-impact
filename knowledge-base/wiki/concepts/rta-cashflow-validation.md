---
type: concept
title: RTA Cashflow Validation
created: 2026-08-23
updated: 2026-08-23
tags: [rta, validation, cashflow, settlement, dvp]
related: [auto-dvp, ebbs-rta-notification, receive-to-pay-cashflow-linkage, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md"]
---
# RTA Cashflow Validation

RTA-to-receive validation is the control that verifies an EBBS RTA corresponds to the RATAN receive cashflow before Auto DVP attempts pay-leg linkage.

The required conditions are:

- RTA currency equals RATAN receive-cashflow currency.
- RTA amount equals RATAN receive-cashflow amount.
- RATAN payment date is less than or equal to RTA value date.
- RTA value date is less than or equal to RATAN payment date plus two business days.

A validation failure must not close a pay DVP exception.

The universal value-date window requires clarification for South Africa because Razor reference behavior reportedly avoids value-date matching for some African countries.