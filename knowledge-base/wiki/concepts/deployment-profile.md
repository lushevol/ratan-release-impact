---
type: concept
title: Deployment Profile
created: 2026-08-24
updated: 2026-08-24
tags: [deployment, configuration, continuous-delivery, architecture]
related: [cash-settlement-platform, deployment-cd-script, cash-settlement-dc-failover-strategy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Active-Active to Active-Passive.md"]
---
# Deployment Profile

A deployment profile is an environment-specific configuration set used to deploy the Cash Settlement Platform.

Option-1 maintains one profile and uses VIP switching to direct applications to the active data centre. Option-2 maintains two profiles separately for two clusters and requires the deployment CD script to support both profiles in one CD deployment.

The source does not define profile contents, validation, promotion, rollback, ownership, or drift detection. Separate profiles therefore introduce a configuration-consistency concern that requires explicit release controls.
