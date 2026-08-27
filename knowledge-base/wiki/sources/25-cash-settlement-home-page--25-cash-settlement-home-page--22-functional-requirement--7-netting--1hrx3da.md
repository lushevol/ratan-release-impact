---
type: source
title: Cash Settlement Home Page — Functional Requirement — Netting
authors: []
year: 2024
url: ""
venue: "Internal functional requirement"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, netting, functional-requirement, IRS-netting, resultant-cashflow]
related: [irs-resultant-cashflow-netting, nds-product-scope-netting, netting-resultant-cashflow-lifecycle, cashflow-auto-netting, ccil-guaranteed-and-non-guaranteed-netting, beneficiary-bic-based-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting.md"]
---
# Cash Settlement Home Page — Functional Requirement — Netting

## Summary

This functional requirement defines eligibility criteria, grouping keys, supported trading-platform systems, and further-netting behavior for several cashflow netting types. It focuses particularly on allowing selected netting processes to operate on resultant cashflows produced by `IRS Netting`.

The document distinguishes current support from proposed changes and backlog scope. `Bilateral Netting - Adhoc` is identified as the currently supported route for further netting of `IRS Netting` cashflows. Broader support is dependent on `Stella` entity and product onboarding and on resolving the impact on `Stella` booking.

## Netting-Type Matrix

| Netting Type | Netting Criteria | TP systems | Further Netting | Comment |
| --- | --- | --- | --- | --- |
| IRS Netting - Auto | - IRS Cashflows<br>- 2 Cashflows on same VD<br>- Netting key: Value Date/Currency/Entity FMID/Counterparty FMID | - Stella | - Bilateral Netting - Manual — **NA now given netting id in rule**<br>- Bilateral Netting - Adhoc — **Available**<br>- CCIL Netting Guaranteed - Manual — **NA now given netting id in rule**<br>- CCIL Netting Non Guaranteed - Manual — **NA now given netting id in rule**<br>- Ben BIC Netting - Manual — **NA now given netting id in rule**<br>- Bilateral Netting - Auto (In Backlog) — TBC<br>- CPN (In Backlog) — TBC | |
| Bilateral Netting - Manual | - **Netting rule: Component cashflow netting id == blank**<br>- Netting key: Value Date/Currency/Entity FMID/Counterparty FMID | - Stella<br>- Murex 2.11 | NA | |
| Bilateral Netting - Adhoc | - **Component cashflow netting id can have value**<br>- Netting key: Value Date/Currency/Entity FMID/Counterparty FMID | - Stella<br>- Murex 2.11 | NA | |
| Bilateral Netting - Auto (In Backlog) | - Auto Netting rule<br>- Netting key: Value Date/Currency/Entity FMID/Counterparty FMID | | NA | |
| CCIL Netting Guaranteed - Manual | - **Netting rule: Component cashflow netting id == blank**<br>- Settlement Method == CCIL<br>- Counterparty FMID == 400021949<br>- Product == IRS<br>- Currency == INO<br>- Netting key: Value Date/Currency/Entity FMID/Counterparty FMID | - Murex 2.11<br>- Stella | NA | |
| CCIL Netting Non Guaranteed - Manual | - **Netting rule: Component cashflow netting id == blank**<br>- Settlement Method == CCIL<br>- Counterparty FMID not 400021949<br>- Product == IRS<br>- Currency == INO<br>- Netting key: Value Date/Currency/Entity FMID | - Murex 2.11<br>- Stella | NA | |
| Ben BIC Netting - Manual | - **Netting rule: Component cashflow netting id == blank**<br>- Ben BIC Static<br>- Netting key: Value Date/Currency/Entity FMID/Ben BIC | - Stella<br>- Murex 2.11 | NA | |
| NDS Netting - Auto | - Product Scope: Typology in (`NDS`, `NDS Fixing`, `NDIRS`, `NDCF`, `NDFRA`, `ND CDS Fixing`, `ND CDS` and `ND-Convert`)<br>- VD = Business VD Today, Tomorrow & Day After<br>- Netting key: Value Date/Currency/Entity FMID/Counterparty FMID/NID | - Murex 2.11<br>- Stella | NA | |
| CPN (In Backlog) | | | | |

## IRS Netting Resultant-Cashflow Pre-Check

The proposed common pre-check applies when the component cashflow ID starts with `N` and the netting ID is not blank:

```text
When component cashflow id is starting with 'N' and the netting id is not blank,
only if the payment type == 'IRS Netting' can pass the netting pre-check.
Any other payment types would be rejected.
```

The source does not establish whether `component cashflow id` and `component cashflow netting id` are the same field. This distinction must be resolved before implementation.

## Proposed Changes

| Netting Type | Problem / Change |
| --- | --- |
| Bilateral Netting - Manual | Update the rule to add `IRS Netting` as an exception case. |
| Bilateral Netting - Adhoc | No change; further netting is already supported. |
| Bilateral Netting - Auto (In Backlog) | TBC. |
| CCIL Netting Guaranteed - Manual | Add `IRS Netting` as an exception case. The resultant cashflow must inherit settlement method from component cashflows. |
| CCIL Netting Non Guaranteed - Manual | Add `IRS Netting` as an exception case. The resultant cashflow must inherit settlement method from component cashflows. |
| Ben BIC Netting - Manual | Add `IRS Netting` as an exception case. Confirm BIC stamping and whether a new query is required when the resultant cashflow is published to workflow. |
| CPN (In Backlog) | TBC. |

The long-term target is to make `IRS Netting` resultant-cashflow netting available across all netting types as additional `Stella` entities and products are onboarded. The document does not provide production approval or implementation sign-off for this target.

## Lifecycle Restriction

The source proposes that a pending netting cashflow cannot be un-netted, manually or automatically, by withdrawing a component cashflow:

```text
Pending Netting cashflow can't be un-neted
(manual or auto by withdrawal on component).
```

The exact transition behavior is unspecified. It is not clear whether the withdrawal should be rejected, leave the resultant cashflow unchanged, or move the resultant cashflow to an exception state.

## Open Questions

- Are `component cashflow id` and `component cashflow netting id` distinct fields?
- What is the precedence between blank-netting-ID validation and the `IRS Netting` exception?
- What does the `N` prefix signify?
- What is the canonical lifecycle outcome when a component of a pending netting cashflow is withdrawn?
- Should `NDS Fixing Netting` receive the same pre-check and lifecycle treatment?
- Is `INO` the authoritative currency value?
- Why does CCIL Non-Guaranteed Netting omit Counterparty FMID from its grouping key?
- Is `NID` an independent required key for NDS Netting?
- Which `Stella` entities and products support IRS resultant-cashflow booking?
- Has the proposed behavior been tested and approved for `Murex 2.11`, `Stella`, and workflow publication?

## Referenced Internal Material

- [Auto Un-Net - Trade market event](https://confluence.global.standardchartered.com/display/DSP/Auto+Un-Net+-+Trade+market+event)
- [Beneficiary BIC Netting](https://confluence.global.standardchartered.com/display/DSP/Beneficiary+BIC+Netting)
- [Business User Case](https://confluence.global.standardchartered.com/display/DSP/Business+User+Case)
- [CCIL Netting](https://confluence.global.standardchartered.com/display/DSP/CCIL+Netting)
- [CPN Business Scenario](https://confluence.global.standardchartered.com/display/DSP/CPN+Business+Scenario)
- [CPN Tech Design - Draft for now](https://confluence.global.standardchartered.com/display/DSP/CPN+Tech+Design+-+Draft+for+now)
- [Cashflow Auto Netting- 2024](https://confluence.global.standardchartered.com/display/DSP/Cashflow+Auto+Netting-+2024)
- [IRS Fix Leg & Floating leg payment handling](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2726685251)
- [NDS Auto Netting](https://confluence.global.standardchartered.com/display/DSP/NDS+Auto+Netting)
- [Netting Rules Static Data](https://confluence.global.standardchartered.com/display/DSP/Netting+Rules+Static+Data)
- [Netting Service - GUI & API intergration](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2594781981)
- [Netting Story Board](https://confluence.global.standardchartered.com/display/DSP/Netting+Story+Board)
- [Product Agnostic model to identify all cashflows for a specific value date to support Auto Aggregation](https://confluence.global.standardchartered.com/display/DSP/Product+Agnostic+model+to+identify+all+cashflows+for+a+specific+value+date+to+support+Auto+Aggregation)
- [Settlement Netting Validation/Generation](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2386165321)
- [[Draft] Auto Aggregation based on Normalized Payment Schedule](https://confluence.global.standardchartered.com/display/DSP/%5BDraft%5D+Auto+Aggregation+based+on+Normalized+Payment+Schedule)

## Evidence Status

This document is a functional requirement and design reference. Its matrix provides moderate evidence for intended eligibility and scope, while the proposed exception logic and lifecycle restriction require confirmation through implementation details, transition specifications, testing, and approval records.

See [[irs-resultant-cashflow-netting]], [[nds-product-scope-netting]], and [[netting-resultant-cashflow-lifecycle]] for focused summaries.