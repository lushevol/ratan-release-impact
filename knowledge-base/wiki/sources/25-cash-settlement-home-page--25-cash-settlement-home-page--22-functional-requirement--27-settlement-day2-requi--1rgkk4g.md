---
type: source
title: SSI Selection Not Treated as Ad Hoc SSI — UAT
authors: []
year: 2026
url: "https://uklvadapp1342.uk.dev.net:8453/?show_normal_login=y"
venue: FMO Post Trade Portal UAT
created: 2026-08-23
updated: 2026-08-23
tags: [uat, ssi, settlement-instructions, adhoc-ssi, maker-checker, swift]
related: [fmo-post-trade-portal, ssi-selection-provenance-and-ad-hoc-classification, field-70-72-customization-and-reference-id, cashflow-amendment-maker-checker-control, pre-adhoc-error-and-adhoc-ssi-exception-lifecycle, what-is-the-authoritative-reference-id-and-ssi-id-contract-for-field-70-72-customization, why-can-checkers-select-an-incorrect-ssi-with-a-similar-financial-id]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI/SSI selection not treat as adhoc SSI - UAT.md"]
---
# SSI Selection Not Treated as Ad Hoc SSI — UAT

This UAT document records 19 maker/checker scenarios in the [[fmo-post-trade-portal]] for retaining the distinction between an SSI selected from available settlement instructions and manually entered settlement details.

## Evidence status

The document contains scenario narratives, test data, and screenshot references. Its formal **Test Result** and **Test Result After Adding Reference ID** columns are blank for all scenarios.

Scenarios 3, 6, 9, 12, 16, 17, and 18 are explicitly marked **Need to retest**. Consequently, the stated Reference ID design and much of the field-70/72 behaviour should be treated as intended or partially exercised behaviour, not confirmed acceptance evidence.

## UAT-derived behaviour

- Selecting an available SSI without further amendment populates SSI ID, whether an SSI was initially auto-stamped or not.
- Manually entering settlement details without selecting an SSI leaves SSI ID blank.
- Changing a settlement field other than SWIFT field 70 or 72 clears SSI ID. Evidence includes account number, settlement means, Address 2, and field 58 address.
- Returning a non-70/72 field to its original value does not restore SSI ID. The user must explicitly select the SSI again.
- Changing field 70 or 72 produces a persistent **Field 70/72 Customized** tag, including where the field is subsequently restored to its prior value.
- The post-change requirement says that field-70/72 customization must leave SSI ID blank and populate Reference ID. This requirement remains unverified.
- A checker who manually recreates values for an SSI selected by the maker receives a validation error; the checker must select the available SSI.
- Scenario 17 specifies a special, unverified checker view: after an auto-stamped SSI, maker SSI selection, and field-70/72 customization, the checker should be shown the originally stamped SSI identity or Reference ID rather than the maker-selected SSI identity.

## Scope and limitations

This source documents UI-level behaviour and does not identify persistence fields, APIs, or backend lifecycle states. SSI ID clearing may indicate ad hoc treatment, but the evidence does not establish transitions such as `PRE_ADHOC_ERROR` or `ADHOC_SSI_EXCEPTION`; see [[pre-adhoc-error-and-adhoc-ssi-exception-lifecycle]].

The source uses “SI” and “SSI” interchangeably. It does not formally define whether these labels are synonymous in the product.

## Selection ambiguity

In scenario 3, the checker selected SSI ID `00021922` instead of `40150418`, reportedly because both records had similar Financial IDs. The document does not determine whether this reflects an accepted workflow, a static-data issue, or a UI defect. See [[why-can-checkers-select-an-incorrect-ssi-with-a-similar-financial-id]].