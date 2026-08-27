---
type: source
title: Ratan and EBBS 14147
authors: [Junying Jiang, Yunzhe Ta, Daiqi Wang]
year: 2026
url: ""
venue: "RATAN Interfaces"
tags: [ratan, ebbs, accounting, solace, interface, settlement]
related: [ratan, ebbs, solace, ratan-ebbs-accounting-feed, settlement-accounting, operational-level-agreement, what-is-the-canonical-ratan-to-ebbs-interface-contract, is-the-ratan-to-ebbs-interface-published-and-production-ready]
sources: ["RATAN/RATAN -Interfaces/Ratan and EBBS 14147.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Ratan and EBBS 14147

## Summary

This interface overview describes an intended real-time accounting-message feed from [[ratan]] to [[ebbs]]. RATAN is expected to generate payment-accounting entries and send JSON messages through [[solace]].

The stated end-to-end route is:

```text
Ratan →Central solace ->Ebbs
```

The document frames this capability as an objective of FMRP 2024 H1. It supports an architecture intention, but it does not establish production readiness, delivery guarantees, or a complete interface contract.

## Review and publication status

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| @Junying Jiang @Yunzhe Ta | 2026-01-26 | @Yunzhe Ta @Daiqi Wang | 2026-01-26 | |

The source instructs that status should be updated to `Published` after review, but its Status field is blank. Therefore, the document's authoritative and production status remains unconfirmed.

## Stated integration characteristics

- **Producer:** RATAN
- **Consumer:** eBBS, also written as `EBBS` and `Ebbs` in the source
- **Transport:** Central Solace
- **Payload representation:** JSON
- **Business purpose:** Feed payment-accounting entries to eBBS on a real-time basis
- **Operational reference:** Existing BPMS OLA, stated as requiring no change

## Scope supplied by the source

| country code | Countries in scope |
| --- | --- |
| CN, MY, IN, SG | China, Malaysia, India, Singapore |
| UK, DE | United Kingdom, Germany |
| MU, AE, ID, PH, US, JP, ZA, HK, EG, NP, SA | MAURITIUS,DUBAI,JAKARTA,MANILA,NEWYORK,TOKYO,JOBURG,DIFC,PHILIP FCU, Hong Kong, Egypt, Nepal, Saudi |

This is retained verbatim because the values mix countries, cities, and possible business or booking entities. It should not be used as a canonical country inventory until validated.

## OLA reference

The source refers to the existing BPMS OLA:

[RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA)

It states: “BPMS OLA location, no change required.” The article does not show the applicable targets, support owner, escalation path, service hours, or rationale for applying that OLA to this interface.

## Missing contract details

The source contains no documented:

- JSON schema, example payload, field definitions, or schema-version policy
- Event trigger, message identifier, or correlation identifier
- Solace topic, queue, subscription, environment, or ownership details
- Authentication, authorization, or encryption requirements
- Delivery semantics, ordering, retry, idempotency, duplicate handling, or dead-letter process
- Latency definition or measurement for “real time”
- Monitoring, alerting, reconciliation, troubleshooting, or interface-team contact
- Change-management process or confirmed go-live evidence

The Interface Specification section only references `attachments/image-2026-1-26_10-46-38.png`; its contents are not available in the supplied source text.

## Related wiki pages

This source adds a concrete flow to [[ratan-interface-architecture]] and should be considered when maintaining [[ratan-interface-inventory]] and [[settlement-accounting]]. Its missing technical and operational details are tracked in [[what-is-the-canonical-ratan-to-ebbs-interface-contract]].