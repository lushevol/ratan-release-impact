---
type: query
title: Which Downstream Systems Use the Updated Manually Rounded Cashflow Amount?
created: 2026-08-23
updated: 2026-08-23
tags: [manual-rounding, cashflow, swift, accounting, downstream-processing]
related: [manual-cashflow-rounding, settlement-accounting, outbound-property-propagation-to-swift-mt-mx]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Manual Rounding.md"]
---
# Which Downstream Systems Use the Updated Manually Rounded Cashflow Amount?

The final wording of the requirement states that SWIFT and Settlement Accounting should use the same updated amount. The source does not provide the message fields, accounting interface, posting behavior, or complete downstream system list.

## Required resolution

Confirm the end-to-end propagation of the amended amount through:

- SWIFT payment generation;
- Settlement Accounting;
- reconciliation and reporting;
- any netting, splitting, release, or settlement-posting services.

The result should distinguish confirmed behavior for SWIFT and Settlement Accounting from assumptions about EBBS or other platforms. It should also define what happens if one downstream system receives the updated amount while another retains the original.
