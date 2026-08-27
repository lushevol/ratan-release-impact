---
type: query
title: What Is the Authoritative RATAN Manual Netting API and Resultant Cashflow Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, netting, api, cashflow, contract]
related: [ratan-manual-netting-transformation, ratan, cashflow-record]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 13 (31th Oct 2022- 11th Nov 2022).md"]
---
# What Is the Authoritative RATAN Manual Netting API and Resultant Cashflow Contract?

The Sprint 13 demo expects manual invocation of a RATAN Netting API to set component cashflows to `Netted` and create a resultant cashflow in `Queued`.

## Questions to Resolve

- What API endpoint, request schema, response schema, and authentication model are authoritative?
- Which cashflows are eligible to net, and which dimensions form a netting set?
- How is the resultant amount calculated and linked to component cashflows?
- Is component state transition and resultant creation atomic?
- What idempotency, reversal, unnetting, retry, and exception rules apply?

The demo document does not provide an API contract or execution evidence.