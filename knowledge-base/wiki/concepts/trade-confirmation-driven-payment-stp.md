---
type: concept
title: Trade Confirmation-Driven Payment STP
created: 2026-08-24
updated: 2026-08-24
tags: [payment-stp, trade-confirmation, comp, cash-settlement, operations]
related: [murex-korea, mxml-trade-confirmation-event-integration, ratan, cash-settlement-dependent-service-failure]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Korea Murex Trade COMP High Level Solution.md"]
---
# Trade Confirmation-Driven Payment STP

Trade confirmation-driven payment STP is the automatic progression of payments when a corresponding trade has received the required confirmation status, represented in this design by `COMP`.

For the Korea Murex flow, the document presents `COMP` as mandatory for payment STP. If the confirmation status is unavailable to [[ratan]], payments remain pending for manual OPS affirmation. Korea OPS identifies this automation as a business go-live requirement because manual processing capacity is insufficient for the expected workload.

The source documents the operational dependency but provides no quantitative volumes, staffing model, exception rate, service-level objective, or acceptance criteria. It should therefore be treated as a stated business requirement rather than a measured capacity conclusion.

The proposed mechanism for satisfying the dependency is described in [[mxml-trade-confirmation-event-integration]].