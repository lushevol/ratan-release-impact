---
type: concept
title: Maker-Checker Configuration Governance
created: 2026-08-24
updated: 2026-08-24
tags: [maker-checker, approval, audit, governance]
related: [self-service-entity-branch-onboarding, centralized-static-configuration-management, ratan-static-entity-onboarding-config]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Self Service new branch entity onboarding Design.md"]
---
# Maker-Checker Configuration Governance

Maker-checker configuration governance is the proposed control pattern for self-service onboarding changes. The source repeatedly specifies CRUD, record audit, paginated history, confirm, and cancel operations, with fields including `dataStatus`, `makerId`, and `checkerId`.

The intent is that a user creates or changes configuration and a separate checking action confirms or cancels it. However, the draft does not define:

- Valid `dataStatus` values and transitions.
- Whether maker and checker must be distinct and authorized for the configuration domain.
- Approval behavior for updates and deletes.
- Whether propagation starts before or after confirmation.
- Conflict detection, versioning, retention, or immutable audit history.

The API examples therefore establish a control intention, not a finalized governance contract.