---
type: source
title: CN Vostro Migration Analysis and Delivery Plan
authors: []
year: 2022
url: "https://confluence.global.standardchartered.com/display/DSP/Murex+2.11+Vostro+SSI"
venue: "Cash Settlement Home Page functional requirements"
tags: [vostro-ssi, murex-2-11, cn-entities, static-data, migration, cfi-code]
related: [murex-2-11, cn-entities, ssi-plus, ratan, cn-vostro-murex-211-ssi-migration, cfi-code-mapping-for-murex-vostro-ssi, ssi-plus-cfi-enrichment-and-republication, settlement-account-means-maintenance, should-ssi-plus-batch-updates-be-suppressed-to-murex-211]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/CN Vostro Migration Analysis & Delivery Plan.md"]
---

# CN Vostro Migration Analysis and Delivery Plan

## Summary

This document is an operational delivery plan for migrating and updating Vostro Settlement Standing Instructions associated with Murex 2.11 CN entities. It covers scope identification, security-to-CFI-code mapping, SSI+ enrichment and republication, settlement-account and means maintenance, downstream impact analysis, regression testing, SSI stamping validation, and production release preparation.

The plan is not a finalized functional specification. Several activities have no recorded status, owner, acceptance criteria, release date, or rollback procedure.

## Scope

The stated scope is:

- SSIs containing a Murex 2.11 security, with `SCBIRDIRS` given as an example.
- Alert SSIs for FX products are excluded.

The source does not provide the complete SSI inventory, CN legal-entity names, FM Codes, or a formal definition of the Murex 2.11 security and Alert SSI classifications.

## Delivery Plan

