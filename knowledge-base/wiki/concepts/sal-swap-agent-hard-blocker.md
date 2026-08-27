---
type: concept
title: SAL SWAP_AGENT Hard Blocker
created: 2026-08-22
updated: 2026-08-22
tags: [sal, swap-agent, hard-blocker, nstp, settlement-day-2, release-control]
related: [nstp, murex, swap-agent, sal-mtm-and-coupon-auto-netting, auto-netting-resultant-nstp, manual-cashflow-netting, netting-resultant-cashflow, pending-auto-netting-state, settlement-suppression-exceptions, fmo-post-trade-portal]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Self testing evdience.md"]
---
# SAL SWAP_AGENT Hard Blocker

The SAL `SWAP_AGENT` hard blocker is an NSTP rule that prevents qualifying cashflows from being released or approved for bilateral settlement.

## Rule scope

The explicitly recorded predicate is:

```text
(Cashflow__Netting_Id == null || Cashflow__Netting_Id == "") &&
Instrument_Common__Murex_Product_Strategy == "SWAP_AGENT" &&
(Cashflow__Payment_Type == "Coupon" || Cashflow__Payment_Type == "Interim MTM")
```

The rule therefore covers `SWAP_AGENT` `Coupon` and `Interim MTM` cashflows without an existing netting identifier. The evidence should not be generalized to every SAL payment type or every Murex product strategy.

## Observable behavior

When the rule matches:

- The `Hard block Swap Agent` exception is shown in red.
- Release or approval attempts display the message: “This is a Swap Agent Coupon or Interim MTM cashflow, can't be released from Ratan.”
- Maker submission is rejected when the rule is maker-controlled.
- Checker approval is rejected when the rule is checker-controlled.
- A hard-blocked item is excluded from bulk submission.

The exact UI text and punctuation should be verified against an authoritative interface or API contract before being treated as immutable.

## Netting behavior

The hard blocker does not necessarily prevent resultant creation. In tested same-payment-type cases, source cashflows could be netted and a resultant was generated. The resultant then received the hard-blocker exception and could not be released or approved through the prohibited workflow.

Different payment-type combinations were rejected during manual netting, including combinations involving `Coupon`, `Interim MTM`, `Initial Notional`, `Final Notional`, and, in one scenario, `RECALC`. This demonstrates a payment-type compatibility restriction but not a complete compatibility matrix.

## Exclusions

`SWAP_AGENT` `Initial Notional` and `Final Notional` cashflows did not hit this hard-blocker rule in the tested scenarios and were released through the tested process. This is a predicate-specific observation, not a guarantee for all rule versions.

## Coexisting exceptions and actions

The hard blocker can coexist with Missing Vostro, Missing Nostro, Pending Affirmation, and other settlement exceptions. The evidence indicates that some lifecycle or exception-management actions remained available, including unnetting, Swift suppression, manual failure, reinstatement, hold/unhold, and cashflow suppression. Their authorization and sequencing are not fully defined.