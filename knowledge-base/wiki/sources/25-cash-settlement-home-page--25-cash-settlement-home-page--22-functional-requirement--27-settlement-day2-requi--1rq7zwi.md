---
type: source
title: Inter-Entity STP
authors: []
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6473009"
venue: Azure DevOps
tags: [cash-settlement, settlement-day-2, inter-entity-stp, Murex, MX]
related: [murex-2-11, murex, inter-entity-cashflow-stp, internal-counterparty-exception-bypass, settlement-day-2, manual-entity-swift-mx-bifurcation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity STP.md"]
---
# Inter-Entity STP

## Source context

This functional requirement is associated with Azure DevOps Story 6473009, **STP SCB counterparty cashflows**.

## Requirement

> STP Inter Entity Cashflows of Murex2.11 (agree with Prakash & Amol that this will be only for MX cashflows)

> Internal Counterparty identifier that can be used to bypass exceptions

## Summary

The requirement proposes straight-through processing for inter-entity cashflows originating from Murex 2.11. Its stated scope is limited to MX cashflows. It also calls for an internal-counterparty identifier that can be used to bypass exceptions for eligible flows.

The document does not define the identifier field, its owning system, eligible values, the exception taxonomy, non-bypassable controls, audit requirements, or acceptance criteria. The requirement should therefore be treated as a documented functional intent rather than a complete implementation specification.

## Scope boundary

The source supports the following narrow interpretation:

- Murex version: **2.11**
- Flow type: **inter-entity cashflows**
- Cashflow category: **MX only**
- Proposed control: internal-counterparty identification with exception bypass

The source does not establish a general MX-only rule for all Murex cashflows, all inter-entity processing, or all manual-entity settlement flows. It also does not authorize bypassing hard blockers, compliance controls, settlement-risk controls, or other specific exception classes.

## Open implementation questions

See [[which-exceptions-may-internal-counterparties-bypass]], [[what-is-the-authoritative-internal-counterparty-identifier]], and [[is-inter-entity-stp-limited-to-murex-211-mx-cashflows]].