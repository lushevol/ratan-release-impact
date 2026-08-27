---
type: query
title: Are Delete Rule Queue and Delete Message Queue the Same FMSGW Queue?
created: 2026-08-23
updated: 2026-08-23
tags: [fmsgw, deletion, manual-queue, uat, terminology]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h, scb-dhaka-dac-in-country, fmsgw-manual-cancellation-queue, high-value-payment-approval-queue]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/015 BANGLADESH SCB DHAKA DAC(In Country).md"]
---
# Are Delete Rule Queue and Delete Message Queue the Same FMSGW Queue?

Bangladesh UAT case 4 describes a manually deleted message moving through Low Value, Threshold, or High Value Approval Queue and then to a “Delete Rule Queue.” Its expected result instead says that the approved message is sent to the “Delete Message Queue.”

The source does not establish whether the two names identify one queue, separate workflow stages, or a documentation error.

## Resolution Needed

Confirm the authoritative FMSGW queue names and lifecycle for manual deletion, including:

- The queue entered after approval.
- Whether rule evaluation occurs before or after the approval workflow.
- The terminal message status and any downstream deletion event.
- Whether naming differs by configuration or jurisdiction.

The UAT pass establishes a high-level approved deletion flow for [[scb-dhaka-dac-in-country]], but not the authoritative queue terminology.