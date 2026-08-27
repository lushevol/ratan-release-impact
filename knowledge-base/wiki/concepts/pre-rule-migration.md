---
type: concept
title: Pre-rule Migration
created: 2026-08-22
updated: 2026-08-22
tags: [rules, migration, suppression, netting]
related: [cash-settlement-re-platforming, cashflow-migration, ratan, murex-2-11, auto-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/2025 Target.md"]
---
# Pre-rule Migration

Pre-rule migration is the identification, mapping, recreation, and validation of upstream processing rules when responsibility moves between platforms.

## Roadmap Context

The source warns that pre-rules in [[murex-2-11]], including suppression and netting, are expected to be set up in [[ratan]].

This creates a functional-parity dependency for the broader [[cash-settlement-re-platforming]] effort. Moving cashflows without equivalent rules could change which records are processed, suppressed, displayed, or netted.

## Required Evidence

A complete migration assessment would normally require:

1. An inventory of source rules
2. Rule ownership and business rationale
3. Mapping from Murex behavior to RATAN configuration
4. Product, entity, and jurisdiction applicability
5. Expected outcomes and exception handling
6. Parallel-run or regression-test evidence
7. UAT and operational sign-off
8. Monitoring after release
9. A documented treatment for rules intentionally not migrated

The source provides none of these details and does not confirm parity.

## Related Sprint Evidence

The roadmap separately records BIC Netting for Prime cashflow as released and NDS Auto Netting for SG as Murex-dependent. These specific items should not be treated as proof that all netting pre-rules were migrated.