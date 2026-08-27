---
type: query
title: What Is the Authoritative Cashflow Lifecycle State-Transition and Persistence Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, lifecycle, state-machine, persistence, workflow]
related: [cashflow-lifecycle-state-machine-restructuring, cashflow-status-restoration, manual-cashflow-holding, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--13iana4]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement 2.0 Technical Design.md"]
---
# What Is the Authoritative Cashflow Lifecycle State-Transition and Persistence Contract?

The source proposes restructuring lifecycle-service but supplies no textual state model. It identifies a failure mode where lifecycle status becomes `released2Razor` although workflow has not successfully consumed the corresponding message.

## Questions to resolve

- What are the canonical lifecycle and workflow states, including `released2Razor` and `TechFail`?
- Which service owns each transition and the authoritative cashflow status?
- What guards, versions, ordering rules, and duplicate-event controls govern concurrent transitions?
- How are lifecycle persistence and workflow message delivery made atomic or reconciled when they diverge?
- How do reinstatement, holding, netting, UnNetting, and component-status changes interact with the state machine?
- Does the generic lifecycle-service in this source refer to [[ratan-cashflow-lifecycle-service]]?

The referenced UML is not present as text, so it cannot establish the contract.