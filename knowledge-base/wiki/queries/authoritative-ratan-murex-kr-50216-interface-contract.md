---
type: query
title: What Is the Authoritative RATAN-Murex KR 50216 Interface Contract?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, murex-kr, interface-contract, mq, sftp, kafka, documentation-quality]
related: [ratan-murex-kr-mt-to-mx-interface, ratan-interface-architecture, ratan-interface-inventory, ratan-enisis-swift-interface, murex-kr, enisis]
sources: ["RATAN/RATAN -Interfaces/Ratan and Murex KR 50216.md"]
---
# What Is the Authoritative RATAN-Murex KR 50216 Interface Contract?

## Question

What is the authoritative, production-approved contract for the Murex KR to RATAN to ENISIS flow documented under interface 50216?

## Evidence currently available

The source describes the high-level flow:

```text
Murex KR → MQ → RATAN → SFTP → ENISIS
```

It also lists Kafka topics:

```text
KR_MXG_SWF_ACK
KR_MXG_SWF_IN
Swift_MX_ENISIS_Out
KR_MXG_SWF_IN_Internal
```

However, it does not explain whether Kafka is part of the runtime flow, an operational monitoring path, or a parallel integration. The source’s `Connection details`, `Interface Specification`, `Other Useful Docs`, and `Known Issues` sections are empty. Its status field is also blank despite review metadata and guidance referring to publication after review.

## Information needed to resolve the question

- MQ queue names, endpoints, and ownership.
- SFTP endpoints, directories, authentication, and file conventions.
- MT, MxML, payment XML, and MX schemas.
- ACK semantics, retry policy, timeout behavior, and failure notifications.
- Kafka topic direction, ownership, schemas, retention, and relationship to MQ and SFTP.
- Replay eligibility, idempotency, duplicate prevention, and audit requirements.
- The authoritative source and reconciliation rules for missing ENISIS payments.
- The meaning and lifecycle of `COMP` in `ratan_cashflow_group_management_service.ratan_trade`.
- Confirmation of publication status and current operational ownership.

## Related pages

This query should be considered alongside [[concepts/ratan-enisis-swift-interface]], [[concepts/ratan-interface-architecture]], [[concepts/ratan-interface-inventory]], and [[entities/murex-kr]]. It concerns the Korea-specific Murex flow and should not be used as a generic contract for other Murex integrations.
