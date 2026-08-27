---
type: query
title: Which RATAN Consumers Use smallBankExem or cftcClearingExemption?
tags: [ratan, sci, counterparty-data, schema-change, impact-assessment]
related: [sci, ratan, sci-regulatory-field-schema-deprecation, ratanone-data-ambassador]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Investigate SCI Response Data - eueNotice.md"]
---
# Which RATAN Consumers Use smallBankExem or cftcClearingExemption?

## Question

Which RATAN services, rules, databases, GraphQL clients, or user interfaces consume `smallBankExem` or `cftcClearingExemption`?

## Evidence

SCI plans to remove `smallBankExem` and add list-of-values entries for `cftcClearingExemption`. The investigation documents field-level evidence only for `eueNotice`; it does not provide a code search, rule search, payload evidence, or consumer inventory for the other attributes.

## Required resolution

Search source code, rule-engine records, API schemas, database mappings, and frontend fragments for both attribute names and their downstream aliases. Validate whether new CFTC values are compatible with existing validation and persistence constraints.