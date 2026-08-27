---
type: entity
title: Apache JMeter
created: 2026-08-24
updated: 2026-08-24
tags: [performance-testing, load-testing, test-tool]
related: [find-currency2-by-currency1, fxu-operation-performance-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case/PT.md"]
---
# Apache JMeter

Apache JMeter is the load-testing tool named in the performance-test dashboards for [[find-currency2-by-currency1]].

The source records a JMeter throughput setting of `10` for two 360-second tests. For the two tests using the `ultimate` rate-limiter setting, the JMeter throughput field is recorded as not set. The source does not identify thread counts, virtual-user configuration, connection settings, ramp-up profile, or the metric unit represented by the throughput field.

JMeter throughput configuration must be distinguished from actual achieved throughput reported by a dashboard and from queue-specific TPS metrics.