---
type: query
title: Is Auto Split in Scope for FMRP CN Settlement?
created: 2026-08-23
updated: 2026-08-23
tags: [auto-split, fmrp, razor, murex-2-11, cn-settlement]
related: [fmrp, razor, murex-2-11-cn-derivative-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Ops weekly session/2022-11-16.md"]
---
# Is Auto Split in Scope for FMRP CN Settlement?

Razor BAU is reported to auto-split selected country and currency payments above static currency-level thresholds, with parent-payment linkage in SWIFT Field 72.

For Murex 2.11 derivatives, the session stated that no auto-split requirement exists; client-requested splits are manual in Opics and have no original-to-split linkage.

An explicit scope decision is required for FMRP CN Settlement. Razor behavior is reference information and must not be adopted by default.