---
type: query
title: What Does MATH Mean in the FMRP Cashflow Lifecycle?
created: 2026-08-24
updated: 2026-08-24
tags: [FMRP, MATH, state-model, release-processing]
related: [fmrp, fmrp-cashflow-publication-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change.md"]
---
# What Does MATH Mean in the FMRP Cashflow Lifecycle?

`client.scb.fmrp.inbound.syncRelease` sets `SCB_FMRP_DBF.M_STATUS` to `MATH` after a RATAN release response. The source does not define the term, permitted predecessors, permitted successors, terminality, or relationship to the `SNTR2RLSR` payment action and `RLSR` status.

An authoritative FMRP state model is required to determine whether `MATH` means released, release acknowledged, matched, or another internal processing state.