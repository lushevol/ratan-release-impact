---
type: query
title: How Will ECLIPS 400452428 Cashflow Suppression Be Resolved?
created: 2026-08-22
updated: 2026-08-22
tags: [ECLIPS, cashflow-suppression, auto-netting, UAT, dependency]
related: [ratan, cashflow-auto-netting, swift-versus-cashflow-suppression, irs-net-over-net, what-is-the-canonical-eclips-name-and-scope]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting for TAIFEX CITIC LCH HKEX ECLIPS.md"]
---
# How Will ECLIPS 400452428 Cashflow Suppression Be Resolved?

## Question

What change, owner, target date, and successful end-to-end retest will resolve the ECLIPS booking-entity `400452428` path being suppressed before auto-netting?

## Evidence

The proposed ECLIPS auto-netting condition includes booking entities `2` and `400452428` for counterparty `400883001`. A UAT mock cashflow for `400452428` / `400883001` instead matched an existing cashflow-suppression rule, entered `CASHFLOW_SUPPRESSED`, and did not reach the auto-netting rule.

Yew Fuong Hii stated that the cashflow-suppression matter would be handled internally, but the source provides no remediation condition, accountable owner, delivery date, or post-remediation evidence.

## Required closure evidence

- The exact cashflow-suppression rule and condition causing preemption.
- An approved correction or exception for `400452428` / `400883001`.
- Confirmation that the cashflow reaches the ECLIPS auto-netting rule.
- A successful end-to-end test covering aggregation, resultant creation, and SWIFT-suppression treatment.
- Formal UAT acceptance.