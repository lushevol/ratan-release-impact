---
type: concept
title: FMRP–Murex 2.11 Settlement Workflow
created: 2026-08-24
updated: 2026-08-24
tags: [fmrp, murex-211, settlement, workflow, ratan, mls]
related: [murex-211, fmrp, ratan-10123, fmrp-cashflow-status-synchronization, ratan-cashflow-acknowledgement-and-release-processing, surrounding-system-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0130.md"]
---

# FMRP–Murex 2.11 Settlement Workflow

## Purpose

The workflow separates payment insertion from external settlement routing for Murex 2.11 cashflows. FMRP and MLS are explicit branches selected by the Murex action and are not interchangeable destinations.

## Outbound flow

`docPayment` emits either `insert` or `extSettle`.

- `insert` routes to `INIT2SNTR`.
- `extSettle` routes to `extSettleRouter`.
- `extSettleRouter` sends FMRP actions to `FmrpFilter`.
- The FMRP branch synchronizes status, enriches the payment XML, removes payment context, and publishes through `FmrpOutboundMQ`.
- The MLS branch continues to `PaymentMLSOUTboundRouter`.

The action mapping is:

| Murex action | Route |
|---|---|
| `RI2C` | MLS |
| `MCXI` | MLS |
| `MIXC` | MLS |
| `FAIS` | FMRP |
| `FMIS` | FMRP |
| `FMSI` | FMRP |
| `I2SR` | FMRP |

The formula has no explicit fallback for unsupported actions.

## FMRP outbound processing

`FmrpFilter` applies `client.scb.fmrp.SyncStatus`. A publishable result proceeds to `FmrpSettleEnrichment`, which appends `scbExtraInfoBlock`. `FmrpSettleFilter` excludes the payment context using `mxcontext.dtd`. `FmrpOutboundMQ` then publishes the enriched message.

The enrichment contains publication time, validation level, entity and counterparty identifiers, trader ID, portfolio business unit, and amendment status.

## Retry path

`INIT2SNTR` performs the `I2SR` payment action. On success it goes to `FmrpPurge`. On error, `FmrpRemoveError` passes the message to `FmrpRetryCheck`. The retry counter permits attempts while the counter is below three; otherwise the message is stopped and purged.

## Inbound flow

The inbound MQ task receives RATAN responses. The later 2023-01-17 design replaces `FmrpAckRouter` with `FmrpInboundRouter`, `SNTR2RLSR`, `FmrpAckProcessor`, and `FmrpReleaseProcessor`.

Inbound messages are correlated using `/MxPayMLResponse/MXG2000/flowID`. Only RATAN cashflow messages with a positive Murex flow ID and message type `RATAN Acknowledged` or `RATAN Released` are accepted.

## Boundaries

The FMRP-specific status transitions, entity eligibility checks, and precious-metal exclusions must not be generalized to MLS, Vostro selection, or unrelated cashflow processes. The source also does not prove ownership of the MQ queues whose names contain `MLS`.