---
type: query
title: What Is the Authoritative RATAN Rule Service API and Schema Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, rule-service, api-contract, database-schema, archived-design]
related: [ratan-rule, ratan-drools-rule, ratan-drools-fact-processor, rule-governance-and-auditability, what-replaced-the-archived-ratan-rule-engine-design]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Tech Design.md"]/Rule Service Tech Design.md"]/Rule Service Tech Design.md"]
---
# What Is the Authoritative RATAN Rule Service API and Schema Contract?

The archived design documents `/v2/rules` maintenance and validation endpoints plus three proposed database tables. It is insufficient as an authoritative contract because it contains conflicting and incomplete details.

## Known ambiguities

- `NOT_EXECUTED` appears in URLs, while `NOT_EXECUTION` is listed as a supported value.
- `needDryRunFlag` is used in request parameters, while `needDryRun` appears in responses.
- `DELETE_PEDING` appears as a status value.
- A `SAVE_CONFIRMED` transition example returns `CREATING`.
- Several routes do not state an HTTP method.
- `SETTLEMENT1` appears in examples although documented business flows are `CONFIRMATION`, `SETTLEMENT`, and `SETTLEMENT_AUTO_NETTING`.
- The `ratan_drools_rule` index refers to `business_workflow`, but the table documents `business_flow`.
- The `ratan_rule` requirement that either `rule` or `fact_processor` be non-null has no stated enforcement mechanism.

## Evidence needed

- Current OpenAPI definitions or gateway route configuration.
- Current migration files and database DDL.
- The deployed status enum and transition guards.
- Authentication, authorization, backward-compatibility, and payload-versioning policies.
- Confirmation of whether the archived service was deployed, superseded, or retired.