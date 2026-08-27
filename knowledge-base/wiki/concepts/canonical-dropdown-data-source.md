---
type: concept
title: Canonical Dropdown Data Source
created: 2026-08-24
updated: 2026-08-24
tags: [ui, dropdowns, canonical-data, source-of-truth, reference-data]
related: [ui-dropdown-data-source-governance, ratan-ui-dropdown-data-source, static-configuration-management, centralized-static-configuration-management]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Dropdown Data Source.md"]
---
# Canonical Dropdown Data Source

A canonical dropdown data source is the authoritative owner of an option set and its business semantics. It is not necessarily the same component or API that renders the options in a UI.

## Scope

For each option set, the owning contract should define:

- Stable code or identifier
- Display label and localization behavior
- Active or retired status
- Effective dates, where applicable
- Entitlement rules
- Ordering and filtering semantics
- Versioning and compatibility expectations
- Update and approval responsibilities

## Cash Settlement Context

The [[ratan-ui-dropdown-data-source]] document asks for a “Proper Data Source” for many Cash Settlement dropdowns but does not define the term or populate the field. It therefore does not establish whether a given option set belongs to [[entities/static-data-service]], [[entities/ratan-static-data-service]], a configuration domain, or an operational service.

Potentially configuration-oriented entries include Settlement Methods/Settlement Means, Nostro Static, and Bic Net Flag. State and exception entries may instead depend on operational domain contracts. These are hypotheses for validation, not conclusions from the source.