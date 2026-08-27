---
type: query
title: Does Message Bridge Change Uber End-to-End STP Performance?
created: 2026-08-24
updated: 2026-08-24
tags: [uber, message-bridge, settlement-stp, performance-testing]
related: [uber, uber-scbml-performance-regression-testing, solace-to-kafka-fan-in, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--19101up]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/PT result for UBER.md"]
---
# Does Message Bridge Change Uber End-to-End STP Performance?

## Status

Open.

The recorded Round 1 Uber performance observation was run without Message Bridge. It therefore does not represent the full end-to-end path if Message Bridge participates in production Uber processing.

Measure matched workloads with and without the intermediary path. Capture end-to-end latency percentiles, throughput, retries, terminal failures, queue lag, and service resource consumption. Determine whether the Message Bridge contribution changes the SCBML no-regression outcome or Uber operational behavior.