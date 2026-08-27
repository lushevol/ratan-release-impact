---
type: source
title: RATANONE UI Form Principles
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, ui, forms, validation, draft]
related: [ratan-ui-form, ratanone-ui-form-principles, frontend-backend-form-validation, form-rendering-action-gating, where-are-ratanone-ui-validation-rules-authoritatively-maintained]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Design Principle/RATANONE UI Form Principles.md"]
authors: []
year: 2025
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/8414445"
venue: "Azure DevOps Story 8414445"
---
# RATANONE UI Form Principles

This draft design document defines UI-form principles for [[ratan-ui-form]] under Story 8414445, “[RATAN UI Form] Principles for UI form.”

## Status and scope

- **Status:** DRAFT
- **Recorded change:** 2025-05-12, “1. Draft”
- **Target release, owner, designer, developers, and QA:** Not specified

The document identifies observed form-behaviour issues but does not provide implementation design, acceptance criteria, reproduction steps, production metrics, or evidence of adoption. Its statements should therefore be treated as draft requirements.

## Reported issues

1. Some UI forms allow an action to be submitted before the entire page has rendered.
2. Mandatory-field validation does not take effect when a field is disabled for editing.
3. Validation may take effect only in the frontend or only in the backend, although both should apply the same validation rules.

## Draft principles

1. Actions are allowed only after form rendering is complete.
2. Both frontend and backend validate a submitted UI form.
3. UI-form validation applies whether fields are enabled or disabled.
4. Validation rules are centrally maintained.

These principles are summarized by [[ratanone-ui-form-principles]]. The rendering prerequisite is detailed in [[form-rendering-action-gating]], while the two-layer validation requirement is detailed in [[frontend-backend-form-validation]].

## Unspecified architecture

The document does not state:

- What conditions define completed form rendering.
- Which actions must be gated beyond submission.
- Which layer is authoritative when frontend and backend validation disagree.
- Where validation rules are maintained.
- How centrally maintained rules are distributed, generated, or consumed by both layers.
- How users or systems correct an invalid value in a disabled mandatory field.

The rule-ownership and synchronization question is tracked in [[where-are-ratanone-ui-validation-rules-authoritatively-maintained]].

## Related rule-maintenance material

Existing material on [[rule-maintenance-and-validation-pipeline]] may offer relevant context on rule maintenance. This source does not establish that [[ratanone-rule-service]] or [[ratan-rule-engine]] owns, serves, or executes RATANONE UI validation rules.