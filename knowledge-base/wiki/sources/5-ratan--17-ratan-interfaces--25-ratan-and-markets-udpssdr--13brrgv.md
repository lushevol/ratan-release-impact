---
type: source
title: Ratan and Markets UDP (SSDR)
authors: [Yunzhe Ta, Zhenzhen Liu, Junying Jiang, Jie Cai]
year: 2026
url: ""
venue: "Confluence"
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, markets-udp, ssdr, pv-data, settlement, interface]
related: [ratan-markets-udp-pv-integration, marketudp, ssdr-51507, ovv, solace, sabre, valuation-data-ver-his, what-is-the-authoritative-ratan-markets-udp-pv-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and Markets UDP（SSDR）.md"]
---
# Ratan and Markets UDP (SSDR)

## Summary

This source describes the integration between [[entities/ratan]] and [[entities/marketudp]] for retrieving present-value (PV) data. RATAN uses the retrieved data for P&L and PV-impact calculations, then generates CnA exceptions for user review in the exception blotter.

The documented flow is event-then-fetch: [[entities/ovv]], a service within Markets UDP, sends a readiness notification to RATAN through [[entities/solace]], after which RATAN fetches the PV data through the Markets UDP API.

## End-to-End Flow

```text
Sabre feed
  -> OVV within Markets UDP
  -> Solace notification to RATAN when PV data is ready
  -> RATAN fetches PV data through Markets UDP API
  -> RATAN calculates P&L / PV impact
  -> RATAN generates CnA exceptions
  -> User reviews exceptions in the exception blotter
```

The source does not provide the API endpoint, request or response schema, authentication contract, Solace subject, notification payload, correlation mechanism, retry behavior, or CnA exception rules.

## Expected Processing Windows

The source provides the following timing data verbatim:

| | **Expected Timing Sabre Feed to ****OVV**** (Market UDP)** | **Expected Timing Ratan to generate exceptions** |
| --- | --- | --- |
| **Batch 1** | T 03:00 PM SGT (6:00AM UTC) | T 04:00 PM SGT (7:00AM UTC) |
| **Batch 2** | T 03:00 PM UKT (2:00PM UTC) | T 04:00 PM UKT (3:00PM UTC) |
| **Batch 3** | T 03:00 PM UST (6:00PM UTC) | T 04:00 PM UST (7:00PM UTC) |
| **Batch EOD** | T+1 00:00AM UTC | T+1 01:00AM UTC to get the previous version trade's PV •The PV from this EOD file is for Ratan to get the previous version trade's PV when calculate PV impact |

The timing table suggests an approximately one-hour interval between the upstream feed to OVV and RATAN’s exception generation. The meanings of `UKT` and `UST` should be confirmed before treating these times as operational SLA commitments.

The EOD batch has a distinct purpose: its PV data is used to obtain the previous version of a trade’s PV when calculating PV impact.

## Operational Dependency and Risk

For the `VALUATION_DATA_VER_HIS` view, the source notes that Sabre may have a Friday release. If MRB release activities occur on Friday, the Sabre team is expected to provide advance notification of a potential delay. This activity may affect the Friday readiness of `VALUATION_DATA_VER_HIS`.

The source identifies the risk but does not specify its frequency, recovery procedure, monitoring owner, or escalation policy.

## Interface Specification

The source includes an image link, but no machine-readable interface details were available in the extracted content:

![Interface specification](https://confluence.global.standardchartered.com/download/attachments/3449110848/image-2025-9-15_14-11-49.png?version=1&modificationDate=1757916710000&api=v2)

## OLA Reference

The source states:

> BPMS OLA location, no change required

It references the following document:

[RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA)

No OLA targets, service hours, incident priorities, ownership, or escalation obligations are included in this source.

## Review Metadata

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| @Yunzhe Ta @Zhenzhen Liu @Junying Jiang | 2026-01-28 | @Yunzhe Ta @Jie Cai | 2026-01-28 | |

The surrounding text says that status should be updated to `Published` after review, but the status field is blank. Publication status is therefore unresolved.

## Source Limitations

The source does not establish whether `SSDR`, `Market UDP`, and `Markets UDP` are separate systems, interface identifiers, or naming variants. It also does not define the exact relationship between SSDR and Markets UDP.
