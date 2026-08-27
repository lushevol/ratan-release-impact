---
type: query
title: What Is the Authoritative Korea KRO Payment Routing Matrix?
created: 2026-08-23
updated: 2026-08-23
tags: [korea, kro, tis, swift, routing]
related: [ratan, tis, enisis, korea-kro-non-kro-payment-routing, ratan-tis-payment-query]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Ratan One Processing Guide(DOI)-Korea.md"]
---
# What Is the Authoritative Korea KRO Payment Routing Matrix?

The guide states that all KRO payments are manually handled through TIS and that RATAN generates SWIFT only for non-KRO payments. Its detailed TIS cases also include `KRO` and `FCY` settlement-account variants, plus SCBLKR and non-SCBLKR conditions.

Clarify:

- The business definition of KRO.
- Whether KRO is determined by settlement account, currency, entity, payment type, or another attribute.
- How each documented TIS case maps to TIS handling, OLTP accounting, and SWIFT generation.
- Whether any KRO case can enter [[enisis]] or require SWIFT exception handling.