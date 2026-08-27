---
type: query
title: What Are the Two eBBS Transaction-Entry Leg Ordering and Currency Rules?
created: 2026-08-23
updated: 2026-08-23
tags: [eBBS, accounting, Nostro, bridge-account, currency, Korea, open-question]
related: [ebbs-accounting-message-mapping, ebbs, ratan-accounting-reconciliation-api, korea-accounting-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Korea Accounting Recon - RATAN- TLM.md"]
---
# What Are the Two eBBS Transaction-Entry Leg Ordering and Currency Rules?

## Question

The response sample contains two transaction entries and the mapping defines separate Nostro and bridge-account fields, but the requirement does not explicitly define entry ordering. The sample also hardcodes `casa-currency-code` as `USD`, while Korea static data distinguishes `KRW` and `FCY`.

## Evidence

The Korea bridge-account mappings are:

```text
SCFB_SEOUL / 10036645 / KRW -> 000287
SCFB_SEOUL / 10036645 / FCY -> 040446
```

The sample uses `casa-currency-code: USD` for both entries.

## Required resolution

Confirm which entry is the Nostro leg, which is the bridge leg, whether ordering is contractual, and whether `casa-currency-code` is always `USD` or should follow transaction or account currency.