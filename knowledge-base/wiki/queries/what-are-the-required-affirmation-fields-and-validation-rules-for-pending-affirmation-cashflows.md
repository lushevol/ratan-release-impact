---
type: query
title: What Are the Required Affirmation Fields and Validation Rules for Pending Affirmation Cashflows?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, pending-affirmation, validation, maker-checker, audit]
related: [pending-affirmation-bulk-processing, bulk-cashflow-exception-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Processing for Multi Exception Demo.md"]
---
# What Are the Required Affirmation Fields and Validation Rules for Pending Affirmation Cashflows?

The requirement states that users manually enter affirmation details for selected `Pending Affirmation` cashflows and that those details apply only to the relevant cashflows. It does not define the information model or controls.

## Questions

- Which affirmation fields are required, optional, or conditionally required?
- What format, reference-data, and cross-field validations apply?
- Can mixed selections contain different affirmation values per cashflow?
- Are maker-entered details visible to the checker, and may the checker amend them?
- What audit history records data entry, amendment, approval, and rejection?
- How are affirmation details retained when a bulk operation partially succeeds or is retried?

See [[pending-affirmation-bulk-processing]].