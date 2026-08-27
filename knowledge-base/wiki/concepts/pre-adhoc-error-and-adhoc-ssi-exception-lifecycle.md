---
type: concept
title: PRE_ADHOC_ERROR and ADHOC_SSI_EXCEPTION Lifecycle
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, ssi, exception-lifecycle, auto-stamping, nostro, vostro]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--17g3zt, nostro-stamping, what-is-the-authoritative-pre-adhoc-error-and-adhoc-ssi-exception-state-model, what-does-adletosendperssiadhocexception-control-in-auto-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SCB Receive Cashflow Stamping/Cashflow Auto Stamping.md"]
---
# PRE_ADHOC_ERROR and ADHOC_SSI_EXCEPTION Lifecycle

`PRE_ADHOC_ERROR` and `ADHOC_SSI_EXCEPTION` are exception identifiers used in the cashflow auto-stamping and ad hoc SSI process.

## Stated Eligibility for `PRE_ADHOC_ERROR`

The source permits `PRE_ADHOC_ERROR` generation when any of these conditions applies:

- A checker approves after a Vostro/Nostro Exception has closed.
- Auto SSI stamping finds no Vostro/Nostro Exception.
- Auto SSI stamping finds a Vostro/Nostro Exception and `adleToSendPerSSIAdhocException== true`.

The exact meaning, owner, spelling, and default behavior of `adleToSendPerSSIAdhocException` are not defined by the source.

## Ordered Exception Sequence

The specified sequence is:

```text
PRE_ADHOC_ERROR
  → close
  → generate ADHOC_SSI_EXCEPTION
  → close ADHOC_SSI_EXCEPTION
  → generate PRE_ADHOC_ERROR again
```

`ADHOC_SSI_EXCEPTION` is generated on an ad hoc SSI reject or submit action.

## Scope and Limits

This requirement is an exception-lifecycle rule associated with auto SSI stamping and Vostro/Nostro Exceptions. It does not establish rules for dedicated Nostro, RFI selection, particular services, APIs, or data models.

The source does not state:

- whether regenerated `PRE_ADHOC_ERROR` is a new record or a reopening;
- whether final regeneration is conditional on renewed eligibility;
- whether submit and reject have different effects;
- legal states, idempotency controls, or error handling.

See [[nostro-stamping]] for the broader Nostro-stamping domain. Track unresolved state semantics in [[what-is-the-authoritative-pre-adhoc-error-and-adhoc-ssi-exception-state-model]].