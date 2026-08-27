---
type: source
title: SCB Receive Cashflow Stamping
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page functional requirement"
tags: [cash-settlement, scb, ssi-stamping, vostro, nostro, swift]
related: [scb-receive-vostro-validation, precious-metal-cashflow-vostro-requirement, what-is-the-authoritative-scb-receive-vostro-validation-rule, concepts/nostro-stamping, entities/scb-london, entities/scb-korea, entities/azure-devops]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SCB Receive Cashflow Stamping.md"]
---
# SCB Receive Cashflow Stamping

## Summary

This functional requirement changes SSI stamping and manual SSI-update validation for SCB cashflows. The business problem is that `vostro` data is currently optional for SCB receive cashflows, although SWIFT generation requires vostro information for some precious-metal currencies. Missing data can therefore leave a cashflow in a SWIFT-generation error.

The requirement moves the relevant checks upstream into stamping and SSI-update validation. The rule is specific to SCB cashflows and should not be generalized to other entities, RFI flows, or SWIFT-suppressed flows without separate evidence.

## Traceability

- [ADO 5510918](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/5510918)
- [ADO 6473001](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6473001)

## Auto-stamping requirement

The current and target behavior is:

- SCB pay cashflows: `vostro` remains mandatory.
- SCB receive cashflows with currency `XAU`, `XAG`, `XPD`, or `XPT`: `vostro` becomes mandatory.
- Other SCB receive cashflows: `vostro` generally remains optional.

The precious-metal currency codes are:

- `XAU`
- `XAG`
- `XPD`
- `XPT`

## Manual SSI-update requirement

When a user adds adhoc SSI through the Cashflow Details UI and submits the change:

1. SCB pay cashflows retain the existing validation.
2. SCB receive cashflows with `XAU`, `XAG`, `XPD`, or `XPT` use the same validation.
3. SCB receive cashflows with settlement means `"Over-Account"` use the same validation.
4. Other SCB receive cashflows bypass the existing vostro-mandatory validation.
5. For an otherwise exempt SCB receive cashflow where `vostro SSI Type` is null, the system automatically populates:
   - vostro settlement means from the nostro settlement means;
   - vostro settlement account from the nostro settlement account.

For cases subject to mandatory validation:

- Mandatory vostro and nostro fields must be present.
- Vostro settlement means must equal nostro settlement means.
- Vostro settlement account must equal nostro settlement account.

## Superseded warning proposal

The source contains a struck-through soft-warning proposal:

> vostro info required to generate swift, are you sure to proceed?

This warning should not be treated as the final requirement. The stated target behavior favors deterministic validation and conditional auto-population.

## Rule summary

```text
Auto stamping:
  SCB pay:
    vostro = mandatory

  SCB receive:
    currency IN ('XAU', 'XAG', 'XPD', 'XPT'):
      vostro = mandatory
    otherwise:
      vostro = optional

Manual SSI update:
  SCB pay:
    enforce mandatory vostro/nostro fields
    vostro settlement means = nostro settlement means
    vostro settlement account = nostro settlement account

  SCB receive AND currency IN ('XAU', 'XAG', 'XPD', 'XPT'):
    enforce mandatory vostro/nostro fields
    vostro settlement means = nostro settlement means
    vostro settlement account = nostro settlement account

  SCB receive AND settlement means = 'Over-Account':
    enforce mandatory vostro/nostro fields
    vostro settlement means = nostro settlement means
    vostro settlement account = nostro settlement account

  Other SCB receive:
    bypass existing vostro-mandatory validation
    if vostro SSI Type IS NULL:
      vostro settlement means = nostro settlement means
      vostro settlement account = nostro settlement account
```

## Evidence and limitations

The document provides strong requirement-level evidence for the target rules but does not establish implementation or production status. It contains no API contract, code reference, acceptance-test evidence, deployment confirmation, error metrics, or migration plan.

The source also leaves unresolved whether `"Over-Account"` takes precedence across all currencies, where auto-population occurs, what a null `vostro SSI Type` means, and which SCB legal entities or branches are in scope.

This requirement extends the broader [[concepts/nostro-stamping]] domain with a conditional SCB-specific policy. It is adjacent to [[concepts/nostro-centralization]] but does not itself define a static-data migration or notification process.