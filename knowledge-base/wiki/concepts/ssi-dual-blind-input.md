---
type: concept
title: SSI Dual-Blind Input
created: 2026-08-22
updated: 2026-08-22
tags: [ssi, maker-checker, dual-blind, settlement-instructions, cash-settlement]
related: [ssi-stamping-hierarchy, manual-entity-static-data-onboarding, maker-checker-hard-blocker-operational-levels]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/NSTP Workflow.md"]
---
# SSI Dual-Blind Input

SSI dual-blind input is a Maker–Checker control in which the Checker independently selects or enters settlement-instruction values rather than simply accepting the Maker's values.

The workflow proposes field-level behavior:

- A Checker should re-enter only fields that mismatch or were newly enriched after Maker input where possible.
- If Maker input is rejected, the same Maker should see the previously entered values when correcting the SSI.
- Checker rejection comments must be visible to the Maker.
- Maker-modified SSI should be retained even if a newer upstream SSI arrives after client affirmation.
- Field 70 and Field 72 changes should be highlighted to the Checker.
- Cover Flag and mandatory currency or routing fields should be validated in the SI input screen.
- A hard warning should identify Nostro versus Vostro settlement-means or settlement-account mismatches.

The Missing Vostro rule is direction-dependent: payments require a Vostro, while receipts should receive the default Nostro without a Missing Vostro exception.
