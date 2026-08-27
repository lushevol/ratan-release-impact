---
type: query
title: How Does the 12-Character Indonesia Cashflow ID Format Handle Sequence Overflow?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow-id, indonesia, sequence-overflow, netting, splitting, compatibility]
related: [configurable-cashflow-id-prefixes, story-13292989, what-is-the-resultant-and-split-cashflow-id-prefix-contract-for-indonesia, ratan-indonesia, ratan-gdc]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Netting Spliting ID prefix.md"]
---
# How Does the 12-Character Indonesia Cashflow ID Format Handle Sequence Overflow?

## Question

What is the authoritative formatting and overflow behavior for Indonesia split and netting-resultant IDs when `SID` and `NID` must fit within 12 total characters?

## Evidence

The source proposes `SID` and `NID` for [[ratan-indonesia]], compared with `S` and `N` in [[ratan-gdc]], while requiring a 12-character identifier.

The cited generation paths use `Utils.getCashFlowId` and `cashflow_id_seq`:

```java
Utils.getCashFlowId(Constant.SPLIT_CASHFLOW_PREFIX, 11, String.valueOf(cashflowIdSeq));
```

```java
Utils.getCashFlowId("N", 11, String.valueOf(cashflowIdSeq));
```

```sql
select nextval('cashflow_id_seq')
```

The Indonesia example is `SID000062866`, which implies a three-character prefix plus a nine-digit suffix.

## Required resolution

Confirm:

1. Whether the numeric length argument to `Utils.getCashFlowId` means suffix length, total target length, or another formatting parameter.
2. Whether `cashflow_id_seq` can exceed nine digits and, if so, whether the utility fails, expands the ID, truncates, wraps, or changes formatting.
3. Whether the sequence is shared between GDC and Indonesia and what collision guarantees apply.
4. All database columns, APIs, events, reports, reconciliation tools, and downstream systems that validate, parse, or store cashflow IDs.
5. Whether existing one-character-prefix identifiers remain valid during migration, replay, and cross-environment data movement.
6. Whether `SID` and `NID` are approved values or remain the proposal associated with [[story-13292989]].

This question concerns identifier construction and compatibility, not monetary amount calculation. A prefix-only change has no demonstrated direct effect on cashflow amounts, but can affect processing where identifiers are constrained or interpreted.