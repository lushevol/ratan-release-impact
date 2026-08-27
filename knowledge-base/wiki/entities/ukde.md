---
type: entity
title: UKDE
created: 2026-08-22
updated: 2026-08-22
tags: [ukde, uk, cash-settlement, swift, accounting]
related: [settlement-accounting-suppression, uk-specific-swift-logic, cash-settlement, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis.md"]
---
# UKDE

UKDE is the entity scope named in the Q3 2024 requirement to generate a SWIFT message while suppressing settlement accounting and UK accounting for PM processing.

The source records ticket **4038613** with test-case readiness, development readiness, and UAT running. It does not document the exact accounting entries suppressed, exception conditions, UAT outcome, or production status.

## Related Processing

The requirement belongs to the wider UK settlement modernization portfolio, which also includes [[concepts/uk-specific-swift-logic]], [[entities/murex-2-11]], and [[entities/ratan]].

---