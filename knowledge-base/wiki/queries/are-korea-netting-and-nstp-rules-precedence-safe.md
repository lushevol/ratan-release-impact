---
type: query
title: Are Korea Netting and NSTP Rules Precedence-Safe?
created: 2026-08-22
updated: 2026-08-22
tags: [Korea, auto-netting, NSTP, rule-precedence, cash-settlement]
related: [korea-static-settlement-configuration, seoul, nds-auto-netting, high-risk-nstp-rule, cashflow-suppression, netting-key-selection]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/Static date summary.md"]
---
# Are Korea Netting and NSTP Rules Precedence-Safe?

## Question

Do the Korea auto-netting, Pending NDS Netting NSTP, and cashflow-suppression rules produce the intended lifecycle without conflicting outcomes?

## Evidence

The Pending NDS Netting NSTP rule requires:

```text
Entity__Booking_Entity_SCI_FMID != "10036645"
```

The Seoul NDS Auto Netting rule requires:

```text
Entity__Booking_Entity_SCI_FMID == "10036645"
```

Dedicated Seoul suppression rules coexist with a broad non-FMRP suppression rule that excludes Seoul. These conditions may be intentionally partitioned, but the source does not state rule execution order, priority, or precedence.

## Required resolution

Document rule evaluation order, priority, terminal versus non-terminal outcomes, and representative test cases for Seoul and non-Seoul NDS cashflows. Confirm that netting, NSTP, and suppression cannot create duplicate settlement or contradictory operational instructions.