---
type: concept
title: FMRP Manual Cashflow Publication
created: 2026-08-24
updated: 2026-08-24
tags: [fmrp, murex-211, ratan, manual-processing, cashflow-publication]
related: [fmrp-murex-211-settlement-workflow, fmrp-cashflow-publication-lifecycle, murex-ratan-hybrid-batch-and-realtime-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 DOI Document - H2 2024.md"]
---
# FMRP Manual Cashflow Publication

`FMRP:INIT2SNTR MAN` is the controlled manual route for publishing a Murex payment to Ratan when automatic publishing fails or an ad hoc requirement applies.

The DOI instructs operators to select an approved settlement profile, filter by value date and counterparty, and publish no more than 30 payments per action. Commodity payments require the COMMODITY flow checkbox before processing.

A payment manually moved from `SNTR` back to `INIT` no longer triggers automatic publishing. To republish it, an operator must manually move it from `INIT` to `SNTR`.

The source does not specify maker-checker approval, enforced limits, authorization criteria, or retained evidence for manual actions.