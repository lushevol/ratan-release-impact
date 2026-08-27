---
type: concept
title: Netting Key Eligibility
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, eligibility, validation, beneficiary-bic]
related: [beneficiary-bic-netting, bic-net-eligibility-flag, netting-resultant-cashflow, what-is-the-authoritative-netting-key-and-bic-netting-preview-error-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/03 Beneficiary BIC Netting.md"]
---
# Netting Key Eligibility

For the Beneficiary BIC Netting acceptance criteria, selected cashflows cannot be netted when they differ in any of the following fields:

- Booking Entity
- Currency
- Value Date

When incompatible cashflows are selected through `BIC Net Selected Cashflow`, the expected popup is:

```text
Cashflow Netting Preview Can not Netting
```

The source also says there is no UI warning like CCIL, but does not define whether the stated popup is blocking, its exact presentation requirements, or the intended CCIL distinction.

## Scope and limitations

These three fields are documented disqualifiers, not a complete netting-key definition. The source does not authoritatively define eligibility requirements for Counterparty BIC, cashflow direction, amount sign, settlement method, rule priority, or other attributes.

This rule applies specifically to [[beneficiary-bic-netting]] in the cited acceptance criteria. It should not be generalized to Bilateral Netting or other netting modes without supporting evidence.