---
type: concept
title: SSI UI Form Validation
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, ui-validation, conditional-validation, cash-settlement, vostro, nostro]
related: [ssi-stamping-notification, cash-settlement-home-page, covered-payment-ui-enforcement, nostro-account-scope, what-are-the-missing-ssi-ui-validation-rules-for-account-and-bic-fields, what-is-the-authoritative-ssi-settlement-means-taxonomy-and-validation-regex-contract, what-is-the-authoritative-popdubai-visibility-and-reset-behavior]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Validation Rule for UI Form.md"]
---

# SSI UI Form Validation

SSI UI form validation is the set of requiredness, length, character-set, enumeration, and behavioral rules applied to SSI-related payment fields in the [[entities/cash-settlement-home-page]].

## Validation Model

The form does not use one static required-field set. Requiredness depends on payment context, including:

- `swiftType`
- `tradingCurrency`
- `settlementMeans`
- `coveredPayment`
- entity FMID
- settlement-account content
- beneficiary identity fields

The principal Vostro requirements are:

- `settlementAccount`, `settlementMeans`, `ssiType`, and `swiftType` are always mandatory.
- `accountWithInstitutionAccount` is mandatory for MT103 with RUB trading currency.
- `beneficiaryAccount` is mandatory for MT103, and for MT202 when `settlementMeans = Over-Account`.
- For MT202, either `beneficiaryBic` or `beneficiaryName` is required, with each becoming mandatory when the other is empty.
- `ebbsNostroAccount` is mandatory in the Nostro scope.

Requiredness is separate from format validation. A pattern such as `^.{0,20}$` can accept an empty value even when a separate mandatory rule prohibits emptiness.

## Field Validation

The source defines:

- Upper-case alphanumeric BIC-like values with lengths of 8 or 11 characters.
- Alphanumeric-and-space fields with limits such as 35, 50, 60, 70, or 90 characters.
- Enumerated values for `charges`, `settlementMeans`, `ssiType`, `swiftType`, `coveredPayment`, and `isThirdPartyPayment`.
- Free-form patterns for remittance-information and sender-to-receiver lines.

The source explicitly leaves the length and format of `accountWithInstitutionAccount`, `intermediaryAccount`, `orderCustomerBic`, and `receiversCorrespondentAccount` unspecified.

## Conditional UI Behavior

Two rules go beyond ordinary field validation:

1. [[covered-payment-ui-enforcement]] synchronizes Covered Payment with the receiver’s-correspondent BIC for MT103 payments using `NOS`.
2. `popDubai` is displayed and mandatory only for a Dubai-specific condition involving MT103, entity FMID 5, a non-AED currency, `NOS`, a settlement account containing `MAIN`, and a beneficiary BIC other than `SUPPRESSXXX`.

The source does not define backend enforcement, persistence behavior, SWIFT-message generation, or the reset behavior of fields that become hidden.

## Risks and Ambiguities

The supplied enumeration regexes use alternation without consistently grouping the complete expression. This may allow partial matches in conventional regex engines even though the prose says that only exact values are allowed.

The source also maps several “Country” labels to identifiers containing `City` or `Postcode`. These may be legacy identifiers, but the document does not establish the intended API or domain semantics.

The relationship between `NOS`, `Nostro`, `NOSCENT`, and `Non-Nostro` is unresolved. See [[queries/what-is-the-authoritative-ssi-settlement-means-taxonomy-and-validation-regex-contract]].