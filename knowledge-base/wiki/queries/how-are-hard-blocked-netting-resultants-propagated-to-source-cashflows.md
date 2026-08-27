---
type: query
title: How Are Hard-Blocked Netting Resultants Propagated to Source Cashflows?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, netting-resultant, lifecycle, NSTP, hard-blocker, Swift-Suppressed]
related: [hard-block-swap-agent-nstp-rule, netting-resultant-cashflow, netting-resultant-cashflow-lifecycle, ratan-cashflow-lifecycle-state-machine, clearing-resultant-swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Block UAT testing.md"]
---
# How Are Hard-Blocked Netting Resultants Propagated to Source Cashflows?

## Question

When a netting resultant hits the `Hard block Swap Agent` NSTP rule, which object owns the exception and which objects receive subsequent lifecycle or suppression status changes?

## Evidence

In the new-solution same-type Coupon test:

1. C1 and C2 were netted.
2. Resultant `N1` was generated.
3. `N1` hit the NSTP hard-blocker rule.
4. The GUI displayed the `Hard block Swap Agent` exception in red.
5. Maker submission was rejected.
6. The document records C1 as reaching `Swift Suppressed`.

The evidence does not state whether C2 also reached `Swift Suppressed`, whether `N1` was suppressed, or whether `N1` was withdrawn or made `DEAD`.

Historical old-solution tests provide a different lifecycle pattern: after hard-blocked resultants were un-netted, `N1` became `DEAD`, while the source cashflows returned to statuses such as `Pending Auto Netting` and `Pending Exception`.

## Resolution Needed

The authoritative lifecycle should specify:

- Exception ownership for `N1`, C1, and C2.
- Status transitions for each source cashflow and the resultant.
- Whether `Swift Suppressed` can be applied to a source flow after the resultant is hard-blocked.
- Whether un-netting is required or permitted.
- Whether maker/checker state is preserved across the transition.