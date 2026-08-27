---
type: query
title: What Is the Authoritative Murex FlowStatus-to-SCBML State Mapping?
created: 2026-08-24
updated: 2026-08-24
tags: [flow-status, lifecycle, scbml, murex-211, open-question]
related: [murex-payment-mxml-to-scbml-transformation, cashflow-lifecycle-state-model, scbml-cashflow-payload, murex-211]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - MxML mapping to SCBML.md"]
---
# What Is the Authoritative Murex FlowStatus-to-SCBML State Mapping?

## Question

What complete conversion table maps Murex `flowStatus` values to SCBML workflow states?

## Current evidence

The source maps:

- Murex `/MxPayML/flowStatus = CHCK`
- SCBML state = `PROJECTED`

The field description mentions Queued, Pending, Released, Settled, validation states, and Failed. A nested flow example uses status `SNTR`.

No complete conversion matrix or state ownership rule is provided.

## Required resolution

Document the authoritative mapping for at least:

- `SNTR`.
- `CHCK`.
- Queued.
- Pending.
- Released.
- Settled.
- Failed.
- To-be-validated and validated states.

Also define behavior for unknown, missing, or conflicting status values.