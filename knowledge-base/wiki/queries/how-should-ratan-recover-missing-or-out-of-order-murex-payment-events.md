---
type: query
title: How Should RATAN Recover Missing or Out-of-Order Murex Payment Events?
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, murex, event-recovery, reconciliation, payment-lifecycle]
related: [murex, ratan, murex-ratan-reversal-and-replacement-lifecycle, murex-payment-trade-lineage-identifiers]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Analyse murex event impacting payment to Ratan.md"]
---
# How Should RATAN Recover Missing or Out-of-Order Murex Payment Events?

## Question

What operational and technical process should RATAN use when a Murex payment event is missing, duplicated, delayed, or received out of order?

## Evidence

The source explicitly identifies “Messge lost” as an exception scenario without defining recovery behaviour. It also documents that a reversal may be generated before a re-fixing replacement, with the replacement arriving hours or days later. Reverse/new outputs can also be non-1:1.

## Required design coverage

The recovery design should define:

- message persistence and idempotency;
- sequence-independent lifecycle processing;
- detection of missing expected events;
- aging and escalation of unmatched flows;
- replays and source-of-truth reconciliation;
- treatment of released payments affected by Scan & Modify; and
- named operational ownership and service-level targets.

See [[what-is-the-approved-ratan-correlation-key-for-murex-reversal-and-new-payments]].