---
type: concept
title: Force-Complete and Next-Batch Concurrency
tags: [cash-settlement, force-complete, optimistic-locking, batch-processing, concurrency]
related: [azure-devops-bug-6617079, group-service, adaptor, cashflow-locking-and-retry-policy, were-bugs-6526173-and-6617079-released-and-validated]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Lock Process.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Force-Complete and Next-Batch Concurrency

A reported regression blocked Auto STP when a force-complete event overlapped with payment processing for the next batch. The symptom was described as an optimistic database-update conflict.

The proposed remediation was to remove a reentrant lock in [[group-service]] after it consumes messages from [[adaptor]], so force-complete messages and payments can be locked with each other.

The source does not explain the relationship between the reentrant application lock and optimistic database locking, define the intended mutual-exclusion boundary, or provide concurrency and recovery test evidence. It records a release target of 2025-01-11, not confirmed deployment or validation. Verification is tracked in [[were-bugs-6526173-and-6617079-released-and-validated]].