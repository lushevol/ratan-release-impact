---
type: concept
title: FileIT Solace Transfer Notifications
created: 2026-08-23
updated: 2026-08-23
tags: [fileit, solace, messaging, file-transfer, acknowledgement]
related: [fileit, ratan, aspire, what-is-the-required-ratan-handling-of-fileit-acknowledgements-and-failures]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Aspire Accounting.md"]
---
# FileIT Solace Transfer Notifications

The RATAN-to-Aspire FileIT transfer uses a Solace request containing a per-request UUID and can receive FileIT notifications covering acceptance, initiation, completion, and failure.

Documented success progression includes `1000 ACCEPTED`, `1100 INITIATED`, and `2000 CFT_SUCCESSFUL`. Failure codes cover authorization, request, routing, service availability, source and target path, permission, processing, and transfer failures.

Meeting minutes state that “ACK/NACK is not required,” while the technical section defines an acknowledgement queue, message structure, and return-code catalogue. This may distinguish Aspire business acknowledgement from FileIT operational notification, but the RATAN monitoring, persistence, retry, and reconciliation policy is not specified.