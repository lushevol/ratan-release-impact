---
type: source
title: Manual Holding Process Technical Design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, manual-hold, cashflow, technical-design, ratanone]
related: [manual-cashflow-holding, cashflow-status-restoration, manual-hold-representation-options, what-is-the-authoritative-manual-hold-status-transition-contract, holding-release-precheck]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Manual Holding Process Tech Design.md"]
authors: []
year: 2026
url: "https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2560471970"
venue: "Internal technical design"
---
# Manual Holding Process Technical Design

This technical design evaluates three ways to implement manual holding for cashflows in RATANONE Cash Settlement. It explicitly selects use of the cashflow's main status rather than a dedicated `isHeld` attribute or a checker-only exception.

Under the selected approach, a hold blocks the listed in-progress operations: Pending Exception, Pending Netting, Ready, Queued, and Projected. Unhold is intended to restore the original status so that work is not duplicated.

The design rejects exception-based holding because it couples manual hold semantics to exception remediation and produces status-dependent behavior. It does not define the canonical held status, state persistence model, transition guards, concurrency behavior, or final service ownership.

## Source data

```text
| | ~~Additional attribute in cashflow~~ | ~~Using exception~~ | Selected one, use main status |
| --- | --- | --- | --- |
| Solution | 1. **Create a new attribute in cashflow model, "isHeld", boolean** 2. **Lifecycle service to provide the ability of switching it on/off** 3. **Query service to support the fields query** 4. **UI to add the fields in blotter, and highlight it in the details page** 5. **Release holding check to be adjusted with the logic: apart from seeing whether queued cutoff passed, also need to check the new attribute** | 1. **Create a checker only exception on manual hold action** 2. **Camunda to support achoc exception creation** 3. **UI to highlight in the details page on the exception** | 1. Hold will block all the in progress operations 1. Pending Exception (pending operator/verification) 2. Pending Netting 3. Ready 4. Queued 5. Projected 2. Unhold will revert back to the original status, to eliminate the duplicated work |
| PROs | 1. Holding process is independent with exception handling | 1. Less change on the services 2. No entity structure change | |
| CONs | 1. A bit complicated, more services need to be adjusted 2. Entity structure change | 1. Coupled the holding with exception handling, if a user want all exceptions to be fixed, but still be held, it cannot be done 2. Behavior cannot be standardized 1. On Waiting status, hold means 1. exception +1 2. status no change 2. On Ready status, hold means 1. exception +1 2. status move back to Waiting/pending verification | |
```

## Related pages

- [[manual-cashflow-holding]] defines the selected behavior.
- [[cashflow-status-restoration]] captures the requirement to restore pre-hold workflow state.
- [[manual-hold-representation-options]] compares the evaluated designs.
- [[what-is-the-authoritative-manual-hold-status-transition-contract]] tracks the unresolved implementation contract.
- [[holding-release-precheck]] is relevant because release checks must account for manual holding as well as queued-cutoff conditions.