---
type: concept
title: RATAN Application Health Check
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, health-check, disaster-recovery, eureka, itrs, monitoring]
related: [ratan, ratan-disaster-recovery-failover, incident-investigation]
sources: ["RATAN/RATAN -Service Restart Guide/RATAN DR Plan.md"]
---
# RATAN Application Health Check

## Definition

A RATAN application health check is a layered validation of service placement, user-interface availability, messaging and monitoring state, and transaction-failure indicators during DR failover.

## Required signals

The DR plan identifies these checks:

- Eureka service placement on the expected node or site.
- Accessibility of the FMO MFE login interface.
- Green ITRS status for Solace, Kafka, service monitoring, and transaction failures.
- Node-specific health checks after network isolation and reinstatement.
- RATAN EOD confirmation from ETL squads during ARK→WAT.
- Communication of readiness and verification completion in Group Chat.

## Limitations

The runbook does not specify:

- The complete expected Eureka service inventory.
- Quantitative thresholds for ITRS status.
- Named business transactions to execute.
- Who authorizes a pass or failure.
- Rollback criteria.
- The exact meanings of A, B, P, and S node labels.

Screenshots are supporting evidence only and should not replace live status checks or approved monitoring records.