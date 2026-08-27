---
type: entity
title: OLTP
created: 2026-08-23
updated: 2026-08-25
tags: ["oltp", "accounting", "real-time", "cash-settlement", "korea", "settlement", "interface-reference", "integration", "posting", "acknowledgement", "reconciliation", "core-banking", "downstream-system"]
related: ["korea-cash-settlement-migration", "ratan", "korea-ratan-settlement-migration", "tlm", "ebbs", "accounting-posting-statuses", "korea-accounting-reconciliation", "korea-ratan-oltp-accounting-integration", "oltp-accounting-message-contract", "ratan-accounting-status-lifecycle", "oltp-eod-accounting-exception-handling", "kredmi", "fm-solace", "ratan-oltp-korea-accounting-feed", "what-is-the-authoritative-ratan-oltp-interface-contract"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Korea OLA and other release related DOCs.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Korea Accounting Recon - RATAN- TLM.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Korea Cashflow Migration -Ratan to OLTP Accounting.md", "RATAN/RATAN -Interfaces/Ratan and OLTP.md"]
---

# OLTP

OLTP is expanded as **On Line Transaction Posting** in the **Ratan and OLTP** interface source.

## Role and Scope

The **Korea Cashflow Migration - Ratan to OLTP Accounting** source describes OLTP as the downstream Korean core-banking accounting consumer in the [[korea-ratan-oltp-accounting-integration]]. It receives real-time accounting messages from [[RATAN]], validates `TRANDATA` posting and reconciliation data, and responds with an ACK or NACK.

The **Ratan and OLTP** interface source describes OLTP as the downstream consumer of RATAN Korea accounting messages in the documented normal processing path. In that source, OLTP receives and validates accounting JSON forwarded by [[kredmi]]. It returns an acknowledgement when it successfully consumes an accounting entry, or an error code when it cannot consume the entry.

The Korea cash-settlement migration source identifies OLTP as the downstream system for RATAN real-time accounting and lists an OLTP development contact.

The Korea OLA and release-related documents source refers to OLTP as the subject of a RATAN interface reference. That source does not establish that OLTP is within the Korea migration scope.

## Documented Processing Path

According to the **Ratan and OLTP** interface source, the normal topology is:

`RATAN → FM Solace → KREDMI → OLTP → KREDMI → FM Solace → RATAN`

This topology is source-specific and does not alter the separate **Korea Cashflow Migration - Ratan to OLTP Accounting** description of OLTP receiving real-time accounting messages from RATAN.

## Accounting Messages and Acknowledgements

According to the **Korea Cashflow Migration - Ratan to OLTP Accounting** source:

- An OLTP ACK moves the RATAN accounting record to `SUCCESS`.
- A NACK, including validation and processing errors `TXN00001` through `TXN00063`, results in `REJECTED`.

The **Ratan and OLTP** interface source likewise states that RATAN records successful OLTP consumption as `SUCCESS` and an OLTP error outcome as `REJECTED`.

The Korea accounting reconciliation requirement represents OLTP outcomes using the following acknowledgement statuses:

| Status | Meaning |
|---|---|
| `SUCCESS` | OLTP acknowledgement indicates successful processing. |
| `REJECTED` | OLTP acknowledgement indicates rejection. |
| `SENT` | No OLTP response has yet been received. |

The same reconciliation requirement states that [[TLM]] is intended to reconcile these outcomes using records retrieved from [[RATAN]].

## End-of-Day Processing and Exceptions

The **Korea Cashflow Migration - Ratan to OLTP Accounting** source states that, during the 23:30–00:30 KST EOD interval, connectivity or timeout exceptions are routed for manual operational handling rather than automatic retry. See [[oltp-eod-accounting-exception-handling]].

Separately, the **Ratan and OLTP** interface source states that, during the 11:30–12:30 KST EOD window, OLTP is not shown in the processing path; [[kredmi]] instead returns a NACK to RATAN.

## Available Detail and Source-Specific Gaps

The Korea cash-settlement migration source provides no accounting message structure, processing guarantees, ownership model, or operational status.

The Korea OLA and release-related documents source does not describe OLTP's interface behavior, message contract, operational ownership, or readiness status.

The Korea accounting reconciliation requirement does not define the OLTP acknowledgement API or its operational retry behavior. The separate **Korea Cashflow Migration - Ratan to OLTP Accounting** source does describe ACK/NACK outcomes and manual handling for EOD connectivity or timeout exceptions.

The **Ratan and OLTP** interface source does not provide OLTP endpoints, queue or topic names, payload schemas, acknowledgement formats, error-code catalogues, retry behavior, or support ownership. These omissions are tracked in [[what-is-the-authoritative-ratan-oltp-interface-contract]].