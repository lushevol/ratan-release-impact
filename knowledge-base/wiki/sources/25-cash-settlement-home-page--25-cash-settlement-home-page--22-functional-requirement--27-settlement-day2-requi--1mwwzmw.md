---
type: source
title: HVP Tech Design
authors: []
year: 2026
url: ""
venue: Internal technical design
tags: [settlement-day-2, high-value-payment, ratan, swift, technical-design]
related: [ratan, swift, settlement-day-2, high-value-payment-control-technical-architecture, outbound-property-propagation-to-swift-mt-mx, parent-cashflow-resolution-by-splitting-id]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/High Value Payment Control - RATAN/HVP Tech Design.md"]
---
# HVP Tech Design

This technical-design fragment assigns High Value Payment (HVP) control responsibilities across Orchestration, Lifecycle, Swift, Query, and Netting services within [[settlement-day-2]]. It describes intended dependencies and message flow, not a complete HVP policy or production-ready interface contract.

![Architecture note](../media/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--1mwwzmw/image-2026-7-3_14-34-38.png)

## Stated service responsibilities

- **Orchestration service** parses cashflow SCBML for `cashflowId` and `businessVersion`, calls Lifecycle service for STP/NSTP information and `lastUser`, and updates topic publishing to add the `X-Outbound-Property-` message header.
- **Lifecycle service** provides an internal API to retrieve STP/NSTP information and `lastUser`.
- **Swift service** consumes the message header and adds it to the MT/MX message header.
- **Query service** supports querying and saving a USD-equivalent value.
- **Netting service** provides an internal API to retrieve a parent cashflow by `splittingId`.

The design distinguishes routing of LOANIQ cashflows to `message-bridge` and Fmrp cashflows to Swift service. It does not state whether the two routes apply equivalent HVP metadata propagation.

## Scope and limitations

The source supports the cross-service decomposition recorded in [[high-value-payment-control-technical-architecture]]. It does not specify:

- an HVP threshold, classification rule, approval rule, or release rule;
- FX-rate source, valuation time, rounding, or precision for USD equivalent;
- Lifecycle API endpoint, schemas, authorization, timeout, or error behavior;
- the complete `X-Outbound-Property-` header name, value, or mandatory status;
- concrete MT or MX message elements receiving the propagated metadata;
- whether HVP assessment applies to split cashflows, their parent, or an aggregate amount.

The design should therefore be treated as an incomplete technical dependency map for [[ratan]], rather than evidence of an implemented or validated HVP-control solution.