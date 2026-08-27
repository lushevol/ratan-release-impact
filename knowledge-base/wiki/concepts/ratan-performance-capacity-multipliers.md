---
type: concept
title: RATAN Performance Capacity Multipliers
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, capacity, performance-testing, stp, throughput, concurrency]
related: [ratan-capacity-factors, ratan-sla-capacity-baseline, why-is-ratan-trade-eod-capacity-targeted-at-2x, are-ratan-capacity-factors-tested-or-only-sla-assumptions]
sources: ["RATAN/RATAN -Capacity/RATAN -Capacity.md"]
---
# RATAN Performance Capacity Multipliers

The RATAN capacity plan states that RATAN is capable of processing up to four times hourly volume based on the SCB performance-testing standard. Its explicit process-level targets are:

| Workload | Base peak value | Multiplier | Stated target |
|---|---:|---:|---:|
| Settlement STP | 19,396 | 4X | 77,584 per hour |
| Trade intraday STP | 10,927 | 4X | 43,708 per hour |
| Trade EOD STP | 58,713 | 2X | 117,426 per hour |
| Concurrent users | 103 | 4X | 412 |

## Trade EOD exception

Trade EOD is explicitly calculated at **2X**, unlike Settlement, intraday Trade, and concurrent users, which are calculated at 4X. The broad “up to 4 times” statement must therefore not be interpreted as a uniform requirement for every process.

The rationale and authoritative standard behind this exception remain open in [[why-is-ratan-trade-eod-capacity-targeted-at-2x]].

## Evidence limitation

These values are stated capacity targets or calculations. This source does not include executed-test results, infrastructure configuration, observed bottlenecks, or pass/fail evidence.