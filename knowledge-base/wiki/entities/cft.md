---
type: entity
title: CFT
created: 2026-08-24
updated: 2026-08-24
tags: [CFT, FileIT, file-transfer, cash-settlement]
related: [fileit, aspire, fileit-return-code-taxonomy, accounting-file-delivery-acknowledgement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan FileIT infra setup introduction.md"]
---
# CFT

## Role

CFT is the file-transfer component referenced by FileIT request acknowledgements and return codes in the Ratan-to-Aspire accounting-file integration.

The source identifies CFT as a component that can be unavailable, unauthorized, receive invalid source or target configuration, fail preprocessing or post-processing, or fail during transfer.

## Evidence from the integration

CFT appears in the following acknowledgement fields:

- `Component`
- `SubComponent`
- `TrackingID`
- `Status.Code`
- `Status.Reason`
- `Status.Causes.Details`

The documented successful transfer reason is `CFT_SUCCESSFUL` with code `2000`. The source does not define CFT ownership, deployment topology, credential provisioning, or retry semantics.

## Related concepts

See [[fileit-return-code-taxonomy]] for the documented status groups and [[entities/fileit]] for the FileIT integration context.