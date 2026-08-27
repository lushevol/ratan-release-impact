---
type: entity
title: ManualCraft
created: 2026-08-24
updated: 2026-08-24
tags: [manualcraft, payment-integration, mxml-enrichment, cn-settlement]
related: [manualcraft-mxml-enrichment, murex-211, cn-settlement-murex-211-integration, murex-ratan-cashflow-message-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Payment MXML sample files.md"]
---
# ManualCraft

ManualCraft is identified in the source as the enrichment stage applied to raw MXML payment messages in the CN Settlement and [[entities/murex-211]] integration.

The source does not specify whether ManualCraft is a product, service, tool, or operational process. It also does not document its implementation, ownership, interface, transformation logic, validation behavior, or downstream consumers.

## Evidenced role

The intended processing boundary is:

```text
Murex 2.11 raw payment MXML
        |
        v
ManualCraft enrichment
        |
        v
Enriched payment MXML
```

The source lists message categories for this comparison, including `mt202_CMS`, `mt210`, `mt103`, `mt202`, `mt202_210_cms`, `mt192`, `mt103_cms`, `mt103_cover`, `mt202_cover_new`, and `mt192_cover`.

No actual input or output payloads are included. Consequently, no field-level behavior should be attributed to ManualCraft without additional evidence. The open transformation question is tracked in [[queries/what-does-manualcraft-change-in-murex-211-payment-mxml]].