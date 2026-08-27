---
type: concept
title: RATAN Indonesia Time-Zone Contract
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, timestamps, utc, api-contract, audit]
related: [timestamp-semantic-and-format-consistency, ratan-indonesia, 51358-ratan-cash-settlement-query-service, audit-trail, ratan-indonesia-onshoring-2026]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UTC Time zone impact - Indonesia/Time Fields Summary.md"]
---
# RATAN Indonesia Time-Zone Contract

A time-zone contract must define timestamp semantics independently from presentation labels such as “Local Time.” The Indonesia Cash Settlement Platform inventory shows UTC upstream fields, local audit and UI fields, naive values, and values carrying UTC designators.

## Required field contract

Every time-bearing field should specify:

- field owner and source system;
- business meaning;
- storage type and canonical time zone;
- API serialization format;
- permitted inbound forms and their interpretation;
- display time zone;
- conversion owner: upstream, backend, BFF, or UI;
- fractional-second precision and round-trip expectations.

## Conversion rules

- An offsetless date-time must be treated as a local wall-clock value only when the field contract explicitly assigns it a zone.
- A `Z` suffix denotes UTC and must not be reinterpreted as an Indonesia UTC+7 wall-clock value.
- Numeric offsets, including `+00:00`, must be retained during parsing.
- Textual WIB values require a separately specified parser and should not be processed through an ISO-only path.
- User-entered Indonesia local date-times may be converted to UTC by subtracting seven hours, but this path must be distinct from API-response parsing.

## Scope

The contract is especially relevant to mixed Cashflow History fields in [[51358-ratan-cash-settlement-query-service]], backend audit fields recorded by [[audit-trail]], and production-readiness testing for [[ratan-indonesia-onshoring-2026]].

Open implementation questions are tracked in [[does-idns-time-to-utc-incorrectly-reinterpret-z-suffixed-utc-timestamps]] and [[what-is-the-canonical-indonesia-cash-settlement-timestamp-contract]].