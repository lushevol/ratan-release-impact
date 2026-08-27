---
type: concept
title: Withdrawal Cashflow Query Exclusion
tags: [withdrawal, cashflow, tis, query, reversal, settlement]
related: [tis, tis-cashflow-eligibility-rules, oltp, does-otlp-in-the-ratan-tis-document-mean-oltp, authoritative-cashflow-lifecycle-and-system-owners-2026-08-24-104403]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and TIS.md"]
---
# Withdrawal Cashflow Query Exclusion

The RATAN–TIS interface source states that withdrawal cashflows will not be available for `TIS/OTLP` query. It further says that such cashflows will be in `Settled` status with a `Reversed/Reversal` flag.

## Ambiguities

The statement is not a complete query rule:

- `OTLP` may be a typographical variant of [[oltp|OLTP]], which is referenced elsewhere in the same source as `OLTP(UI)`, but this is unconfirmed.
- `Reversed/Reversal` is not an exact field name, event name, or permitted value.
- The source does not explain how a cashflow can be `Settled` yet excluded, beyond its association with reversal.
- TIS scope separately permits `Settled` cashflows while requiring “No reversal event”; see [[tis-cashflow-eligibility-rules]].

The likely reconciliation is that the no-reversal condition excludes withdrawal cashflows, but the source does not formally establish this predicate logic.