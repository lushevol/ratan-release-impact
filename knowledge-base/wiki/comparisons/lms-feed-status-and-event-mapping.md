---
type: comparison
title: LMS Feed Status and Event Mapping
created: 2026-08-23
updated: 2026-08-23
tags: [LMS, cashflow, status, business-event, Swift]
related: [swift-suppressed-lms-feed-contract, receive-only-swift-suppressed-cashflow, scbml-cashflow-data-message, lms]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/Include Swift Suppressed status in LMS feed (only for receipts).md"]
---
# LMS Feed Status and Event Mapping

The requirement distinguishes cashflow status from the LMS business event carried in the SCBML message. The initial feed rule is established for receipt-only Swift Suppressed cashflows, but the event mapping is incomplete.

| Cashflow status or transition | Feed treatment | Event mapping status |
|---|---|---|
| `RELEASED` | Send to LMS | Existing behavior |
| `SETTLED` | Send to LMS | Existing behavior |
| `New -> Swift Suppressed (Receive Only)` | Send to LMS | Exact event representation not defined |
| `Undo Swift Suppression` | Send another message | Message required; event and payload not defined |
| Withdrawal to `CANCELLED` | Send another message | Message required; event and payload not defined |
| Manual Failed to `FAILED` | Undecided | No decision recorded |
| Other statuses | Do not send under the proposed rule | No exception specified |

## Interpretation

`New` and `Withdrawal` are shown as sample `businessEvent` values in the SCBML template, but they do not by themselves explain every status transition. LMS must confirm whether the status is represented by a business event, an explicit status field, or both.
