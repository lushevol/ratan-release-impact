---
type: entity
title: GHANA SCB GHANA ACC(GBS)
created: 2026-08-23
updated: 2026-08-23
tags: [manual-entity, settlement, uat, ghana, scb, gbs]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--1nt2e1n, manual-entity-settlement-enablement, manual-entity-settlement-onboarding, country-specific-settlement-uat-coverage, ratan, fmsgw, amh]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/008 GHANA SCB GHANA ACC(GBS).md"]
---
# GHANA SCB GHANA ACC(GBS)

## Identity

**GHANA SCB GHANA ACC(GBS)** is a manual settlement entity covered by UAT for the manual-entity settlement enablement capability. The source tests its integration through [[entities/fmsgw]], with settlement messages originating from [[entities/ratan]] and downstream delivery to [[entities/amh]].

## UAT status

All listed UAT scenarios are recorded as **Pass**. The source provides Ghana-specific evidence rather than a general guarantee for all manual settlement entities.

## Tested message and workflow scope

- Standard inbound routing for `MT103/202COV`, `MT202`, and `MT192/292`.
- ACK return from `FMSGW` to `RATAN`.
- ACK-dependent release of `MT202COV` after successful ACK of the associated `MT103`.
- Back value-dated message handling through the Back Valued Messages Queue.
- `DEF`-rule high-value payment handling for `MT103` and `MT202`.
- Cancelled-trade handling through the Manual Cancellation Queue.
- Manual processing of `MTn92` messages.
- Duplicate-message processing for `MT103`, `MT202`, and `MT202COV`.

## Evidence boundaries

The UAT record does not specify the environment, release version, execution date, tester, message identifiers, rule thresholds, notification content, or failure and retry behavior. It also contains no test case 5; the numbering moves from 4 to 6.
