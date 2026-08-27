---
type: query
title: When and How Is ebbsAccountNum Derived for Held Accounting Tasks?
created: 2026-08-23
updated: 2026-08-23
tags: [ebbsAccountNum, accounting, nostro, hold, data-derivation]
related: [ratan-cash-settlement-accounting-service, held-accounting-request-nostro-regeneration, settlement-accounting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/[Accounting Enhancement", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/[Accounting Enhancement] Prepare Nstro Account Info before Sent.md"] Prepare Nstro Account Info before Sent.md"] Prepare Nstro Account Info before Sent.md"]
---
# When and How Is ebbsAccountNum Derived for Held Accounting Tasks?

The source asks when `ebbsAccountNum` is populated for accounting tasks generated in `HOLD`, but only confirms that Nostro-related partial request information must be regenerated before downstream send after a Nostro refresh.

## Open points

- Is `ebbsAccountNum` included in the Nostro-related portion that must be regenerated?
- Is it populated during task creation, at dispatch preparation, or at both points?
- Does it always derive from the currently valid Nostro account?
- What lookup attributes identify the applicable Nostro record?
- What occurs if the refreshed Nostro is missing, inactive, invalid, or non-unique?
- Which audit fields record the Nostro version and `ebbsAccountNum` used for dispatch?

A resolved contract should distinguish task-creation values from the value actually used in the outbound request.