---
type: concept
title: Murex 2.11 Vostro SSI Reuse
tags: [vostro-ssi, murex-211, ratan, ssi-reuse, static-data]
related: [ratan, ssi-plus, murex-211, cfi-code-mapping-for-murex-vostro-ssi, murex-211-vostro-ssi-data-quality]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/Murex 2.11 Vostro SSI.md"]
---
# Murex 2.11 Vostro SSI Reuse

Murex 2.11 Vostro SSI reuse is the requirement that RATAN use the existing Murex 2.11 SSI population instead of creating a separate settlement-instruction population.

## Operating model

RATAN selects an existing SSI using a CFI code stamped on the cashflow. To support that lookup, existing Security IDs in [[ssi-plus]] must be updated with the relevant CFI codes.

This makes SSI reuse dependent on both:

1. Correct CFI-code stamping for Murex 2.11 cashflows.
2. Sufficient completeness and correctness of the existing SSI+ attributes.

## Constraints

The SSI population is not maintained at full product-equivalent CFI granularity. The source uses `XFXXXX` as an example of a broad mapping shared by FX Spot, Forward, and Swap products. This may be intentional reuse, but the requirement does not establish whether the same SSI is safe for every product in that group.

The source also reports substantial data gaps, including a 98.8% blank rate for Settlement Account and Settlement Means. Reuse should therefore not be treated as operational readiness without field-level validation.