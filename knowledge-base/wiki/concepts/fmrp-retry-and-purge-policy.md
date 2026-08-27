---
type: concept
title: FMRP Retry and Purge Policy
created: 2026-08-24
updated: 2026-08-24
tags: [fmrp, retry, purge, error-handling, murex-211]
related: [fmrp, murex-211, ratan-murex-211-cashflow-integration, what-is-the-production-fmrp-mq-endpoint-and-failure-escalation-policy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0118.md"]
---
# FMRP Retry and Purge Policy

The historical `INIT2SNTR` error path removes the error body, evaluates `FmrpRetryCheck`, and either retries `INIT2SNTR` or sends the document to `FmrpPurge`.

`STPDOC_DATA_TYPE3` holds the retry count:

- An empty count becomes `1`.
- A non-empty count increments by one.
- Retry continues while the numeric value is less than `3`.
- At `3`, routing returns `stop`, leading to purge.

The source documents disposal after the retry limit but does not document a dead-letter queue, alerting, retry delay or backoff, audit record, operational owner, or manual recovery process.

The January 2023 revision replaces direct `docPayment → INIT2SNTR` insertion with `PayInsertionFilter → SNTR`, but it does not explicitly state whether this retry-and-purge path remains attached to the revised process. Current operational behavior requires confirmation.