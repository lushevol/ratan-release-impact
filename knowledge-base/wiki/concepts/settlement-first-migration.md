---
type: concept
title: Settlement-First Migration
created: 2026-08-22
updated: 2026-08-22
tags: [settlement-migration, trade-migration, RATAN, Murex, FMRP]
related: [strategic-settlements-platform, murex-cashflow-migration-to-ratan, murex-to-ratan-cashflow-integration, ratan, murex, fmrp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Strategic Cash Settlements Features.md"]
---

# Settlement-First Migration

Settlement-first migration moves settlement processing to a strategic platform before the underlying trade population has fully migrated.

In the source architecture, RATAN receives cashflows from both Murex 2.11 trade populations and FMRP strategic trades. RATAN then centralises downstream settlement and payment processing. Countries can therefore settle from one system while trade migration continues separately.

## Purpose

The approach is intended to:

- Remove the settlement-payment dependency on Murex earlier.
- Prepare the strategic settlement platform before full trade migration.
- Support a mixed legacy and strategic cashflow population.
- Give each country a single settlement-processing system.
- Separate trade migration timing from settlement migration timing.

## Boundary

Settlement-first migration does not mean that Murex immediately stops being used for all trade or cashflow origination. Murex may remain a transitional source while RATAN assumes settlement and payment responsibility.

The source does not provide country-level completion evidence, implementation milestones, or production metrics.