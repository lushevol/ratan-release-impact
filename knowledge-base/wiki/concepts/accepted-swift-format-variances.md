---
type: concept
title: Accepted SWIFT Format Variances
tags: [swift, reconciliation, accepted-variance, message-format, ratan, murex]
related: [ratan, murex, swift-message-reconciliation, swift-block-3-tagging, static-data-readiness]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Murex and Ratan Swift Difference Review.md"]
---
# Accepted SWIFT Format Variances

Accepted SWIFT format variances are differences between Murex replay output and RATAN output that the review explicitly classifies as requiring no RATAN change.

Examples include:

- RATAN generating tag `53` when Murex does not;
- `53A` versus `53B`;
- `58A` versus `58D`;
- differences in BIC second lines or account-number presentation;
- differences in field 72 prefixes, sequencing, or content;
- Murex-only tags such as `23E`, `25`, `56`, `71A`, or `33B`;
- sequence-B field 57 differences;
- message-type or stamping differences;
- differences in casing, truncation, address lines, and reference rendering.

Acceptance is contextual. A “no change required” note is a reconciliation disposition, not evidence that the variance is harmless for every downstream, payment, or regulatory use. Material variances should have explicit acceptance criteria and validation evidence.