---
type: concept
title: RATAN-to-FMSGW Settlement Messaging
tags: [ratan, fmsgw, settlement, swift, mt, mx, solace, interface]
related: [ratan, fmsgw, swift, solace, ratan-settlement, ratan-interface-inventory, ratan-interface-architecture, what-is-the-authoritative-ratan-fmsgw-interface-contract, is-thailand-duplicated-in-the-ratan-fmsgw-mt-country-scope]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and FMSGW 54949.md"]
---
# RATAN-to-FMSGW Settlement Messaging

## Definition

RATAN-to-FMSGW settlement messaging is the documented flow in which [[entities/ratan|RATAN]] generates real-time SWIFT messages and sends them to [[entities/fmsgw|FMSGW]] for settlement through [[entities/solace|Solace]]. The source identifies this integration as interface `54949`.

```text
Ratan --(Solace)-->FMSGW
```

## Feed and Country Scope

The source distinguishes MT and MX feeds and records the following country coverage:

| Data Feed | Countries in scope |
| --- | --- |
| RATAN MT real-time messages | CN, MY, IN, SG, UK, DE, HK, TH, TW, US , ID, JP, MU, PH, UAE, ZA, TH |
| RATAN MX real-time messages | MU, UK, CN, UAE, HK, SG, ZA, TW, MY, PH, TH, ID, IN, US, JP, DE |

Both rows appear to contain the same 16 unique country codes. The MT row lists `TH` twice, but the source does not establish whether that repetition is meaningful or erroneous. This is tracked in [[queries/is-thailand-duplicated-in-the-ratan-fmsgw-mt-country-scope]].

## What This Source Establishes

- RATAN is the producing application.
- FMSGW is the receiving application or gateway.
- Solace is the named transport.
- The stated business purpose is settlement.
- The feed categories are SWIFT MT and SWIFT MX.
- The source provides country lists for each feed.

## What This Source Does Not Establish

“Real-time” is not defined as a latency target, service-level commitment, processing mode, or delivery guarantee. The source also omits:

- Specific MT message types and MX business message definitions
- Payload schemas and validation rules
- Solace topics, queues, endpoints, and security configuration
- Acknowledgement, retry, replay, dead-letter, and idempotency behavior
- Monitoring, alerting, support ownership, and escalation paths
- Country-level rollout or production status
- The formal role and ownership of FMSGW

This is therefore an interface summary, not a complete authoritative technical contract. The contract question remains open in [[queries/what-is-the-authoritative-ratan-fmsgw-interface-contract]].