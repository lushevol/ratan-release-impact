---
type: query
title: What Is the Authoritative RATAN-OLTP Interface Contract?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, oltp, interface-contract, accounting, korea]
related: [ratan-oltp-korea-accounting-feed, oltp, kredmi, fm-solace, 5-ratan--17-ratan-interfaces--14-ratan-and-oltp--2a76vb]
sources: ["RATAN/RATAN -Interfaces/Ratan and OLTP.md"]
---
# What Is the Authoritative RATAN-OLTP Interface Contract?

## Question

What approved specification defines the RATAN-to-OLTP integration topology, connection endpoints, FM Solace destinations, accounting JSON schema, acknowledgement and error-code formats, ownership, and recovery requirements?

## Evidence

The available source documents a high-level normal path through KREDMI and an EOD NACK path, but its connection-details and interface-specification sections are empty. Its review and publication fields are also blank.

## Information needed

- Confirmation of whether KREDMI is mandatory for all OLTP traffic.
- FM Solace queues, topics, subscriptions, and message-routing details.
- Versioned accounting JSON schema and mandatory fields.
- ACK, NACK, and OLTP error-code contracts.
- Idempotency, timeout, retry, reconciliation, and support-ownership procedures.
- Review and publication status of the source and `FM ESB Aide Common_9.22.docx`.