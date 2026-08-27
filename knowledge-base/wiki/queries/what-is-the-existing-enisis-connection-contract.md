---
type: query
title: What Is the Existing Enisis Connection Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [enisis, integration, connectivity, open-question, cash-settlement]
related: [enisis, enisis-legacy-connection-retention, korea-swift-enisis, swift-service, accounting-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Swift - Enisis.md"]
---
# What Is the Existing Enisis Connection Contract?

## Question

What exact connection mechanism is referred to by “the old way for Enisis connection,” and which parts of that mechanism must remain unchanged?

## Why It Matters

The source requires legacy-connection retention but does not define the compatibility boundary. Without the existing contract, implementation and validation teams cannot determine whether a proposed change preserves the required behavior.

## Questions to Resolve

- What protocol and transport are used?
- Which endpoint or endpoints are involved?
- How are authentication, certificates, and secrets managed?
- What network route and connectivity prerequisites apply?
- Which service owns the connection?
- What are the timeout, retry, and failure-handling rules?
- How are acknowledgements and delivery outcomes represented?
- What operational support and rollback procedures exist?
- What regression evidence is required to show that the legacy connection remains intact?

## Current Evidence

The only documented requirement is to retain the old Enisis connection approach. The source does not confirm that [[swift-service]] or [[accounting-service]] owns the connection.

## Expected Resolution

Resolve this query with an authoritative connection configuration, service ownership record, interface specification, and regression or connectivity acceptance criteria.