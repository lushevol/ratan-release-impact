---
type: source
title: FMRP China Cash Settlement Delivery Plan — 2023 Q2 Demo 1
authors: []
year: 2023
url: "https://fmo-mfe.uk.dev.net:8453/"
venue: "FMRP China Cash Settlement delivery plan and QA/demo acceptance record"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, netting, settlement-exceptions, q2-2023, fmrp-china, qa-demo]
related: [fmrp-china-cash-settlement, fmo-post-trade-portal, client-level-cashflow-netting, irs-auto-netting, hold-and-un-hold, manual-failure-and-reinstatement, settle-as-gross, adhoc-settlement-instructions, cashflow-status-and-substate-model, which-currency-code-is-valid-for-netting-eligibility, which-cashflow-identifiers-are-authoritative-in-the-q2-demo]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md"]
---

# FMRP China Cash Settlement Delivery Plan — 2023 Q2 Demo 1

## Scope

This source records a Q2 2023 product delivery plan and demonstration of six cash-settlement functions in the [[fmo-post-trade-portal]]:

1. Client-level netting
2. Hold and un-hold
3. IRS auto netting
4. Manual failure and reinstatement
5. Settle as gross
6. Adhoc SSI

The upstream test flow describes trades being booked in [[blade]], cashflows being sent by [[stella]] to [[ratan]], and operators using the FMO Post Trade Portal cashflow blotter.

## Netting eligibility rule

The source provides the following rule. The value `CNO` is preserved exactly as documented; it differs from the `CNY` values used in test scenarios and requires validation.

| Attribute | Operator | Value |
| --- | --- | --- |
| Entity.Booking_Entity_SCI_FMID | IN | 10036642,400899993 |
| Cashflow.Payment_Currency | IN | CNO,USD |
| Entity.Counterparty_SCI_FMID | IN | 10032025,400054708 |
| Instrument_Common.CFI_Code | == | SESXXX |
| Cashflow.Netting_Id | == | 10036642,300068459 |

## Functional results

### Client-level netting

Eligible cashflows can be selected from the cashflow blotter and processed with **Net Selected Cashflow**, followed by **Netting All Cashflow** and an affirmation step.

The stated result is that component cashflows change to `Netted` and resultant cashflows are created in `Queued`–`Waiting`. Mixed-currency selections are grouped by currency. A group with enough eligible cashflows may net while a currency group containing only one cashflow remains unnetted and in `Waiting`.

### IRS auto netting

For an IRS with value date before `T+2`, the fixed and floating legs are automatically netted. The source states that both component legs become `Netted` with `Sub State Type` `NA`. The resultant cashflow is `Queued`–`Waiting` with `Sub State Type` `Pending Exception`.

The source also demonstrates a later netting operation on two IRS-generated resultant cashflows. In that scenario, four underlying component cashflows become `Netted`, the two prior auto-netting resultants become `Dead`, and a new resultant cashflow becomes `Waiting`.

These lifecycle results apply to the IRS scenarios and should not be generalized to every netting operation.

### Hold and un-hold

Operators can select `Waiting` and `Ready` cashflows, choose **Hold**, enter a comment, and submit. The selected cashflows become `Hold`.

The **Un-Hold** action also requires a comment. The source states that the cashflows return to their respective prior states: `Waiting` and `Ready`.

### Manual failure and reinstatement

A `Waiting` or `Ready` cashflow can be manually moved to `Failed` through the **Failed** action and a comments window. A failed `Ready` cashflow can subsequently be reinstated. The original failure comment persists, a reinstatement comment is collected, and the cashflow returns to `Queued` for processing.

### Settle as gross

**Settle as Gross** is available for cashflows with `Sub State Type` `Pending Netting` and for cashflows with `pending another leg`. After the operator enters a comment and submits, the cashflow changes to `Queued` and the stated observed `Sub State Type` becomes `NA`.

The scenario wording also mentions `Pending Exception` as a possible result. The source does not specify the conditions that would produce `NA` versus `Pending Exception`.

### Adhoc SSI

For eligible `Waiting` cashflows without an SSI Exception and for `Ready` cashflows, the details page provides an **Adhoc SI** button in the `Vostro SI Information` and `Nostro SI Information` areas. After the operator enters and submits the settlement information, the cashflow substate becomes `Pending Verification`.

## Consolidated result matrix

| Function | Input condition | User action | Stated result |
| --- | --- | --- | --- |
| Client-level netting | Multiple eligible cashflows across currencies | Select cashflows → **Net Selected Cashflow** → **Netting All Cashflow** | Components become `Netted`; resultant cashflows become `Queued`–`Waiting` |
| Mixed-currency netting with a single cashflow in one currency | One currency group has only one cashflow | Select three cashflows and submit netting | One currency group nets; another does not; resultant cashflow is `Queued`–`Waiting` |
| Post-IRS netting | Two IRS resultant cashflows | Select and affirm netting | Four component cashflows become `Netted`; two auto-netting cashflows become `Dead`; new resultant becomes `Waiting` |
| Hold | Cashflows in `Waiting` and `Ready` | **Hold**, enter comment, submit | Cashflows become `Hold` |
| Un-hold | Held cashflows | **Un-Hold**, enter comment, submit | Cashflows return to `Waiting` and `Ready` |
| IRS auto netting | Fixed and floating legs, `VD < T+2` | Automatic system processing | Legs become `Netted`/`NA`; resultant is `Queued`–`Waiting`/`Pending Exception` |
| Manual failure | Cashflow in `Waiting` or `Ready` | **Failed**, enter comment, submit | Cashflow becomes `Failed` |
| Reinstate | Failed cashflow | **Reinstate**, submit | Cashflow becomes `Queued` and can be processed again |
| Settle as gross | Cashflow in `Pending Netting` or `pending another leg` | **Settle as Gross**, enter comment, submit | Cashflow becomes `Queued`; subtype becomes `NA` in the stated result |
| Adhoc SSI | `Waiting` without SSI Exception or `Ready` | Open details → **Adhoc SI** → enter Vostro/Nostro information | Substate becomes `Pending Verification` |

## Source limitations and discrepancies

The document is useful evidence of demonstrated UI behavior, but it is not a complete auditable test report. It does not provide execution dates, tester names, approval records, build or environment versions, defect identifiers, formal pass/fail labels, or complete trade-to-cashflow mappings.

Scenario identifiers also conflict with identifiers in several expected-result sections. Examples include differences between the `8192550531xx` scenario IDs and expected-result IDs in the `8192550522xx` range. IRS IDs use `N00000000xxx` values in addition to `81925505xxxx` values.

Terminology is not fully normalized. The source uses `Sub State Type`, `sub status type`, `sub status`, and `Sub State`, as well as variations such as `Failed`/`Faild`, `Adhoc SSI`/`Adhoc SI`, and `Un-hold`/`Un-Hold`.

The source includes screenshot references under `attachments/`, but the screenshots are corroborating evidence rather than reproducible execution records.

## Open validation items

- Confirm whether `CNO` is a valid payment-currency code or a documentation error for `CNY`.
- Reconcile scenario cashflow IDs with expected-result cashflow IDs.
- Define the authoritative meanings and transitions of `Queued`, `Waiting`, `Ready`, `Hold`, `Netted`, `Dead`, and `Failed`.
- Clarify when **Settle as Gross** produces `NA` versus `Pending Exception`.
- Document the NSTP criteria and exception-handling procedures that are left blank in the source table.
- Confirm which system owns the authoritative cashflow lifecycle.
