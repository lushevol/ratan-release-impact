---
type: query
title: What Is the Authoritative Stella Business Event-to-Cashflow Mapping?
created: 2026-08-23
updated: 2026-08-23
tags: [stella, cashflow, trade-events, ratan, deprecated-requirements]
related: [stella, ratan, stella-business-event-cashflow-mapping, cashflow-partial-update, cashflow-withdrawal-and-new, cashflow-amendment-supersession, trade-economic-versus-non-economic-update, what-is-the-authoritative-withdrawal-new-sequencing-and-nstp-rule, how-does-cashflow-blotter-handle-out-of-order-duplicate-and-withdrawal-events]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Stella Business event action & cashflow impact.md"]
---
# What Is the Authoritative Stella Business Event-to-Cashflow Mapping?

A deprecated Stella reference provides incomplete historical action-to-cashflow sequences. It must be reconciled with current functional requirements, implementation behavior, and operational decisions before use as a production rule.

## Questions

- What is the current cashflow outcome for every supported Stella business event and action?
- Under what exact conditions does an economic update produce Amendment rather than [[cashflow-partial-update]]?
- Which RATAN settlement status causes an Amendment to become [[cashflow-withdrawal-and-new]]?
- Is `Withdrawal/New` a pair of independently emitted events, a compound result, or a replacement operation?
- What identifiers and versions correlate New, Amendment, and Withdrawal cashflows?
- What are the complete rules for Partial Termination, Close Out, Expiry, Novation, and Allocation?
- Which CDU confirmation statuses are prerequisites or outputs for each action?
- Does the historical Egypt versus CN & Onward applicability matrix remain valid?

## Evidence

[[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--15-deprecated-docs--45-s--1m8objk]] provides the historical matrix and event sequences, but leaves several mappings and all CDU Confirmation entries blank.

## Related Investigations

- [[what-is-the-authoritative-withdrawal-new-sequencing-and-nstp-rule]]
- [[how-does-cashflow-blotter-handle-out-of-order-duplicate-and-withdrawal-events]]
- [[what-is-the-authoritative-post-split-withdrawal-amendment-and-netting-model]]