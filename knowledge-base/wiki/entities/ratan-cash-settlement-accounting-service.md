---
type: entity
title: ratan-cash-settlement-accounting-service
created: 2026-08-23
updated: 2026-08-23
tags: [service, accounting, settlement, nostro]
related: [settlement-accounting, held-accounting-request-nostro-regeneration, nostro-notification-and-refresh]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/[Accounting Enhancement", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/[Accounting Enhancement] Prepare Nstro Account Info before Sent.md"] Prepare Nstro Account Info before Sent.md"] Prepare Nstro Account Info before Sent.md"]
---
# ratan-cash-settlement-accounting-service

`ratan-cash-settlement-accounting-service` is the service explicitly identified for change in the accounting enhancement requirement concerning Nostro data freshness before delayed downstream sends.

## Stated responsibility

The source associates the service with accounting information that is generated for tasks in `HOLD` and later sent downstream. When relevant Nostro data is refreshed before sending, the service must ensure that applicable held tasks regenerate the Nostro-related portion of their outbound request before dispatch.

## Limits of the available evidence

The source does not specify APIs, events, storage, ownership, downstream system names, task identifiers, retry mechanics, or concurrency controls. It also does not establish whether regeneration occurs on a Nostro-refresh event or immediately before send.

See [[held-accounting-request-nostro-regeneration]] and [[what-is-the-atomicity-and-cutoff-contract-for-nostro-refresh-before-accounting-send]].