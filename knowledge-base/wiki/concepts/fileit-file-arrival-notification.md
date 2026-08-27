---
type: concept
title: FileIT File-Arrival Notification
created: 2026-08-24
updated: 2026-08-24
tags: [fileit, notification, cft, rdm, integration]
related: [fileit, cft, rdm, ratanone, rdm-holiday-and-weekend-ingestion, fileit-return-code-taxonomy, what-is-the-authoritative-ratan-holiday-data-ingestion-path]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan holiday data process from RDM introduction.md"]
---
# FileIT File-Arrival Notification

A FileIT file-arrival notification informs RATAN that an RDM full-data holiday file has arrived at the receiver.

For the documented feed, the notification includes:

- Identifier: `FRDM_HOLIDAY_GL`
- Subcomponent: `FRDM_RATAN_HOLIDAY_GL`
- Source: `38430-RDM`
- Target: `51358-RATAN`
- Component: `CFT`
- Status code: `5000`
- Reason: `CFT_NOTIFICATION`
- Status detail: `File Arrived at Receiver`
- A source-file path and tracking identifiers

The notification contains metadata for routing and tracing, but this source does not define the notification idempotency key, retry policy, replay policy, or success criteria for subsequent file processing.