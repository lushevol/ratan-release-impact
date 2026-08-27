---
type: concept
title: Dummy Trade-ID Management
created: 2026-08-22
updated: 2026-08-22
tags: [trade-id, data-enrichment, downstream-integration, ratan]
related: [blank-flows-enrichment, ratan, lms, ebbs, where-should-ratan-remove-dummy-trade-ids, which-synthetic-trade-id-prefix-is-authoritative]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/RFR and Swap Agent.md"]
---

# Dummy Trade-ID Management

Dummy Trade-ID Management addresses payments for which Murex sends trade ID `0`. The source proposes deriving a synthetic identifier from the flow ID so RATAN can process a payment with otherwise missing trade metadata.

## Downstream constraint

Synthetic IDs are not intended for delivery to [[lms]], [[ebbs]], or FMSWG. The source does not specify whether downstream consumers should receive the original zero, a blank, or another transformed value.

## Options under discussion

| Option | Benefit | Risk or cost |
|---|---|---|
| Remove the dummy ID in the first RATAN workflow task | One centralized cleanup point | Possible lock-control risk involving trade ID |
| Retain the ID in RATAN and remove it dynamically downstream | Avoids RATAN lock-control changes | Customized implementation in LMS and accounting services |

No decision is recorded. Identifier format is also unresolved because the source uses both `R<flow_id>` and `MTR<flow_id>` examples.