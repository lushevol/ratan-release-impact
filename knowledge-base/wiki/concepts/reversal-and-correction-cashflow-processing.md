---
type: concept
title: Reversal and Correction Cashflow Processing
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, reversal, correction, withdrawal, amendment, netting, deprecated]
related: [cashflow-events-control-draft2, cashflow-amendment-supersession, stella-cashflow-amendment-supersession, cashflow-status-lifecycle, cashflow-netting-and-un-netting-state-transitions, what-is-the-authoritative-withdrawal-new-sequencing-and-nstp-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Cashflow Events Control Draft2.md"]
---
# Reversal and Correction Cashflow Processing

A historical draft model for handling an amendment or cancellation after a cashflow has reached `NETTED`, `RELEASED`, or `SETTLED`.

## Proposed distinction

The deprecated draft distinguishes:

- **Reversal cashflow:** a `Withdrawal` event associated with the original cashflow and marked `Reversal = Y`. It is proposed to enter an operational workflow, commonly from `NETTED` or `SETTLED` to `WAITING`.
- **Correction cashflow:** a new replacement cashflow, marked `Correction = Y` in draft examples, that carries amended commercial details such as amount.

For a cashflow changed before `NETTED`, `RELEASED`, or `SETTLED`, the draft instead proposes updating the business version while retaining the operational lifecycle.

## Netting branch

For an amended netted component, the proposed outcome depends on the resultant:

- If the resultant is not settled, operations manually un-net it; the resultant becomes `DEAD`, the affected component and reversal are cancelled, and unaffected components resume processing.
- If the resultant is settled, the settled resultant remains in place; reversals and corrections may be separately netted into a new resultant.

This is non-authoritative historical behavior. It does not define correlation keys, offset logic, duplicate identifiers, audit retention, netting eligibility, or completion semantics.

See [[cashflow-amendment-supersession]], [[cashflow-netting-and-un-netting-state-transitions]], and [[cashflow-events-control-draft2]].