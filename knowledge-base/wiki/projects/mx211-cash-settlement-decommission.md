---
type: project
title: MX2.11 Cash Settlement Decommission
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, mx211-decommission, ratan, china]
related: [26-auto-netting-page-md-files--132-cash-settlement-home-page-cash-settlement-home-page-mx211-decomm-cash-settlem--9wljrh, confirmation-match-based-payment-release, client-settlement-automation-eligibility, payment-and-cashflow-suppression-governance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/Settlement Touchpoints.md"]
status: planned
owner: ""
start_date: ""
target_date: ""
---
# MX2.11 Cash Settlement Decommission

## Brief

A proposed migration workstream to transition selected China cash-settlement workflows from MX2.11 to [[ratan]], while retaining or redesigning workflows that depend on external platforms, manual operations, and product-specific settlement processes.

## Proposed scope

The source proposes RATAN capabilities for confirmation-led payment release, client-specific NSTP/STP, payment affirmation, SSI selection and controls, manual payments, selected netting automation, payment exception remediation, and reporting.

Commodity, CDS premium, China CCS, maturity PCD, bond, TPP, and lien workflows have unresolved scope or target-state ownership.

## Key dependencies

- Client classifications and automation static from SCI.
- SSI data quality and RMA controls through SSI+ and AMH.
- S2B NG, CLSNET, and BATON integration for eligible-client automation.
- RDM rounding governance.
- FMSRE and AMH exception handling.
- CTMU, CMS, and Clearing-team decisions for specialist-product workflows.

## Delivery risks

The supplied workflow inventory is not an approved roadmap. It contains inconsistent Day 1 and target-state semantics, extensive `TBC` items, undefined client eligibility, and incomplete suppression/accounting definitions.

## Decisions

No approved project decisions are evidenced in the source.