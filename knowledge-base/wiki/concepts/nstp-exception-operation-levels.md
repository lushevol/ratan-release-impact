---
type: concept
title: NSTP Exception Operation Levels
created: 2026-08-24
updated: 2026-08-24
tags: [nstp, exception-management, maker-checker, workflow]
related: [nstp-exception-metadata, double-blind-exception-verification, ratanone-rule-service, ratan-rule-engine, what-is-the-authoritative-nstp-rule-and-exception-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Rule Service Technical Design.md"]
---
# NSTP Exception Operation Levels

NSTP exceptions are assigned one of three authorization models: maker only, checker only, or maker checker. The model determines the initial status, eligible actor, and closure path.

## Stated paths

- **Maker only:** starts at `PENDING_OPERATOR`; a successful maker submission changes it to `CLOSED`.
- **Checker only:** starts at `PENDING_VERIFICATION`; a successful checker approval changes it to `CLOSED`.
- **Maker checker:** starts at `PENDING_OPERATOR`; a maker fix changes it to `PENDING_VERIFICATION`; successful checker approval changes it to `CLOSED`.

These paths extend [[nstp-exception-metadata]] with explicit statuses and actor boundaries. They are a functional design statement for the Rule Service but do not prove implementation ownership by either [[ratanone-rule-service]] or [[ratan-rule-engine]].

## Boundaries and omissions

The source does not define transitions for rejection, rework, cancellation, expiry, failed approval, concurrent updates, or operational recovery. It also does not define the rule or configuration that selects an operation level for a particular exception category.

The unresolved complete lifecycle is tracked in [[what-is-the-authoritative-nstp-rule-and-exception-state-machine]].