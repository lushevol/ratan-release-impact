---
type: entity
title: Uber Message Topics
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, uber-messages, cash-settlement, inbound-messaging]
related: [kafka, multi-topic-kafka-consumer-parallelism, fmrp2, staging]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/[group", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/[group] PT of consuming messages on multiple Uber topics.md"] PT of consuming messages on multiple Uber topics.md"] PT of consuming messages on multiple Uber topics.md"]
---
# Uber Message Topics

Uber Message Topics are the seven Kafka inbound topics used to distribute Cash Settlement Uber-message test workloads.

## Topic Family

```text
tdsx_uber_message_json_inbound_fx_other
tdsx_uber_message_json_inbound_fx_spot
tdsx_uber_message_json_inbound_equity
tdsx_uber_message_json_inbound_cash
tdsx_uber_message_json_inbound_commodity
tdsx_uber_message_json_inbound_interestrate
tdsx_uber_message_json_inbound_loan
```

Splitting the workload across these topics increases the available partition-level processing parallelism. The performance tests show that realized end-to-end capacity remains dependent on active partitions, consumer concurrency, downstream service capacity, and database connections.

See [[multi-topic-kafka-consumer-parallelism]].