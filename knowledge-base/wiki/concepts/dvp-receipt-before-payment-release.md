---
type: concept
title: DVP Receipt-Before-Payment Release
created: 2026-08-22
updated: 2026-08-22
tags: [dvp, receipt-confirmation, payment-release, nstp, nostro]
related: [ratan, tlm, confirmation-match-based-payment-release, last-mile-payment-release-control, nstp-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/Global Rates - Settlement Strategy Process & Dependency.md"]
---
# DVP Receipt-Before-Payment Release

DVP receipt-before-payment release is a conditional settlement flow in which RATAN delays payment until external evidence confirms settlement of the corresponding receipt.

The source describes the following sequence:

1. Stella stamps the trade as DVP.
2. RATAN holds the DVP cashflow as NSTP.
3. TLM provides the Nostro agent account-statement subscription.
4. RATAN confirms settlement of the SCB receipt cashflow.
5. RATAN automatically releases the SCB pay cashflow.

The source does not specify matching keys, message formats, timeouts, reversal behavior, or manual override controls.