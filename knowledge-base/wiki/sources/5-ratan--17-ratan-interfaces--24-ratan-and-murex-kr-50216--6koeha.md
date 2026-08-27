---
type: source
title: Ratan and Murex KR 50216
authors: ["Yunzhe Ta", "Zhenzhen Liu", "Junying Jiang"]
year: 2026
url: "https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA"
venue: "Internal RATAN interface documentation"
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, murex-kr, enisis, mq, sftp, swift, iso-20022, interface]
related: [ratan, murex-kr, enisis, ssdr-51507, swift, ratan-murex-kr-mt-to-mx-interface, ratan-operational-resilience-plans, authoritative-ratan-murex-kr-50216-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and Murex KR 50216.md"]
---

# Ratan and Murex KR 50216

## Source status and review metadata

The document records updates by Yunzhe Ta, Zhenzhen Liu, and Junying Jiang on 2026-01-28. It records review by Yunzhe Ta and Pengpeng Li on the same date. The `Status` field is blank, although the surrounding guidance says that the status should be changed to `Published` after review.

## Description

Murex KR sends MT and MxML messages to RATAN through MQ. RATAN converts the messages to MX format, described as ISO 20022, and transmits the resulting messages to ENISIS through SFTP.

## End-to-end data flow

```text
[MX KR]
   │
   ▼
MT SWIFT Messages & Payment XML Files
   │
   ▼
Via MQ → [Ratan]
   │
   ▼
Ratan converts messages from MT to MX (ISO 20022) format
   │
   ▼
Via SFTP → [ENISIS]
```

The documented flow is high-level. Connection details and the interface specification are empty, so the source does not establish queue names, SFTP endpoints, directories, authentication, schemas, acknowledgements, schedules, retry behavior, or service-level targets.

## Interface contacts

| Role | Contact |
| --- | --- |
| Murex Korea lead | [JaeHyeon.Oh@sc.com](mailto:JaeHyeon.Oh@sc.com) |
| KR Murex support | [SCBK.FM_Support@sc.com](mailto:SCBK.FM_Support@sc.com) |

## OLA

The source refers to the BPMS OLA without requiring a change:

[RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA)

## Related Kafka topics

The source lists the following topics but does not specify their ownership, direction, producers, consumers, schemas, retention, environment, or relationship to the documented MQ and SFTP flow:

```text
KR_MXG_SWF_ACK
KR_MXG_SWF_IN
Swift_MX_ENISIS_Out
KR_MXG_SWF_IN_Internal
```

## Troubleshooting procedures

### Murex sends MT and MxML, but RATAN does not receive them

Murex sends an exception email to Korea FMO. Korea FMO consults the PSS or development team to identify the issue. If the payment cannot be resumed by the system because of a technical issue, the fallback is to manually draft the MX message in ENISIS or draft the payment in [[entities/oscar]].

### RATAN Swift exception caused by invalid Murex data

RATAN does not return an ACK to Murex. Murex sends an exception email to Korea FMO, which investigates with the PSS or development team. If the payment cannot be resumed automatically, the fallback is manual drafting in ENISIS or [[entities/oscar]].

This behavior is documented for invalid Murex data and should not automatically be generalized to every RATAN interface failure.

### RATAN Swift-generation exception

Korea FMO monitors exceptions in the RATAN MX exception blotter and consults the PSS or development team to determine the cause.

If the exception resulted from incorrect static data or a temporarily unavailable service, Korea FMO may correct the static data or wait for service recovery and then replay the message from the MX exception blotter. Replay retriggers the MT-to-MX conversion.

If replay does not resolve the technical issue, the fallback is manual drafting in ENISIS or [[entities/oscar]].

The source does not define replay eligibility, idempotency, duplicate prevention, or audit requirements.

### RATAN sends a message, but ENISIS does not receive it through SFTP

1. Murex extracts the payment report and sends it to [[entities/ssdr-51507]].
2. Korea FMO downloads the report from SSDR.
3. Korea FMO manually extracts MX messages from ENISIS by source system.
4. Korea FMO operations compares the Murex payment report with the ENISIS extraction and identifies discrepancies.
5. Missing or failed payments are manually drafted in ENISIS or [[entities/oscar]].

The source does not define the authoritative record, report fields, reconciliation frequency, or escalation threshold.

## Missing confirmation-message diagnostic

For a cashflow that failed or was suppressed as a `Pending Affirmation` exception and was not processed by the system, the source recommends checking whether the related `COMP` message was received by RATAN.

The exact query is:

```sql
select trade_id,trade_state from ratan_cashflow_group_management_service.ratan_trade where trade_id ='*trade id*' and trade_state='COMP'.
```

The source states that a null result indicates that no `COMP` message was received by RATAN. This interpretation is operational guidance rather than a complete proof of non-receipt because the source does not define the full `trade_state` lifecycle, retention behavior, duplicate handling, or asynchronous-processing semantics.

## Evidence and limitations

The end-to-end flow and troubleshooting actions are explicitly documented, providing moderate evidence for the described operational practice. The Kafka topic association is weaker because the source provides names without implementation details. The SQL procedure is concrete, but the broader interpretation of a null result requires confirmation against the underlying data model and persistence behavior.

The blank status, empty connection-details section, empty interface-specification section, and empty known-issues section mean that this document should not be treated as a complete or formally published interface contract.

## Related wiki context

This Korea-specific flow extends the broader RATAN interface inventory and is related to [[concepts/ratan-enisis-swift-interface]], [[concepts/ratan-interface-architecture]], [[concepts/ratan-interface-inventory]], and [[concepts/ratan-operational-resilience-plans]]. It should remain distinct from other Murex or ENISIS integrations.
