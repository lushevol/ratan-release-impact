---
type: concept
title: Indonesia Hybrid GDC-ID Message Flow
created: 2026-08-24
updated: 2026-08-24
tags: [indonesia, gdc, messaging, batch-processing, netting, murex, solace]
related: [ratan-indonesia-onshoring-2026, ratan-cash-settlement-batch-service, ratanone-message-bridge, solace, cash-settlement-dc-failover-strategy, cashflow-lineage-and-operational-visibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Development Integration Plan.md"]
---
# Indonesia Hybrid GDC-ID Message Flow

The implementation plan describes a hybrid GDC-ID arrangement rather than wholly Indonesia-local processing.

## Documented flow elements

- Batch processing remains GDC-only; Indonesia does not deploy `ratan-cash-settlement-batch-service`.
- The GDC batch service must publish to `Cash_Settlement_Mxg_Inbound_Batch_All`.
- [[ratanone-message-bridge]] consumes that topic and has a mandatory GDC deployment dependency.
- `51358-ratan-mxg-cashflow-adaptor` is marked “Only GDC.”
- Netting is described as “ID drive.”
- Netting-resultant and splitting-resultant cashflow IDs require prefixes.

## Limits of the available design

The plan does not provide a topology diagram, event schema, message ownership boundaries, data-residency controls, ordering rules, deduplication approach, failure recovery, replay policy, or a determination of whether GDC dependencies are temporary.

The arrangement therefore requires resolution through [[what-is-the-approved-indonesia-gdc-id-message-processing-topology]]. Cashflow-ID prefix semantics are separately tracked in [[what-is-the-resultant-and-split-cashflow-id-prefix-contract-for-indonesia]].