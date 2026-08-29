---
type: source
title: Beneficiary BIC Netting
authors: []
year: 2025
url: ""
venue: Cash Settlement Home Page Functional Requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, beneficiary-bic, acceptance-criteria, manual-netting]
related: [beneficiary-bic-netting, netting-key-eligibility, netting-static-blotter, netting-resultant-cashflow, bic-netting-un-netting, automatic-un-netting-on-trade-market-events, is-ac-006-a-bilateral-netting-case-misfiled-under-beneficiary-bic-netting, what-is-the-complete-component-cashflow-state-model-after-withdrawal-of-a-released-or-settled-resultant, what-is-the-authoritative-netting-key-and-bic-netting-preview-error-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/03 Beneficiary BIC Netting.md"]
---
# Beneficiary BIC Netting

This requirements document specifies acceptance criteria for manual Beneficiary BIC Netting in the Cash Settlement Home Page. A live manual rule places qualifying cashflows in `WAITING` with sub-state `Pending Netting`. Users select eligible cashflows through `BIC Net Selected Cashflow` and `Net All Cashflows`.

Successful Beneficiary BIC Netting is expected to transition components to `NETTED` and create a resultant such as `N1` or `N2`. The resultant must have the correct amount, payment type `Ben BIC Netting`, and completed NSTP processing with `MAKER_CHECKER`. Operations then release the resultant from [[ratan]].

## Active acceptance criteria

| AC-NO | Function | Scenario | Expected result |
| --- | --- | --- | --- |
| AC-Settlement-Manual Netting-001 | Beneficiary BIC Netting | Create a manual netting rule in the netting static blotter. Book C1 from [[murex]] and C2 from stella with the same Counterparty BIC and matching rule conditions. Select `BIC Net Selected Cashflow`, then `Net All Cashflows`. Operations release the cashflow. | The manual rule is live. C1 and C2 are `WAITING` / `Pending Netting`. C1 and C2 become `NETTED`; N1 is generated with correct amount, payment type `Ben BIC Netting`, and NSTP complete (`MAKER_CHECKER`). |
| AC-Settlement-Manual Netting-002 | Beneficiary BIC Netting - Un-Net | Create a manual rule and book matching C1 and C2. Net them using `BIC Net Selected Cashflow` and `Net All Cashflows`. Select N1 and use `Un-Net Cashflow` followed by `Un-Net all Cashflow`. Re-net C1 and C2. | N1 becomes `DEAD`. C1 and C2 return to `WAITING` / `Pending Netting`. Re-netting creates N2 with correct amount, payment type `Ben BIC Netting`, and NSTP complete (`MAKER_CHECKER`). |
| AC-Settlement-Manual Netting-003 | Beneficiary BIC Netting - Different Netting key | Create a manual rule and book C1 and C2 that meet the rule but have different Booking Entity, Currency, or Value Date. Select `BIC Net Selected Cashflow`. | The manual rule is live and C1/C2 are `WAITING` / `Pending Netting`. The system shows `Cashflow Netting Preview Can not Netting`; the source states that there is no UI warning like CCIL. |
| AC-Settlement-Manual Netting-004 | Withdrawal before netting | Create a manual rule and book C1, C2, and C3. Withdraw C1. Net C2 and C3 using `BIC Net Selected Cashflow` and `Net All Cashflows`. Release the resultant. | C1 becomes `CANCELLED`. C2 and C3 become `NETTED`; N1 is generated with correct amount, payment type `Ben BIC Netting`, and NSTP complete (`MAKER_CHECKER`). N1 is released from Ratan. |
| AC-Settlement-Manual Netting-005 | Withdrawal after netting - Resultant cashflow state != `SETTLED` or `RELEASED` | Create a manual rule and book C1, C2, and C3. Net all three. Withdraw C1. Net C2 and C3. Release the new resultant. | The system automatically un-nets N1: N1 becomes `DEAD`; C1 becomes `CANCELLED`; C2 and C3 return to `WAITING` / `Pending Netting`. Re-netting C2 and C3 creates N2 with correct amount, payment type `Ben BIC Netting`, and NSTP complete (`MAKER_CHECKER`). N2 is released from Ratan. |
| AC-Settlement-Manual Netting-006 | Withdrawal after netting - Resultant cashflow state = `SETTLED` or `RELEASED` | Create a manual rule and book C1, C2, and C3. In the cashflow blotter, use `Net Selected Cashflow`, `Net All Cashflows With Affirmation`, and Submit. Release the cashflow. Withdraw C1. | The source expects N1 to have affirmation status `Affirmed`, payment type `Bilateral Netting`, and NSTP complete (`MAKER_CHECKER`). N1 remains `SETTLED` or `RELEASED`; C1 becomes `WAITING`; C2 remains `NETTED`. C3 is not specified. This scenario conflicts with the Beneficiary BIC Netting actions and resultant type in the other criteria. |
| AC-Settlement-Manual Netting-007 | Pending Netting - Manual Fail-Reinstate | Create a manual rule and book C1, C2, and C3. Apply `Manual Fail` then `Reinstate` to C1. Net all components. | C1 transitions from `FAIL` / `NA` to `WAITING` / `Pending Netting`. C1, C2, and C3 can then be netted into N1 with payment type `Ben BIC Netting` and NSTP complete (`MAKER_CHECKER`). |
| AC-Settlement-Manual Netting-008 | Pending Netting - Settle As Gross | Create a manual rule and book C1, C2, and C3. Apply `Settle As Gross` to C1. Net C2 and C3. | C1 remains `WAITING` but moves to `Pending Exception`, with settlement method `Gross`. C2 and C3 become `NETTED`; N1 is generated with payment type `Ben BIC Netting` and NSTP complete (`MAKER_CHECKER`). |
| AC-Settlement-Manual Netting-009 | Pending Netting - Hold-Unhold | Create a manual rule and book C1, C2, and C3. Apply `Hold`, then `Unhold`, then net all components. | The components move from `WAITING` / `Pending Netting` to `Hold` / `NA`, then return to `WAITING` / `Pending Netting`. They can then be netted into N1 with payment type `Ben BIC Netting` and NSTP complete (`MAKER_CHECKER`). |
| AC-Settlement-Manual Netting-010 | Pending Netting - Swift Suppression | Create a manual rule and book C1, C2, and C3. Apply `Swift Suppression`. A checker rejects the request. Net all components. | Components move from `WAITING` / `Pending Netting` to `WAITING` / `Swift Suppression`, then return to `WAITING` / `Pending Netting` after rejection. They can be netted into N1 with payment type `Ben BIC Netting` and NSTP complete (`MAKER_CHECKER`). |
| AC-Settlement-Manual Netting-011 | Pending Netting - Suppress Cashflow | Create a manual rule and book C1, C2, and C3. Apply `Suppress Cashflow`. A checker rejects `Confirm Suppression`. Net all components. | Components move from `WAITING` / `Pending Netting` to `WAITING` / `Cashflow Suppression`, then return to `WAITING` / `Pending Netting` after rejection. They can be netted into N1 with payment type `Ben BIC Netting` and NSTP complete (`MAKER_CHECKER`). |

## Deprecated acceptance criteria

| AC-NO | Function | Deprecated expected behaviour |
| --- | --- | --- |
| ~~AC-Settlement-Manual Netting-006~~ | ~~Manual Netting Refresh - Disable/Update existing rule~~ | ~~Disabling or updating a live manual netting rule would cause C1, C2, and C3 to no longer have sub-state `Pending Netting`.~~ |
| ~~AC-Settlement-Manual Netting-012~~ | ~~Beneficiary BIC Rule > Bilateral Rule~~ | ~~A Beneficiary BIC Rule with `BIC_Net_Flag=Y` was proposed to take precedence over a Bilateral Rule based on booking entity and counterparty.~~ |

The struck-through criteria are historical only and are not evidence of current behaviour.

## Open issues

- AC-006 uses Bilateral Netting actions and expects a `Bilateral Netting` payment type despite being labelled as a Beneficiary BIC Netting scenario. See is ac 006 a bilateral netting case misfiled under beneficiary bic netting.
- The post-withdrawal state of C3, the sub-state of C1, and later eligibility after a released or settled resultant are unspecified. See what is the complete component cashflow state model after withdrawal of a released or settled resultant.
- The listed netting-key fields and the preview popup contract are incomplete. See what is the authoritative netting key and bic netting preview error contract.