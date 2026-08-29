---
type: concept
title: IRS Resultant-Cashflow Netting
created: 2026-08-22
updated: 2026-08-22
tags: [IRS-netting, resultant-cashflow, netting, cash-settlement, pre-check]
related: [cashflow-auto-netting, netting-resultant-cashflow-lifecycle, auto-netting-rule-management, ccil-guaranteed-and-non-guaranteed-netting, beneficiary-bic-based-netting, does-an-empty-netting-id-indicate-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting.md"]
---
# IRS Resultant-Cashflow Netting

## Definition

IRS resultant-cashflow netting concerns the further netting of a resultant cashflow created by `IRS Netting`. The source proposes a targeted exception rather than a general permission for all previously netted cashflows.

The relevant objects must remain distinct:

- **Component cashflows** are the input cashflows used to create a netting result.
- **Resultant cashflows** are produced by the netting process.
- **Component cashflow ID**, **component cashflow netting ID**, and **netting ID** may be separate fields; the source does not resolve their exact relationship.

## Proposed Common Pre-Check

When the component cashflow ID starts with `N` and the netting ID is populated, the proposed pre-check permits participation only when the payment type is `IRS Netting`:

```text
if component cashflow id starts with 'N'
   and netting id is not blank:
       payment type == 'IRS Netting' => pass
       otherwise => reject
```

This rule is proposed functional behavior, not confirmed production behavior. The meaning of the `N` prefix and the field identity used by the check require confirmation.

## Current and Target Support

`Bilateral Netting - Adhoc` is identified as the current supported route for further netting of `IRS Netting` cashflows. The source proposes:

- an exception for `Bilateral Netting - Manual`;
- exceptions and settlement-method inheritance for both CCIL manual variants;
- an exception and BIC-stamping review for `Ben BIC Netting - Manual`;
- confirmation for backlog capabilities, including `Bilateral Netting - Auto` and `CPN`.

The long-term objective is broader support as more `Stella` entities and products are onboarded. `Murex 2.11` booking is described as not problematic, whereas `Stella` booking is expected to be impacted.

## Netting-Key Context

The source uses different keys by process:

- Bilateral Netting: `Value Date/Currency/Entity FMID/Counterparty FMID`.
- CCIL Guaranteed Netting: `Value Date/Currency/Entity FMID/Counterparty FMID`.
- CCIL Non-Guaranteed Netting: `Value Date/Currency/Entity FMID`.
- Beneficiary BIC Netting: `Value Date/Currency/Entity FMID/Ben BIC`.

The IRS Netting auto key is `Value Date/Currency/Entity FMID/Counterparty FMID`. These differences must not be collapsed into a universal netting key.

## Resultant-Cashflow Attributes

For the proposed extensions:

- CCIL Guaranteed and Non-Guaranteed resultant cashflows should inherit settlement method from their component cashflows.
- Beneficiary BIC resultant cashflows require BIC stamping, with workflow-publication query behavior still to be checked.

See [[ccil-settlement-method-stamping]] and beneficiary bic based netting.

## Related Lifecycle Constraint

The source proposes that a pending netting cashflow cannot be un-netted by withdrawing a component, whether the withdrawal is manual or automatic. The exact state transition is unresolved; see [[netting-resultant-cashflow-lifecycle]] and what is the authoritative pending netting withdrawal behavior.

## Limitations and Open Questions

This concept should not be treated as an approved implementation specification until the following are resolved:

- field semantics for cashflow ID versus netting ID;
- exception precedence over blank-netting-ID rules;
- supported `Stella` entity and product scope;
- workflow behavior for BIC stamping;
- applicability to `NDS Fixing Netting`.