---
type: concept
title: SWIFT MX Regression Retest Normalization
created: 2026-08-23
updated: 2026-08-23
tags: [swift-mx, regression-testing, uat, message-reconciliation, korea-migration]
related: [ratan-swift-message-generation, swift-message-reconciliation, swift-status-lifecycle-and-reconciliation, korea-cash-settlement-migration, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--12-2026-changes--34-cash--7tkpsr]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Swift Generation UAT cases retest.md"]
---
# SWIFT MX Regression Retest Normalization

SWIFT MX regression retesting compares UAT and retest payloads while separating expected runtime-generated values from substantive message-content changes.

## Observed Korea Migration treatment

The Korea Migration UAT retest evidence explicitly accepts changed `CreDt` and `CreDtTm` values in three passed case groups. The original UAT fixtures use `9999-12-31T00:00:00+00:00`, while retests use actual message-creation timestamps.

For the passed `pacs.008.001.08` examples, a change from `EndToEndId=NOTPROVIDED` to a generated `DV70...` identifier was also recorded and accepted. This observation is limited to the documented passed cases; it is not evidence of an authoritative rule for every SWIFT MX message type.

## Comparison controls

A regression comparison should distinguish:

- Runtime values, such as message creation timestamps.
- Identity values generated for a particular retest cashflow.
- Fixture-specific payment fields that can differ when UAT and retest use distinct cashflows.
- Business-critical fields, including message family, sender and receiver BICs, settlement method, routing instructions, settlement account, amount, currency, and cancellation references.

A difference is acceptable only when the applicable test evidence explicitly classifies it as such. The absence of a recorded result cannot be treated as a pass.

## Cancellation comparison

For `camt.056.001.08`, comparisons should retain the relationship to the original payment: original message identifier and type, original UETR, interbank settlement amount and date, and cancellation reason. Assignment creation time may legitimately be runtime-generated, but underlying-payment changes require explicit review.

This method extends [[swift-message-reconciliation]] for the Korea SWIFT MX route and supports validation of [[ratan-swift-message-generation]].