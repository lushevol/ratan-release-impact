---
type: concept
title: Cashflow Expiry Versioning
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, expiry, value-date, versioning, stella, ratan]
related: [value-date-based-cashflow-materialization, cashflow-event-versioning, cashflow-lifecycle-supersession-and-audit-history, stella, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Cashflow Events Control Draft 1.md"]
---
# Cashflow Expiry Versioning

Cashflow expiry versioning is the draft model in which [[entities/stella]] creates later cashflow versions to represent physical expiry while [[entities/ratan]] continues processing the prior operational record.

## Draft sequence

1. Stella creates a `New` cashflow with business version `0`, cashflow version `0`, and physical status `Live`.
2. Ratan processes that record, potentially reaching `FAILED`, `RELEASED`, `SETTLED`, `NETTED`, or `SPLIT`.
3. On `VD+1`, Stella creates a later cashflow version and eventually marks it physically `Dead`.
4. Ratan filters out the expiry version and continues working on the previous Ratan record.

For example:

```text
Stella:
C101 / New / business version 0 / cashflow version 0 / physical status Live
C101 / New / business version 0 / cashflow version 1 / physical status Dead

Ratan:
C101 / cashflow version 0 / PROJECTED -> QUEUED -> WAITING -> FAILED
```

For records that reached `RELEASED`, `SETTLED`, `NETTED`, or `SPLIT`, the draft shows intermediate Stella versions remaining `Live` and the later expiry version becoming `Dead`.

## Interpretation

The draft implies that an expiry version is not necessarily a new executable payment instruction. Ratan must distinguish the later Stella physical-status version from the prior processing record and avoid replacing the operational history with the expiry record.

The authoritative filtering rule, version correlation rule, and behavior for every Ratan terminal state remain unresolved.
