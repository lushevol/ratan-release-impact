---
type: query
title: What Is the Current CN Rule Service Rule Engine and Rule Source?
created: 2026-08-24
updated: 2026-08-24
tags: [cn-rule-service, drools, redis, architecture-status]
related: [cn-rule-service, drools, cached-rule-loading, drools-based-nstp-rule-evaluation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]
---
# What Is the Current CN Rule Service Rule Engine and Rule Source?

The available evidence is an archived proposal for an NSTP-only Drools proof of concept and a possible Redis rule-loading layer. It does not establish current implementation status.

## Questions

- Is Drools currently used by CN Rule Service?
- Did the NSTP Drools PoC complete, and what were its acceptance results?
- Which rule types, if any, use Drools?
- Is Redis the active rule source, and is PostgreSQL still authoritative?
- What implementation superseded this archived proposal, if any?

## Evidence needed

Current service architecture, deployed configuration, rule-loading code, PoC outcomes, performance results, and a current architecture decision record.