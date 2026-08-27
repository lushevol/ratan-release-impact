---
type: concept
title: Suppression Field Data-Type Parsing
created: 2026-08-24
updated: 2026-08-24
tags: [suppression, typed-data, XPath, schema-evolution]
related: [ratan-suppression-fields-xpath-v2, ratanone-rule-service, schema-evolution-for-cash-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan-rule-service reconstruction for rule-engine.md"]
---
# Suppression Field Data-Type Parsing

Suppression-field extraction should interpret values according to the `data_type` configured in `ratan_suppression_fields_xpath_v2`.

The proposed types are:

- `Boolean`
- `String`
- `Date`
- `Numeric`

For example, textual `true` and `false` values should be converted to Boolean values. The design does not define invalid-value handling, date formats, numeric precision, null semantics, or whether parsing failures reject the rule evaluation or produce an untyped value.