---
type: entity
title: FileIT
created: 2026-08-23
updated: 2026-08-24
tags: [file-transfer, integration, cash-settlement, accounting, ratan, reference-data]
related: [ratan, aspire, fileit-solace-transfer-notifications, accounting-aspire-execution, accounting-file-delivery-acknowledgement, ebbs, brdm, brdm-bank-code-ingestion, fileit-file-arrival-notification, 5-ratan--17-ratan-interfaces--20-ratan-and-brdm-51330--1bpyud7]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Aspire Accounting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Settlement Accounting for Aspire Tech design.md", "RATAN/RATAN -Interfaces/Ratan and BRDM 51330.md"]
---
# FileIT

## Cash-settlement and accounting integration

### Functional-requirements description

The functional-requirements source describes FileIT as the managed file-transfer service used to deliver RATAN Aspire payment-accounting files. RATAN submits a transfer request through Solace, and FileIT can publish lifecycle notifications for acceptance, initiation, success, and failure.

That source states that FileIT mapping already exists in production and will be extended on the change-request day. It does not establish the required RATAN response to each notification or whether source files must be retained after delivery. See [[fileit-solace-transfer-notifications]].

### Technical-design description

The technical-design source describes FileIT as the proposed file-transfer integration used to copy accounting transaction files after generation.

The design expects FileIT to return a response that updates an [[accounting-aspire-execution]] record. Example outcomes include `response_code = 2000`, `response_desc = SUCCESS`, and acknowledgement states `ACKED` or `NACK`.

The technical-design source does not define a FileIT request schema, response payload, correlation identifier, duplicate handling, timeout behavior, or NACK recovery procedure.

## BRDM bank-code route

The RATAN and BRDM source identifies FileIT as the intermediate integration component in the documented high-level bank-code route from [[brdm]] to [[ratan]]:

```text
BRDM → FileIT → Ratan
```

This source establishes only FileIT's position in that route. It does not state whether FileIT performs file transfer, file-arrival notification, polling, transformation, validation, or replay for this feed.

The documented BRDM route must not be assumed to use the same mechanics as other FileIT-related integrations, including [[fileit-file-arrival-notification]], without an authoritative interface contract.