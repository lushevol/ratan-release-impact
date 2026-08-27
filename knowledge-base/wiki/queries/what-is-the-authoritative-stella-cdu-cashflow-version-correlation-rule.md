---
type: query
title: What Is the Authoritative Stella CDU Cashflow Version Correlation Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [stella, cdu, ratan, cashflow, tracking-version, scbml]
related: [stella, cdu, cdu-lake, ratan, scbml, trade-event-id-lineage, trade-confirmation-driven-cashflow-stp, what-are-the-authoritative-cashflow-version-and-business-version-rules]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Deprecated - Stella Market events & cashflow generation.md"]
---
# What Is the Authoritative Stella CDU Cashflow Version Correlation Rule?

## Question

What authoritative correlation key or algorithm allows [[ratan]] to apply a [[cdu]] confirmation status to the correct Stella-generated cashflows when trade, confirmation, and cashflow tracking versions differ?

## Historical evidence

The deprecated source gives several non-equal version pairs:

- CDU confirmation tracking version `4` and cashflow tracking version `0`;
- CDU confirmation tracking version `4` and cashflow tracking version `2`;
- a narrative in which Ratan consumes confirmation tracking version `3` for cashflows at tracking version `0`;
- a later confirmation tracking version `6` for cashflows at tracking version `4`.

The evidence rules out treating equal tracking-version values as a universal correlation rule. It does not identify the replacement rule.

## Required resolution

Obtain the current message contracts and processing logic that define:

1. identifiers used to link a CDU confirmation to a trade and its cashflow generation;
2. the meaning and lifecycle of trade tracking version, confirmation tracking version, cashflow version, and cashflow business version;
3. behavior for out-of-order, duplicate, stale, or skipped confirmation messages;
4. whether [[cdu-lake]] is a distinct integration component and which version it publishes;
5. audit evidence required when confirmation changes a cashflow from NSTP to STP.

## Related questions

- [[what-are-the-authoritative-cashflow-version-and-business-version-rules]]
- [[how-are-cashflow-amendments-correlated-and-discarded]]
- [[how-does-cashflow-blotter-handle-out-of-order-duplicate-and-withdrawal-events]]