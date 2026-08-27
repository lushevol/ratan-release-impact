---
type: concept
title: SCBML Cashflow Ingestion and Persistence
created: 2026-08-22
updated: 2026-08-22
tags: [scbml, cashflow, ingestion, persistence, ratan]
related: [scbml, stella, murex-2-11, tds3, ratan-settlement, cashflow-logical-model, cash-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/Cashflow Logical Model Fields & Data Store.md"]
---
# SCBML Cashflow Ingestion and Persistence

Ratan’s required inbound path is Stella/Murex 2.11 → TDS3 → Ratan. Ratan converts new SCBML cashflow messages and stores the resulting data locally. Ratan domain-service processing and FMO GUI actions also create locally stored cashflow results, normally as new versions.

## Persistence grain

The required unit of persistence and cashflow-blotter display is one record per `<scb:cashflow>` element.

This differs from message-level processing: a `Withdrawal & New` SCBML message has two `<scb:cashflow>` elements and must therefore produce two stored records and two GUI rows. The two events can refer to the same cashflow ID while carrying different lifecycle versions.

## Versioning

The model distinguishes:

- `Cashflow.Cashflow_Version`, incremented when the payment transaction changes;
- `Cashflow.Cashflow_Business_Version`, incremented when the payment business version is materialized;
- `Cashflow.Cashflow_Major_Version`, incremented for Book, Update, Cancel, or Undo; and
- `Cashflow.Cashflow_Minor_Version`, used for Ratan minor versions.

The requirement does not define idempotency, replay behavior, atomic processing behavior for multi-cashflow messages, or recovery if a single record in such a message fails.