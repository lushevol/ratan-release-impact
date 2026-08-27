---
type: entity
title: MQ
created: 2026-08-25
updated: 2026-08-25
tags: [messaging, middleware, ratan, murex-kr]
related: [ratan, murex-kr, enisis, ratan-murex-kr-mt-to-mx-interface]
sources: ["RATAN/RATAN -Interfaces/Ratan and Murex KR 50216.md"]
---
# MQ

## Role in the interface

MQ is the documented inbound transport between Murex KR and RATAN. Murex KR sends MT and MxML or payment XML messages through MQ to RATAN for processing.

The source does not provide queue names, connection details, delivery guarantees, acknowledgement semantics, retry rules, or ownership information.

## Boundary

```text
Murex KR → MQ → RATAN
```

The source also lists Kafka topics associated with troubleshooting, but it does not establish whether those topics implement, monitor, or supplement the MQ path. See [[queries/authoritative-ratan-murex-kr-50216-interface-contract]].
