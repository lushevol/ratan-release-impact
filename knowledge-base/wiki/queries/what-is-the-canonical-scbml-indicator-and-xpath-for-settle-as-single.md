---
type: query
title: What Is the Canonical SCBML Indicator and XPath for SettleAsSingle?
created: 2026-08-22
updated: 2026-08-22
tags: [scbml, auto-netting, settle-as-single, nstp, xpath]
related: [single-cashflow-auto-netting-exception, ratan-rule-service, lifecycle-service, nstp, 26-auto-netting-page-md-files--112-cash-settlement-home-page-cash-settlement-home-page-tech-design-cash-settlem--1o5gc6g]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Auto Netting TechDesign.md"]
---
# What Is the Canonical SCBML Indicator and XPath for SettleAsSingle?

The design uses two potentially distinct names for the single-cashflow outcome:

- `SettleAsSingle`, the Lifecycle status-update action and stated NSTP condition;
- `SingleCashflow`, the proposed SCBML indicator.

It explicitly says the `SingleCashflow` XPath must be confirmed. The canonical field name, XPath, datatype, permitted value, message version, and NSTP rule mapping must be agreed before implementation.

## Decision needed

Define one authoritative SCBML contract and identify how [[nstp]] consumes it to create the “Single Cashflow” exception.