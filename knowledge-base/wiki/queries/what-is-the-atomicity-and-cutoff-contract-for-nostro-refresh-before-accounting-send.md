---
type: query
title: What Is the Atomicity and Cutoff Contract for Nostro Refresh before Accounting Send?
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, accounting, dispatch, concurrency, idempotency, data-freshness]
related: [held-accounting-request-nostro-regeneration, ratan-cash-settlement-accounting-service, nostro-notification-and-refresh]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/[Accounting Enhancement", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/[Accounting Enhancement] Prepare Nstro Account Info before Sent.md"] Prepare Nstro Account Info before Sent.md"] Prepare Nstro Account Info before Sent.md"]
---
# What Is the Atomicity and Cutoff Contract for Nostro Refresh before Accounting Send?

The source requires regeneration of Nostro-related accounting request information before downstream sending after a Nostro refresh, but it does not define the mechanism or concurrency boundary.

## Open points

- Is regeneration triggered by a Nostro-refresh event or by a lookup immediately before dispatch?
- What identifies all tasks affected by a refresh?
- What is the cutoff if refresh and dispatch occur concurrently?
- Can an already constructed but unsent request be replaced?
- How are failed sends retried if Nostro data changes between attempts?
- How is idempotent downstream delivery guaranteed?
- Which timestamps, Nostro identifiers, and request versions must be retained for audit?

The resulting contract should distinguish immutable persisted cashflow data from refreshable outbound accounting payload data.