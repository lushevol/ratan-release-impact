---
type: source
title: Ratan and FMSGW 54949
authors: [Yunzhe Ta, Junying Jiang, Pengpeng Li]
year: 2026
url: ""
venue: "RATAN interface inventory"
tags: [ratan, fmsgw, swift, solace, settlement, interface-inventory]
related: [fmsgw, ratan, swift, solace, ratan-fmsgw-settlement-messaging, operational-level-agreement]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and FMSGW 54949.md"]
---
# Ratan and FMSGW 54949

## Summary

This interface-inventory entry documents a high-level settlement-message flow from [[entities/ratan|RATAN]] to [[entities/fmsgw|FMSGW]] through [[entities/solace|Solace]]. RATAN generates SWIFT MT and MX messages in real time and sends them to FMSGW for settlement.

The source identifies interface `54949`, but it does not provide a complete technical or operational contract. Connection details, interface specifications, support contacts, known issues, troubleshooting steps, message schemas, Solace configuration, delivery semantics, and production status are absent.

## Document Metadata

The source records an update and review date of 2026-01-21. Yunzhe Ta and Junying Jiang are listed as contributors, and Yunzhe Ta and Pengpeng Li are listed as reviewers. The status field is blank even though the document guidance states that reviewed articles should be marked `Published`.

## Documented Data Feeds

| Data Feed | Countries in scope |
| --- | --- |
| RATAN MT real-time messages | CN, MY, IN, SG, UK, DE, HK, TH, TW, US , ID, JP, MU, PH, UAE, ZA, TH |
| RATAN MX real-time messages | MU, UK, CN, UAE, HK, SG, ZA, TW, MY, PH, TH, ID, IN, US, JP, DE |

The MT row contains `TH` twice. The source does not explain whether this is an intentional distinction or a documentation duplication.

## End-to-End Flow

```text
Ratan --(Solace)-->FMSGW
```

The documented purpose is: “RATAN generated Swift message and sent to FMSGW for settlement.”

## Referenced OLA

The entry references the FM Settlement OLA:

[RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA)

The OLA is referenced but not reproduced. Its service commitments, ownership model, escalation procedures, and availability targets should not be inferred from this interface-inventory entry.

## Documentation Gaps

The source leaves the following sections empty or at placeholder text:

- Connection details
- Interface Specification
- Interface team contact
- Other Useful Docs
- Known Issues
- Troubleshooting Steps

Consequently, this source supports the existence and high-level direction of the interface, but not implementation-level or production-readiness claims. See [[queries/what-is-the-authoritative-ratan-fmsgw-interface-contract]].