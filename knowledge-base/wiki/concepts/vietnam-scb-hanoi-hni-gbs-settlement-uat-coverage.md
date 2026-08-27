---
type: concept
title: Vietnam SCB Hanoi HNI(GBS) Settlement UAT Coverage
created: 2026-08-23
updated: 2026-08-23
tags: [uat-coverage, settlement, vietnam, fmsgw, manual-entities, settlement-day-2]
related: [vietnam-scb-hanoi-hni-gbs, country-specific-settlement-uat-coverage, manual-entity-settlement-onboarding, fmsgw-inbound-message-routing, ratan-fmsgw-amh-settlement-message-routing, mt103-mt202cov-acknowledgement-sequencing, mt202cov-ack-dependent-release, back-valued-message-queue, high-value-payment-queue, manual-cancellation-queue, fmsgw-duplicate-message-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/012 VIETNAM SCB HANOI HNI(GBS).md"]
---

# Vietnam SCB Hanoi HNI(GBS) Settlement UAT Coverage

## Definition

This concept represents the entity-specific UAT coverage recorded for Vietnam SCB Hanoi HNI(GBS) in the manual-entity Settlement Day 2 enablement scope. It should not be generalized as evidence that every FMSGW settlement path is validated.

## Coverage matrix

| Area | Status | Interpretation |
|---|---|---|
| MT103 and MT202 COV inbound routing | Pass | The source reports delivery to AMH and an ACK to RATAN. |
| MT202 COV release after MT103 ACK | Pass | The positive ACK-dependent release path was reported as successful. |
| MT202 inbound routing | Pass | The source reports delivery to AMH and an ACK to RATAN. |
| MT192/292 scenario | Pass | The source reports a passing scenario, although the supplied evidence shows MT103 paired with MT192 and does not show a separate MT292. |
| Back value-dated handling | Pass | Queue placement, validation-failure detail, ACK, and notification were expected and reported as passing; the payload evidence is ambiguous. |
| DEF-rule high-value payment | Descoped | No production scenario was available. |
| Cancelled trade after original release | Descoped | No production scenario was available. |
| MTn92 manual cancellation | Descoped | No production scenario was available. |
| Duplicate payment processing | Descoped | No production scenario was available. |
| Test case 5 | Missing from source | The numbering jumps from 4 to 6, and the intended scope is unknown. |

## Interpretation

The evidence supports the successful positive-path routing of several inbound message scenarios for this entity. It also supports the positive case in which an MT202 COV is released after its related MT103 receives a successful ACK.

The four descoped scenarios are unvalidated coverage, not failures. In particular, this document cannot establish whether high-value approval, cancellation, MTn92 processing, or duplicate-message handling works in production or in another test environment.

The terms “RATAN” and “inbound system” are used inconsistently for ACK destinations. The source suggests RATAN is the inbound system in the principal flow, but this should be confirmed before treating the terminology as normative.