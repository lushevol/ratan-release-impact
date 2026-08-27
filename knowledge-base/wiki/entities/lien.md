---
type: entity
title: LIEN
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, lien, cashflow, trade-attribute]
related: [lien-stamping-and-re-stamping, pending-fixing-flag-processing, lifecycle-service, netting-service, rule-service, scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/LIEN Processing & Pending Fixing Flag Technical Design.md"]
---
# LIEN

## Role

LIEN is a trade or cashflow attribute used during cash settlement processing. The design requires the current LIEN amount to be retrieved, stamped onto the cashflow representation, and refreshed when lifecycle processing changes the cashflow context.

The source does not establish the canonical system of record for LIEN. It refers to TDSX and an existing DA connection as possible integration points, so source-of-truth ownership remains an open question.

## Processing responsibilities

- `ratan-cash-settlement-netting-service` retrieves LIEN amounts for components before resultant generation.
- `ratan-cashflow-lifecycle-service` queries the trade LIEN amount and stamps it onto cashflow SCBML during applicable status updates.
- `ratan-rule-service` may add NSTP handling for cashflows with LIEN amounts and generate LIEN on trade exceptions.

## Consistency rule

For resultant generation, the latest LIEN value should be obtained immediately before generation. This requirement is specific to the netting-service flow and should not be generalized to other services without confirming their contracts.

## Unresolved behavior

The design does not define:

- The canonical LIEN source.
- Behavior when the LIEN query times out, fails, or returns no value.
- Whether LIEN stamping and status changes are atomic.
- Whether repeated stamping is idempotent.
- Whether a LIEN change emits a separate event.
- Whether LIEN generation on trade exceptions changes NSTP classification or only adds an attribute.

See [[lien-stamping-and-re-stamping]] and [[what-is-the-authoritative-lien-stamping-and-restamping-state-machine]].