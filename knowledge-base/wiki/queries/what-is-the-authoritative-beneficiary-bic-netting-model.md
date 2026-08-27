---
type: query
title: What Is the Authoritative Beneficiary BIC Netting Model?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, beneficiary-bic, netting, open-question]
related: [beneficiary-bic-netting, cash-settlement-beneficiary-bic-netting-design, trade-standing-settlement-instructions, cashflow-standing-settlement-instructions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Beneficiary BIC Netting Design.md"]
---
# What Is the Authoritative Beneficiary BIC Netting Model?

## Question

How does Beneficiary BIC affect Cash Settlement netting, and which services own, validate, propagate, display, and audit the resulting data?

## Why This Is Open

The source lists affected services but does not define the functional behavior or the authoritative data model. In particular, it does not establish whether Beneficiary BIC is used to form netting groups, prevent netting, select settlement instructions, route payment instructions, or enrich netting results.

## Evidence

The source names Front End, Netting service, Lifecycle service, Static data service, Query service, and Rule service as affected areas. It limits Rule service involvement to static data, but does not identify the concrete deployed services represented by the generic labels.

Potentially related service pages include [[ratanone-rule-service]], [[51358-ratanone-static-data-service]], [[ratan-cashflow-lifecycle-service]], [[51358-ratanone-query-service]], and [[51358-ratan-cash-settlement-query-service]]. These relationships are provisional.

## Information Needed

A complete answer should specify:

1. The authoritative source and owner of Beneficiary BIC.
2. The netting grouping, exclusion, and segregation keys.
3. The relationship to SSI, counterparty, account, currency, legal entity, and settlement-date data.
4. The API, database, event, and query contracts.
5. Propagation and consistency behavior across the listed services.
6. Handling of missing, invalid, inactive, amended, or conflicting BIC values.
7. UI, audit, migration, reconciliation, and regression-test requirements.
8. The deployment or regional scope of the design.

## Current Assessment

This remains an unresolved design question. The available source supports service-impact scope only and is insufficient to approve an implementation model.