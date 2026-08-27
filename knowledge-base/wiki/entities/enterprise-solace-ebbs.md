---
type: entity
title: ENTERPRISE_SOLACE_EBBS
created: 2026-08-24
updated: 2026-08-24
tags: [enterprise-solace, ebbs, rdm, messaging, manifest, ratan]
related: [solace, ratan-indonesia-network-segmentation, cash-settlement-platform]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design/Indonesia Upstream Downstream Details.md"]
---
# ENTERPRISE_SOLACE_EBBS

## Role

`ENTERPRISE_SOLACE_EBBS` supports EBBS and RDM messaging integration for RATAN Indonesia. It uses port `55443` and requires Manifest-based onboarding.

## Manifest declaration

```text
- sourceitam: 51358
  sourceinfra: LAN
  destinationitam: 51080
  destinationinfra: LAN
  destinationservice: FD
```

## Connectivity status

The source records `TCP_FAIL` for staging checks involving the `ENTERPRISE_SOLACE_EBBS` endpoints. It does not identify whether the failure is caused by firewall status, endpoint configuration, staging restrictions, or service availability.