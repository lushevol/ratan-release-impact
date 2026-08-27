---
type: concept
title: CCIL Guaranteed and Non-Guaranteed Netting
created: 2026-08-22
updated: 2026-08-22
tags: [CCIL, netting, guaranteed, non-guaranteed, IRS, Ratan]
related: [ccil, ratan, bilateral-netting, ad-hoc-cashflow-netting, ccil-settlement-method-stamping, cashflow-logical-model, swift-versus-cashflow-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CCIL Netting.md"]
---
# CCIL Guaranteed and Non-Guaranteed Netting

## Definition

CCIL netting separates eligible Indian IRS cashflows into guaranteed and non-guaranteed populations.

- **Guaranteed CCIL cashflows** are cleared and novated to the CCIL central counterparty. They are identified by `Settlement Method = CCIL` and counterparty FMID `400021949`.
- **Non-guaranteed CCIL cashflows** are not cleared and retain their original counterparties, but are operationally netted to a resultant facing CCIL. They are identified by `Settlement Method = CCIL`, `Cashflow Status = WAITING`, `Cashflow_Sub_State_Type = Pending Netting`, and a counterparty FMID other than `400021949`.

## Netting Paths

Guaranteed cashflows use Ratan's existing **Bilateral Netting** action. Non-guaranteed cashflows use the new **CCIL Netting(Non Guaranteed)** action. Both populations must be held as NSTP and be separately filterable in the GUI and backend.

A non-guaranteed cashflow can be removed from the netting population through `Settle as Gross`. The source requires an additional exception and four-eye validation; this is an ad hoc exception rather than a separate netting category.

## Resultant

The resultant faces CCIL central counterparty FMID `400021949` and shortcode `CCIL/MMB`. For the manually created non-guaranteed resultant, `Settlement_Method` and `Delivery_Method` are both configured as `CASH`, the cashflow ID is `N` plus 11 numeric characters, and the netting ID is a UUID. Other attributes are copied from the first selected cashflow.

SWIFT generation is bypassed for the resultant, but accounting remains required.

## Boundary and Limitation

FMID `400021949` is central to the guaranteed classification, but it may not be sufficient by itself. The source explicitly excludes Cash and Bond flows booked with the same FMID from netting with guaranteed IRS flows. The exact product, family, group, typology, and currency predicate remains unresolved; see [[what-exactly-excludes-non-ccil-flows-booked-with-ccil-fmid-from-guaranteed-netting]].