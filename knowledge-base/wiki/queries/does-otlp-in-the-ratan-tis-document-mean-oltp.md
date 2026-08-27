---
type: query
title: Does OTLP in the RATAN-TIS Document Mean OLTP?
tags: [otlp, oltp, tis, ratan, query-eligibility, terminology]
related: [oltp, tis, withdrawal-cashflow-query-exclusion, 5-ratan--17-ratan-interfaces--13-ratan-and-tis--1t8tke0]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and TIS.md"]
---
# Does OTLP in the RATAN-TIS Document Mean OLTP?

The source says that users manually key payment information through `OLTP(UI)`, but later says withdrawal cashflows are unavailable for `TIS/OTLP` query.

## Why this matters

If `OTLP` means [[oltp|OLTP]], the source may be describing a shared query exclusion affecting both TIS and the existing manual-entry channel. If it identifies another application or query layer, the affected system scope and ownership differ.

## Required confirmation

Confirm:

- whether `OTLP` is a typographical error for `OLTP`;
- whether TIS and OLTP use the same cashflow-query service and eligibility criteria;
- whether withdrawal exclusion applies to both systems;
- the exact system, API, or UI to which the query restriction applies.

Until confirmed, the withdrawal statement should remain limited to the source wording documented in [[withdrawal-cashflow-query-exclusion]].