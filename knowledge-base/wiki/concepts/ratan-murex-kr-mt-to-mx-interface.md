---
type: concept
title: RATAN-Murex KR MT-to-MX Interface
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, murex-kr, enisis, mt, mx, iso-20022, mq, sftp, payment-processing]
related: [ratan, murex-kr, enisis, mq, swift, ssdr-51507, oscar, ratan-enisis-swift-interface, ratan-interface-architecture, ratan-interface-inventory]
sources: ["RATAN/RATAN -Interfaces/Ratan and Murex KR 50216.md"]
---
# RATAN-Murex KR MT-to-MX Interface

## Overview

The RATAN-Murex KR interface is a Korea-specific integration in which Murex KR provides MT SWIFT messages and MxML or payment XML files to RATAN. RATAN converts the incoming messages into MX, described in the source as ISO 20022, and delivers the output to ENISIS through SFTP.

```text
Murex KR
  │ MT SWIFT messages and MxML/payment XML
  ▼
MQ
  ▼
RATAN
  │ MT-to-MX conversion
  ▼
SFTP
  ▼
ENISIS
```

This page describes the flow documented for interface 50216. It should not be generalized to all Murex integrations or all ENISIS inbound paths.

## System responsibilities

- **Murex KR** originates MT and MxML/payment XML messages and provides a payment report for reconciliation.
- **MQ** transports inbound messages from Murex KR to RATAN.
- **RATAN** performs the MT-to-MX conversion and exposes an MX exception blotter for certain operational recovery actions.
- **SFTP** transports generated MX messages from RATAN to ENISIS.
- **ENISIS** receives the generated MX messages and is also a destination for manual MX drafting when automated delivery fails.
- **SSDR** provides the Murex payment report used during manual reconciliation.
- **Korea FMO** monitors exceptions, coordinates with the PSS or development team, replays eligible messages, reconciles reports, and performs or coordinates manual fallback processing.
- **OSCAR** is an alternative manual payment-drafting destination.

## Failure and recovery boundaries

### Inbound delivery failure

When Murex sends messages but RATAN does not receive them, Murex sends an exception email to Korea FMO. Korea FMO investigates with the PSS or development team. If system recovery is not possible, the payment is manually drafted in ENISIS or OSCAR.

### Invalid source data

For a RATAN Swift exception caused by invalid Murex data, RATAN does not return an ACK to Murex. Murex sends an exception email to Korea FMO, which investigates and uses manual fallback when automated recovery is unavailable.

### RATAN conversion failure

Korea FMO monitors the RATAN MX exception blotter. If the failure is caused by static data or a temporarily unavailable service, the message may be replayed after the underlying issue is corrected. Replay retriggers MT-to-MX conversion. Technical failures that cannot be resolved by replay require manual drafting.

### Downstream delivery failure

If RATAN sends a message but ENISIS does not receive it through SFTP, Korea FMO downloads the Murex payment report from SSDR, extracts MX messages from ENISIS by source system, and compares the two datasets. Missing or failed payments are manually drafted in ENISIS or OSCAR.

### Missing confirmation

For a `Pending Affirmation` cashflow, the documented diagnostic checks for a related `COMP` row in `ratan_cashflow_group_management_service.ratan_trade`:

```sql
select trade_id,trade_state from ratan_cashflow_group_management_service.ratan_trade where trade_id ='*trade id*' and trade_state='COMP'.
```

The source treats a null result as indicating that RATAN did not receive a `COMP` message, but the complete state model and persistence semantics are not documented.

## Interface gaps

The source does not specify:

- MQ queues and connection configuration.
- SFTP endpoints, directories, credentials, or file naming.
- MT, MxML, payment XML, or MX schemas.
- ACK, retry, timeout, and duplicate-handling behavior.
- Replay idempotency and audit controls.
- The role of the listed Kafka topics.
- Reconciliation ownership, frequency, and escalation thresholds.
- The publication status of the document, whose status field is blank.

See [[queries/authoritative-ratan-murex-kr-50216-interface-contract]] for the unresolved contract questions.
