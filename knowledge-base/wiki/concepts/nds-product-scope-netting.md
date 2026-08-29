---
type: concept
title: NDS Product-Scope Netting
created: 2026-08-22
updated: 2026-08-22
tags: [NDS, NDS-fixing, auto-netting, product-scope, value-date]
related: [irs-resultant-cashflow-netting, cashflow-auto-netting, business-calendar-relative-netting-time]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting.md"]
---
# NDS Product-Scope Netting

## Definition

NDS Netting - Auto is described as automated netting for a defined set of non-deliverable product typologies and near-term value dates. The source lists the supported product scope as:

```text
NDS
NDS Fixing
NDIRS
NDCF
NDFRA
ND CDS Fixing
ND CDS
ND-Convert
```

## Eligibility and Grouping

The source specifies:

- value date is business value date Today, Tomorrow, or Day After;
- netting key is `Value Date/Currency/Entity FMID/Counterparty FMID/NID`;
- supported TP systems are `Murex 2.11` and `Stella`.

The source does not define `NID`, the timezone or business-calendar interpretation of the three-day value-date window, or the behavior when product typology and netting-rule scope disagree.

## Relationship to IRS Resultant-Cashflow Netting

The document asks whether the proposed treatment for `IRS Netting` resultant cashflows should also apply to `NDS Fixing Netting`. No decision is recorded. Therefore, the IRS resultant-cashflow exception must not be generalized to NDS Netting without an explicit decision.

See [[irs-resultant-cashflow-netting]] and should nds fixing netting follow the irs resultant cashflow rule.