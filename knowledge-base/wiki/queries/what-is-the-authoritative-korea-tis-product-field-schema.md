---
type: query
title: What Is the Authoritative Korea TIS Product Field Schema?
created: 2026-08-23
updated: 2026-08-23
tags: [tis, schema, product-fields, api-contract, korea-migration]
related: [ratan-tis-payment-query-integration, korea-tis-payment-type-classification, tis, ratan, korea-cash-settlement-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Ratan to TIS.md"]
---
# What Is the Authoritative Korea TIS Product Field Schema?

## Question

What are the authoritative field names and lengths for product group and product type in pay-side and receipt responses?

## Evidence

The receipt schema lists `PRODUCT` and `PRODTYPE`, but the supplied receipt JSON row contains `PRODUCT` and `TYPE`.

The source also contains conflicting target sizes:

- Pay-side mapping: `PRODUCT` `CHAR(5)` to `CHAR(200)` and `TYPE` `CHAR(20)` to `CHAR(200)`.
- Receipt mapping: `PRODUCT` `CHAR(5)` to `CHAR(20)` and `PRODTYPE` `CHAR(20)` to `CHAR(50)`.
- Open-question text proposes extending product group and product type to `20` and `50`.

## Why it matters

TIS consumer schema, payload validation, backward compatibility, and truncation risk depend on a single field-name and length definition.

## Needed decision

Approve a versioned response schema for both endpoints, including exact field names, character lengths, nullability, migration timing, and ownership.