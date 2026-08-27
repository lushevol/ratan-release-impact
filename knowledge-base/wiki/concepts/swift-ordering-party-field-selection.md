---
type: concept
title: SWIFT Ordering-Party Field Selection
tags: [swift, field-50, field-52, payment, ratan]
related: [ratan, swift-message-reconciliation, static-data-readiness]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Murex and Ratan Swift Difference Review.md"]
---
# SWIFT Ordering-Party Field Selection

The review records the following rule for selecting between SWIFT fields `50` and `52`:

> If the party is a bank or equivalent, generate `52`; otherwise generate `50`.

This rule was classified as requiring no change during the H1 review. It is separate from individual discrepancies caused by account numbers, BICs, or SSI/Nostro values.