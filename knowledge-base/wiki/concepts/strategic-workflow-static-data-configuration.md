---
type: concept
title: Strategic Workflow Static-Data Configuration
tags: [strategic-workflow, fmrp, static-data, nostro, swift, bridge-account]
related: [fmrp, bcs-strategic-workflow-migration, manual-entity-go-live-static-data-controls, ebbs-accounting-configuration, swift]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Migrating BCS to Strategic Workflow.md"]
---
# Strategic Workflow Static-Data Configuration

## Definition

Strategic Workflow static-data configuration is the requirement to configure in FMRP the settlement and messaging values used by the legacy and Strategic flows.

## Listed Configuration

The source identifies the following items:

- Nostro static.
- Currency cut-off.
- Branch-code mapping.
- Bridge account.
- Swift-related BICs for the sender, `53`, and `58`.

## Parity and Ownership

The source states that legacy and Strategic flows share the same static data while also requiring configuration in FMRP. This indicates that shared business values may still require separate system configuration.

The source does not provide authoritative values, configuration ownership, environment, deployment status, or evidence that FMRP configuration is complete.