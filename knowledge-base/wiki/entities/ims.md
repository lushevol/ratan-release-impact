---
type: entity
title: IMS
created: 2026-08-24
updated: 2026-08-24
tags: [ims, monitoring, alerting, cash-settlement]
related: [cash-settlement-ola-break-monitoring, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md"]
---
# IMS

IMS is the proposed alerting destination for Ratan-to-Razor OLA-break records.

The source states that RATAN PSS should configure API calls to the IMS server and use resulting alerts to notify OPS of cashflows that may need manual replay from the cashflow blotter.