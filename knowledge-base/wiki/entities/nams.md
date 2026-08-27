---
type: entity
title: NAMS
created: 2026-08-23
updated: 2026-08-23
tags: [nams, nostro, static-data, cash-settlement]
related: [ssi-plus, nostro-centralization, nostro-static-data-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Centralization.md"]
---
# NAMS

## Role

`NAMS` is identified as the planned consolidation platform for Nostro static data. The source describes the current state as fragmented maintenance within individual TP systems and proposes consolidation in `NAMS`.

The source does not state whether `NAMS` remains the authoritative runtime system after migration or how it relates operationally to [[entities/ssi-plus|SSI+]].

## Relationship to SSI+

The stated operating model is:

1. Nostro static data is consolidated in `NAMS`.
2. Data Ops creates, amends, and closes the static data in `SSI+`.
3. TP systems integrate with and consume data from `SSI+`.

The ownership boundary and synchronization mechanism between `NAMS` and `SSI+` require confirmation.

## Unknowns

- Authoritative system-of-record status.
- Canonical Nostro identifier ownership.
- Migration and historical-reference behavior.
- Query and notification interfaces.
- Reconciliation between `NAMS` and `SSI+`.
