---
type: query
title: Where Should RATAN Remove Dummy Trade IDs?
created: 2026-08-22
updated: 2026-08-22
tags: [architecture, trade-id, ratan, lms, accounting]
related: [dummy-trade-id-management, blank-flows-enrichment, ratan, lms, ebbs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/RFR and Swap Agent.md"]
---

# Where Should RATAN Remove Dummy Trade IDs?

The requirement records two alternative designs for preventing RATAN-generated trade IDs from reaching LMS, eBBS, and FMSWG, but does not select one.

## Options

1. Remove the synthetic ID during the first RATAN workflow task, centralizing cleanup but risking trade-ID lock-control effects.
2. Retain the ID within RATAN and dynamically remove it in LMS and accounting services, avoiding RATAN lock-control changes but requiring distributed customization.

## Decision needed

Select an ownership point for removal, define the downstream replacement value, and validate lock-control, reconciliation, audit, and service-change impacts.