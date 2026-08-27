---
type: query
title: What Actions Are Authoritatively Permitted While a Cashflow Is on HOLD?
tags: [cashflow, hold, processing-controls, ssi, netting, suppression]
related: [cashflow-hold-and-unhold, ratan, cashflow-suppression, swift-suppression, cashflow-split-and-unsplit]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Hold UnHold.md"]
---
# What Actions Are Authoritatively Permitted While a Cashflow Is on HOLD?

The HOLD/UNHOLD requirement has conflicting statements about processing during `HOLD`.

It says HOLD stops further processing, including materialization, exception checking, and SSI stamping. Its available-actions table nevertheless permits Adhoc SSI, Netting, Un-Net, SWIFT Suppression, Cashflow Suppression, and UNHOLD.

## Questions to resolve

- Does HOLD block automated SSI stamping while permitting manual Adhoc SSI?
- Are Netting and Un-Net positively supported from HOLD, or merely listed after removal of a prior restriction?
- Does invoking an allowed action supersede HOLD, preserve it, or create a distinct successor lifecycle?
- Which processing components must reject or defer work while a cashflow is held?

A current authoritative status-machine specification and implementation-level test evidence are needed before this requirement can be used as a complete processing-control contract.