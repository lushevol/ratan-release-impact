---
type: query
title: What Is the Lifecycle STP/NSTP and lastUser API Contract?
tags: [open-question, lifecycle, stp, nstp, api, lastuser]
related: [high-value-payment-control-technical-architecture, ratan, what-is-the-authoritative-high-value-payment-decision-rule]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/High Value Payment Control - RATAN/HVP Tech Design.md"]
---
# What Is the Lifecycle STP/NSTP and lastUser API Contract?

Orchestration service must obtain STP/NSTP information and `lastUser` from an internal Lifecycle service API after parsing `cashflowId` and `businessVersion`.

## Information needed

Define the API's:

- request and response schemas;
- meaning and allowable values of STP/NSTP information;
- `businessVersion` lookup semantics;
- `lastUser` provenance and privacy controls;
- authentication and authorization model;
- timeout, retry, error, and unavailable-service behavior;
- consistency and versioning guarantees.

The source establishes the dependency but provides none of these interface details.