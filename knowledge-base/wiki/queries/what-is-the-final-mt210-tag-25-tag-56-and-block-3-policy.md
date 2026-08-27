---
type: query
title: What Is the Final MT210 Tag 25, Tag 56, and Block 3 Policy?
tags: [query, mt210, swift, block-3, ratan, murex]
related: [ratan, murex, swift-block-3-tagging, accepted-swift-format-variances, swift-message-reconciliation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Murex and Ratan Swift Difference Review.md"]
---
# What Is the Final MT210 Tag 25, Tag 56, and Block 3 Policy?

The source contains conflicting or incomplete dispositions:

- H1 records removal of Block 3 tag `121` for MT210.
- H1 records no change for Murex-only tag `25` and missing tag `56`.
- UK/DE records MT210 Block 3 as confirmed in H1 with no change, but says tags `25` and `56` are to be added in H2.
- Tranche 2 classifies missing field `56` as expected RATAN behavior.

The final policy, implementation status, and release evidence are not established.