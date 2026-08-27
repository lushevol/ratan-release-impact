---
type: query
title: What Is the Authoritative Nostro Threshold Precedence?
created: 2026-08-22
updated: 2026-08-22
tags: [nostro-threshold, static-data, matching-precedence, cashflow-splitting]
related: [nostro-threshold-matching-precedence, split-child-threshold-redistribution, cashflow-splitting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT.md"]
---

# What Is the Authoritative Nostro Threshold Precedence?

The UAT tested three matching records for one currency: currency-only, booking entity plus currency, and nostro BIC plus currency. The observed result selected the booking-entity-plus-currency record.

The complete precedence order is not documented. In particular, the source does not establish whether booking entity or nostro BIC has priority when both match, or how fallback behaves when the most specific record is absent.

An authoritative rule should define matching priority, fallback, uniqueness constraints, and behavior when multiple records remain eligible.