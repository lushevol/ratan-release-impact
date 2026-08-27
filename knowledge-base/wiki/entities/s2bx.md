---
type: entity
title: S2BX
created: 2026-08-23
updated: 2026-08-23
tags: [fx-booking, upstream-system, fx-utilization]
related: [blade, stella, fxu, utilization-eligibility-static]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis.md"]
---
# S2BX

S2BX is an upstream FM booking system named as a source of FX trades for utilization processing.

The design proposes automatically stamping S2BX-originated eligible trades and cashflows with settlement method `UTIL`, based on client utilization static data. A pending MVP item requires identification of the client leg for an S2BX trade ID.

The source does not establish whether S2BX, [[blade]], or [[stella]] is authoritative for utilization-client static data. See [[where-is-the-authoritative-util-client-static-maintained]].