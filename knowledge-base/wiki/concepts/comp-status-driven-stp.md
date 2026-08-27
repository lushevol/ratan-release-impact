---
type: concept
title: COMP-Status-Driven STP
created: 2026-08-23
updated: 2026-08-23
tags: [stp, comp, cash-settlement, korea, migration]
related: [korea-cash-settlement-migration, trade-validation-gated-group-processing, trade-validation-group-advancement, bulk-manual-stp-group-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration.md"]
---
# COMP-Status-Driven STP

## Definition

`COMP`-status-driven STP is a referenced control model in which `COMP` status drives straight-through processing for the Korea Murex-to-RATAN migration.

The source establishes this relationship only through the linked document title **COMP status to drive STP process**. It does not define what `COMP` means, which system owns it, or how it is assigned.

## Known Scope

The source does not establish whether `COMP` applies at trade, cashflow, group, or major-version level. It also does not specify withdrawal conditions, exception handling, retries, or precedence over other settlement controls.

## Relationship to Existing Controls

This concept may interact with [[concepts/trade-validation-gated-group-processing]], [[concepts/trade-validation-group-advancement]], and [[concepts/bulk-manual-stp-group-blotter]]. No equivalence between `COMP` and `is_trade_validated`, cashflow state, group completion, or manual STP should be assumed until the primary design is reviewed.

## Evidence Boundary

This page records a referenced design subject, not an approved implementation rule. The governing definition and precedence remain open in [[what-is-comp-status-and-how-does-it-drive-stp-in-korea-migration]].