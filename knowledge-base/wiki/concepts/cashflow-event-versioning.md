---
type: concept
title: Cashflow Event Versioning
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, versioning, business-version, cashflow-version, ratan-version, audit-history]
related: [cashflow-lifecycle-supersession-and-audit-history, cashflow-status-lifecycle, cashflow-amendment-supersession, cashflow-withdrawal-and-new, stella, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Cashflow Events Control Draft 1.md"]
---
# Cashflow Event Versioning

Cashflow Event Versioning is the draft’s use of multiple version fields to correlate successive cashflow events across Stella and Ratan.

## Version fields

The source distinguishes:

- **Business Version:** Incremented in examples when a withdrawal or amendment creates a new business event for the same cashflow ID.
- **Cashflow Version:** Incremented in examples when a new version of the cashflow representation is created.
- **Ratan Version:** A processing-version sequence that advances as Ratan moves a record through lifecycle operations.

The source also distinguishes Stella physical status, such as `Live` and `Dead`, from Ratan processing status.

## Examples

An amendment retains the cashflow ID while incrementing business and cashflow versions:

```text
C101 / New        / business version 0 / cashflow version 0 / amount 100
C101 / Amendment  / business version 1 / cashflow version 1 / amount 150
```

A withdrawal-and-new flow uses the original ID for the withdrawal and a new ID for the replacement:

```text
C101 / Withdrawal / business version 1 / cashflow version 1
C201 / New        / business version 0 / cashflow version 0
```

The expiry model may create a later cashflow version while retaining the same business version:

```text
C101 / New / business version 0 / cashflow version 0 / physical status Live
C101 / New / business version 0 / cashflow version 1 / physical status Dead
```

## Controls and unresolved contract

Versioning supports supersession and audit history, but the draft does not establish:

- Whether versions are incremented once per source event or once per Ratan representation.
- How duplicate, delayed, or out-of-order events are correlated.
- Whether superseded records remain queryable.
- Which system owns the authoritative version.
- How Stella status, Stella physical status, and Ratan status are reconciled.

The examples contain inconsistent version transitions, so this page records historical design intent rather than a final schema.
