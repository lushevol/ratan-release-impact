---
type: concept
title: RATAN Disaster Recovery Automation
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, disaster-recovery, dr, vip, redis, rto, rpo]
related: [ratan-ktlo-tracker, redis, ratan-interface-architecture]
sources: ["RATAN/RATAN -KTLO Tracker/RATAN -KTLO Tracker.md"]
---
# RATAN Disaster Recovery Automation

RATAN disaster recovery automation is the capability to execute and validate recovery procedures with minimal manual intervention, including VIP activation, dependency health checks, and Redis-outage handling.

## Reported Gaps

GENERIC TASK 7991917 states that PSS must manually start a VIP on the required node during DR and describes this as difficult to manage. The requested outcome is a one-click DR test that allows RATAN to complete DR successfully and meet its RTO and RPO objectives.

STORY 6832041 requests automatic handling of [[entities/redis|Redis]] outages to avoid processing impact. The issue is linked to a DR incident and is expected to be addressed before the next DR exercise.

The tracker also calls for health-check information collection and further investigation involving Irisa, Nick, Dennis, and the network team.

## Required Evidence

The source does not provide RTO or RPO values, test results, recovery measurements, or proof of compliance. Readiness should therefore be established through documented evidence covering:

- VIP activation and failover/failback steps.
- Dependency health checks and gating conditions.
- Redis outage detection, fallback, recovery, and data-consistency behavior.
- Manual steps remaining in the DR runbook.
- Recovery duration and data-loss measurements.
- Ownership, escalation, and operator permissions.
- Results from repeatable DR exercises.

The one-click DR objective is a proposed enhancement, not evidence that automation or RTO/RPO compliance has already been achieved.