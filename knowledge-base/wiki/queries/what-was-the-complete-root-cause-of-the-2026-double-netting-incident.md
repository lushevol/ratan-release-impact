---
type: query
title: What Was the Complete Root Cause of the 2026 Double-Netting Incident?
created: 2026-08-22
updated: 2026-08-22
tags: [query, netting, incident, RATAN, root-cause-analysis]
related: [cashflow-netting-renetting, payment-release-concurrency-control, resultant-cashflow-status-consistency, netting-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Auto Release Process.md"]
---
# What Was the Complete Root Cause of the 2026 Double-Netting Incident?

## Question

What does the truncated root-cause item `Lock space` mean, and what complete set of technical and process causes produced the reported double-netting outcome?

## Known Incident Facts

The production incident involved 357 component cashflows and two resultants:

- `N00000267689`
- `N00000266337`

`user1` triggered netting at `02:07:39`, acquired the Netting Service lock at `02:07:43`, and completed at `02:07:49`. `user2` had triggered a call at `02:07:44`, acquired the lock at `02:07:52`, and completed at `02:07:58`. The source states that `N00000266337` subsequently lost component cashflows from its netting ID.

The source identifies two interpretable causes:

1. `NETTED` allowed the `Net` action in a context where it represented a wrong or duplicate action.
2. The status-movement API no longer validated minor version.

The third cause is recorded only as `Lock space` and must not be expanded without the complete incident documentation.

## Investigation Scope

The investigation should establish:

- The intended lock key, scope, lease, and release semantics.
- Whether the second operation revalidated status after lock acquisition.
- Whether status and minor version were updated atomically.
- Whether the two resultants shared component cashflows or an outdated snapshot.
- Whether remediation changed the `NETTED` action matrix.
- Whether version-aware conditional updates and monitoring were deployed.
- Whether any downstream reconciliation or recovery was required.

See [[payment-release-concurrency-control]] for the control model.