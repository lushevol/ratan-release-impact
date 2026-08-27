---
type: query
title: What Is the Authoritative Ratan Expiry Filtering Key and Version Model?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, expiry, filtering, versioning, physical-status, ratan, stella]
related: [cashflow-events-control-draft2, cashflow-expiry-event-filtering, cashflow-lifecycle-supersession-and-audit-history, cashflow-status-lifecycle, ratan, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Cashflow Events Control Draft2.md"]
---
# What Is the Authoritative Ratan Expiry Filtering Key and Version Model?

The deprecated draft proposes that Ratan ignore a VD+1 Stella expiry version marked `Physical Status = Dead` and continue processing the earlier record. It does not define the actual filtering rule.

## Questions to resolve

- Which fields identify an expiry-generated record: physical status, event type, version, timestamp, or another indicator?
- How are `Business Version`, `Cashflow Version`, and `Ratan Version` owned, incremented, and correlated?
- Does the same filtering outcome apply to failed, released, settled, netted, and split records?
- How are out-of-order, duplicate, or corrected expiry events handled?
- What audit trail is retained for filtered records and their predecessors?

The source is non-authoritative and should not establish the production versioning contract.