---
type: source
title: Cashflow Filter Enhancement
authors: []
year: 2025
url: ""
venue: ""
tags: [cash-settlement, cashflow-blotter, functional-requirement, ktlo, ui-enhancement]
related: [cashflow-blotter, cash-settlement-home-page, cashflow-blotter-filter-rationalization, alphabetical-custom-search-view-ordering, deprecated-functional-requirements]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/KTLO Requirement/9244022-Cashflow filter enhancement.md"]
---
# Cashflow Filter Enhancement

## Scope

This KTLO requirement concerns the **Custom Search/View** dropdown in the Cashflow Blotter, within the [[entities/cash-settlement-home-page]] functional area.

The source proposes two user-interface changes:

1. Remove filters that are not utilized.
2. Sort filters and views alphabetically.

The requirement does not define changes to cashflow processing, settlement status, accounting, or upstream and downstream integrations.

## Requirements

### Remove unutilized filters

The source states that the Custom Search/View dropdown contains many filters and that some are not utilized. It proposes removing those filters.

The specific filter-removal scope is not defined. The source explicitly records the following dependency:

> TBC: Ask PO to provide the unutilized filters list then we can remove them

No individual filter should therefore be treated as approved for removal based on this document alone.

### Alphabetical ordering

The source requires the filters and views to be sorted alphabetically. It does not specify:

- the locale or collation rules;
- case sensitivity;
- treatment of numbers, punctuation, or symbols;
- whether system, shared, and user-created views are sorted together or separately;
- whether the ordering must remain stable after a view is created, renamed, edited, or shared.

## Evidence and limitations

The referenced attachment, `image-2025-7-4_15-55-3.png`, illustrates the current dropdown but does not establish an authoritative inventory of filters or views.

The source provides no usage data, technical identifiers, role-specific scope, permission model, saved-search compatibility assessment, or rollback plan. The removal requirement is consequently not implementation-ready until Product Owner input is obtained.

## Related documentation

The current requirement should remain separate from the deprecated [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--15-deprecated-docs--18-c--11740pp]] and should not inherit current behavior from that historical document without validation. See [[concepts/deprecated-functional-requirements]] and [[queries/which-cash-settlement-requirement-documents-are-authoritative-after-deprecation]].