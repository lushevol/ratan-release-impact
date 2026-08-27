---
type: concept
title: RATAN-OLTP Korea Accounting Feed
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, oltp, korea, accounting-feed, real-time-messaging, integration]
related: [ratan, oltp, kredmi, fm-solace, murex-kr, settlement-accounting, ratan-accounting-status-lifecycle, what-is-the-authoritative-ratan-oltp-interface-contract, how-does-ratan-oltp-handle-eod-nacks]
sources: ["RATAN/RATAN -Interfaces/Ratan and OLTP.md"]
---
# RATAN-OLTP Korea Accounting Feed

The RATAN-OLTP Korea Accounting Feed is the documented integration for transmitting Korea accounting entries from [[ratan]] to [[oltp]] through [[fm-solace]] and [[kredmi]].

## Normal processing

RATAN generates accounting JSON. FM Solace transports the message to KREDMI, KREDMI forwards it to OLTP, and the OLTP validation result returns through KREDMI and FM Solace to RATAN.

The documented flow supports the following interpretation:

`RATAN → FM Solace → KREDMI → OLTP`

`OLTP → KREDMI → FM Solace → RATAN`

Although introductory wording says RATAN sends feeds “to KREDMI and OLTP,” the numbered flow supports KREDMI as the intermediary rather than a direct RATAN-to-OLTP connection.

## Scope

The source states that this feed replaces a Murex-KR role for real-time accounting messages to OLTP. Its cashflow scope is stated to be the same as the flow entering RATAN from [[murex-kr]].

This statement establishes a business-scope relationship only. It does not establish equivalent interfaces, payloads, or system responsibilities.

## EOD exception

From 11:30 to 12:30 KST, the documented route ends at KREDMI:

`RATAN → FM Solace → KREDMI → NACK → FM Solace → RATAN`

The source does not state whether the NACK causes retry, suspension, rejection, or later reconciliation. This makes the operational meaning of “real time” conditional on the normal processing path. See [[how-does-ratan-oltp-handle-eod-nacks]].

## Interface limitations

No connection details, message schema, topic or queue definitions, error-code catalogue, ownership model, or troubleshooting process is provided. The source should not be used as an authoritative interface contract; see [[what-is-the-authoritative-ratan-oltp-interface-contract]].