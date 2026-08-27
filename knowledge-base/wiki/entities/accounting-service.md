---
type: entity
title: Accounting Service
tags: [cash-settlement, accounting, status-update, retry, microservice, SSI-stamping, Swift]
related: [cashflow-locking-and-retry-policy, ratan-cashflow-lifecycle-service, ssi-stamping-and-best-match, trade-level-ssi-stamping, cashflow-lifecycle-state-machine-restructuring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Lock Process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/Uber Dev Testing Question.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Accounting Service

`Accounting Service` (also referred to as `accounting-service`) is a downstream service involved in accounting updates after Swift suppression and SSI-stamp changes.

## Retry and locking

The Cash Settlement Lock Process source identifies Accounting Service as automatically retrying accounting status updates until success. Its documented lock key is `Cashflow Id`.

That source does not define the accounting message contract, retry policy details, idempotency behavior, or terminal-failure handling.

## SSI-stamp update

For cashflow `C06810140005`, Swift suppression initially did not update accounting. The Uber development-testing source reports that the issue was fixed by updating the accounting-service SSI-stamp URL and parameters and upgrading the accounting-service version to `2.0.0`.

The source does not include a successful post-fix response or accounting message, so the fix is recorded as reported rather than independently verified.