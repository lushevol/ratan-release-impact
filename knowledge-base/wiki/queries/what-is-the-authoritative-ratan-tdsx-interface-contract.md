---
type: query
title: What Is the Authoritative RATAN-TDSX Interface Contract?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, tdsx, interface-contract, rest-api, solace, operations]
related: [tdsx, ratan-tdsx-integration, sabre, tds3, solace, ratan-trade-control, trade-validation]
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (TDSX)-29126.md"]
---
# What Is the Authoritative RATAN-TDSX Interface Contract?

The available source establishes a high-level RATAN–[[tdsx|TDSX]] relationship but is not an authoritative implementation contract.

## Information required

- Confirm the canonical interface name: RATAN–TDSX, RATAN–SABRE TDSX, RATAN–TDS3, or another registered name.
- Obtain REST endpoint paths, HTTP methods, API versions, request and response schemas, authentication, authorization, timeout, and error-handling requirements.
- Identify how TDSX routes or resolves requests across TDS2 and [[tds3|TDS3]].
- Obtain [[solace|Solace]] topic or queue names, message schemas and versions, ordering, retry, delivery, dead-letter, and acknowledgement rules for Uber messages.
- Document the end-to-end sequence for Payment Schedule retrieval, Trade Blotter display, and trade validation.
- Define failure recovery, reconciliation, operational monitoring, escalation procedures, and interface-specific OLA targets.
- Verify the source review status and malformed SABRE contact addresses.

## Evidence

[[5-ratan--17-ratan-interfaces--26-ratan-and-sabre-tdsx-29126--c4prc]] documents only that RATAN retrieves Payment Schedule data from TDSX, calls a TDSX REST API for trade validation, and receives TDSX-published Uber messages over Solace. Its technical-specification and troubleshooting sections are empty.

The scope and interaction modes are summarized in [[ratan-tdsx-integration]].