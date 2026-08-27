---
type: concept
title: SWIFT Block 3 Tagging
tags: [swift, block-3, mt202, mt210, mt604, mt605, message-generation]
related: [ratan, murex, swift-message-reconciliation, accepted-swift-format-variances]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Murex and Ratan Swift Difference Review.md"]
---
# SWIFT Block 3 Tagging

The review records a RATAN common pattern for SWIFT Block 3:

```text
Murex has logic to generate different tag in block 3
Ratan set common logic to
- {3:{121:uuid}} for 202,202Flip,103, 103COV,n92
- {3:{108:UUID}}for 604,605,692
- {3:{119:COV{121:uuid}} for 202COV
```

The confirmed H1 action is:

```text
Keep ratan logic remove tag121 for MT210
```

Later UK/DE notes state that MT210 Block 3 was confirmed in H1 and required no change. This may indicate that the H1 action had already been accepted or implemented, but the source does not state its status. The final MT210 policy remains open.