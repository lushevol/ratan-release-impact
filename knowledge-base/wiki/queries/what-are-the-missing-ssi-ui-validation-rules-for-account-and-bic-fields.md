---
type: query
title: What Are the Missing SSI UI Validation Rules for Account and BIC Fields?
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, ui-validation, validation-gaps, bic, account-fields]
related: [ssi-ui-form-validation, covered-payment-ui-enforcement, ssi-validation-rule-for-ui-form, ssi-stamping-notification]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Validation Rule for UI Form.md"]
---

# What Are the Missing SSI UI Validation Rules for Account and BIC Fields?

## Question

What are the authoritative length, character-set, and regular-expression rules for the following SSI form fields?

- `accountWithInstitutionAccount`
- `intermediaryAccount`
- `orderCustomerBic`
- `receiversCorrespondentAccount`

## Evidence

The source marks all three validation dimensions as `??` for these fields. It defines requiredness for `accountWithInstitutionAccount` when `swiftType = MT103` and `tradingCurrency = RUB`, but provides no format contract. The other three fields have no documented requiredness or format rule in this source.

The missing definitions prevent confident implementation and may produce inconsistent front-end and back-end behavior.

## Resolution Needed

The owning team should confirm:

1. Whether each field is an account, BIC, or free-form identifier.
2. Maximum and minimum lengths.
3. Permitted characters and whitespace behavior.
4. Whether the UI and API use the same validation.
5. Whether SWIFT field-specific constraints override the generic UI rules.

Until resolved, the `??` entries should remain unresolved rather than being inferred from neighboring fields.