---
type: entity
title: Azure DevOps
created: 2026-08-22
updated: 2026-08-25
tags: [work-management, traceability, ado, delivery-planning, requirements, azure-devops, issue-tracking]
related: [fmrp, f2b, cash-settlement-2025-roadmap, which-2025-f2b-milestones-actually-went-live, story-11137292-manual-rounding, manual-cashflow-rounding, ratan-ktlo-tracker]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/2025 backlog.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Manual Rounding.md", "RATAN/RATAN -KTLO Tracker/RATAN -KTLO Tracker.md"]
---
# Azure DevOps

Azure DevOps, abbreviated as ADO in the cash-settlement source, is a work-management system and platform used to identify and link many items in the 2025 [[fmrp]] cash-settlement backlog.

It is also used by the RATAN KTLO tracker to reference production-support work items and prioritisation discussions.

## Cash-Settlement Backlog Usage

ADO identifiers provide traceability across:

- [[f2b]] go-live milestones.
- Murex cashflow migration tranches.
- Day 2 features.
- KTLO controls, enhancements, and defect remediation.

Identifiers appear in mixed forms, including descriptive links, raw URLs, and bare numbers. Some backlog items have no identifier.

Azure DevOps also hosts the requirement reference for Manual Rounding. The Manual Rounding source links to the Azure DevOps work item [[story-11137292-manual-rounding]].

## RATAN KTLO Usage

The RATAN source links to the `[RATAN PROD ISSUE - Boards]` query in the `FMQPR` project and references work items including stories and generic tasks. These references provide incident examples and proposed work, but the tracker does not establish that any item is complete or that its linked description is the authoritative technical specification.

See [[ratan-ktlo-tracker]] for the complete work-item register and operational evidence.

## Interpretation Constraint

The presence of an ADO feature or work-item identifier confirms that a trackable item was referenced. It does not establish implementation, acceptance, release, or production go-live. Owners, status, dependencies, acceptance criteria, and release evidence would need to be obtained from the work items or associated release records.

This constraint also applies to the RATAN references: the tracker does not establish that any referenced item is complete or that its linked description is the authoritative technical specification.