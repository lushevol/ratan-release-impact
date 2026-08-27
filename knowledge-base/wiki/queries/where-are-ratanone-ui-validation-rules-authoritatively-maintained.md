---
type: query
title: Where Are RATANONE UI Validation Rules Authoritatively Maintained?
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, ui, validation, rule-management, architecture]
related: [ratanone-ui-form-principles, frontend-backend-form-validation, ratan-ui-form, rule-maintenance-and-validation-pipeline]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Design Principle/RATANONE UI Form Principles.md"]
---
# Where Are RATANONE UI Validation Rules Authoritatively Maintained?

The draft [[ratanone-ui-form-principles]] requires validation rules to be centrally maintained while requiring both frontend and backend validation. It does not identify the authoritative store, rule owner, rule representation, or synchronization method.

## Questions to resolve

- Is there one shared rule definition consumed by frontend and backend?
- Are validators generated for each layer from a common definition?
- Does one layer expose a validation service used by the other?
- If separate implementations exist, which layer is authoritative when results differ?
- How are rules versioned by form, workflow state, role, or release?
- How are disabled mandatory fields supplied, validated, and corrected when invalid?

## Scope caution

[[rule-maintenance-and-validation-pipeline]] is relevant background, but the available source does not establish that [[ratanone-rule-service]] or [[ratan-rule-engine]] owns the UI validation-rule contract.