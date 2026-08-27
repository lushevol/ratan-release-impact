---
type: entity
title: ratan-mxg-cashflow-adaptor
tags: [ratan, mxg, cashflow, adaptor, mxml, scbml]
related: [scbml, nd-parent-trade-metadata, nds-cashflow-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NDS Cashflow Processing Design.md"]
created: 2026-08-24
updated: 2026-08-24
---
# ratan-mxg-cashflow-adaptor

`ratan-mxg-cashflow-adaptor` is the adapter identified in the NDS design as responsible for mapping NID from MXML into SCBML for downstream processing.

The source records this as a minor code change. It does not define the MXML source field, mapping validation, missing-value handling, or whether existing messages are backfilled.

The mapped data supports the [[nd-parent-trade-metadata]] used by downstream [[nstp-and-ndirs-rule-routing]].