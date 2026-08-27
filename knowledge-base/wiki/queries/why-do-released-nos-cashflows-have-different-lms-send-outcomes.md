---
type: query
title: Why Do Released NOS Cashflows Have Different LMS Send Outcomes?
tags: [lms, nos, cashflow, uat2, message-eligibility]
related: [lms, lms-cashflow-lifecycle-message-eligibility, manual-entity-lms-reference-data-feed]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/Self testing.md"]
---
# Why Do Released NOS Cashflows Have Different LMS Send Outcomes?

## Evidence

The UAT2 record places released NOS samples `M00202510117`, `M00202510118`, `M00202510120`, `M00202510122`, `M00202510123`, and `M00202510132` in its send-to-LMS testing area. In contrast, it explicitly records:

> `M00202510128 NOS CURR|FXD|FXD 401036553 NOT SEND TO LMS Released`

The readable source does not identify the field or rule responsible for the distinction.

## Information needed

- Full cashflow attributes and lifecycle histories for all compared samples.
- Relevant booking-entity, counterparty, account, product, and static-data configurations.
- Eligibility-rule configuration and outbound-event logs at the test time.
- LMS audit, acknowledgement, and reconciliation results for each sample.
- Confirmation whether the table's send-to-LMS column represents expected result, actual result, or test objective.

## Working constraint

Do not infer that NOS plus Released status either permits or prevents LMS transmission until the differentiating condition is evidenced.