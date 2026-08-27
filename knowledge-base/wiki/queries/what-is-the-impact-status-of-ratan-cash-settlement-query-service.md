---
type: query
title: What Is the Impact Status of ratan-cash-settlement-query-service?
tags: [ratan, query-service, sci, counterparty-data, impact-assessment]
related: [ratan, sci, ratanone-data-ambassador, sci-regulatory-field-schema-deprecation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Investigate SCI Response Data - eueNotice.md"]
---
# What Is the Impact Status of ratan-cash-settlement-query-service?

## Question

Does `ratan-cash-settlement-query-service` consume SCI-derived `eueNotice`, `smallBankExem`, or `cftcClearingExemption` data?

## Evidence

The investigation labels this service `No ??`, which is not a conclusive no-impact assessment. No code references, requested-field lists, or test evidence are supplied.

## Required resolution

Identify the service's counterparty-data integrations and query projections. Search its code and runtime requests for the changed attributes, then document a field-level impact decision with test evidence.