---
type: concept
title: Incremental Enisis Flow Extension
created: 2026-08-24
updated: 2026-08-24
tags: [enisis, integration, flow-extension, backward-compatibility, cash-settlement]
related: [enisis, enisis-legacy-connection-retention, korea-swift-enisis, what-new-enisis-logic-is-required-in-the-existing-flow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Swift - Enisis.md"]
---
# Incremental Enisis Flow Extension

## Definition

Incremental Enisis flow extension is the design approach of adding Enisis-specific logic to an established processing flow instead of introducing a wholly separate end-to-end flow.

The source states:

> Follow the existing flow and add new logic for Enisis

## Design Intent

This approach keeps the existing flow as the implementation baseline and limits the documented change to Enisis-specific processing. It is intended to operate alongside [[enisis-legacy-connection-retention]], which preserves the existing Enisis connection approach.

## Undefined Details

The source does not identify:

- the existing flow;
- the insertion point for new logic;
- triggering conditions;
- input and output data;
- message or accounting mappings;
- exception behavior; or
- acceptance tests.

These details are tracked in [[what-new-enisis-logic-is-required-in-the-existing-flow]].