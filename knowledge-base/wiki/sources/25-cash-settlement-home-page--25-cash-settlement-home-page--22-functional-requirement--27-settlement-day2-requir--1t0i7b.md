---
type: source
title: Cash Settlement Home Page — Settlement Day 2 Swap Agent Hard Blocker Requirement
authors: []
year: 2025
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/9832947"
venue: "Cash Settlement Home Page functional requirement and UAT specification"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, settlement-day-2, swap-agent, nstp, hard-blocker, uat]
related: [hard-block-swap-agent-nstp-rule, swap-agent, cash-settlement-home-page, manual-cashflow-netting, netting-resultant-cashflow, clearing-swift-suppression, bulk-exception-eligibility, swap-agent-mtm-coupon-netting-separation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker.md"]
---
# Cash Settlement Home Page — Settlement Day 2 Swap Agent Hard Blocker Requirement

## Summary

This functional requirement defines a Settlement Day 2 control for preventing `SWAP_AGENT` Coupon and Interim MTM cashflows from being released and settled bilaterally from Ratan. The requirement follows a production accident in which the UK settlement team released two `SWAP_AGENT` Coupon cashflows that should have been handled by Clearing Ops and remained Swift-suppressed in Ratan.

The requested solution combines:

- A manual-netting UI restriction for incompatible payment types.
- An NSTP `HARD_BLOCKER` rule for qualifying single and resultant cashflows.
- Component-to-resultant hard-block propagation.
- Restrictions on maker submission, checker approval and bulk submission.
- Regression coverage for BIC, CCIL, bilateral, bulk and non-hard-blocker NSTP processing.

The scope is explicitly limited to `SWAP_AGENT`.

## Requirement scope

The affected single cashflows satisfy both of the following conditions:

```text
Instrument_Common__Murex_Product_Strategy == "SWAP_AGENT"
Cashflow__Payment_Type == "Coupon" or "Interim MTM"
```

A resultant cashflow is also affected when one of its components is a `SWAP_AGENT#Coupon` or `SWAP_AGENT#Interim MTM` cashflow.

The control is intended to prevent release from Ratan. Containment and lifecycle actions such as un-netting, Swift suppression, manual failure, hold and cashflow suppression may remain available where specified by the scenario.

## Manual-netting requirement

For cashflows with the same booking entity, counterparty, currency and payment date:

| Cashflow 1 | Cashflow 2 | Manual-netting expectation |
| --- | --- | --- |
| `SWAP_AGENT` Coupon | `SWAP_AGENT` Coupon | Allowed; resultant is hard-blocked by NSTP |
| `SWAP_AGENT` Interim MTM | `SWAP_AGENT` Interim MTM | Allowed; resultant is hard-blocked by NSTP |
| `SWAP_AGENT` Coupon | `SWAP_AGENT` Interim MTM | Blocked |
| `SWAP_AGENT` Coupon | Initial Notional | Blocked |
| `SWAP_AGENT` Coupon | Final Notional | Blocked |
| `SWAP_AGENT` Interim MTM | Initial Notional | Blocked |
| `SWAP_AGENT` Interim MTM | Final Notional | Blocked |
| `SWAP_AGENT` Coupon or Interim MTM | Another product or payment type | Blocked |

The specified UI error is:

```text
SWAP AGENT Coupon or Interim MTM can't net with the other payment type cashflow to avoid clearing eligible cashflows settling Bilaterally
```

## NSTP configuration

The final proposed condition is:

```text
((Instrument_Common__Murex_Product_Strategy == "SWAP_AGENT" && Cashflow__Payment_Type in ("Coupon", "Interim MTM")) || Cashflow__Is_Hard_Blocker == true)
```

| Field | Value |
| --- | --- |
| Exception Code | `Hard Block Swap Agent` |
| Exception Category | `HARD_BLOCKER` |
| Operational Level | `MAKER_CHECKER` |
| Bulk Eligible | Not ticked |
| Requestor/Eops reference | `Hard Block Swap Agent` |

The source records these superseded implementation conditions:

```text
(Cashflow__Netting_Id == null || Cashflow__Netting_Id == "") &&
Instrument_Common__Murex_Product_Strategy == "SWAP_AGENT" &&
(Cashflow__Payment_Type == "Coupon" || Cashflow__Payment_Type == "Interim MTM")
```

```text
(Cashflow__Netting_Id != null && Cashflow__Netting_Id != "") &&
(
  Cashflow__Component_Strategy_Payment_Hard_Blocker matches
  "(?i)^.*(^|,)SWAP_AGENT#Coupon(,|$).*$"
  ||
  Cashflow__Component_Strategy_Payment_Hard_Blocker matches
  "(?i)^.*(^|,)SWAP_AGENT#Interim MTM(,|$).*$"
)
```

The final condition uses the direct single-cashflow attributes or `Cashflow__Is_Hard_Blocker` rather than retaining separate netting-ID branches.

## Expected operational behavior

When a qualifying single or resultant cashflow hits the rule:

- `Hard Block Swap Agent` is displayed in red in the GUI.
- Maker submission is rejected.
- Checker approval is rejected.
- The GUI displays:

```text
This is a Swap Agent Coupon or Interim MTM cashflow ,can't be release from Ratan
```

The exception is a complete blocker rather than a remediable high-risk exception. A `SWAP_AGENT` Initial Notional or Final Notional cashflow is outside the blocker condition and should remain releasable when no other exception prevents release.

## Resultant cashflow behavior

Same-type Coupon and same-type Interim MTM cashflows may be manually or automatically netted, producing a resultant such as `N1`. The resultant must:

- Preserve or derive the component hard-block indication.
- Hit `Hard Block Swap Agent`.
- Remain unreleasable from Ratan.
- Support specified containment actions, including Swift suppression, failure, pending exception, hold, cashflow suppression and un-netting where applicable.

The requirement expects auto-netting to create a resultant while source cashflows become `NETTED`; in the stated scenario the resultant is `SWIFT_SUPPRESSED` and hits the hard-block NSTP rule.

## UAT coverage

The documented acceptance criteria cover:

- Mixed-payment-type manual-netting rejection.
- Same-payment-type netting followed by resultant hard blocking.
- Single cashflows moved from `Pending Auto Netting` through `Settle as Gross`.
- Multiple exceptions, including Missing Vostro and Pending Affirmation.
- Bulk submission when `Bulk Eligible` is both unticked and ticked.
- Auto-netting with automatic Swift suppression disabled.
- Non-target Initial Notional and Final Notional flows.
- Creation of non-hard-blocker NSTP rules.
- Regression for BIC, CCIL, bilateral, bulk-submit and bulk-approve functions.

The source does not include formal UAT execution results or production sign-off.

## Evidence and unresolved interpretation

The production incident, explicit predicates, exception metadata, UI messages and acceptance criteria provide strong evidence for the intended hard-block behavior. Implementation certainty is lower because the source does not establish whether resultant detection is populated through `Cashflow__Is_Hard_Blocker` or still requires `Cashflow__Component_Strategy_Payment_Hard_Blocker`.

The manual-netting requirement also contains a contradiction. The detailed requirement and proposed solution prohibit mixed payment-type netting, while the 2025-10-14 open-question answer says that `SWAP_AGENT` Coupon and Interim MTM will net with other payment types. This conflict is tracked in [[what-is-the-authoritative-swap-agent-mixed-payment-netting-rule]].

## References

- Story 9832947: [Swap Agent Day2 hard blocker requirement finalization](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/9832947)
- UAT reference: [Hard Block UAT testing - Derivative Strategy Projects](https://confluence.global.standardchartered.com/display/DSP/Hard+Block+UAT+testing)
- Related control: [[hard-block-swap-agent-nstp-rule]]
- Related resultant behavior: [[component-cashflow-hard-block-marker]]