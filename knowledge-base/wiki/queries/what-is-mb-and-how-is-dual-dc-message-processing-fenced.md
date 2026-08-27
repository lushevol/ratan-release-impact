---
type: query
title: What Is MB and How Is Dual-Data-Centre Message Processing Fenced?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, mb, messaging, fencing, active-active]
related: [mb, message-racing-prevention-in-dual-dc-deployments, cash-settlement-dc-failover-strategy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Active-Active to Active-Passive.md"]
---
# What Is MB and How Is Dual-Data-Centre Message Processing Fenced?

The source states that MB startup must be manually restricted under Option-2 to avoid message racing, but it does not define MB.

## Evidence Needed

- The expanded name and ownership of MB.
- The messages, queues, brokers, or workflows it processes.
- The rule for selecting the active data centre.
- Automated fencing, lease, leader-election, or consumer-exclusivity controls.
- Handling of duplicate, delayed, and in-flight messages during failover.
- Monitoring and operator evidence that only one site is processing.

Until these details are confirmed, the two-profile design should not be treated as a validated Active-Active architecture.
