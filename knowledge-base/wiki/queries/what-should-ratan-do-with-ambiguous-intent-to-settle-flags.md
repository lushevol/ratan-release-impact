---
type: query
title: What Should Ratan Do with Ambiguous Intent-to-Settle Flags?
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, scbml, payment-selection, data-quality, settlement-risk]
related: [intent-to-settle-payment-selection, scbml, ratan-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/Cashflow Logical Model Fields & Data Store.md"]
---
# What Should Ratan Do with Ambiguous Intent-to-Settle Flags?

The current requirement says that when a multi-payment cashflow has zero or more than one `scb:isIntentToSettle=true` value, Ratan must select the first payment.

This requires an operational decision:

- retain first-payment selection;
- reject the inbound cashflow;
- create a validation or settlement exception;
- route it for FMO review; or
- process it while recording a warning and monitoring metric.

The decision should state the required treatment for replayed messages, message ordering changes, and any payment that was sent to Razor under this fallback.