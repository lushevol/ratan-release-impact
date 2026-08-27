---
type: query
title: Were Bugs 6526173 and 6617079 Released and Validated?
tags: [cash-settlement, regression, release-validation, testing]
related: [azure-devops-bug-6526173, azure-devops-bug-6617079, force-complete-next-batch-concurrency, release-time-cashflow-status-gating]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Lock Process.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Were Bugs 6526173 and 6617079 Released and Validated?

Both regression remedies were marked “To be released by 2025-01-11.” The source does not confirm implementation, release, production deployment, regression testing, or post-release outcomes.

## Evidence Needed

- Azure DevOps work-item history and final disposition for both bugs.
- Release records for the 2025-01-11 target.
- Regression tests for the `WAITING` plus `Pending Exception` transition gate.
- Concurrency and recovery tests for force-complete events and next-batch payments.
- Production monitoring or incident evidence following deployment.