---
type: concept
title: Configurable Mandatory-Field Validation
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, validation, mandatory-fields, configuration, orchestration]
related: [orchestration, holding-release-precheck, cash-settlement-home-page, what-is-the-authoritative-holding-release-verification-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Unresolved exception & mandatory field check.md"]
---
# Configurable Mandatory-Field Validation

Configurable mandatory-field validation uses configuration to define required fields instead of relying exclusively on hard-coded validation rules.

## Cash Settlement Home Page design

The source requires mandatory-fields configuration to be added to orchestration properties. This configuration is intended to support the verification step inserted after the multiple exception check and before holding release.

No field names, data types, configuration keys, validation scope, or missing-value behavior are specified.

## Governance questions

The design does not state:

- Which team owns the configuration.
- Who approves changes.
- Whether configuration is versioned.
- How configuration is deployed.
- Whether it is loaded at startup or refreshed dynamically.
- Whether requirements vary by transaction, cashflow, product, or workflow type.

These details are part of the unresolved verification contract tracked in [[what-is-the-authoritative-holding-release-verification-contract]].
