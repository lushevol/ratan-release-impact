---
type: query
title: What Is the Authoritative Manual Hold Status Transition Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, manual-hold, status-transition, workflow, open-question]
related: [manual-cashflow-holding, cashflow-status-restoration, manual-hold-representation-options, cashflow, ratan-cashflow-lifecycle-service, query-service, holding-release-precheck]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Manual Holding Process Tech Design.md"]
---
# What Is the Authoritative Manual Hold Status Transition Contract?

The design selects main-status representation for manual cashflow holding, but does not define the corresponding status-transition contract.

## Questions to resolve

- What canonical status represents a manually held cashflow?
- Are Waiting, Pending Exception, and pending verification distinct statuses or informal descriptions of the same state?
- Where and how is the original pre-hold status persisted?
- Can hold and unhold actions be repeated safely and idempotently?
- What happens when lifecycle processing, exception updates, netting, or queued processing race with a hold request?
- Can a held cashflow receive new exceptions or external status updates?
- Which service owns hold, unhold, state restoration, audit history, and authorization?
- How do [[query-service]] and UI clients identify and filter held cashflows?
- How does [[holding-release-precheck]] distinguish manual holding from queued-cutoff restrictions?
- Does unhold resume processing automatically or only restore the prior status?

## Evidence

[[manual-hold-representation-options]] records that the selected design blocks five in-progress operations and restores the original status on unhold. It does not supply a state diagram, API contract, persistence model, or concurrency rules.