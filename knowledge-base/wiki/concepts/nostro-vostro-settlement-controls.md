---
type: concept
title: Nostro and Vostro Settlement Controls
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, nostro, vostro, controls, standard-settlement-instructions]
related: [standard-settlement-instructions, ssi-selection-hierarchy, delivery-versus-payment, settlement-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/2025 backlog.md"]
---
# Nostro and Vostro Settlement Controls

Nostro and Vostro settlement controls govern account selection, required account information, duplicate configurations, and exceptions during cashflow settlement.

## Backlog Requirements

The 2025 FMRP backlog identifies several control changes:

- A receipt cashflow should not require Vostro when an Adhoc Nostro SI has been provided, with a stated need to preserve control for Precious Metals receipts and over-account flows.
- Vostro should be mandatory for Precious Metal receipts.
- Nostro SI should be selected automatically from the currency pair for Egypt and Saudi.
- Multiple Nostro setups should be permitted for FXBRREC when the Ebbs account number differs.
- External Nostro is the third phase of [[delivery-versus-payment]] automation and may move to 2026.

## Relationship to Settlement Instructions

These controls interact with [[standard-settlement-instructions]] and [[ssi-selection-hierarchy]]. The source proposes both validation and selection changes, but it does not define the complete hierarchy or explain how Adhoc Nostro SI interacts with standing instructions.

The apparently different Vostro requirements apply to different conditions and should not be treated as contradictory without flow-level analysis.