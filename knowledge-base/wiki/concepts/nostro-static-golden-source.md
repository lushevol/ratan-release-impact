---
type: concept
title: Nostro Static Golden Source
created: 2026-08-24
updated: 2026-08-24
tags: [nostro-static-data, golden-source, reference-data, rdm, nams, fmo]
related: [nostro-centralization, nostro-static-data-migration, nostro-notification-and-refresh, nams, rdm, ratan, sci]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Nostro SSI/Nostro Static Golden Source.md"]
---

# Nostro Static Golden Source

## Definition

The Nostro static golden-source model is the proposed centralization of settlement-account reference data for FMO systems. The design positions [[nams]] as the source of existing Nostro static data and [[rdm]] as the enrichment, normalization, and distribution layer.

## Proposed responsibilities

- **NAMS:** Maintains existing Nostro-originated attributes.
- **RDM:** Adds settlement classification, effective dates, FMO eligibility, system scope, notice-to-receive, PSGL, and normalized consuming-system values.
- **SCI:** Supplies legal-entity and agent-bank descriptive data.
- **FMO systems:** Consume the distributed model rather than independently maintaining authoritative copies.
- **RATAN:** Acts as the pilot consumer before wider distribution to RAZOR, GPTM, and other systems.

## Architectural tension

Calling NAMS the golden source is not sufficient to establish end-to-end ownership. RDM creates or owns several required fields and directly maintains metal-currency Nostros that are absent from NAMS. The final architecture should distinguish the source of record, canonical normalized model, distribution layer, and exception-data owner.

This concept extends [[concepts/nostro-centralization]] and [[concepts/nostro-static-data-migration]] but should not be treated as an approved target architecture until the open ownership questions are resolved.