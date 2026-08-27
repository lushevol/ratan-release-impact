---
type: concept
title: Nostro Centralization
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, static-data, centralization, reference-data, cash-settlement]
related: [nams, ssi-plus, nostro-stamping, nostro-notification-and-refresh, nostro-static-data-migration, ratan, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Centralization.md"]
---
# Nostro Centralization

## Definition

Nostro centralization is the planned consolidation of Nostro static-data ownership and maintenance into a common operating model. The source describes current maintenance as distributed across TP systems with differing formats. The target direction is consolidation in [[entities/nams|NAMS]], with Data Ops performing create, amend, and close operations in [[entities/ssi-plus|SSI+]].

## Target operating model

TP systems are expected to consume centralized data through `SSI+`. The requirement identifies two complementary integration patterns:

- Query-based access for Nostro stamping and accounting.
- Event-based notification that triggers downstream refresh.

This creates an architectural distinction between centralized ownership and any local TP cache or copy. The source does not decide whether runtime queries, local copies, or a hybrid model is authoritative.

## Risks and boundaries

Centralization must resolve identifier continuity, deletion behavior, local refresh, terminology normalization, and historical cashflow treatment. The source does not provide enough detail to conclude that `NAMS` or `SSI+` is the final system of record.
