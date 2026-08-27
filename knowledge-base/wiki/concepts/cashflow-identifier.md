---
type: concept
title: Cashflow Identifier
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, identifier, uat, settlement]
related: [cashflow-auto-netting, uat-test-case, booking-and-counterparty-fmcode]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Cashflow Auto Netting UAT testing sample.md"]
---
# Cashflow Identifier

A cashflow identifier is the record-level identifier used to select a settlement cashflow for UAT. The Cashflow Auto Netting sample lists one identifier for each of its 184 cases.

Most identifiers begin with `M`, such as `M00120278190`. All SCH identifiers in the supplied inventory begin with `N`, such as `N00000062354`.

The source does not define the identifier format, namespace, generating system, uniqueness constraints, or the meaning of the `M` and `N` prefixes. The prefixes must not be interpreted as separate processing workflows without corroborating documentation.

The complete identifier inventory is preserved in [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--1p3a3x|Cashflow Auto Netting UAT Testing Sample]].