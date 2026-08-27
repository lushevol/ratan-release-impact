---
type: query
title: "What Is the Authoritative SAL Hard-Blocker Action Matrix?"
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, sal, swap-agent, nstp, hard-blocker, authorization, lifecycle]
related: [sal-swap-agent-hard-blocker, maker-checker-hard-blocker-operational-levels, nstp-hard-blocker-bulk-eligibility, netting-resultant-cashflow-lifecycle, clearing-resultant-swift-suppression, ratan-rule-lifecycle-management]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Self testing evdience.md"]
---
# What Is the Authoritative SAL Hard-Blocker Action Matrix?

The UAT evidence establishes that the SAL `SWAP_AGENT` hard blocker prevents tested release or approval paths, but it does not provide a complete authorization matrix.

The open question is which actions are permitted for each combination of:

- Source cashflow versus netting resultant
- `Coupon` or `Interim MTM` payment type
- `Maker Only`, `Checker Only`, or `Maker Checker`
- `WAITING`, `Pending Auto Netting`, `Pending Exception`, `NETTED`, `Failed`, `Hold`, or `SWIFT_SUPPRESSED` state
- Hard blocker alone versus hard blocker combined with Missing Vostro, Missing Nostro, Pending Affirmation, or other exceptions
- Manual netting versus auto-netting
- Automatic Swift suppression enabled versus disabled

The evidence reports testing of unnet, Swift suppression, manual failure, reinstatement, hold/unhold, cashflow suppression, maker submission, checker approval, and operator release, but does not define the authoritative service-side rule or precedence model.

Resolution should identify the governing requirement, implementation contract, or signed-off test evidence and distinguish release eligibility from general status-transition eligibility.