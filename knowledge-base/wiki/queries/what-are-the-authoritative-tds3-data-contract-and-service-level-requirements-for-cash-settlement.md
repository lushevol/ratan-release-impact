---
type: query
title: What Are the Authoritative TDS3 Data Contract and Service-Level Requirements for Cash Settlement?
tags: [tds3, cash-settlement, data-contract, service-levels, open-question]
related: [tds3, data-ambassador, trade-information-sourcing-for-cash-settlement]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Trade Information Tech Design.md"]
---
# What Are the Authoritative TDS3 Data Contract and Service-Level Requirements for Cash Settlement?

## Question

What are the authoritative lookup keys, response fields, and operational requirements for retrieving Entity LEID, Trader ID, and Instrument from TDS3?

## Evidence

The source identifies the required information but provides no API signature, event contract, schema, lookup key, field type, nullability rule, freshness expectation, or versioning policy.

It also provides no latency, throughput, availability, timeout, retry, fallback, authorization, audit, or observability requirements for a direct TDS3 access pattern.

## Information Needed

The contract should define the source and semantics of each field, lookup identity, response and error model, freshness and consistency expectations, access controls, and compatibility policy. Service-level requirements should cover expected cashflow-event volume, latency targets, availability targets, dependency isolation, retry limits, and fallback behavior.

## Status

Open. The trade-information design cannot be operationalized from the source alone.
