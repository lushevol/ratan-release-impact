---
type: entity
title: ratan_suppression_fields_xpath_v2
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, suppression, XPath, typed-data]
related: [suppression-field-data-type-parsing, ratanone-rule-service, schema-evolution-for-cash-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan-rule-service reconstruction for rule-engine.md"]
---
# `ratan_suppression_fields_xpath_v2`

`ratan_suppression_fields_xpath_v2` stores suppression-field names, XPath mappings, activation state, and the Ratan label used for configuration.

## Proposed `data_type` field

The design adds `data_type` with the documented values `Boolean`, `String`, `Date`, and `Numeric`. It controls how extracted values are interpreted. For example, `true` and `false` should be converted to Boolean values rather than treated as untyped strings.

The source does not specify coercion rules, invalid-value behavior, accepted-value enforcement, or backward compatibility for existing rows.