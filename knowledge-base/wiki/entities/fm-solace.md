---
type: entity
title: FM Solace
created: 2026-08-24
updated: 2026-08-24
tags: ["messaging", "integration", "settlement", "solace", "ola", "settlement-integration", "korea-migration", "fm-solace", "ratan", "indonesia", "disaster-recovery", "transport", "production"]
related: ["ratan", "operational-level-agreement-for-settlement-interfaces", "korea-ratan-settlement-migration", "ratan-pss", "enisis", "ratan-enisis-fm-solace-integration", "what-is-the-final-ratan-enisis-fm-solace-header-contract", "solace", "cash-settlement-platform", "cash-settlement-dc-failover-strategy", "ratan-indonesia-network-segmentation", "ratan-srack-subnet-connectivity", "ratan-enisis-swift-interface"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Korea OLA and other release related DOCs.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/RATAN to ENISIS.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design/Indonesia Upstream Downstream Details.md", "RATAN/RATAN -Interfaces/Ratan and ENISIS 50157.md"]
---
# FM Solace

FM Solace is the messaging transport named for the Korea PROD connection between [[ratan]] and [[enisis]].

It carries the MX and MT publication flows from RATAN to ENISIS and the corresponding MX and MT ACK/NACK flows from ENISIS back to RATAN.

## Documented transport settings

All four documented channels specify a maximum bind count of `6`, maximum spool usage of `300 MB`, and `Reject-msg-to-sender-on-discard` set to `Y`. The source documents an expected average volume of `100` messages per day, peak volume of `2000` messages per day, and maximum message size of `15K`.

The source does not define FM Solace tenancy, endpoint addresses, authentication, authorization, encryption, subscription configuration, or whether the stated parameters are observed production limits or planning assumptions.