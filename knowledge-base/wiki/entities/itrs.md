---
type: entity
title: ITRS
created: 2026-08-22
updated: 2026-08-25
tags: [monitoring, operations, ratan, eod, itrs, alerting, cash-settlement, observability]
related: [ratan, controlm, aspire, itrs-to-control-m-file-monitor-mapping, what-are-the-complete-itrs-monitoring-parameters-for-ratan-eod-files, cash-settlement-ola-break-monitoring, murex, ratan-ktlo-tracker, ratan-operational-observability, ratan-interface-inventory]
sources: ["RATAN - 51358/RATAN/RATAN -Infra/Control-M Job Details RATAN.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md", "RATAN/RATAN -KTLO Tracker/RATAN -KTLO Tracker.md"]
---
# ITRS

ITRS is referenced in several RATAN operational contexts:

- RATAN end-of-day file monitoring.
- Murex-related operational-level agreement breaks and cash-settlement exception handling.
- RATAN KTLO monitoring and operational-observability requirements.

The RATAN KTLO tracker identifies ITRS as the monitoring platform and states that current ITRS monitoring does not cover all required operational aspects.

## RATAN EOD file monitoring

The Control-M inventory documentation describes ITRS as the monitoring platform referenced for RATAN EOD file monitoring.

The documented scope is limited to four filename-to-producer mappings for Aspire accounting outputs:

| Filename mapping | Producer |
|---|---|
| HK | Aspire |
| TH | Aspire |
| TW | Aspire |
| JE | Aspire |

For this RATAN EOD monitoring scope, the source provides no ITRS monitor IDs, monitored file locations, expected arrival times, alert thresholds, escalation routing, or response runbooks.

See [[itrs-to-control-m-file-monitor-mapping]] and [[what-are-the-complete-itrs-monitoring-parameters-for-ratan-eod-files]].

## Murex cash-settlement exception handling

The Exception Handling design describes ITRS as the monitoring and alerting mechanism referenced for Murex-related operational-level agreement breaks.

In that context:

- ITRS provides the primary real-time alert for missing Murex-to-Ratan cashflows.
- ITRS is also referenced for Murex acknowledgement delays during Ratan-to-Murex status write-back.

See [[cash-settlement-ola-break-monitoring]] and [[murex]].

## RATAN KTLO monitoring gaps

The RATAN KTLO tracker reports missing or incomplete ITRS monitoring for the following operational aspects:

- Business volume.
- Interface connectivity.
- RATAN API availability.
- Throughput and processing latency.
- SLA and OLA commitments.

The tracker identifies these gaps under **GENERIC TASK 10913098**. The requested enhancement is intended to enable earlier detection of abnormalities.

The tracker mentions RATAN 2.0 scope and ongoing knowledge-transfer sessions for Ratan Foundation 2.0. It does not document implemented dashboards, alert thresholds, owners, or delivery commitments.

See [[ratan-operational-observability]] for the cross-cutting monitoring requirements.