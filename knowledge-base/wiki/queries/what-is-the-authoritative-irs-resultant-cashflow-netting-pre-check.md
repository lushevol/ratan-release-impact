---
type: query
title: What Is the Authoritative IRS Resultant-Cashflow Netting Pre-Check?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, IRS-netting, pre-check, netting-ID, cashflow-ID]
related: [irs-resultant-cashflow-netting, auto-netting-rule-management, does-an-empty-netting-id-indicate-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting.md"]
---
# What Is the Authoritative IRS Resultant-Cashflow Netting Pre-Check?

## Question

What exact validation and precedence rules should be used when a cashflow has an `N`-prefixed component cashflow ID, a populated netting ID, and payment type `IRS Netting`?

## Evidence

The source proposes that only payment type `IRS Netting` passes the common pre-check in this condition. Other payment types should be rejected. Elsewhere, manual bilateral, CCIL, and Beneficiary BIC rules require a blank component cashflow netting ID, while Bilateral Netting - Adhoc permits a populated value.

The source does not establish:

- whether component cashflow ID and component cashflow netting ID are distinct fields;
- what the `N` prefix signifies;
- whether the IRS exception overrides blank-netting-ID validation;
- whether the rule applies to a resultant cashflow, its components, or both;
- whether the behavior is current, proposed, or environment-specific.

## Required Resolution

An authoritative rule should define field names, evaluation order, rejection behavior, and examples for every netting type. It should also identify the approved support matrix for `Murex 2.11` and `Stella`.