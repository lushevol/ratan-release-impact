---
type: query
title: What Is the Canonical Trade Validation Key by Source System?
created: 2026-08-24
updated: 2026-08-24
tags: [trade-validation, FMRP, Murex, trade-identity, TDS3]
related: [trade-validation-gating, fmrp-major-version-backward-validation, fmrp, murex, tds3, scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Trade Validation Confirmation Process Tech Design.md"]
---
# What Is the Canonical Trade Validation Key by Source System?

The design specifies different validation keys for FMRP and Murex, but does not define the canonical lookup contract or identifier normalization rules.

## Proposed rules

- FMRP: trade ID + major version + status.
- Murex: trade ID + status.
- FMRP validation at a higher major version applies backward to earlier major versions.
- Murex has no stated major-version inheritance rule.

## Unresolved details

The design does not specify:

- Whether trade IDs are normalized before lookup.
- How `originalTradeId` and `tradeId` are selected for Murex.
- How `majorVersion` and `trackingVersion` are used for Stella.
- How status history and late-arriving validation are queried.
- How conflicting TDS3 records are resolved.
- How validation reversals affect an already released group.

The answer should be documented separately for each source system rather than generalized across FMRP, Murex, and Stella.
