---
type: source
title: Cash Settlement Hot NSTP Rule Exception Generation
authors: []
year: 2023
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, NSTP, exceptions, Razor, workflow]
related: [hot-nstp-rule-exception-reconciliation, razor-release-boundary-for-hot-rule-evaluation, nstp-rules, orchestration, rule-service, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Hot NSTP Rule Exception Generation.md"]
---
# Cash Settlement Hot NSTP Rule Exception Generation

## Summary

This design note describes a requirement for applying newly created or removed [[nstp-rules]] to cashflows that are already running in workflow but have not yet been released to [[razor]]. The expected result is dynamic generation or removal of the corresponding exceptions.

The requirement implies a flow across the GUI, [[rule-service]], and [[orchestration]], but the source does not define the implementation responsibilities or interfaces for those components.

## Stated Requirement

When cashflows are in workflow, a user may create or remove NSTP rules through the GUI. The system should apply those rule changes to cashflows that have not yet been released to Razor and should generate or remove exceptions accordingly.

The source does not specify:

- The NSTP rule data model or evaluation criteria.
- The authoritative status indicating release to Razor.
- The exception identity, lifecycle, or provenance model.
- Whether rule changes are propagated synchronously or asynchronously.
- The selection, batching, retry, or reconciliation strategy.
- The behavior when Razor release races with rule evaluation.
- The handling of manual exception changes or multiple applicable rules.

## Implied Processing Flow

1. A user creates or removes an NSTP rule through the GUI.
2. The rule change is persisted or exposed by Rule Service.
3. Orchestration identifies cashflows that remain in workflow and have not been released to Razor.
4. Eligible cashflows are evaluated against the changed rule set.
5. Exceptions are generated for newly applicable rules and removed or otherwise reconciled when rules no longer apply.

This flow is an interpretation of the requirement rather than a confirmed implementation design.

## Development Sections

The source contains headings for the following development areas, but no detailed content:

- GUI
- Rule Service
- Orchestration

## System Integration

The source references an image at `attachments/image2023-3-24_13-53-37.png`. The image contents are not transcribed in the available source text, so no component topology or integration contract can be confirmed from it.

## Design Implications

The central safeguard is the [[razor-release-boundary-for-hot-rule-evaluation]]: hot NSTP-rule processing must not modify cashflows after they have been released to Razor.

The create and remove paths require distinct reconciliation semantics. In particular, removal should be attributable to the relevant rule and should not incorrectly remove an exception still supported by another active rule or modified manually.

A production design would also need idempotency, rule versioning or ordering, auditability, bounded bulk processing, retry handling, and reconciliation after partial failure. These are design implications, not specifications supplied by the source.