---
type: query
title: Are UTIL and UITL the Same FXU Settlement-Method Value?
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, util, uitl, settlement-method, terminology]
related: [fxu, gross-util-settlement-method-transition, utilization-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/Draft Design For Phase2.md"]
---
# Are UTIL and UITL the Same FXU Settlement-Method Value?

The draft consistently presents `UTIL` as the settlement-method value in transition rules and the manual-stamping API, but one explanatory sentence uses `UITL` when describing FXU scope.

Confirm whether `UITL` is a typographical error or a distinct persisted or external value. This must be resolved before validators, API enumerations, database updates, and event projections are implemented.