| Task | Details | Task Owner | Status | Comment |
| --- | --- | --- | --- | --- |
| In Scope SSI identification | 1. SSI with Murex 2.11 Security ( e.g. SCBIRDIRS) 2 Exclude the Alert SSI( For FX product) | Ratan | Done | |
| Murex 2.11 cashflow SSI distribution | 📎 [2022_Payments_SSI.xlsx](attachments/2022_Payments_SSI.xlsx) | Amy | Done | |
| Security to CFI Code mapping | To work with PO & Ops to decide the mapping | Ratan | In Progress | [Murex 2.11 Vostro SSI - Derivative Strategy Projects - Confluence (standardchartered.com)](https://confluence.global.standardchartered.com/display/DSP/Murex+2.11+Vostro+SSI) |
| SSI+ Security update with CFI Code | | TBC | | |
| SSI Republication to reflect the CFI | | TBC | | |
| Settlement Account/Means update | - Prepare the import spreadsheet & review with all users/PO - Testing the batch import in testing env | Ratan | | |
| Impact analysis of SSI & downstream | - To confirm if the updated CFI & Murex 2.11 SSI will impact any other downstream - To advise if the SSI batch updates can be suppressed to Murex 2.11 - Regression testing with these updated SSI | SSI+ | | |
| Impact analysis to Murex 2.11 BAU | - Analysis if there's any impact from change of settlement account/means - Regression testing with these updated SSI( Security/Settlement Account/Means) | Amy | | |
| SSI stamping testing | Run the SSI Stamping scenarios with the new updated SSI | Ratan | | |
| Release to prod | 1. Runbook & updating document/script. | Ratan/RTS | | |

## Recorded Status

The completed activities are in-scope SSI identification and distribution of the Murex 2.11 cashflow SSI workbook. Security-to-CFI-code mapping is recorded as in progress. The source does not record completion for SSI+ updates, SSI republication, settlement-account or means updates, impact analysis, regression testing, SSI stamping testing, or production release preparation.

## Dependencies and Open Issues

The mapping decision is a prerequisite for SSI+ security enrichment and SSI republication. The plan does not identify the authoritative mapping table, exception process, approval authority, or effective date.

The plan also asks whether SSI batch updates can be suppressed to Murex 2.11. It does not establish whether suppression is technically possible, temporary, or intended as a steady-state integration rule.

Settlement-account and means maintenance requires an import spreadsheet, user and Product Owner review, and batch-import testing in a test environment. The source does not define the canonical fields, permitted values, validation rules, effectivity rules, or rollback process.

## Validation and Release

The plan requires downstream and Murex 2.11 BAU impact analysis, regression testing using updated SSI data, SSI stamping scenario testing, and production runbook preparation. It provides no test scenario inventory, expected results, sign-off owner, production deployment date, reconciliation procedure, or rollback plan.

## Related Wiki Pages

- [[concepts/cfi-code-mapping-for-murex-vostro-ssi]]
- [[entities/ssi-plus]]
- [[entities/ratan]]
- [[concepts/vostro-data-sourcing-from-ssi-plus]]
- [[concepts/nostro-stamping]]
- [[projects/cn-vostro-murex-211-ssi-migration]]
---

---FILE: wiki/entities/murex-2-11.md---
---
type: entity
title: Murex 2.11
tags: [murex, trading-platform, vostro-ssi, cash-settlement]
related: [cn-entities, cn-vostro-murex-211-ssi-migration, cfi-code-mapping-for-murex-vostro-ssi, ssi-plus]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/CN Vostro Migration Analysis & Delivery Plan.md"]
---

# Murex 2.11

Murex 2.11 is the platform used in the source to define part of the CN Vostro SSI migration population. SSIs containing a Murex 2.11 security are in scope, while Alert SSIs for FX products are explicitly excluded.

`SCBIRDIRS` is provided as an example of a Murex 2.11 security identifier. The source does not provide a complete security inventory or define the full classification rule.

## Migration Relevance

Murex 2.11 security identifiers require mapping to CFI codes before the planned [[concepts/ssi-plus-cfi-enrichment-and-republication]]. The plan also calls for analysis of downstream effects and Murex 2.11 BAU impact resulting from changes to security, settlement-account, and means data.

The source leaves unresolved whether SSI batch updates should be suppressed from reaching Murex 2.11. This is tracked in [[queries/should-ssi-plus-batch-updates-be-suppressed-to-murex-211]].
---

---FILE: wiki/entities/cn-entities.md---
---
type: entity
title: CN Entities
tags: [cn-entities, legal-entities, fm-code, vostro-ssi, static-data]
related: [murex-2-11, cn-vostro-murex-211-ssi-migration]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/CN Vostro Migration Analysis & Delivery Plan.md"]
---

# CN Entities

CN entities are the legal-entity population associated with the Murex 2.11 Vostro SSI migration described in the source.

The plan begins by requesting identification of each legal entity name and FM Code, but it does not provide those names or codes. No complete CN-entity inventory can therefore be derived from this source.

## Scope Role

The relevant CN-entity SSIs are those containing Murex 2.11 securities, subject to exclusion of Alert SSIs for FX products. The authoritative entity list and FM-Code mapping remain open questions.
---

---FILE: wiki/concepts/ssi-plus-cfi-enrichment-and-republication.md---
---
type: concept
title: SSI+ CFI Enrichment and Republication
tags: [ssi-plus, cfi-code, security-enrichment, republication, vostro-ssi, static-data]
related: [ssi-plus, cfi-code-mapping-for-murex-vostro-ssi, vostro-data-sourcing-from-ssi-plus, murex-2-11, cn-vostro-murex-211-ssi-migration]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/CN Vostro Migration Analysis & Delivery Plan.md"]
---

# SSI+ CFI Enrichment and Republication

SSI+ CFI enrichment and republication is the planned sequence of updating SSI+ security records with approved CFI codes and republishing affected SSIs so consumers receive the revised static data.

## Planned Dependency Chain

The source implies the following sequence:

1. Decide the security-to-CFI-code mapping.
2. Update SSI+ security data with the CFI code.
3. Republish affected SSIs.
4. Assess downstream and Murex 2.11 BAU impact.
5. Run regression and SSI stamping tests.
6. Prepare and execute the production release.

The mapping activity is assigned to Ratan with PO and Ops and is marked in progress. SSI+ enrichment and SSI republication have no assigned owner or recorded status in the source.

## Unspecified Controls

The source does not define the authoritative mapping dataset, data contract, update trigger, republication mechanism, consumer acknowledgement, exception handling, or approval criteria. These details must not be inferred as implemented behavior.
---

---FILE: wiki/concepts/settlement-account-means-maintenance.md---
---
type: concept
title: Settlement Account and Means Maintenance
tags: [settlement-account, means, static-data, batch-import, vostro-ssi, migration]
related: [cn-vostro-murex-211-ssi-migration, ssi-plus, murex-2-11]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/CN Vostro Migration Analysis & Delivery Plan.md"]
---

# Settlement Account and Means Maintenance

Settlement-account and means maintenance is the planned update of settlement-account and “means” data for the CN Vostro SSI migration.

## Planned Process

Ratan is assigned to:

- Prepare an import spreadsheet.
- Review the spreadsheet with users and the Product Owner.
- Test the batch import in a test environment.

The source does not state whether this work has started or completed.

## Data-Model Gaps

The source does not define canonical field names, source-of-truth ownership, allowed means values, validation rules, effective-date behavior, downstream propagation, reconciliation, or rollback procedures. Murex 2.11 BAU impact from security, settlement-account, and means changes is a separate planned analysis assigned to Amy.
---

---FILE: wiki/projects/cn-vostro-murex-211-ssi-migration.md---
---
type: project
title: CN Vostro Murex 2.11 SSI Migration
status: planned
owner: Ratan
start_date: ""
target_date: ""
tags: [vostro-ssi, murex-2-11, cn-entities, static-data, migration, release]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--11-static-data--10-vostro--yvzdhs, murex-2-11, cn-entities, ssi-plus, cfi-code-mapping-for-murex-vostro-ssi, ssi-plus-cfi-enrichment-and-republication, settlement-account-means-maintenance]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/CN Vostro Migration Analysis & Delivery Plan.md"]
---

