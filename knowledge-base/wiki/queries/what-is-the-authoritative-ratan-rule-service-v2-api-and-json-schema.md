---
type: query
title: What Is the Authoritative RATAN Rule Service v2 API and JSON Schema?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, api, json-schema, rule-engine]
related: [ratan-rule-engine, json-based-rule-evaluation, domain-owned-rule-fact-enrichment]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]
---
# What Is the Authoritative RATAN Rule Service v2 API and JSON Schema?

## Question

What API, JSON request schema, result schema, error model, field typing, and versioning policy govern RatanOne Rule Service v2?

## Evidence

The archived overview delegates API details to a separate “Rule Service Tech Design” v2 API series. It illustrates `businessFlow`, `ruleType`, `logicFacts`, and `additionalFacts`, but does not define them normatively.

## Why it matters

Consuming services need a stable contract for domain-owned enrichment, custom fact paths, matched-rule results, validation, and compatibility during v1 migration.