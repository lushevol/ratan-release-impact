---
type: query
title: Does Nostro Refresh Regenerate Accounting Requests for Netted, Released, and Withdrawn Cashflows?
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, accounting, netting, release, withdrawal, hold]
related: [held-accounting-request-nostro-regeneration, ratan-cash-settlement-accounting-service, settlement-accounting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/[Accounting Enhancement", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/[Accounting Enhancement] Prepare Nstro Account Info before Sent.md"] Prepare Nstro Account Info before Sent.md"] Prepare Nstro Account Info before Sent.md"]
---
# Does Nostro Refresh Regenerate Accounting Requests for Netted, Released, and Withdrawn Cashflows?

The source presents, but does not answer, a scenario where `c1 + c2` net to `c3`; `c3` is released from `HOLD`; `c1` is withdrawn and released; Nostro data is then refreshed before scheduled dispatch.

## Open question

Should the sends for both `c3` and `c1` regenerate their Nostro-related accounting request data and use refreshed `nostro2` rather than `nostro1`?

## Required clarification

The authoritative rule should define:

- whether netted cashflow `c3` remains eligible for regeneration after release;
- whether withdrawn and released `c1` remains eligible for dispatch and regeneration;
- whether lifecycle state changes supersede, cancel, or preserve held accounting tasks;
- whether netting changes the task-to-cashflow relationship;
- how duplicate or superseded sends are prevented.

This source provides no outcome and must not be interpreted as establishing one.