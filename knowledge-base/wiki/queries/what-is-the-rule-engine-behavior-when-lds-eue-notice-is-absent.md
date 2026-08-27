---
type: query
title: What Is the Rule Engine Behavior When Lds_Eue_Notice Is Absent?
tags: [ratan, rule-engine, eue-notice, schema-change, trade-validation]
related: [ratanone-rule-service, ratanone-trade-service, eue-notice-trade-validation-rule-dependency, sci-regulatory-field-schema-deprecation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Investigate SCI Response Data - eueNotice.md"]
---
# What Is the Rule Engine Behavior When Lds_Eue_Notice Is Absent?

## Question

Does [[ratanone-rule-service]] evaluate an omitted `Lds_Eue_Notice` field identically to a present `null` field when applying `Lds_Eue_Notice != "Y"`?

## Evidence

The supplied validation payload contains `Lds_Eue_Notice: null`, while two active `TRADE_VALIDATION` / `FO_SUPERVISION` rules evaluate the field. SCI plans to remove the upstream `eueNotice` attribute.

## Required resolution

Run controlled validation cases with `Lds_Eue_Notice` present as `null`, omitted, set to `"Y"`, and set to a non-`"Y"` value. Record rule outcomes, errors, fallback calls to `ratan_scbml_field_rest_config`, and behavior by validation API version.