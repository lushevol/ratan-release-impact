---
type: comparison
title: SWAP_AGENT Single versus Resultant Hard Blocking
created: 2026-08-22
updated: 2026-08-22
tags: [swap-agent, hard-blocker, resultant-cashflow, nstp, settlement-day-2]
related: [hard-block-swap-agent-nstp-rule, component-cashflow-hard-block-marker, netting-resultant-cashflow, netting-resultant-cashflow-lifecycle, clearing-swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker.md"]
---
# SWAP_AGENT Single versus Resultant Hard Blocking

| Aspect | Single cashflow | Resultant cashflow |
| --- | --- | --- |
| Detection basis | `Instrument_Common__Murex_Product_Strategy == "SWAP_AGENT"` and payment type `Coupon` or `Interim MTM` | At least one component is `SWAP_AGENT#Coupon` or `SWAP_AGENT#Interim MTM`, represented directly or through `Cashflow__Is_Hard_Blocker` |
| Typical trigger | `Settle as Gross`, including from `Pending Auto Netting` | Manual or automatic netting of qualifying components |
| NSTP exception | `Hard Block Swap Agent` | `Hard Block Swap Agent`, alongside any other applicable exceptions |
| Category | `HARD_BLOCKER` | `HARD_BLOCKER` |
| Operational level | Proposed `MAKER_CHECKER` | Proposed `MAKER_CHECKER` |
| GUI display | Exception code appears in red | Exception code appears in red with other exceptions |
| Maker submission | Rejected | Rejected |
| Checker approval | Rejected | Rejected |
| Release from Ratan | Not permitted | Not permitted |
| Containment actions | Swift suppression, failure, hold or cashflow suppression may be available by scenario | Un-netting, Swift suppression, failure, pending exception, hold or cashflow suppression may be available by scenario |
| Non-target payment types | Initial Notional and Final Notional do not match the hard-block predicate | A resultant is blocked only when it contains a prohibited component |

## Key distinction

The hard blocker is not a universal prohibition on netting. Same-type Coupon and same-type Interim MTM cashflows may be netted, but the resulting cashflow remains unreleasable from Ratan. Mixed-payment-type eligibility is unresolved because the source contains contradictory clarification history; see [[what-is-the-authoritative-swap-agent-mixed-payment-netting-rule]].

## Lifecycle interpretation

For both forms, the control separates release from containment:

- Submission and approval cannot release the affected cashflow from Ratan.
- Operations may still perform approved lifecycle actions that keep the cashflow from bilateral settlement.
- A resultant must retain enough component information to preserve the hard-block decision after netting.

The source does not provide formal UAT sign-off confirming which operational-level variant was approved for production.