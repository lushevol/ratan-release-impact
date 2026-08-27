---
type: concept
title: Razor Release Boundary for Hot Rule Evaluation
created: 2026-08-24
updated: 2026-08-24
tags: [Razor, release-boundary, NSTP, cashflows, workflow]
related: [hot-nstp-rule-exception-reconciliation, razor, nstp-rules, release-time-cashflow-status-gating]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Hot NSTP Rule Exception Generation.md"]
---
# Razor Release Boundary for Hot Rule Evaluation

## Definition

The Razor release boundary is the eligibility constraint that limits hot NSTP-rule application to cashflows that have not yet been released to Razor.

It is the primary lifecycle safeguard in the source: once a cashflow has crossed the Razor release boundary, a later NSTP rule create or remove operation should not apply to that cashflow under this requirement.

## Enforcement Questions

The source does not define:

- The authoritative release status or field.
- The service that owns the status transition.
- Whether the eligibility check is enforced in Rule Service, Orchestration, the database query, or multiple layers.
- Whether eligibility evaluation and exception mutation are atomic with Razor release.
- The recovery behavior when release and rule reconciliation race.

These details are necessary to prevent a hot-rule process from modifying a cashflow after downstream dispatch.

## Scope

This concept is specific to the NSTP/Razor requirement. It is related to the broader [[release-time-cashflow-status-gating]] pattern, but existing controls for other workflows or systems must not be assumed to define the Razor contract.