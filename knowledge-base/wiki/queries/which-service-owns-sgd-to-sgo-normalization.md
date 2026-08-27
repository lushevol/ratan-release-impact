---
type: query
title: Which Service Owns SGD to SGO Normalization?
tags: [open-question, currency-normalization, architecture, netting, group-management]
related: [currency-alias-normalization, currency-normalization-layer-ownership, group-management, standardization-module, netting-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Online Offline currency conversion solution.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Which Service Owns SGD to SGO Normalization?

Should `SGD → SGO` be canonicalized in [[group-management]], [[netting-service]], or at an earlier shared boundary so that all required downstream consumers receive `SGO`?

## Why This Is Open

The source presents Group Management and Netting Service as mutually exclusive alternatives without an approved decision.

A Group Management implementation is narrow but may not be visible to downstream systems or manual netting. A Netting Service implementation covers named netting paths but does not establish that Netting Service is the only downstream consumer or that normalized values are delivered to all consumers.

## Evidence Needed

- A complete inventory of consumers of the currency field.
- Data-flow evidence showing where each consumer receives its value.
- Ownership of the canonical alias map and its change process.
- A decision on original-versus-normalized value retention.
- End-to-end tests covering delivery, manual netting, IRS, validators, grouping, and auto-netting.