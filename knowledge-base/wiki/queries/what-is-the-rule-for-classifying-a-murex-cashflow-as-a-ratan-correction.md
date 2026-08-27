---
type: query
title: What Is the Rule for Classifying a Murex Cashflow as a RATAN Correction?
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, ratan, amendments, correction, nstp]
related: [cashflow-business-and-message-versioning, released-settled-amendment-control, ratan-lms-action-event-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex2.11 Technical Design.md"]
---
# What Is the Rule for Classifying a Murex Cashflow as a RATAN Correction?

The design identifies flow `03` as a correction that receives a new RATAN ID, event `New`, version `0`, and NSTP status for user intervention. It cites “Rule 9” as the basis for identifying a correction, but that rule is absent from the source.

Without the rule, the conditions that distinguish a correction from an original, reversal, replacement, or other amendment cannot be verified.

## Evidence needed

- The missing Rule 9 specification.
- Murex amendment and market-operation examples for each classification.
- RATAN implementation logic and test cases for correction detection.
- User decision and release controls for correction cashflows.