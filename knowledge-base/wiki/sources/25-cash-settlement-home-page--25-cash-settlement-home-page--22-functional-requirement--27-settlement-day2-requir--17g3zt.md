---
type: source
title: Cashflow Auto Stamping
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, auto-stamping, ssi, exception-lifecycle, nostro, vostro]
related: [pre-adhoc-error-and-adhoc-ssi-exception-lifecycle, what-is-the-authoritative-pre-adhoc-error-and-adhoc-ssi-exception-state-model, what-does-adletosendperssiadhocexception-control-in-auto-stamping, what-are-the-vostro-and-nostro-trigger-stamping-requirements, nostro-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SCB Receive Cashflow Stamping/Cashflow Auto Stamping.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Cashflow Auto Stamping

## Summary

This functional-requirement fragment defines an exception sequence for cashflow auto SSI stamping. It specifies three conditions under which `PRE_ADHOC_ERROR` may be generated, the ordering between `PRE_ADHOC_ERROR` and `ADHOC_SSI_EXCEPTION`, and the ad hoc SSI actions that generate `ADHOC_SSI_EXCEPTION`.

The source includes headings for Vostro and Nostro trigger stamping but provides no requirements below either heading.

## Stated `PRE_ADHOC_ERROR` Generation Conditions

The source says that `PRE_ADHOC_ERROR` requires any of the following conditions:

1. A checker approval after closure of a Vostro/Nostro Exception.
2. Auto SSI stamping with no Vostro/Nostro Exception.
3. Auto SSI stamping with a Vostro/Nostro Exception where `adleToSendPerSSIAdhocException== true`.

The wording appears to express an OR relationship across these conditions, but does not formally define eligibility evaluation, timing, or persistence.

## Exception Ordering

The stated lifecycle ordering is:

```text
PRE_ADHOC_ERROR open
  → PRE_ADHOC_ERROR closes
  → ADHOC_SSI_EXCEPTION is generated
  → ADHOC_SSI_EXCEPTION closes
  → PRE_ADHOC_ERROR is generated again
```

The source does not establish whether regeneration creates a new exception record or reopens an existing record. It also does not specify whether the `PRE_ADHOC_ERROR` eligibility conditions are re-evaluated after `ADHOC_SSI_EXCEPTION` closes.

## Ad Hoc SSI Trigger

`ADHOC_SSI_EXCEPTION` is generated when an operator performs either an ad hoc SSI reject or an ad hoc SSI submit action. No different state-transition or downstream behavior is stated for rejection versus submission.

## Missing Requirement Content

The source has the following headings without supporting content:

- Vostro trigger stamping
- Nostro trigger stamping

No trigger criteria, selection behavior, exception handling, or implementation ownership can be inferred for these sections.

## Related Pages

- [[pre-adhoc-error-and-adhoc-ssi-exception-lifecycle]]
- [[nostro-stamping]]
- [[what-is-the-authoritative-pre-adhoc-error-and-adhoc-ssi-exception-state-model]]
- [[what-does-adletosendperssiadhocexception-control-in-auto-stamping]]
- [[what-are-the-vostro-and-nostro-trigger-stamping-requirements]]