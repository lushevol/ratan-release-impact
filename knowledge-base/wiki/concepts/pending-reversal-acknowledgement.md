---
type: concept
title: Pending Reversal Acknowledgement
created: 2026-08-22
updated: 2026-08-22
tags: [payment-reversal, duplicate-payment-prevention, hard-block, fmsre, fmswift]
related: [murex-ratan-reversal-and-replacement-lifecycle, fmswift-gateway, fmsre]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/NSTP Workflow.md"]
---
# Pending Reversal Acknowledgement

Pending Reversal Ack is the state in which a replacement payment follows a reversal but the payment gateway has not yet acknowledged the original reversal.

The proposed control is a hard block: RATAN must prevent release of the new payment until FMSWIFT Gateway acknowledges the reversal. The Day 1 workflow is expected to use [[entities/fmsre]].

If an override path permits release, the source specifies a soft warning:

> Releasing a New Payment might result in duplicate payment. Has the Original Payment cancelled / funds have been recalled?

The warning should provide Yes, Proceed to release New payment and Exit actions. The distinction between the hard block before acknowledgement and the soft-warning override path requires precise state-transition and authority documentation.
