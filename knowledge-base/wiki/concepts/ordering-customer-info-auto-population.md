---
type: concept
title: Ordering Customer Information Auto-Population
created: 2026-08-23
updated: 2026-08-23
tags: [ordering-customer, auto-population, SSI, cash-settlement, MT210]
related: [ratan, sci, mt210, sci-counterparty-lookup, primary-nostro-fallback, ssi-stamping, adhoc-ssi-workflow, maker-checker-ssi-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto Populate Ordering Info for Notice to Receive Cashflow.md"]
---
# Ordering Customer Information Auto-Population

Ordering customer information auto-population is the SCI-based enrichment of RATAN settlement-instruction fields for specific SCB Receive cashflows.

## Eligibility Boundary

The feature is limited to cashflows that meet all of these conditions:

- SCB Receive.
- No vostro stamped and no SSI exception.
- `notice to receive = Y`.
- `paymentCurrency` is not `XAU`, `XAG`, `XPD`, or `XPT`.
- The unresolved `settlement means = NOS` condition must not be treated as authoritative until confirmed.

The feature applies to SSI auto stamping only. It does not change adhoc SSI behavior.

## Processing

1. Identify an eligible cashflow during the auto-stamping flow.
2. Classify the counterparty using the configured bank client-type list.
3. Query [[entities/sci]] using the bank or non-bank lookup strategy.
4. Map returned SCI data to RATAN ordering-customer fields.
5. Continue through maker-checker, release, and [[entities/mt210]] generation.

Bank counterparties use BIC-first processing. If a BIC is found, RATAN populates the ordering-customer BIC and account number. If no BIC is found, RATAN populates name, address, country, and account number. Non-bank counterparties use the name, address, country, and account-number path directly.

## Mapping

| RATAN target | SCI source and transformation |
|---|---|
| `Settlement_Instruction.Account.Ordering_Customer_BIC_Code` | `fmSysContact.addrLine` where `fmSystemContact.mediumCode="SWIFT"` and `mediumUsage="MAIN"` |
| `Settlement_Instruction.Account.Ordering_Customer_Account_Name` | `fmAccount.fmLongName` |
| `Settlement_Instruction.Account.Ordering_Customer_Street_Address` | `fmAddress.addressLine1 + " " + fmAddress.city` |
| `Settlement_Instruction.Account.Ordering_Customer_City` | `Convert(fmAddress.country)` |
| `Settlement_Instruction.Account.Ordering_Customer_Account_Number` | `Entity.Counterparty_SCI_FMID` |

The country-to-`Ordering_Customer_City` mapping requires clarification.

## Failure Behavior

If SCI returns no value or raises an exception, the requirement specifies that nothing is auto-populated. In the documented no-data acceptance case, the subsequent MT210 message is generated with an error.

The requirement does not define retries, observability, partial-field behavior, release blocking, or SSI-exception creation.