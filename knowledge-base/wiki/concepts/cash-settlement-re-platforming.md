---
type: concept
title: Cash-Settlement Re-platforming
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, migration, platform-modernization]
related: [cash-settlement-2025-roadmap, cashflow-migration, ratan, murex-2-11, pre-rule-migration, standard-settlement-instructions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/2025 Target.md"]
---
# Cash-Settlement Re-platforming

Cash-settlement re-platforming is the transfer of cash-settlement processing from a legacy platform to a strategic platform, including the data, rules, integrations, controls, and operational processes needed to run the target service.

## Application in the 2025 Roadmap

The [[cash-settlement-2025-roadmap]] identifies [[murex-2-11]] as the source and [[ratan]] as the strategic target. The work includes more than moving cashflow records. It also covers:

- Static and reference data
- Accounting integration
- SSI selection and stamping
- Suppression and netting rules
- UAT and reconciliation
- Data entitlement
- Dashboard and blotter coverage
- Status synchronization
- Capacity and database housekeeping

## Transitional Coexistence

Re-platforming can include a period in which source and target systems remain connected. The roadmap provides direct examples: NDS Auto Netting for SG depends on Murex, and RATAN sends release-status updates to Murex.

These dependencies mean the source does not support describing the transition as a completed replacement.

## Validation Requirements

A robust re-platforming assessment would require evidence for:

- Functional parity
- [[pre-rule-migration]]
- Data reconciliation
- Accounting integrity
- SSI behavior
- Entitlements and operational controls
- Performance and resilience
- Production sign-off
- Dependency retirement

The roadmap records planned work but does not provide all of this evidence.