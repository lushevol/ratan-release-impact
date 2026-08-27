---
type: concept
title: RDM Holiday and Weekend Ingestion
created: 2026-08-24
updated: 2026-08-24
tags: [rdm, holiday-calendar, ingestion, cash-settlement, fileit]
related: [rdm, ratanone, fileit, cft, ratan-static-rdm-holiday-weekend-message, ratan-static-cashflow-currency-holiday, fileit-file-arrival-notification, holiday-data-composite-duplicate-key, what-is-the-authoritative-ratan-holiday-data-ingestion-path]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan holiday data process from RDM introduction.md"]
---
# RDM Holiday and Weekend Ingestion

RDM holiday and weekend ingestion is the documented flow by which RATAN receives reference calendar data for cash settlement.

The source identifies two persistence layers:

1. Raw inbound messages in [[ratan-static-rdm-holiday-weekend-message]].
2. Structured records in [[ratan-static-cashflow-currency-holiday]].

It also identifies full BCDF files delivered by [[fileit]] and a FileIT notification addressed to RATAN. RATAN is documented as a consumer of that notification.

The relationship between message-level data, full-file processing, and structured-table population remains unspecified. It must not be assumed that either path is authoritative without further evidence.