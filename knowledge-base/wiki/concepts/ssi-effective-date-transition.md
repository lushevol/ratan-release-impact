---
type: concept
title: SSI Effective-Date Transition
created: 2026-08-23
updated: 2026-08-23
tags: [SSI, effective-date, future-effective, ED, SGO, cashflow, Missing-Vostro]
related: [sgo-ssi-replication, ssi-refresh-exception-lifecycle, ssi-id-persistence-and-edit-provenance, pre-adhoc-error-and-adhoc-ssi-exception-lifecycle, what-is-the-authoritative-ssi-effective-date-transition-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/FMRP SGO Testing.md"]
---
# SSI Effective-Date Transition

## Definition

An SSI effective-date transition controls when a future-dated SSI becomes eligible for cashflow selection. The testing record represents a future-effective record with an `_ED` suffix and expects it to transition to the corresponding live SSI identifier when the effective date is reached.

## Expected lifecycle

```text
Future-effective SSI created
→ Cashflows before effective date do not select the SSI
→ Effective date is reached
→ _ED record transitions to live SSI
→ Eligible cashflows select or refresh to the live SSI
```

The same pattern applies to SGO records:

```text
74704323_ED     → 74704323
74704323_SGO_ED → 74704323_SGO
```

## Test evidence

Cases 11–14 were recorded as `PASS` for the before-and-after effective-date behavior. The source also records:

```text
74704072_ED     / 74704072_SGO_ED
Effective date: 2025-10-05

74704323_ED     / 74704323_SGO_ED
Effective date: 2025-10-01

75260413_ED     → 75260413
75260413_SGO_ED → 75260413_SGO
Observed: 2025-10-09
```

Cases 15–18 contain amendment and transition evidence, but their formal pass/fail fields are blank.

## Unresolved rule

Case 17 describes a cashflow as triggering `Missing Vostro` if its value date is beyond the effective date, while the surrounding expected transition indicates that the live SSI should become available after the effective date. The source does not establish whether this wording is intentional or erroneous.

The authoritative rule for cashflows before, on, and after the effective date is tracked in [[what-is-the-authoritative-ssi-effective-date-transition-rule]].
