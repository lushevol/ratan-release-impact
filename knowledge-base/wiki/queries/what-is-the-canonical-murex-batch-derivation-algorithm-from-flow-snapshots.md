---
type: query
title: What Is the Canonical Murex Batch Derivation Algorithm From Flow Snapshots?
tags: [murex-211, batch-control, flow-snapshots, integration, ratan]
related: [murex-211, ratan, cashflow-batch-control, murex-ratan-cashflow-ringfencing]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control.md"]
---
# What Is the Canonical Murex Batch Derivation Algorithm From Flow Snapshots?

Murex 2.11 batching is illustrated through cumulative `<Flows>` snapshots, with Ratan expected to compare each incoming list against a retained batch audit. The document does not specify a deterministic algorithm.

## Required definition

Specify:

- the canonical snapshot identity and normalization rules;
- whether `<flow>` ordering is significant;
- how newly appended, deleted, amended, duplicate, or reordered flows are classified;
- how concurrent source publications are handled;
- how batch ID, major version, sequence, and count are persisted and replayed; and
- reconciliation and audit requirements when inferred results differ from source expectation.

This is required before Murex behaviour can reliably align with the Stella batch contract.