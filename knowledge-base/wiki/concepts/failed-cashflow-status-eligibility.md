---
type: concept
title: Failed Cashflow Status Eligibility
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, failed-status, status-transition, eligibility]
related: [scheduled-failed-cashflow-job, manual-cashflow-failure, cashflow-event-versioning, cashflow-suppression, swift-suppression, what-is-the-authoritative-failed-cashflow-transition-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Scheduled Failed Job Manual Fail.md"]
---
# Failed Cashflow Status Eligibility

Failed Cashflow Status Eligibility defines which current cashflow statuses can transition to `FAILED` through either scheduled or manual failure processing.

| Cashflow Status | Can move to Failed? |
| --- | --- |
| PROJECTED | Y |
| QUEUED | Y |
| WAITING | Y |
| READY | Y |
| ONHOLD | Y |
| CANCELLED | N |
| NETTED | N |
| SPLIT | N |
| DEAD | N |
| SUPPRESSED | N |
| PAYMENT SUPPRESSED | N |
| RELEASED | N |
| SETTLED | N |
| NOSTRO MATCHED | N |

## Interpretation

The matrix explicitly permits transitions from five statuses: `PROJECTED`, `QUEUED`, `WAITING`, `READY`, and `ONHOLD`. Although the source prose refers to “specific cashflow status” in the singular, the table is the explicit rule and records five eligible statuses.

`SUPPRESSED` and `PAYMENT SUPPRESSED` are excluded, preserving their distinction from failure processing described in [[cashflow-suppression]] and [[swift-suppression]].

The source does not define treatment for a cashflow already in `FAILED`, versioning of the update, or whether transition validation is atomic with status update. These points require resolution through [[what-is-the-authoritative-failed-cashflow-transition-contract]].