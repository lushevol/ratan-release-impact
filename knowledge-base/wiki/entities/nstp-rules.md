---
type: entity
title: NSTP Rules
created: 2026-08-24
updated: 2026-08-24
tags: [NSTP, rules, cash-settlement, workflow]
related: [hot-nstp-rule-exception-reconciliation, rule-service, razor-release-boundary-for-hot-rule-evaluation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Hot NSTP Rule Exception Generation.md"]
---
# NSTP Rules

## Role

NSTP rules are configurable business rules that determine whether cashflows in the Cash Settlement workflow require corresponding exceptions.

The source states that users can create or remove NSTP rules through a GUI while cashflows are already running in workflow. Those changes are expected to affect eligible cashflows that have not yet been released to Razor.

## Hot Changes

A newly created NSTP rule may require exceptions to be generated for already active, unreleased cashflows. Removing a rule may require corresponding exceptions to be removed or otherwise reconciled.

The source does not define whether rule removal is a hard delete, soft delete, deactivation, or version supersession. It also does not define rule effective dates, evaluation inputs, or rule-to-exception cardinality.

## Related Components

The requirement implies coordination between:

- The GUI, which initiates rule changes.
- [[rule-service]], which is a named development area and may own rule persistence or change propagation.
- [[orchestration]], which may identify and reevaluate affected cashflows.
- [[razor]], whose release boundary limits the eligible population.

See [[hot-nstp-rule-exception-reconciliation]] for the required processing behavior.