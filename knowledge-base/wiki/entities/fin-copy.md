---
type: entity
title: FIN_COPY
tags: [fin-copy, murex, nostro, vostro, static-data, swift]
related: [ratan, murex, swift-block-2-receiver-derivation, nostro-static-data]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Murex and Ratan Swift Difference Review.md"]
---
# FIN_COPY

`FIN_COPY` is a Vostro UDF used in the documented MT604 and MT605 Block 2 receiver-BIC derivation logic.

The source distinguishes cases where `FIN_COPY` is blank and non-blank. The explicit RATAN action is to copy the Murex logic “with FINCOPY is blank,” but it does not establish whether the non-blank path is already implemented or out of scope. This unresolved boundary is tracked in [[queries/which-mt604-mt605-fin-copy-receiver-derivation-paths-are-in-ratan-scope]].