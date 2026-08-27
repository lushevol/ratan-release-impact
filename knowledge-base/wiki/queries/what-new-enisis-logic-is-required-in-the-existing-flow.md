---
type: query
title: What New Enisis Logic Is Required in the Existing Flow?
created: 2026-08-24
updated: 2026-08-24
tags: [enisis, integration, flow-extension, open-question, cash-settlement]
related: [enisis, incremental-enisis-flow-extension, enisis-legacy-connection-retention, korea-swift-enisis]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Swift - Enisis.md"]
---
# What New Enisis Logic Is Required in the Existing Flow?

## Question

What Enisis-specific logic must be added to the existing flow, and which existing flow is intended as the implementation baseline?

## Why It Matters

The source establishes implementation direction but does not define the functional change. Without these details, the scope cannot be assigned to generation, validation, routing, accounting, acknowledgement processing, exception handling, or reconciliation.

## Questions to Resolve

- Which concrete Swift-generation or settlement-accounting flow is being reused?
- Where should the Enisis-specific logic be inserted?
- What inputs and outputs does the new logic require?
- What triggering conditions apply?
- Are message mappings or transformations required?
- Does the change affect validation, routing, accounting, acknowledgements, exceptions, or reconciliation?
- Which service and team own the implementation?
- What regression, connectivity, reconciliation, and rollback tests are required?

## Current Evidence

The source only states:

> Follow the existing flow and add new logic for Enisis

It provides no sequence, interface, schema, mapping, or acceptance criteria.

## Expected Resolution

Resolve this query with an approved flow description, change boundary, ownership assignment, interface or mapping specification, and measurable acceptance tests. Preserve [[enisis-legacy-connection-retention]] while defining the functional extension.