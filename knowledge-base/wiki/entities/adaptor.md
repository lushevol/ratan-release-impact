---
type: entity
title: Adaptor
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, integration-component, Murex]
related: [cashflow-status-write-back, backward-workflow-design, murex-2-11, mxg-adaptor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Backward Workflow Design.md"]
---
# Adaptor

## Role

Adaptor is the generic integration component shown between Ratan and Murex2.11 in the backward workflow:

```text
Ratan → Adaptor → Murex2.11
```

The source provides a Ratan-to-Adaptor payload but does not identify the Adaptor by product name, service name, deployment, or repository.

## Contract Boundary

The Adaptor-to-Murex behavior is defined by reference to Section 2 of an external `CN Settlement - Murex2.11 Technical Design` Confluence page. The supplied source does not specify how the Adaptor transforms, validates, acknowledges, retries, or forwards the Ratan payload.

This generic entity must not be assumed to be the same component as [[mxg-adaptor]] without confirmation.
