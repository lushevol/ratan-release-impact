---
type: entity
title: Deployment CD Script
created: 2026-08-24
updated: 2026-08-24
tags: [continuous-delivery, deployment, automation, configuration]
related: [cash-settlement-platform, deployment-profile, cash-settlement-dc-failover-strategy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Active-Active to Active-Passive.md"]
---
# Deployment CD Script

The deployment CD script is the delivery automation identified as requiring revision under Option-2.

The revised script must support one CD deployment for two independently maintained [[deployment-profile]]s. The source does not define the pipeline, promotion controls, rollback behavior, profile validation, or safeguards against configuration drift between data centres.
