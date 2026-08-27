---
type: concept
title: RATAN-ENISIS FM Solace Integration
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, korea-migration, fm-solace, amh, swift, observability]
related: [ratan, enisis, mxg-kr, fm-solace, korea-migration, swift-status-lifecycle-and-reconciliation, swift-message-reconciliation, is-technical-ack-firstsentok-terminal-for-ratan-enisis-korea-messages, what-is-the-final-ratan-enisis-fm-solace-header-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/RATAN to ENISIS.md"]
---
# RATAN-ENISIS FM Solace Integration

This is the target Korea settlement-message integration in which [[ratan]] receives payment-initiation input from [[mxg-kr]] and delivers qualifying MT210 and MX messages to [[enisis]] over [[fm-solace]].

## Response Processing

RATAN consumes the AMH `UniqueID`, `Status`, `StatusText`, `StatusDate`, and `StatusMessage` fields. It does not consume `StatusSource`, detailed SWIFTNet `StatusAttributes`, or `XTSResponsePayload`.

| Outcome | Status | StatusText | RATAN status message |
| --- | ---: | --- | --- |
| Final acknowledgement | 0 | `FinalSentOK` | `ACK received` |
| Negative acknowledgement | 1 | `FinalCancelled` | MT FIN error code; MX NAK text |
| Technical acknowledgement | 2 | `FirstSentOK` | `ACK received` |

Technical acknowledgement terminality is unspecified. A technical acknowledgement must not be assumed to be a final delivery or settlement outcome.

## Correlation and Observability

The integration requires preservation or controlled derivation of message identifiers and IMS metadata. `imsCorrelationId`, `imsTraceId`, and `imsPreviousCorrelationId` are returned from the request; response `imsEvent` is `RECEIVED`; and ENISIS updates `imsTimestamp` using its system time. `imsSpans` is expected to become `RATAN,ENISIS`.

This route-specific contract extends [[swift-message-reconciliation]] and [[swift-status-lifecycle-and-reconciliation]] but does not establish behavior for other RATAN integrations.