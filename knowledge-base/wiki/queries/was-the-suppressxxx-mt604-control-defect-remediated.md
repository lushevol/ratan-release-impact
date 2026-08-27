---
type: query
title: Was the SUPPRESSXXX MT604 Control Defect Remediated?
created: 2026-08-23
updated: 2026-08-23
tags: [fmswg, swift, mt604, bic, production-incident, validation]
related: [fmswg, amh, fmswg-swift-message-validation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Production Issue - Swift Message.md"]
---
# Was the SUPPRESSXXX MT604 Control Defect Remediated?

## Question

Was [[FMSWG]] changed to reject `SUPPRESSXXX` and equivalent placeholder BICs before MT604 generation and AMH submission?

## Evidence

On 2025-01-20, an MT604 contained `:87A:SUPPRESSXXX` and AMH returned `T28008`. The source states that the dummy BIC was not stopped by FMSWG. Its status and resolution fields are blank.

## Information needed

- the remediation owner, change record, and deployment date;
- the fields and SWIFT message types covered by the validation;
- regression and production evidence that placeholder values are rejected before AMH;
- confirmation of whether existing queued or generated messages were remediated.