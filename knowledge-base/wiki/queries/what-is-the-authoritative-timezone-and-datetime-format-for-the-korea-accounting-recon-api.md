---
type: query
title: What Is the Authoritative Timezone and DateTime Format for the Korea Accounting Reconciliation API?
created: 2026-08-23
updated: 2026-08-23
tags: [RATAN, TLM, API, datetime, timezone, GMT, Korea, open-question]
related: [ratan-accounting-reconciliation-api, korea-accounting-reconciliation, utc-local-time-display-toggle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Korea Accounting Recon - RATAN- TLM.md"]
---
# What Is the Authoritative Timezone and DateTime Format for the Korea Accounting Reconciliation API?

## Question

The parameter table specifies `yyyy-mm-dd HH24:MM:SS` and says that values must be converted to GMT. The request example uses ISO-like `T` separators and no timezone offset.

## Evidence

The sample uses:

```text
2026-04-02T00:00:00
```

The parameter description uses:

```text
yyyy-mm-dd HH24:MM:SS
```

The source does not state whether inputs are Korea local time, GMT, or UTC, nor whether `publishTimestamp` uses the same convention.

## Required resolution

Define the accepted wire format, timezone, offset requirements, conversion responsibility, and interpretation of boundary timestamps.