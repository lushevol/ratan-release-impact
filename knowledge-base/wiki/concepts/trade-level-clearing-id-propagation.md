---
type: concept
title: Trade-Level Clearing ID Propagation
created: 2026-08-22
updated: 2026-08-22
tags: [clearing-id, murex, cashflow-blotter, traceability, swap-agent]
related: [murex, ratan-cashflow-blotter, swap-agent, cashflow-logical-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Day2 Auto Netting TestCase.md"]
---
# Trade-Level Clearing ID Propagation

## Definition

Trade-level Clearing ID propagation is the transfer of a Clearing ID from a source trade into the generated cashflow so that the identifier can be displayed in the ratan cashflow blotter.

## Tested behavior

For a Murex trade:

- The trade UDF contains a Clearing ID.
- Cashflow generation runs.
- The generated Murex cashflow displays the trade-level Clearing ID.

For a non-Murex trade, the Clearing ID field on the cashflow is blank.

The source does not identify the exact Murex UDF field name, define null-handling behavior, or establish whether the same rule applies to source systems other than Murex.

## Scope qualification

This behavior is recorded in the Swap Agent Day2 test suite. Further evidence is required before applying it to all Ratan cashflows or all netting categories.
