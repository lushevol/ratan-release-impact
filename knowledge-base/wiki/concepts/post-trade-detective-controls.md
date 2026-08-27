---
type: concept
title: Post-Trade Detective Controls
tags: [post-trade, detective-controls, trade-validation, regulatory-compliance, ratan]
related: [ratan, apollo-rule-engine, trade-validation, post-trade-orchestration, what-is-the-authoritative-ratan-apollo-rule-engine-interface-contract]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN -Interfaces/RATAN and Apollo 51527.md"]
---
# Post-Trade Detective Controls

## Definition

Post-trade detective controls are controls intended to identify trade issues after trade capture or processing. In the source, these controls are a stated business purpose of the integration between [[entities/ratan]] and [[entities/apollo-rule-engine]].

## RATAN and Apollo Context

The documented flow uses Apollo Rule Engine to evaluate trade data against business requirements:

```text
RATAN --(API)--> Apollo Rule Engine
```

RATAN extracts the resulting rule response and saves it in an exception data store. This indicates a control pattern in which rule outcomes are retained for exception visibility, investigation, or remediation.

## Relationship to Regulatory Compliance

The source identifies regulatory compliance as a second business purpose. It does not specify the regulations, control objectives, evidence requirements, retention period, or reporting process. The compliance contribution should therefore be treated as a stated objective rather than a demonstrated outcome.

## Boundaries

This page does not establish that Apollo participates in the canonical NSTP exception platform, the RATAN rule-service lifecycle, or any specific cash-settlement filtering process. Those relationships require additional technical and operational evidence.

The broader relationship to [[concepts/post-trade-orchestration]] is conceptual; the source only documents the Apollo trade-validation flow.