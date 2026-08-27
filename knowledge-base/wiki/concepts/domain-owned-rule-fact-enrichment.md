---
type: concept
title: Domain-Owned Rule Fact Enrichment
created: 2026-08-24
updated: 2026-08-24
tags: [rule-engine, domain-services, fact-enrichment, architecture]
related: [ratan-rule-engine, json-based-rule-evaluation, cashflow-precheck-validation, cashflow-lifecycle-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]
---
# Domain-Owned Rule Fact Enrichment

## Definition

Domain-owned rule fact enrichment is the proposed architectural boundary in which domain services perform data retrieval, external lookups, transformations, and domain calculations before sending facts to a generic Rule Service.

The Rule Service retains predicate evaluation rather than owning domain-specific acquisition logic.

## Examples

The source proposes moving the following responsibilities out of RATAN:

- Holiday lookup by currency and date.
- Currency-rate retrieval and USD amount calculation.
- DA lookup using `Counterparty_SCI_FMID`.
- Booking-event and event-reason retrieval.
- Payment-date formatting and current-date comparison.

Generic comparisons, such as a threshold check or matching a value with `REFER` or `CORP`, may remain in the Rule Service.

## Benefits and risks

This boundary makes the Rule Service lighter and reduces central transformation logic. It also transfers transformation ownership, schema consistency, testing, and version coordination to every consuming domain service.

The source does not define a canonical JSON schema, enrichment ownership agreement, or validation SDK.