# CN Vostro Murex 2.11 SSI Migration

## Objective

Migrate and update Vostro SSIs associated with Murex 2.11 CN entities, enrich security data with approved CFI codes, update settlement-account and means data, validate downstream behavior, and prepare the production release.

## Scope

The planned population consists of SSIs containing Murex 2.11 securities. Alert SSIs for FX products are excluded. The complete CN legal-entity and FM-Code inventory is not present in the source.

## Workstreams

- Identify and distribute the in-scope SSI population.
- Decide the security-to-CFI-code mapping.
- Update SSI+ security data and republish affected SSIs.
- Prepare and test settlement-account and means import data.
- Assess downstream and Murex 2.11 BAU impact.
- Execute regression and SSI stamping tests.
- Prepare the production runbook and supporting document or script updates.

## Status

Scope identification and Murex 2.11 cashflow SSI distribution are marked done. Security-to-CFI mapping is in progress. Remaining work has no recorded status in the source, and SSI+ enrichment and republication have no named owner.

## Gates and Risks

The critical dependency is an approved security-to-CFI mapping. Release readiness also depends on defined regression scenarios, expected SSI stamping outcomes, downstream impact analysis, production validation, and rollback controls.

The intended propagation behavior between SSI+, downstream consumers, and Murex 2.11 remains unresolved. See [[queries/should-ssi-plus-batch-updates-be-suppressed-to-murex-211]].
---

---FILE: wiki/queries/what-are-the-cn-entity-fm-codes-for-murex-211-vostro-ssi-migration.md---
---
type: query
title: What Are the CN Entity FM Codes for Murex 2.11 Vostro SSI Migration?
tags: [open-question, cn-entities, fm-code, murex-2-11, vostro-ssi]
related: [cn-entities, murex-2-11, cn-vostro-murex-211-ssi-migration]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/CN Vostro Migration Analysis & Delivery Plan.md"]
---

# What Are the CN Entity FM Codes for Murex 2.11 Vostro SSI Migration?

The source requests identification of the legal-entity names and FM Codes for the CN entities in scope, but supplies neither the names nor the codes.

## Required Resolution

Identify the authoritative CN-entity inventory and record:

- Legal entity name.
- FM Code.
- Relationship to Murex 2.11.
- Confirmation that the entity is included in the Vostro SSI migration population.

This information is needed to make the SSI scope auditable.
---

