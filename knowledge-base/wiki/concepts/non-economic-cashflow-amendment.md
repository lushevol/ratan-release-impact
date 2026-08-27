---
type: concept
title: Non-Economic Cashflow Amendment
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, amendment, classification, workflow]
related: [cashflow, group-management-service, cashflow-replacement-mapping, ratan-cashflow-mapping, cashflow-lifecycle-state-machine-restructuring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Group Management Service - Non-Eco Amendment Technical Design.md"]
---
# Non-Economic Cashflow Amendment

A non-economic cashflow amendment is a `Withdrawal` and `New` event pair within an amendment group that preserves the specified payment and party attributes. The pair must have the same Booking Entity ID, Counterparty FM ID, Payment Currency, Payment Amount, Value Date, and Direction, while having opposite business events.

[[group-management-service]] is described as grouping inbound RATAN cashflows by trade ID and major version before workflow publication. A group containing `Withdrawal` and `New` events is an amendment group. Amendment-group cashflows that do not meet the non-economic pairing condition are classified as economic amendments.

## Workflow Eligibility

The stated current behaviour is to ignore non-economic amendments directly. The proposed correction limits direct ignoring to payments touched by users or already settled. Replacements in `PROJECTED` or `QUEUED` status are explicitly expected to proceed to workflow.

The source does not define user touch, settled status, matching precision, null semantics, ambiguity handling for multiple candidates, source-system participation in the key, or late-event ordering.