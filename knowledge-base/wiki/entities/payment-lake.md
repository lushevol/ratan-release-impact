---
type: entity
title: Payment Lake
created: 2026-08-23
updated: 2026-08-23
tags: [payment-lake, persistence, cashflow, netting]
related: [cpn-service, cpn-netting, entities/stella, tds3, entities/cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CPN Tech Design - Draft for now.md"]
---
# Payment Lake

Payment Lake is the cashflow persistence and indexing platform in the CPN netting design.

## Role in the workflow

Payment Lake receives cashflow versions and status updates from:

- CPN Service for CPN- and Murex-related updates.
- `Stella -> TDS3 -> Payment Lake` for Stella-originated updates.
- Settlement Workflow for resultant review and workflow-state updates.

It stores or indexes:

- Component cashflows and their versions.
- Netting IDs.
- `Netted`, `Queued`, `Pending`, `Validated`, `Released`, `Settled`, and `Dead` states.
- Netting resultants.
- Reversal fields such as `Reversal Flag` and `Reversal ID`.

The draft refers to Payment Lake as the source for Cashflow Blotter indexing and as the destination for new versions. It does not define the underlying schema, consistency guarantees, or version-allocation rules.