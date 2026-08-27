---
type: concept
title: RATAN-Murex Settlement Cashflow Interface
tags: [ratan, murex, settlement, cashflow, mq, sftp, interface-14165]
related: [ratan, murex-g2000, mx-2-11, murex-ratan-batch-acknowledgement-protocol, settlement-accounting, ratan-settlement, ratan-interface-inventory, authoritative-cashflow-lifecycle-and-system-owners-2026-08-24-104403]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and Murex 14165.md"]
---
# RATAN-Murex Settlement Cashflow Interface

Interface 14165 is an operational settlement-cashflow flow in which [[murex-g2000]] sends cashflow data to [[ratan]] for processing and RATAN returns updated cashflow status to [[mx-2-11]].

## Delivery routes

The stated routing policy is:

- **T−1 to T+1:** real-time delivery through MQ for immediate processing.
- **T+2 to T+7:** Murex-generated batch files delivered through SFTP to the RATAN Shared NAS, excluding weekends and public holidays.
- **Fix Flag cases:** manual or corrective files delivered through SFTP for reprocessing regardless of value date.

The source identifies transport and date bands but does not specify MQ destinations, SFTP authentication, file schemas, duplicate prevention, cut-offs, applicable holiday calendars, or handling outside the stated value-date ranges.

## Scope boundary

This interface provides upstream operational context for [[ratan-settlement]] and [[settlement-accounting]], but it does not evidence accounting postings, ledger ownership, or an authoritative cashflow lifecycle. It contributes partial evidence to [[authoritative-cashflow-lifecycle-and-system-owners-2026-08-24-104403]]: Murex is identified as the originator for this flow and RATAN as processor, while final status authority remains unclear.

The interface should remain distinct from [[murex-eod-proxy]] and [[ratan-fx-replication]], which are separate RATAN capabilities.

## Contract status

The source is an operational overview with no populated interface specification. The complete contract is tracked in [[what-is-the-authoritative-ratan-murex-14165-interface-contract]].