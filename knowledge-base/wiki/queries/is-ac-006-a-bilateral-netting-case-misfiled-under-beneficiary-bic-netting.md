---
type: query
title: Is AC-006 a Bilateral Netting Case Misfiled Under Beneficiary BIC Netting?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, beneficiary-bic, bilateral-netting, contradiction]
related: [beneficiary-bic-netting, netting-resultant-cashflow, beneficiary-bic-netting-versus-bilateral-manual-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/03 Beneficiary BIC Netting.md"]
---
# Is AC-006 a Bilateral Netting Case Misfiled Under Beneficiary BIC Netting?

AC-Settlement-Manual Netting-006 is labelled as a Beneficiary BIC Netting withdrawal scenario, but it specifies:

- `Net Selected Cashflow`
- `Net All Cashflows With Affirmation`
- affirmation status `Affirmed`
- resultant payment type `Bilateral Netting`

Other active scenarios in the same source use `BIC Net Selected Cashflow`, `Net All Cashflows`, and payment type `Ben BIC Netting`.

## Questions

- Is AC-006 a copied or misfiled Bilateral Netting scenario?
- Does a released or settled Beneficiary BIC Netting resultant intentionally follow a Bilateral Netting workflow?
- Which UI action and payment type are authoritative for this lifecycle condition?

This inconsistency should remain unresolved in [[beneficiary-bic-netting]] and [[beneficiary-bic-netting-versus-bilateral-manual-netting]] until an authoritative requirement or implementation record resolves it.