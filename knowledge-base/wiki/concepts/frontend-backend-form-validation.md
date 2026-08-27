---
type: concept
title: Frontend-Backend Form Validation
created: 2026-08-24
updated: 2026-08-24
tags: [ui, frontend, backend, forms, validation]
related: [ratan-ui-form, ratanone-ui-form-principles, where-are-ratanone-ui-validation-rules-authoritatively-maintained]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Design Principle/RATANONE UI Form Principles.md"]
---
# Frontend-Backend Form Validation

Frontend-backend form validation is the draft requirement that both layers validate a submitted [[ratan-ui-form]].

Frontend validation provides immediate feedback and can prevent avoidable submission attempts. Backend validation remains necessary as the authoritative boundary for submitted data and must not be omitted because frontend checks exist.

For the RATANONE UI-form scope, validation must also apply to mandatory fields that are disabled for editing. A disabled presentation state does not remove the field's validation requirement.

## Rule consistency

The source says that both layers should apply the same validation rules and that rules should be centrally maintained. It does not specify whether this means a shared rule definition, generated validators, a shared validation service, or duplicated implementations governed by a common specification.

No source evidence identifies [[ratanone-rule-service]] or [[ratan-rule-engine]] as the owner of these UI validation rules. The ownership and synchronization model remains open in [[where-are-ratanone-ui-validation-rules-authoritatively-maintained]].