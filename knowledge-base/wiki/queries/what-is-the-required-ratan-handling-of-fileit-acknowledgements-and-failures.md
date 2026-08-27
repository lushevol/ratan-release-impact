---
type: query
title: What Is the Required RATAN Handling of FileIT Acknowledgements and Failures?
created: 2026-08-23
updated: 2026-08-23
tags: [fileit, acknowledgement, failure-handling, solace]
related: [fileit-solace-transfer-notifications, fileit, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Aspire Accounting.md"]
---
# What Is the Required RATAN Handling of FileIT Acknowledgements and Failures?

Meeting minutes say ACK/NACK is not required, but the interface configuration provides an acknowledgement queue, notification schema, and return-code catalogue.

Clarify whether RATAN must consume and persist notifications, correlate them by UUID, retry failed transfers, alert support, reconcile delivery, and retain source files. Also distinguish FileIT operational notification from any Aspire business acknowledgement.