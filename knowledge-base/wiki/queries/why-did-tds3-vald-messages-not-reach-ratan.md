---
type: query
title: Why Did TDS3 VALD Messages Not Reach RATAN?
created: 2026-08-24
updated: 2026-08-24
tags: [query, tds3, ratan, vald, message-propagation, uat-defect]
related: [tds3, ratan, fmrp-cashflow-status-synchronization, fmrp-murex-cashflow-status-synchronization, trade-validation-cashflow-gating, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--34-trade-validation-cashf--g0i06l]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/UAT test cases - Murex 2.11 booking.md"]
---
# Why Did TDS3 `VALD` Messages Not Reach RATAN?

## Question

Why did `VALD` messages appear in TDS3 evidence but not arrive on the RATAN-consumed topic in UAT scenarios 4 and 6, and what corrective control or replay process produced the later retest passes?

## Evidence

Scenario 4 records that `VALD` was not flown from TDS3 to RATAN. Scenario 6 records `VALD` in Elastic but no matching message visible through AKHQ on the inspected topic. The source states that RATAN did not receive the `VALD` message from TDS3 and that TDS3 assistance was pending.

Both scenarios were later marked `Retest PASS`, but the source does not identify the root cause, remediation, replay, bypass, or monitoring evidence supporting a durable fix.

## Information Needed

- The exact producer, topic, consumer, and correlation key for the `VALD` message.
- Whether the original message was lost, filtered, delayed, malformed, or not consumed.
- The corrective action applied before retest.
- Whether failed messages were replayed or the trades were reprocessed.
- Monitoring and reconciliation controls for future missing status messages.

Until this is documented, automatic cashflow release should be understood as dependent on end-to-end status delivery rather than solely on the presence of `VALD` in TDS3.