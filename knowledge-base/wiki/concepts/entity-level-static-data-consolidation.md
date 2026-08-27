---
type: concept
title: Entity-Level Static Data Consolidation
created: 2026-08-24
updated: 2026-08-24
tags: [static-data, configuration, entity-onboarding, data-model, Cash Settlement]
related: [cash-settlement-entity-onboarding, cash-settlement-service-landscape, cash-settlement-shared-platform-architecture, static-data-service, ratan-static-cashflow-nostro]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Entity level static.md"]
---
# Entity-Level Static Data Consolidation

## Definition

Entity-level static data consolidation is the proposed practice of maintaining multiple booking-entity onboarding attributes through one shared configuration model instead of separately updating each consuming domain.

The source combines entity identifiers, workflow and LMS configuration, branch data, settlement-accounting parameters, and Swift BIC mappings in one proposed table.

## Scope of the proposal

The proposed attributes include:

- Booking Entity FMID and FMCODE.
- Workflow Flag.
- LMS Filter.
- Branch Code.
- Country and posting branch.
- Transaction type, debit, and credit codes.
- EBBS bridge account.
- Currency.
- Correspondent BIC and Sender BIC.

The source presents example values such as `300089409`, `SCB MNL FCD*MNL`, `PH`, `PHP`, and `SCBLPHMMXXX`. These should be treated as illustrative values unless independently confirmed.

## Potential benefits

Consolidation could:

- Reduce the number of manual onboarding updates.
- Provide a common validation point.
- Enable self-service maintenance.
- Reduce change-request dependency.
- Improve consistency between service configuration and entity reference data.
- Shorten onboarding lead time.

## Architectural alternatives

A “one table” proposal does not determine how the architecture must be implemented. Possible forms include:

1. A shared physical table read directly by multiple services.
2. A central static-data service exposing APIs.
3. A central source that publishes domain-specific projections.
4. An onboarding orchestration workflow that updates service-owned stores.

A central source with domain-specific projections may preserve service ownership while reducing repeated operational work, but the source does not evaluate these alternatives.

## Data-model concerns

The proposed fields have different cardinalities and semantics. Swift values may vary by currency, while accounting values may vary by country, posting branch, transaction type, or other combinations. Nostro values additionally depend on settlement means and settlement method.

The design must therefore establish whether the model is:

- One row per booking entity.
- One row per entity and currency.
- One row per entity and domain combination.
- A normalized set of domain tables.
- A typed key/value model.

A single entity identifier is unlikely to be sufficient for all proposed attributes.

## Governance and lifecycle

A consolidated model requires explicit governance for:

- Field-level ownership.
- Authoritative reference sources.
- Validation and referential integrity.
- Authorization and approval.
- Auditability and versioning.
- Effective dates.
- Rollback.
- Consumer synchronization and cache invalidation.
- Partial activation and failure recovery.

The proposed key/value extension for BIC netting static, FXU static, and Profile limit should remain a future consideration until these controls and type semantics are defined.

## Nostro Static exception

[[entities/ratan-static-cashflow-nostro]] remains outside the proposed consolidation. Because Nostro setup is mandatory, the onboarding workflow must coordinate the central entity record with the separate Nostro configuration.

## Related systems

The proposal spans [[entities/static-data-service]], [[entities/cashflow-blotter]], workflow, LMS, Swift Service, and Accounting service within the broader [[concepts/cash-settlement-service-landscape]].