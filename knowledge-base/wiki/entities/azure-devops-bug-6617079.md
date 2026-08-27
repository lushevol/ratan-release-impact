---
type: entity
title: Azure DevOps Bug 6617079
tags: [azure-devops, regression, cash-settlement, optimistic-locking, auto-stp]
related: [group-service, adaptor, force-complete-next-batch-concurrency, were-bugs-6526173-and-6617079-released-and-validated]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Lock Process.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Azure DevOps Bug 6617079

Azure DevOps Bug 6617079 is a 2024-12-04 regression titled “Murex Feeding - Cancelled cashflow didn't get auto closed in group pending.” It reports Auto STP being blocked by an optimistic database-update conflict while force-complete processing overlapped with payments from the next batch.

The proposed solution removes a reentrant lock in [[group-service]] after Adaptor-message consumption. The stated status is “To be released by 2025-01-11”; no release or test outcome is documented.

URL: https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6617079/?view=edit