---FILE: wiki/queries/what-is-the-approved-security-to-cfi-code-mapping-for-murex-211-vostro-ssis.md---
---
type: query
title: What Is the Approved Security-to-CFI-Code Mapping for Murex 2.11 Vostro SSIs?
tags: [open-question, cfi-code, security-mapping, murex-2-11, vostro-ssi, governance]
related: [murex-2-11, cn-vostro-murex-211-ssi-migration, cfi-code-mapping-for-murex-vostro-ssi, ssi-plus-cfi-enrichment-and-republication]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/CN Vostro Migration Analysis & Delivery Plan.md"]
---

# What Is the Approved Security-to-CFI-Code Mapping for Murex 2.11 Vostro SSIs?

Security-to-CFI-code mapping is recorded as in progress and is to be decided with PO and Ops. The source does not provide mapping values, authoritative source data, exceptions, or approval evidence.

## Required Resolution

Establish the approved mapping table, decision authority, exception rules, version or effective date, and sign-off evidence before SSI+ security enrichment and SSI republication proceed.

The existing [[concepts/cfi-code-mapping-for-murex-vostro-ssi]] provides related context but does not resolve this migration-specific question.
---

---FILE: wiki/queries/should-ssi-plus-batch-updates-be-suppressed-to-murex-211.md---
---
type: query
title: Should SSI+ Batch Updates Be Suppressed to Murex 2.11?
tags: [open-question, ssi-plus, murex-2-11, batch-update, downstream-impact, integration]
related: [ssi-plus, murex-2-11, cn-vostro-murex-211-ssi-migration, ssi-plus-cfi-enrichment-and-republication]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/CN Vostro Migration Analysis & Delivery Plan.md"]
---

# Should SSI+ Batch Updates Be Suppressed to Murex 2.11?

The migration plan asks SSI+ to determine whether batch SSI updates can be suppressed to Murex 2.11. It does not state that suppression is required, possible, or implemented.

## Required Resolution

Determine:

- Whether SSI+ updates are expected to propagate to Murex 2.11.
- Which downstream consumers require the enriched CFI and SSI data.
- Whether suppression is technically feasible.
- Whether suppression would be temporary migration control or steady-state behavior.
- How propagation or suppression would be tested, monitored, reconciled, and reversed.

This question should be resolved before production release planning is finalized.
---

---FILE: wiki/queries/what-are-the-cn-vostro-ssi-stamping-regression-scenarios-and-acceptance-criteria.md---
---
type: query
title: What Are the CN Vostro SSI Stamping Regression Scenarios and Acceptance Criteria?
tags: [open-question, ssi-stamping, regression-testing, vostro-ssi, murex-2-11, release-readiness]
related: [cn-vostro-murex-211-ssi-migration, murex-2-11, ssi-selection-as-non-adhoc-ssi, ssi-refresh-exception-lifecycle, nostro-stamping]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/CN Vostro Migration Analysis & Delivery Plan.md"]
---

# What Are the CN Vostro SSI Stamping Regression Scenarios and Acceptance Criteria?

The plan requires SSI stamping scenarios using the updated SSI population and regression testing for security, settlement-account, and means changes. It provides no scenario inventory, expected stamped fields, test data, system coverage, approver, or definition of done.

## Required Resolution

Define the regression matrix, including:

- In-scope Murex 2.11 securities and excluded Alert SSIs.
- CFI-enriched SSI behavior.
- Settlement-account and means changes.
- Downstream propagation or suppression behavior.
- Expected SSI stamping outcomes.
- Negative and exception scenarios.
- Evidence and sign-off required for production release.

Existing SSI-stamping pages provide related context but do not establish the CN Vostro migration acceptance criteria.
---

---FILE: wiki/log.md---
## 2026-08-24 ingest | CN Vostro Migration Analysis and Delivery Plan

- Ingested the CN Vostro migration delivery plan as a source summary.
- Recorded the Murex 2.11 and CN-entity scope, SSI+ CFI-enrichment dependency, settlement-account and means maintenance work, unresolved batch-update propagation question, and testing and release gaps.
- Added related entity, concept, project, and query pages.