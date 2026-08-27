---
type: query
title: Does Cashflow Blotter or Any Other Frontend Consume eueNotice?
tags: [cashflow-blotter, frontend, graphql, eue-notice, impact-assessment]
related: [ratanone-data-ambassador, sci, sci-regulatory-field-schema-deprecation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Investigate SCI Response Data - eueNotice.md"]
---
# Does Cashflow Blotter or Any Other Frontend Consume eueNotice?

## Question

Does Cashflow Blotter or any other frontend use `eueNotice` directly, indirectly, or through a cached GraphQL schema or fragment?

## Evidence

The documented Cashflow Blotter Counterparty Detail query requests selected `doddFrankDetails` fields but does not request `eueNotice`, `smallBankExem`, or `cftcClearingExemption`. The source nevertheless records that frontend confirmation from Judy is pending.

## Required resolution

Obtain frontend-owner confirmation and search client repositories, generated GraphQL artifacts, UI mappings, and runtime telemetry for the three changed SCI attributes.