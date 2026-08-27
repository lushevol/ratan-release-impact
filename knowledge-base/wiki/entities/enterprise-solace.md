---
type: entity
title: ENTERPRISE_SOLACE
created: 2026-08-24
updated: 2026-08-24
tags: [enterprise-solace, solace, rdm, messaging, manifest, ratan]
related: [solace, ratan-indonesia-network-segmentation, cash-settlement-platform]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design/Indonesia Upstream Downstream Details.md"]
---
# ENTERPRISE_SOLACE

## Role

`ENTERPRISE_SOLACE` provides the RDM real-time messaging integration for RATAN Indonesia. It uses port `55443` and is onboarded through Manifest rather than NSSR.

## Manifest declaration

```text
- sourceitam: 51358
  sourceinfra: LAN
  destinationitam: 51080
  destinationinfra: LAN
  destinationservice: FD
```

The source records destination ITAM `51080`, source ITAM `51358`, and destination service `FD`.

## Connectivity status

The source records `TCP_FAIL` for staging connectivity checks. The failure reason and production approval status are not specified.