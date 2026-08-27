---
type: query
title: Does Removing Auto Affirmation Change Netting Release Eligibility?
tags: [cashflow-auto-netting, auto-affirmation, release, settlement-lifecycle]
related: [cashflow-auto-netting, pending-confirmation-affirmation, ratan-cashflow-lifecycle-state-machine, netting-resultant-cashflow-lifecycle]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Enhancement on Auto Netting.md"]
---
# Does Removing Auto Affirmation Change Netting Release Eligibility?

The source requires removal of auto affirmation from [[cashflow-auto-netting]], but does not identify the process that will perform affirmation or its relationship to resultant release.

## Questions to resolve

- Does the change apply to every auto-netting scenario or only Settlement Day2 and inter-entity processing?
- Which process or user action replaces automatic affirmation?
- Are affirmation and release dependent lifecycle gates?
- How are already auto-affirmed cashflows treated?
- Does removal affect resultant creation, release timing, or exception handling?

The answer should reconcile the proposed workflow change with [[pending-confirmation-affirmation]] and [[ratan-cashflow-lifecycle-state-machine]].