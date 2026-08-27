---
type: concept
title: Netting over Netting
created: 2026-08-22
updated: 2026-08-22
tags: [netting, settlement, irs, nd-ccs, configuration]
related: [auto-netting, irs-auto-netting, cross-product-netting, netting-key-selection, should-nd-ccs-support-netting-over-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - FXO.md"]
---
# Netting over Netting

Netting over netting applies an additional netting layer to obligations that have already been netted.

## Current Restriction in the Checklist

The FXO onboarding checklist states that only IRS is allowed to use netting over netting. It also states that ND IRS follows the same ISDA taxonomy.

The source then identifies a potential extension: configuration would need to be updated to allow ND CCS. This is an extension request, not evidence that ND CCS is currently supported.

## Risks and Required Controls

Any extension should define:

- Eligibility and taxonomy rules.
- The identifiers used at each netting layer.
- Preservation of links to component cashflows.
- Prevention of duplicate inclusion.
- Unwind, cancellation, and exception behavior.
- Accounting and payment-message consequences.
- Operational visibility and authorization.

Approval and risk analysis for ND CCS remain unresolved. See [[should-nd-ccs-support-netting-over-netting]].