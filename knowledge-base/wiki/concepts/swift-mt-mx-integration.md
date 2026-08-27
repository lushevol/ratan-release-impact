---
type: concept
title: SWIFT MT/MX Integration
created: 2026-08-22
updated: 2026-08-22
tags: [swift, mt, mx, financial-messaging]
related: [ratan, 51358-ratanone-swift-service, ratan-settlement-korea, settlement-message-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md"]
---
# SWIFT MT/MX Integration

SWIFT MT/MX integration connects legacy SWIFT MT message processing and ISO 20022 MX message processing to settlement workflows.

## Korea Release

For [[ratan-settlement-korea]], [[51358-ratanone-swift-service]] delivers:

- ENISIS real-time ingress and egress.
- MT and MX handling.
- Korea MT210 support.
- KR MX configuration.
- Reuse of `IngressSourceSystem RATAN` for Korea ENISIS processing.

Production PIT also checks sender BIC records for FMID `10036645`.

## Related Frontend Behavior

The cashflow-blotter release adds `FinalCancelled` to the Cashflow/Cashflow Swift Status values used by the Swift Error dashboard filter.