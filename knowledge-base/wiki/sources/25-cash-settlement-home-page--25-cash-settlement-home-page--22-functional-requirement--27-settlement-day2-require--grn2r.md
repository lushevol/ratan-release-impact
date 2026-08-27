---
type: source
title: Cash Settlement Home Page — Cashflow Split Static
authors: []
year: 2025
url: ""
venue: "Cash Settlement Home Page functional requirement"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, cashflow-splitting, nstp, nds, auto-netting, static-configuration]
related: [cash-settlement-home-page, cashflow-splitting, split-cashflow-netting-exclusion, pending-nds-netting, nds-auto-netting, nostro-static, nostro-static-validation, what-is-the-precedence-between-split-nstp-rules, are-split-child-cashflows-excluded-from-all-netting-rules, was-cashflow-split-static-deployed, which-nostro-threshold-static-was-approved]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Split Static.md"]
---
# Cash Settlement Home Page — Cashflow Split Static

## Summary

This functional requirement proposes four new NSTP exception rules for cashflows associated with splitting events and updates the existing pending NDS auto-netting rule identified by `7350773637874561024`. The update excludes split child cashflows by requiring `Cashflow__Splitting_Id` to be null or empty.

The document describes requested configuration changes. It does not provide implementation evidence, approval history, test results, or confirmation that the rules were deployed.

## NSTP rules

| Action | Rule ID | Description | Rule Condition | Exception Code | Operation Level | Exception Category | Bulk Eligible | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| New | | NSTP rule for split child cashflow | `Cashflow__Splitting_Id != null && Cashflow__Splitting_Id != ""` | Split Cashflow | MAKER_CHECKER | NSTP | un-ticked | |
| New | | NSTP rule for amended split child cashflow | `Cashflow__Is_Split_Amend_Amount == true` | Split Amend | MAKER_CHECKER | NSTP | un-ticked | |
| New | | NSTP rule for unsplit cashflow | `Cashflow__Is_Cashflow_Unsplit == true` | Un-Split | MAKER_CHECKER | NSTP | un-ticked | |
| New | | NSTP rule for withdrawal event of split cashflow | `Cashflow__Is_Withdrawal_On_Split == true` | Withdrawal on Split | MAKER_CHECKER | NSTP | un-ticked | |
| Update | 7350773637874561024 | add condition to exclude split child from pending NDS auto netting rule | `Instrument_Common__Murex_Product_Typology in ("NDS", "NDCF", "NDFRA", "ND CDS Fixing", "ND CDS", "ND-Convert", "NDS Fixing") && Cashflow__ND_Parent_Typology != "NDIRS" && Cashflow__Cashflow_Event_Reason not in ("Reversal", "Rebook") && (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "") && ((Cashflow__Duplicate_NDS_FXD == null || Cashflow__Duplicate_NDS_FXD == "")) && (Cashflow__Splitting_Id == null || Cashflow__Splitting_Id == "")` | Pending NDS Netting | MAKER_CHECKER | NSTP | ticked | |

All four new rules are configured at `MAKER_CHECKER` operation level, belong to the `NSTP` exception category, and are not bulk eligible.

## Pending NDS netting change

The update is additive. Existing conditions remain in place:

- The product typology must be one of `NDS`, `NDCF`, `NDFRA`, `ND CDS Fixing`, `ND CDS`, `ND-Convert`, or `NDS Fixing`.
- `Cashflow__ND_Parent_Typology` must not be `NDIRS`.
- `Cashflow__Cashflow_Event_Reason` must not be `Reversal` or `Rebook`.
- `Cashflow__Netting_Id` must be null or empty.
- `Cashflow__Duplicate_NDS_FXD` must be null or empty.
- `Cashflow__Splitting_Id` must be null or empty.

The new condition narrows the pending NDS auto-netting rule. This source does not establish that split cashflows are excluded from every other netting process.

## Nostro threshold static

The document instructs the team to refer to the existing Nostro threshold static and obtain confirmation from Dinesh before onboarding the selected option. The supplied text does not identify the threshold values, unit, currency, scope, selected option, or confirmation outcome. The referenced image is not available as structured source content.

## Open implementation questions

The source does not specify precedence when a cashflow matches more than one split-related rule. It is also unclear whether all matching exceptions are created, whether one exception suppresses another, and how these exceptions interact with pending NDS netting processing.

See [[cashflow-splitting]], [[split-cashflow-netting-exclusion]], and the open questions [[what-is-the-precedence-between-split-nstp-rules]] and [[are-split-child-cashflows-excluded-from-all-netting-rules]].