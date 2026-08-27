---
type: query
title: Is Manual Splitting of IRS Aggregation Resultants in Day 1 Scope?
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-splitting, irs, netting-resultant, scope, decision-needed]
related: [cashflow-splitting, netting-resultant-cashflow-lifecycle, irs-resultant-cashflow-netting, what-is-the-approved-withdrawal-and-accounting-behavior-after-split-child-release]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting.md"]
---
# Is Manual Splitting of IRS Aggregation Resultants in Day 1 Scope?

The source contains incompatible positions on manual splitting of netting resultants and IRS aggregation resultants:

- The main requirement says manual splitting of netting resultants, including IRS aggregation resultants, is not supported in Day 1.
- A business-user test scenario expects manual splitting of an IRS netting resultant.
- An open-question closure dated 2025-09-25 says to disable manual split over a net resultant but support it for an IRS aggregation resultant.
- A later open question dated 2025-10-10 says manual split over an IRS aggregation resultant is not supported.

The later statement suggests exclusion, but no formal decision reconciles the requirement, test cases, withdrawal design, accounting proposal, and UI behavior. A confirmed scope decision is required before implementation and UAT.