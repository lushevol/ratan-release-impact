---
type: comparison
title: Frontend Code Configuration versus Ratan Static Config Service
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, frontend, static-configuration, architecture]
related: [mfe-cashflow-blotter, ratan-static-data-service, static-data-service, static-configuration-management, declarative-ui-configuration, configuration-dependencies]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft)/Static Code In UI.md"]
---
# Frontend Code Configuration versus Ratan Static Config Service

## Current Frontend Code Model

`mfe-cashflow-blotter` stores reference values, UI metadata, query fields, workflow-related status lists, and executable callbacks in source code.

**Strengths:** implementation and behavior are versioned with the frontend release; functions are trusted and locally testable.

**Limitations:** operational changes require code deployment; configuration is dispersed across modules; auditability and maker-checker governance are limited.

## Centralized Data-Only Model

A static configuration service stores only data such as booking entities, labels, status lists, page sizes, field metadata, and filter definitions.

**Strengths:** managed updates, auditability, centralized ownership, and potential regional scoping.

**Limitations:** it cannot represent existing date functions, comparators, style callbacks, or component implementations without redesign. It also introduces runtime availability and version-skew risks.

## Declarative Hybrid Model

A configuration service stores typed, versioned declarative values and references trusted frontend registries for selectable behavior. The frontend owns implementations for functions, components, complex workflow decisions, and security-sensitive action logic.

**Strengths:** preserves the code security boundary while centralizing suitable data; allows schema validation, dependency checking, maker-checker publication, and rollback.

**Limitations:** requires maintained schemas, allow-listed identifiers, compatibility testing, and explicit dependency management.

## Assessment

The source inventory supports the declarative hybrid model. The design must preserve frontend/backend operator and field-name contracts and resolve the default date-horizon inconsistency before configuration is centralized.