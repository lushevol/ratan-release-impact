---
type: query
title: What Does Real Time Mean for the RATAN-to-eBBS Feed?
tags: [ratan, ebbs, real-time, latency, sla, monitoring]
related: [ratan-ebbs-accounting-feed, solace, operational-level-agreement, what-is-the-canonical-ratan-to-ebbs-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and EBBS 14147.md"]
created: 2026-08-24
updated: 2026-08-24
---
# What Does Real Time Mean for the RATAN-to-eBBS Feed?

The source describes the RATAN-to-eBBS accounting feed as “real time,” but it provides no latency target, availability objective, timing boundary, or measurement method.

## Resolution needed

Define and approve:

- The start event for timing measurement.
- The completion event, such as Solace publication, eBBS receipt, validation, or accounting posting.
- Target, warning, and breach latency thresholds.
- Availability and delivery-success targets.
- Monitoring data source, dashboard, alert thresholds, and retention.
- Treatment of retries, duplicate messages, delayed processing, and reconciliation exceptions.
- Whether these targets are covered by the referenced BPMS OLA.

Without these details, “real time” should be interpreted as a high-level design intent rather than a measurable service commitment.