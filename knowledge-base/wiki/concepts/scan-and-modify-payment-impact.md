---
type: concept
title: Scan and Modify Payment Impact
created: 2026-08-22
updated: 2026-08-22
tags: [murex, pss, scan-and-modify, payment-lifecycle, controls]
related: [murex, ratan, murex-ratan-reversal-and-replacement-lifecycle, swap-agent-hard-blocker]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Analyse murex event impacting payment to Ratan.md"]
---
# Scan and Modify Payment Impact

Scan & Modify (S&M) is a Murex modification process performed through PSS. Unlike an operational Modify, the data change may be staged before the S&M procedure is triggered; the payment impact can therefore occur later than the initial modification.

## Payment effect

The source reports that S&M can produce reverse and new payment events, including for a payment already released to RATAN (`RLSR`). It states that S&M may bypass system rules such as hard blockers.

This is a general Murex/PSS observation. It is not evidence that any specific hard-blocker rule, including [[swap-agent-hard-blocker]], is bypassed in every S&M case.

## Operational implication

Downstream processing needs to accommodate payment lifecycle events that occur after a delayed procedure and that may affect released payments. Reconciliation and event recovery should not assume that the time of trade modification equals the time of payment-event delivery.