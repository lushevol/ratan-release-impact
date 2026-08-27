---
type: source
title: Settlement Day 2 SWAP_AGENT Hard Blocker UAT1 Test Results
created: 2026-08-22
updated: 2026-08-22
tags: [uat, settlement-day-2, swap-agent, hard-blocker, nstp, netting]
related: [swap-agent, ratan, swap-agent-hard-blocker, swap-agent-payment-type-netting-control, is-hard-block-swap-agent-currently-enabled, what-is-the-production-setting-and-owner-of-swap-agent-hard-blocker-enabled, what-is-the-complete-swap-agent-payment-type-netting-matrix, cashflow-multi-exception-generation, clearing-resultant-swift-suppression, netting-un-net-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker Tech Design/Hard Blocker Uat1 Test Resault.md"]
authors: []
year: 2025
url: ""
venue: "UAT1 test evidence"
---
# Settlement Day 2 SWAP_AGENT Hard Blocker UAT1 Test Results

This UAT evidence document records tests performed from 2025-10-29 to 2025-11-06 for Settlement Day 2 hard-blocking controls on `SWAP_AGENT` cashflows in RATAN.

The document's `Result` and `Test Result` columns are blank. Screenshots and expected outcomes indicate that scenarios were exercised, but this source does not provide an auditable overall UAT pass or approval decision.

## Tested Behaviour

The tests state that an enabled control prevents manual netting of `SWAP_AGENT` Coupon or Interim MTM cashflows with other payment types, to prevent clearing-eligible cashflows from settling bilaterally. The stated error is:

> "SWAP AGENT Coupon or Interim MTM can't net with the other payment type cashflow to avoid clearing eligible cashflows settling Bilaterally"

Same-type Coupon and Interim MTM cashflows remain nettable. Their net resultant can display the `Hard block Swap Agent` exception and cannot be released through RATAN maker submission or checker approval:

> "This is a Swap Agent Coupon or Interim MTM cashflow ,can't be released from Ratan"

The evidence also tests operational actions on blocked cashflows and resultants, including Swift Suppressed, Failed, Reinstate, Hold, UnHold, Cashflow Suppressed, and Unnet.

## Test Case Register

| Test case | Function | Expected outcome |
| --- | --- | --- |
| AC-Settlement-SAL Hard Blocker-001 | Different payment-type netting | Coupon or Interim MTM cannot be manually netted with Interim MTM, Initial Notional, or Final Notional as applicable. |
| AC-Settlement-SAL Hard Blocker-002 | Same payment-type netting | Coupon-to-Coupon and Interim-MTM-to-Interim-MTM netting creates `N1`; the resultant hits the hard-blocker rule and cannot be maker-submitted. |
| AC-Settlement-SAL Hard Blocker-003 | Pending Auto Netting single cashflow | A Coupon or Interim MTM cashflow settled as gross hits the hard blocker; release is blocked and Swift Suppressed remains available. |
| AC-Settlement-SAL Hard Blocker-004 | Manual actions on a single cashflow | Checker approval is blocked; Failed, Reinstate, Hold, UnHold, and Suppress Cashflow actions are tested. |
| AC-Settlement-SAL Hard Blocker-005 | Bulk exception, Bulk Eligible not ticked | A hard-blocked item is not eligible for bulk submission; a non-hard-blocked item can follow the existing submission process. |
| AC-Settlement-SAL Hard Blocker-006 | Bulk exception, Bulk Eligible ticked | A hard-blocked item is not eligible for bulk submission. The outcome for a concurrently selected non-hard-blocked item is not stated. |
| AC-Settlement-SAL Hard Blocker-007 | Auto SWIFT suppression disabled | Auto-netted same-type Coupon or Interim MTM resultants are generated and hit the hard-blocker NSTP rule. |
| AC-Settlement-SAL Hard Blocker-008 | Initial Notional and Final Notional | An Initial Notional or Final Notional cashflow is expected not to hit the hard blocker and can be released from RATAN. The explicit evidence identifier is for Initial Notional. |
| AC-Settlement-SAL Hard Blocker-009 | Single cashflow with multiple exceptions | Hard blocker coexists with Missing Vostro, Pending Affirmation, or similar exceptions; release is blocked and Swift Suppressed remains available. |
| AC-Settlement-SAL Hard Blocker-010 | Resultant with multiple exceptions | A same-type resultant displays the hard blocker with other exceptions; it cannot be submitted but can be unnetted or manually state-managed. |
| AC-Settlement-SAL Hard Blocker-011 | Auto netting with Auto SWIFT Suppressed rule | Same-type Coupon or Interim MTM source cashflows are netted and create a `SWIFT_SUPPRESSED` resultant with payment type `SAL MTM Netting`. |
| AC-Settlement-SAL Hard Blocker-012 | Non-hard-blocker NSTP rule creation | A non-hard-blocker NSTP rule can be created and approved. |
| AC-Settlement-SAL Hard Blocker-013 | Manual-netting regression | BIC Netting, CCIL Netting, and Bilateral Netting are reported as functioning well; evidence is limited UAT regression evidence rather than comprehensive certification. |

## Enabled Configuration Test Data

| No | Config Value | Function | Scenario | Test Result | Test Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Enabled = false; | Different payment type netting | C1 Interim MTM， C2 Coupon C1 C2 can be netted together. | | M0P551703219 SWAP_AGENT Interim MTM M0P551703220 SWAP_AGENT Coupon Net N00000049789 |
| 2 | Enabled = false; | Same payment type netting | C1 ,C2 Coupon C1 C2 can be netted together. | | SWAP_AGENT Coupon M0P551703221 SWAP_AGENT Coupon M0P551703222 N00000049790 |
| 3 | Enabled = false; | Same payment type netting | C1 ,C2 Interim MTM C1 C2 can be netted together. | | SWAP_AGENT Interim MTM M0P551703218 SWAP_AGENT Interim MTM M0P551703217 N00000049791 |
| 4 | Enabled = false; | Different payment type netting | C1 Final Notional， C2 Coupon C1 C2 can be netted together. | | SWAP_AGENT Final Notional M0P551703230 SWAP_AGENT Coupon M0P551703229 N00000049792 |
| 5 | Enabled = false; | Different payment type netting | C1 Final Notional， C2 Interim MTM C1 C2 can be netted together. | | SWAP_AGENT Final Notional M0P551703231 SWAP_AGENT Interim MTM M0P551703216 |
| 5.1 | Enabled = false; | Same payment type netting | C1 Final Notional， C2 Final Notional， C1 C2 can be netted together. | | SWAP_AGENT Final Notional M0P551703242 SWAP_AGENT Final NotionalM0P551703240 N00000049813 |
| 6 | Enabled = true; | Different payment type netting | C1 Final Notional， C2 Coupon C1 C2 can not be netted together. | | SWAP_AGENT Final Notional M0P551703232 SWAP_AGENT Coupon M0P551703228 |
| 7 | Enabled = true; | Different payment type netting | C1 Final Notional， C2 Interim MTM C1 C2 can not be netted together. | | SWAP_AGENT Final Notional M0P551703232 SWAP_AGENT Interim MTM M0P551703215 |
| 8 | Enabled = true; | Different payment type netting | C1 Interim MTM， C2 Coupon C1 C2 can not be netted together. | | SWAP_AGENT Interim MTM M0P551703215 SWAP_AGENT Coupon M0P551703228 |
| 9 | Enabled = true; | Same payment type netting | C1 ,C2 Interim MTM C1 C2 can be netted together. | | SWAP_AGENT Interim MTM M0P551703214 SWAP_AGENT Interim MTM M0P551703213 N00000049794 |
| 10 | Enabled = true; | Same payment type netting | C1 ,C2 Coupon C1 C2 can be netted together. | | SWAP_AGENT Coupon M0P551703223 SWAP_AGENT Coupon M0P551703224 N00000049795 |

## Limitations

`Enabled` is not identified by a technical property name, owner, persistence location, default value, or production scope. The document also does not provide a complete payment-type matrix, particularly for Initial Notional combinations while enabled.