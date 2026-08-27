---
type: concept
title: Utilization Eligibility Static
created: 2026-08-23
updated: 2026-08-23
tags: [static-data, eligibility, fx-utilization]
related: [fx-utilization, s2bx, blade, stella, utilization-settlement-method-conversion]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis.md"]
---
# Utilization Eligibility Static

Utilization Eligibility Static is client-level configuration that identifies clients eligible for FX Utilization and, separately, clients eligible for auto utilization.

It drives proposed `UTIL` stamping for upstream S2BX trades. The source leaves its authoritative maintenance location open among [[s2bx]], [[blade]], and [[stella]].

For a manually booked BLADE `UTIL` trade where the client is absent from this static, the design proposes `FXBRREC-M` as the default settlement means for manual utilization.