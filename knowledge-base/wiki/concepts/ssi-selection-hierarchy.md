---
type: concept
title: SSI Selection Hierarchy
created: 2026-08-22
updated: 2026-08-22
tags: [ssi, hierarchy, settlement-rules]
related: [standard-settlement-instructions, ssi-stamping, cashflow-migration, ratan, cash-settlement-2025-roadmap]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/2025 Target.md"]
---
# SSI Selection Hierarchy

An SSI selection hierarchy is the ordered rule set used to choose among candidate [[standard-settlement-instructions]].

## Roadmap References

The source includes:

- Work item `7477339`, under which Tranche 1 should follow the UK SSI selection hierarchy
- A Sprint 2 item labeled `RELEASED` in which the SI hierarchy follows a new model for Stella Prime payments
- Related work to align UK Prime trade SSI stamping with cashflow best-match behavior

These references show that SSI selection is a migration dependency rather than a peripheral configuration detail.

## Unknowns

The source does not provide:

- Hierarchy levels
- Matching keys
- Precedence rules
- Effective-date behavior
- Entity or product overrides
- Fallback handling
- Exception management
- Test cases or acceptance criteria

The UK and Stella Prime hierarchies should not be assumed to be identical.