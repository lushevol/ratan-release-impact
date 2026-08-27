---
type: concept
title: Murex Reversal and New-Cashflow Matching
created: 2026-08-22
updated: 2026-08-22
tags: [Murex, Ratan, cashflow, reversal, lineage, migration]
related: [murex-ratan-reversal-and-replacement-lifecycle, murex-flow-group-batch-handling, murex-to-ratan-cashflow-interface, cashflow-migration-readiness]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/01- Function Flow/Cashflow Migration Readiness.md"]
---
# Murex Reversal and New-Cashflow Matching

Murex reversal and new-cashflow matching is the lineage control used to associate a reversal cashflow with the replacement or newly generated cashflow during migration to Ratan.

## Source Position

The source proposes using a snapshot of historical SNTR cashflows from Murex 2.11 so that Ratan can identify batches. However, batch identification does not by itself establish the relationship between a reversal and its replacement cashflow.

The matching logic remained unresolved:

- The linkage approach was discussed with Dinesh and operations on 2023-07-05.
- Predeesh was expected to confirm the approach with the team.
- Sumita's input was still pending.
- Exception handling required additional input.

## Related Event Handling

The source also records an unresolved proposal to send non-economic amended cashflows to Stella. Stella had not yet confirmed the proposal. This creates a separate event-routing decision in addition to reversal/new-cashflow matching.

The open lineage requirement extends [[concepts/murex-ratan-reversal-and-replacement-lifecycle]] and should be kept distinct from [[concepts/murex-flow-group-batch-handling]].