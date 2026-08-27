---
type: query
title: Are the FMRP SWIFT Static-Data Mappings Validated and Owned?
created: 2026-08-23
updated: 2026-08-23
tags: [static-data, swift, ssi, bic, data-governance]
related: [ssi-driven-swift-field-generation, static-data-readiness, settlement-integration-static-data-readiness]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation.md"]
---
# Are the FMRP SWIFT Static-Data Mappings Validated and Owned?

## Question

Who owns validation, approval, and change control for FMID, BIC, branch-code, currency, routing-code, LEI, and precious-metals static mappings used by RATAN SWIFT generation?

## Evidence

The requirement relies on static lookup tables for sender and correspondent BICs, branch codes, local currencies, and precious-metals attributes. It also contains apparently mismatched country/currency combinations, unconfirmed BIC availability for fields 56–58, and references to static data supplied through emails and user-maintained lists.

## Required resolution

A data-governance control should define authoritative sources, validation rules, data-quality thresholds, change approvers, effective dates, and regression testing for every mapping that can affect a payment message.