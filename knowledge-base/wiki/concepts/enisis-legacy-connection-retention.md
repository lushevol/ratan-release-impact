---
type: concept
title: Enisis Legacy-Connection Retention
created: 2026-08-24
updated: 2026-08-24
tags: [enisis, backward-compatibility, integration, connectivity, cash-settlement]
related: [enisis, incremental-enisis-flow-extension, korea-swift-enisis, what-is-the-existing-enisis-connection-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Swift - Enisis.md"]
---
# Enisis Legacy-Connection Retention

## Definition

Enisis legacy-connection retention is the constraint that new Enisis-related processing must preserve the established Enisis connection approach.

The source states this requirement as:

> Retain the old way for Enisis connection

## Implication

The intended change is a functional extension rather than an assumed connectivity migration. New logic may be introduced in the established processing flow, but the source does not authorize replacing or redesigning the existing Enisis connection mechanism.

## Unspecified Compatibility Boundary

The source does not clarify whether retention applies to:

- network connectivity;
- transport protocol;
- endpoint selection;
- authentication or certificates;
- file exchange;
- message format;
- connection ownership; or
- all of these elements.

The exact contract is an open question in [[what-is-the-existing-enisis-connection-contract]].

## Evidence Boundary

This concept records an explicit design constraint. It does not establish API compatibility, message-format compatibility, deployment topology, operational non-impact, or acceptance criteria.