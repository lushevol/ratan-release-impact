---
type: source
title: Auto Populate Ordering Information for Notice to Receive Cashflow
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, RATAN, SSI, SCI, MT210, functional-requirement]
related: [ratan, sci, mt210, ordering-customer-info-auto-population, sci-counterparty-lookup, primary-nostro-fallback, ssi-stamping, adhoc-ssi-workflow, maker-checker-ssi-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto Populate Ordering Info for Notice to Receive Cashflow.md"]
---
# Auto Populate Ordering Information for Notice to Receive Cashflow

## Summary

This functional requirement defines SCI-based auto-population of ordering-customer information for eligible SCB Receive cashflows in RATAN. The change addresses a gap created when no vostro is available and RATAN automatically selects the primary nostro. If the cashflow has `notice to receive = Y`, MT210 generation may require ordering-customer information that is not present in the selected primary-nostro instruction.

The change applies only to SSI auto stamping and has no impact on adhoc SSI.

## Eligibility

The auto-population logic applies when all of the following conditions are met:

1. The cashflow is an SCB Receive cashflow.
2. No vostro is stamped, with no SSI exception.
3. `notice to receive = Y`.
4. `paymentCurrency` is not one of `XAU`, `XAG`, `XPD`, or `XPT`.
5. The proposed `settlement means = NOS` condition remains unresolved. The source records that Dinesh will check and confirm this condition.

## SCI Lookup Logic

For counterparties classified as banks, RATAN first queries SCI for a BIC. When a BIC is available, RATAN populates the ordering-customer BIC and account number. When no BIC is available, RATAN retrieves the ordering-customer name, address, country, and account number.

For non-bank counterparties, RATAN retrieves the ordering-customer name, address, country, and account number directly.

If SCI returns no value or an exception occurs, no ordering-customer fields are auto-populated.

The bank client-type list specified by the source is:

```text
Cient_Type in ('BANK','MULTDEV','INTEBCH','FININST','HDGEFND','INTLACC','INTECOM','INTDESK','FUNDMGR','CENTBK','OSEASBK')
```

The source uses `Cient_Type`; the acceptance criteria use `Client Type`. The authoritative field name requires confirmation.

## Field Mapping

| RATAN field | Logic Model | Source Field in SCI |
|---|---|---|
| Ordering customer BIC | `Settlement_Instruction.Account.Ordering_Customer_BIC_Code` | `fmSysContact.addrLine` where `fmSystemContact.mediumCode="SWIFT"` and `mediumUsage="MAIN"` |
| Ordering customer name | `Settlement_Instruction.Account.Ordering_Customer_Account_Name` | `fmAccount.fmLongName` |
| Ordering customer address | `Settlement_Instruction.Account.Ordering_Customer_Street_Address` | `fmAddress.addressLine1 + " " + fmAddress.city` |
| Ordering customer Country | `Settlement_Instruction.Account.Ordering_Customer_City` | `Convert(fmAddress.country)` |
| Order customer account number | `Settlement_Instruction.Account.Ordering_Customer_Account_Number` | `Entity.Counterparty_SCI_FMID` |

The country mapping is semantically ambiguous because `fmAddress.country` is mapped to a target field named `Ordering_Customer_City`.

## Business User Cases

| AC-No | Scenario | Expected result |
|---|---|---|
| `AC-Settlement-AutoPopulate-001` | Bank client type with a BIC in SCI | After maker-checker moves the cashflow to `READY` and the cashflow is released from RATAN, the ordering-customer BIC and account number are populated and the SWIFT MT210 message is generated successfully. |
| `AC-Settlement-AutoPopulate-002` | Bank client type without a BIC in SCI | After release, the ordering-customer name, address, country, and account number are populated and the SWIFT MT210 message is generated successfully. |
| `AC-Settlement-AutoPopulate-003` | Non-bank client type | After release, the ordering-customer name, address, country, and account number are populated and the SWIFT MT210 message is generated successfully. |
| `AC-Settlement-AutoPopulate-004` | No SCI value exists | No ordering-customer information is auto-populated and the SWIFT MT210 message is generated with an error. |

## Scope and Limitations

The requirement establishes a functional relationship between [[concepts/primary-nostro-fallback]], [[concepts/ssi-stamping]], [[entities/sci]], and [[entities/mt210]]. It does not define SCI API details, retry behavior, exception logging, alerting, partial-data handling, release blocking, or the exact timing of enrichment relative to initial stamping, maker-checker, and release.

The document is a functional specification rather than evidence of production behavior. Its acceptance cases describe expected outcomes but do not provide implementation or test evidence.

## Open Questions

- Is `settlement means = NOS` required?
- Is `Ordering_Customer_City` the correct target for converted country data?
- Is `Cient_Type` a documentation typo for `Client_Type`?
- How should partial SCI responses be handled?
- What are the timeout, retry, logging, and alerting requirements for SCI?
- Does SCI failure create an SSI exception, or only result in an MT210 error?
- Should existing ordering-customer fields be overwritten during re-stamping?