---
type: concept
title: Korea Murex-to-RATAN Interface Readiness
created: 2026-08-23
updated: 2026-08-23
tags: [korea, murex, ratan, mq, comp-trade, interface-readiness]
related: [korea-ratan-settlement-migration, operational-level-agreement-for-settlement-interfaces, murex-korea, ratan, what-are-the-approved-mq-channels-for-murex-korea-payment-and-trade-to-ratan, what-is-the-authoritative-comp-trade-message-contract-volume-and-no-ack-behavior]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Korea OLA and other release related DOCs.md"]
---
# Korea Murex-to-RATAN Interface Readiness

## Definition

Korea Murex-to-RATAN interface readiness is the operational and contractual confirmation required before Korea payment and trade messages can be treated as ready for production support.

## Readiness Dimensions

The source identifies these dimensions:

1. MQ information for payment and trade traffic.
2. Confirmation of the relevant channel.
3. COMP trade volume.
4. COMP trade message format and sample.
5. Acknowledgement behavior.
6. Monitoring arrangements.

Only the acknowledgement behavior is explicitly marked complete: **no ACK for COMP trade**. The remaining dimensions are open or require confirmation.

## Evidence Boundary

The source does not provide queue names, channel owners, security requirements, message schemas, volume measurements, test results, monitoring thresholds, or failure and replay procedures. References to Confluence documents should therefore be treated as pointers to potentially authoritative material, not as evidence that the requirements have been satisfied.

## Related Systems

The interface originates in [[entities/murex-korea]] and targets [[entities/ratan]]. Its readiness is part of the [[projects/korea-ratan-settlement-migration]].