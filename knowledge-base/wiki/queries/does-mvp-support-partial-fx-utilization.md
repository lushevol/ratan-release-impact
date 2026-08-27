---
type: query
title: Does MVP Support Partial FX Utilization?
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, partial-utilization, mvp, validation, open-question]
related: [fxu, fx-utilization, fxu-utilization-validation, fxu-technical-design]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design.md"]
---

# Does MVP Support Partial FX Utilization?

The source contains conflicting evidence:

- The NACK catalogue states `Currently partial utilization is not allowed.`
- An ACK example uses `Util_Type: "VDATE-PART-REV"` with `50.0` USD and `187.5` SAR amounts.
- A technical NACK example uses `EARLY-PART-UTIL` with a partial amount.

The examples may describe a later phase, generic message fixtures, or behavior inconsistent with the MVP restriction. They should not be used to conclude that MVP supports partial utilization.

## Required clarification

Confirm the phase associated with each example and provide the authoritative matrix for full, partial, reverse, early, and past-due utilization types.