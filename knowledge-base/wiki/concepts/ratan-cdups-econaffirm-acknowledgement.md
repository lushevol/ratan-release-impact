---
type: concept
title: RATAN-CDUPS EconAffirm Acknowledgement
created: 2026-08-24
updated: 2026-08-24
tags: [econaffirm, affirmation, ack, nack, duplicate-suppression, ratan, cdups]
related: [ratan, cdups, fm-edmi, ratan-ssi-stamping, ratan-cdups-trade-confirmation-flow, operational-level-agreement]
sources: ["RATAN/RATAN -Interfaces/Ratan and CDUPS 51512.md"]
---
# RATAN-CDUPS EconAffirm Acknowledgement

This concept describes the asynchronous exchange of economic-affirmation status between RATANONE and CDUPS.

## Flow

When an MO affirms a trade directly in RATAN without updating CDUPS, RATAN sends an `EconAffirm` status to CDUPS. CDUPS consumes the status, updates its `Econaffirm` status, and sends an ACK to RATAN. The source states that CDUPS marks the affirmation status as “Under Investigation” when it receives `EconAffirm` in the described condition.

RATANONE is stated not to send duplicate `EconAffirm` messages to CDUPS.

## Interface identifiers

```text
RATANONE -> FM-EDMi(JMS-Json) -> CDU PS
v1/post-trade/51358-ratanone/cdups/json-1.0/ecoaffirm/pub

CDUPS -> FM-EDMi(JMS-Json) -> RATANONE
q-51358-cdups-ratanone-ack
[CDU PS] v1/post-trade/51512-cdups/ratanone/json-1.0/ack/pub
```

## Status and response behavior

The source associates `EconAffirm` with several pre-existing CDUPS states, including Awaiting Affirmation, “Affirmation: Pending approval” with Checker, and Under Investigation where SSI is affirmed but economics are not. It also lists Phone affirmed, Email affirmed, Confirmation Match, Under Investigation where SSI is not affirmed but economics are affirmed, and Affirmation Suppressed as states associated with an `EconAffirm` response that should receive a NACK with an appropriate reason.

The mapping is not sufficiently precise to define a state machine. In particular, “Under Investigation” appears to describe more than one condition, and the NACK reason values are not enumerated.

## Reliability gaps

The source does not define the deduplication key, persistence across restart, retry and redelivery behavior, ACK idempotency, correlation identifiers, or the payload schemas. These omissions prevent this page from serving as a complete message contract.
