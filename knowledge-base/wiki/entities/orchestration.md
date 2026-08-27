---
type: entity
title: Orchestration
created: 2026-08-24
updated: 2026-08-23
tags: [orchestration, workflow, NSTP, cash-settlement, validation]
related: [hot-nstp-rule-exception-reconciliation, nstp-rules, rule-service, razor, cash-settlement-home-page, holding-release-precheck, configurable-mandatory-field-validation, what-is-the-authoritative-holding-release-verification-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Hot NSTP Rule Exception Generation.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Unresolved exception & mandatory field check.md"]
---
# Orchestration

## Role in Cash Settlement Processing

In the referenced Cash Settlement Home Page designs, orchestration controls or coordinates process flow around multiple exception checks and holding release. The designs describe two proposed areas of responsibility.

### Hot NSTP rule processing

The *Cash Settlement Hot NSTP Rule Exception Generation* source identifies orchestration as a development area for applying changed NSTP rules to cashflows already running in workflow.

The source implies that orchestration may coordinate the following activities:

1. Receive or detect an NSTP rule change.
2. Select cashflows that remain in workflow and have not been released to [[razor]].
3. Reevaluate those cashflows against the changed rule set.
4. Generate or remove exceptions accordingly.

These responsibilities are inferred from the stated requirement and are not confirmed by an implementation contract.

### Multiple exception check and holding release

The *Unresolved exception & mandatory field check* source requires orchestration to:

1. Add a verification step after the multiple exception check.
2. Run that verification before sending the process to holding release in diagram `1_6`.
3. Carry mandatory-field configuration in orchestration properties.

That source does not identify the implementation framework or define whether orchestration owns the validation logic itself or delegates it to another component.

## Configuration

The mandatory-field configuration is described only as configuration in orchestration properties. The source does not specify its syntax, field names, ownership, approval process, versioning, or runtime refresh behavior.

This design should therefore be treated as a proposed orchestration change, not as confirmation of an implemented contract. See [[what-is-the-authoritative-holding-release-verification-contract]].

## Open Design Responsibilities

The hot NSTP rule processing source does not specify:

- The event or API used to notify orchestration of an NSTP rule change.
- The cashflow selection query.
- Batching and pagination.
- Retries.
- Idempotency.
- Concurrency control.
- Reconciliation reporting.

Orchestration would also need to account for a race between hot-rule reevaluation and release to [[razor]]. The authoritative release status and the atomicity of the eligibility check remain unresolved.