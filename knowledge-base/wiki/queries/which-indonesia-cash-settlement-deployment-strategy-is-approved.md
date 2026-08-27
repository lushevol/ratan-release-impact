---
type: query
title: Which Indonesia Cash Settlement Deployment Strategy Is Approved?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, cash-settlement, indonesia, architecture-decision, active-passive, active-active]
related: [cash-settlement-platform, cash-settlement-dc-failover-strategy, controlled-dc-switchover, deployment-profile]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Active-Active to Active-Passive.md"]
---
# Which Indonesia Cash Settlement Deployment Strategy Is Approved?

The architecture note compares a one-profile VIP-based Active-Passive design with a two-profile isolated-cluster design, but it does not identify an approved option.

## Decision Evidence Needed

- The approving authority and decision date.
- Whether the target state is strictly Active-Passive or controlled Active-Active.
- Required RTO, RPO, availability, and failover-duration criteria.
- Message ownership and fencing requirements.
- Profile-management, release, rollback, and drift-control requirements.
- Failover test results and operational runbook ownership.

An ADR should be created only when approval evidence and acceptance criteria are available.
