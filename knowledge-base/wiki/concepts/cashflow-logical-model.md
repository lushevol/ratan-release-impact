---
type: concept
title: Cashflow Logical Model
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, data-model, scbml, ratan, settlement-instructions]
related: [scbml, ratan-settlement, tds3, sci, ssi-plus, scbml-cashflow-ingestion-and-persistence, straight-through-processing, nostro-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/Cashflow Logical Model Fields & Data Store.md"]
---
# Cashflow Logical Model

The cashflow logical model maps business attributes to SCBML paths and Ratan-managed values. It covers the following domains:

- data-flow lineage and immutable message identity;
- cashflow identity, lifecycle events, state, and versions;
- payment payer/receiver, currency, amount, date, type, and cutoff;
- netting, un-netting, splitting, auto-netting, and pending-fixing controls;
- trade identifiers, product classifications, portfolios, and TradeLake temporal attributes;
- booking and counterparty entities, SCI identifiers, and personnel attributes;
- SSI source, priority, SWIFT type, nostro/vostro accounts, routing banks, remittance, and charges; and
- Ratan operational data including validation status, exceptions, FMO comments, audit versions, and cutoffs.

## Data provenance

Attributes must be interpreted by provenance:

1. **Inbound SCBML fields** are sourced directly from message paths.
2. **Parent-trade enrichment fields** must be obtained from the [[tds3|TDS3]] trade API with trade ID plus trade version.
3. **SCI-derived fields** include certain entity and counterparty data; some are marked TBC.
4. **Ratan-managed fields** have `NA` or blank physical mappings and are populated through Ratan operations or downstream interactions.

## Mapping-quality constraints

This source is not an executable schema contract. It contains blank data types, `NA` paths, `TBC` derivations, and visibly malformed or inconsistent XPath-like values. It also labels `Cashflow.Position_Id` as TP-system-specific and explicitly unsafe for routine downstream use.

Before implementation or reuse, mappings should be validated against the SCBML schema and assigned clear enrichment ownership and failure handling. The unresolved TDS3 behavior is tracked in [[what-is-the-failure-policy-for-ratan-parent-trade-enrichment]].