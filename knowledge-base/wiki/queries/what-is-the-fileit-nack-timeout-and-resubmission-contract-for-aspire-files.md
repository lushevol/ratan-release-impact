---
type: query
title: What Is the FileIT NACK Timeout and Resubmission Contract for Aspire Files?
created: 2026-08-24
updated: 2026-08-24
tags: [fileit, acknowledgement, retry, accounting, open-question]
related: [fileit, accounting-file-delivery-acknowledgement, accounting-aspire-execution]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Settlement Accounting for Aspire Tech design.md"]
---
# What Is the FileIT NACK Timeout and Resubmission Contract for Aspire Files?

The proposed design records FileIT results such as `ACKED`, `NACK`, `SUCCESS`, and `Invalid Request`, but it does not specify the transport contract or recovery behavior.

An authoritative contract is needed for submission acknowledgement, asynchronous callback correlation, timeout detection, duplicate filenames, NACK classification, retry ownership, resubmission identity, and operational escalation.