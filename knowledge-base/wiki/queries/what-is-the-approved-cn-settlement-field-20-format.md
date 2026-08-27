---
type: query
title: What Is the Approved CN Settlement Field 20 Format?
tags: [cn-settlement, swift, field-20, fmrp, open-question]
related: [cn-settlement, fmswg-swift-message-validation, ssi-data-quality-for-swift-generation, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--32-cn-settlement-ops-week--o3lm83]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Ops weekly session/Open Items.md"]
created: 2026-08-23
updated: 2026-08-23
---
# What Is the Approved CN Settlement Field 20 Format?

## Question

What is the authoritative CN Settlement rule for SWIFT Field 20, including the use of the `MX` prefix and terminal `A`, `B`, or `C` suffixes?

## Evidence

The historical open-items tracker records a 2022-11-16 action to confirm the Field 20 format with CMO. Its status is Open. The tracker does not identify applicable message types, source fields, generation logic, or a governing specification.

A separate agency-booking Field 20 task was closed as not required. That closure is limited to agency booking and does not resolve the general Field 20 question.

## Needed to resolve

- The authoritative specification, approved owner, and effective release.
- Applicable SWIFT message types and payment flows.
- Exact rules for selecting `A`, `B`, or `C`.
- Whether the `MX` prefix and suffix are generated, passed through, or manually supplied.
- Any distinction between agency-booking and non-agency-booking flows.

## Related pages

- [[cn-settlement]]
- [[fmswg-swift-message-validation]]
- [[ssi-data-quality-for-swift-generation]]
- [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--32-cn-settlement-ops-week--o3lm83]]