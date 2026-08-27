---
type: query
title: What Is the Resultant and Split Cashflow ID Prefix Contract for Indonesia?
created: 2026-08-24
updated: 2026-08-24
tags: [indonesia, netting, cashflow-id, lineage, reconciliation]
related: [indonesia-hybrid-gdc-id-message-flow, netting-resultant-stack-derivation, cashflow-lineage-and-operational-visibility, ratan-cash-settlement-batch-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Development Integration Plan.md"]
---
# What Is the Resultant and Split Cashflow ID Prefix Contract for Indonesia?

## Question

What prefix values and uniqueness rules apply to Netting-resultant and splitting-resultant cashflow IDs in the Indonesia flow?

## Evidence

The plan labels Netting as “ID drive” and records two changes: “Netting resultant cashflow id prefix” and “Splitting resultant cashflow id prefix.” The UAT release list describes `ratan-cash-settlement-netting-service` as having a “resultant cf id prefix” change.

## Information required

- Exact prefix format and generation rules.
- Collision domain across GDC and Indonesia processing.
- Whether the prefix is semantic, environment-specific, or merely technical.
- Preservation of trade, cashflow, netting, split, and reversal lineage.
- Downstream reconciliation, reporting, and operational-search impact.
- Backward compatibility for previously generated IDs.

The source provides no contract or downstream-system validation.