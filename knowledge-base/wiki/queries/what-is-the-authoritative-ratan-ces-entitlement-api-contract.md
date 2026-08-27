---
type: query
title: What Is the Authoritative RATAN CES Entitlement API Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, ces, api, data-entitlement, fmaa, interface-contract]
related: [ces, ratan-data-entitlement, functional-versus-data-entitlement]
sources: ["RATAN/RATAN -Interfaces/Ratan and CES 55508.md"]
---
# What Is the Authoritative RATAN CES Entitlement API Contract?

The source states that RATAN calls CES APIs for data-entitlement checks and that FMAA tokens provide authentication. It provides no implementable contract.

## Questions

- Which RATAN component calls CES, and for which cashflow-blotter requests?
- What endpoint, API version, request identity, entity context, and response schema are authoritative?
- What decision semantics apply to allow, deny, partial authorization, and indeterminate responses?
- What FMAA token flow, scope, renewal lifecycle, and validation requirements apply?
- How are entitlement decisions logged and audited?
- Is CES currently live for RATAN or only a target-state integration?

Evidence is limited to the high-level interface overview in [[5-ratan--17-ratan-interfaces--19-ratan-and-ces-55508--1337qxc]].