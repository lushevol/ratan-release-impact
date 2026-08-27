---
type: query
title: What Stamping States Count as SSI Use for Dormancy?
created: 2026-08-24
updated: 2026-08-24
tags: [ssi, stamping, dormancy, bcs, business-rules]
related: [dormant-ssi-processing, ratanone-stamping-service, bcs, what-is-the-authoritative-meaning-and-design-of-ssi-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Dormant SSI processing.md"]
---
# What Stamping States Count as SSI Use for Dormancy?

## Question

Is `STP_STAMPING_SHIPPED` the sole BCS stamping state that should establish SSI usage for dormant-SSI processing?

## Evidence

Both the daily BCS extraction and the historical BCS aggregation filter `cashflow_stamping.state` to `STP_STAMPING_SHIPPED`.

The source establishes this as the documented query condition but does not define the meaning of the state, explain excluded states, or show why this state is both necessary and sufficient for SSI-use evidence.

## Decision needed

Confirm:

- The lifecycle meaning of `STP_STAMPING_SHIPPED`.
- Whether any other completed, repaired, retried, or manually processed state qualifies as SSI use.
- Whether shipped records can later be reversed or invalidated.
- Whether the stamping state is authoritative relative to other cashflow lifecycle events.

This question contributes evidence to [[what-is-the-authoritative-meaning-and-design-of-ssi-stamping]].