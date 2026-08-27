---
type: query
title: What Is the Authoritative SSI Effective-Date Transition Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [SSI, effective-date, future-effective, ED, SGO, cashflow, exception]
related: [ssi-effective-date-transition, sgo-ssi-replication, ssi-refresh-exception-lifecycle, pre-adhoc-error-and-adhoc-ssi-exception-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/FMRP SGO Testing.md"]
---
# What Is the Authoritative SSI Effective-Date Transition Rule?

## Question

What should happen to a cashflow whose value date is before, equal to, or after an SSI effective date, and when should an `_ED` SSI transition to its live identifier?

## Conflicting source wording

Cases 11–14 support the rule that an SSI is not selected before its effective date and is automatically attached after the effective date.

Case 17, however, describes a cashflow as triggering `Missing Vostro` if its value date is beyond the effective date, while also expecting:

```text
74704323_ED     → 74704323
74704323_SGO_ED → 74704323_SGO
```

The source does not clarify whether the `Missing Vostro` wording is intentional, reversed, or a documentation error.

## Required resolution

Define the authoritative behavior for:

- Value dates before the effective date;
- Value dates equal to the effective date;
- Value dates after the effective date;
- Existing cashflows already stamped with an `_ED` record;
- Deletion or amendment during the transition;
- Corresponding SGD and SGO records.

The resolution should include test evidence for both namespaces and update [[ssi-effective-date-transition]].
