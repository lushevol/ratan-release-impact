---
type: entity
title: Azure DevOps Bug 6526173
tags: [azure-devops, regression, cash-settlement, netting, status-transition]
related: [cashflow-release-and-netting-race-condition, release-time-cashflow-status-gating, were-bugs-6526173-and-6617079-released-and-validated]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Lock Process.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Azure DevOps Bug 6526173

Azure DevOps Bug 6526173 is a 2024-11-26 regression titled “Affirmation Exception Auto close handling issue.” It records a release failure, post-netting technical failure, and an incorrect transition to `DEAD` after unnetting.

The proposed mitigation is to move a payment to `READY` only after confirming that its cashflow is `WAITING` and `Pending Exception`. The stated status is “To be released by 2025-01-11”; the source does not confirm release, production deployment, or validation.

URL: https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6526173/?view=edit