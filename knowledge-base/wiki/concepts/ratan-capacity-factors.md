---
type: concept
title: RATAN Capacity Factors
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, capacity-management, sla, throughput, concurrency, performance-testing]
related: [ratan-sla-capacity-baseline, ratan-performance-capacity-multipliers, what-is-the-ratan-capacity-peak-measurement-interval, are-ratan-capacity-factors-tested-or-only-sla-assumptions]
sources: ["RATAN/RATAN -Capacity/RATAN -Capacity.md"]
---
# RATAN Capacity Factors

The RATAN capacity plan organizes SLA capacity across four workload dimensions rather than using a single throughput measure.

1. **Capacity Factor-1 — Daily maximum volume:** 335,771 current daily items.
2. **Capacity Factor-2 — Peak volume:** Settlement, Trade intraday, and Trade EOD peak assumptions, described ambiguously as “per hour or minutes.”
3. **Capacity Factor-3 — Concurrent users:** maximum concurrent users per minute and total-user counts.
4. **Capacity Factor-4 — Multiplier capacity:** stress targets based on the SCB performance-testing standard.

This framework distinguishes overall daily load, short-interval peaks, interactive load, and scale-up testing. It is associated with [[ratan]] and references performance material for [[ratanone]].

## Interpretation limitation

The plan presents these figures under “Capacity agreed in SLA,” but does not explicitly classify each figure as a contractual commitment, planning assumption, test input, observed production load, or validated test result. This distinction remains open in [[are-ratan-capacity-factors-tested-or-only-sla-assumptions]].

The exact interval for peak-volume values remains open in [[what-is-the-ratan-capacity-peak-measurement-interval]].