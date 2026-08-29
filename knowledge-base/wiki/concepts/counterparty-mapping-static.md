---
type: concept
title: Counterparty Mapping Static
created: 2026-08-22
updated: 2026-08-22
tags: [static-data, counterparty, fmid, fmcode, inter-entity-netting]
related: [inter-entity-cashflow-pre-match, inter-entity-auto-netting, auto-netting-static-go-live-sequencing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting.md"]
---
# Counterparty Mapping Static

Counterparty mapping static is backend configuration that maps a counterparty SCI FMID/FMCODE to a canonical internal-entity FMID/FMCODE for [[inter-entity-cashflow-pre-match]].

Without a mapping record, the counterparty FMID itself is used. Mapping therefore enables reciprocal matching when different source identifiers represent the same SCB internal entity, such as London, Hong Kong, Taipei, or Singapore internal structures.

## Governance requirement

The source includes an original requirement mapping table and a smaller confirmed deployment table. Five identifiable rows are absent from the deployment version, although the source says six were excluded. This discrepancy can change match eligibility and must be reconciled with the actual backend configuration.

See which inter entity mapping static is authoritative before treating either table as production-authoritative.