---
type: query
title: What Is the Authoritative Auto Versus Manual Exception Resolution Attribute?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, exceptions, resolution, automation, audit]
related: [high-value-exception-dependency, multi-exception-resolution-handling, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--16-multi-exceptions--38--1pgj0j1]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/High Value Exception Scenario Analysis.md"]
---
# What Is the Authoritative Auto Versus Manual Exception Resolution Attribute?

The High Value rule requires different outcomes for automatic resolution and manual resolution, but the source lists the technical parameter for “Exception Auto/Manually resolved” as `TBD`.

## Required Definition

Establish the authoritative:

- Source system and event carrying resolution origin.
- Field name and permitted values.
- Transition semantics for automatic, Maker, and Checker resolution.
- Persistence and audit-history requirements.
- Behavior for retried, replayed, or corrected resolution events.

Without this attribute, the system cannot reliably decide whether to auto-remove High Value, retain it for Checker, or apply multi-exception closure behavior.