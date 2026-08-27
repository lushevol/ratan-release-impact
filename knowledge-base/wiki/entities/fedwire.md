---
type: entity
title: FEDWIRE
tags: [fedwire, settlement-method, swift, static-data, ado]
related: [ratan, ado, swift-message-reconciliation, settlement-method-stamping]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Murex and Ratan Swift Difference Review.md"]
---
# FEDWIRE

FEDWIRE is a settlement method referenced in the UK/DE SWIFT reconciliation. The source defers the `FW` prefix in field 54 and the first field 57 to a FEDWIRE SSI ADO task.

No ADO work-item identifier or completion evidence is included. The dependency should remain distinct from general RATAN message-generation changes.