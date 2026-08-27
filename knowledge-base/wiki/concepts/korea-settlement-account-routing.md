---
type: concept
title: Korea Settlement-Account Routing
created: 2026-08-23
updated: 2026-08-23
tags: [korea, settlement-account, routing, nostro, tis, ratan]
related: [ratan, tis, oltp, enisis, ssi-plus, korea-migration, ratan-tis-payment-query-integration, korea-tis-payment-type-classification, settlement-integration-static-data-readiness, nostro-static-data-governance, what-is-the-approved-korea-settlement-account-inventory-for-tis-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Ratan to TIS.md"]
---
# Korea Settlement-Account Routing

Korea settlement-account routing classifies cashflows for the RATAN-to-TIS interface using settlement means, account markers, payment direction, currency, beneficiary account, and beneficiary BIC.

## Account-marker routes

| Settlement means | Account marker | Direction | Route |
| --- | --- | --- | --- |
| `NOX` | `UISUS` | Pay | RATAN → TIS → OLTP(UI) |
| `NOX` | `UIBOK` | Pay | RATAN → TIS → OLTP(UI) |
| `NOX` | `UIDD` | Receive | RATAN → TIS → OLTP(UI) |
| `NOS` | `MAIN`, `KEBSEO`, `WRBSEO` | External client, FCY | SWIFT through [[enisis]] |
| `NOX` | `BOKSEO` | Client is Bank, KRW | Manual SSDR query and OLTP upload |

`UISUS`, `UIBOK`, and `UIDD` are routing markers embedded in `Settlement_Instruction.Account.SCB_Nostro_Account_Number`. They are prerequisites for selecting the pay-side or receipt API and for later UINO derivation.

## Classification controls

- `SCBLKR%` identifies a Korea SCB BIC route.
- A beneficiary account beginning with `BR%` is an internal-movement condition.
- A beneficiary account absent or equal to `dummy`, case-insensitively, is a BOK settlement condition for `UIBOK`.
- `KRW` and `KRO` are both recognized as Korean-currency values.
- External foreign-currency client flows outside `UISUS` and `UIBOK` remain outside TIS scope and use [[enisis]].

## Static-data dependency

Routing correctness depends on complete and governed account data, including the outstanding inventory for `KRO UISUS`, `KRO UIBOK`, and `CNH UISUS`, plus the Vostro migration to [[ssi-plus]]. The source does not establish that these prerequisites have been completed; see [[what-is-the-approved-korea-settlement-account-inventory-for-tis-routing]].

The documented filters also include `Settled` cashflows, while the routing matrix describes the TIS paths as `Released`; see [[are-settled-cashflows-intentionally-in-scope-for-korea-tis-query]].