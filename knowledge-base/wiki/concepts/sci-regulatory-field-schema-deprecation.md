---
type: concept
title: SCI Regulatory Field Schema Deprecation
tags: [sci, schema-deprecation, counterparty-data, regulatory-data, compatibility]
related: [sci, ratan, ratanone-data-ambassador, eue-notice-trade-validation-rule-dependency, which-ratan-consumers-use-smallbankexem-or-cftcclearingexemption]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Investigate SCI Response Data - eueNotice.md"]
---
# SCI Regulatory Field Schema Deprecation

SCI regulatory field schema deprecation is the removal or alteration of attributes under `legalEntity.doddFrankDetails` that are consumed by downstream services.

The investigated change removes `eueNotice` and `smallBankExem` and extends the list of values for `cftcClearingExemption`. A schema change must be assessed across field extraction, mapping, payload construction, rule evaluation, persistence, user interfaces, and fallback lookups.

The source demonstrates a specific downstream dependency for `eueNotice`, but it provides no consumption evidence for `smallBankExem` or `cftcClearingExemption`. Absence of evidence in this investigation is not proof that those attributes have no consumers.