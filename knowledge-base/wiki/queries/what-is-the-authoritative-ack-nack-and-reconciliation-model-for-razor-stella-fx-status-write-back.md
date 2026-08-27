---
type: query
title: What Is the Authoritative ACK, NACK, and Reconciliation Model for Razor-Stella FX Status Write-Back?
tags: [ack, nack, reconciliation, fx, razor, ratan, stella, control-gap]
related: [fx-cashflow-status-write-back, razor, ratan, stella, what-are-the-authoritative-currency-and-amount-tolerances-for-razor-stella-fx-cashflow-matching]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FX Cashflow Status Write Back - Razor to Stella.md"]
---
# What Is the Authoritative ACK, NACK, and Reconciliation Model for Razor-Stella FX Status Write-Back?

The source contains incompatible statements: ACK is required from Razor; failed matching should store a NACK in RATAN for phase 1; and no ACK/NACK mechanism or reconciliation is in place.

The ambiguity is material because the write-back is intended as a duplicate-payment control.

## Questions to resolve

- What acknowledgement is required, and in which direction does it travel?
- Is a RATAN NACK an internal match-failure record, an outbound response to Razor, or both?
- What persistence, retry, idempotency, and error-handling rules apply?
- Who owns unresolved matches and what service-level target applies?
- How are unmatched, duplicate, delayed, malformed, and failed write-back messages reconciled?
- What evidence demonstrates that all eligible Razor events updated the intended Stella cashflows?

Until resolved, the proposed control cannot establish complete and accurate processing assurance.