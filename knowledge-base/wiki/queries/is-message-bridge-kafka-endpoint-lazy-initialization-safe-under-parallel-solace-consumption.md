---
type: query
title: Is Message Bridge Kafka Endpoint Lazy Initialization Safe Under Parallel Solace Consumption?
created: 2026-08-24
updated: 2026-08-24
tags: [message-bridge, apache-camel, kafka, solace, concurrency]
related: [message-bridge, solace-to-kafka-fan-in, lazy-kafka-endpoint-initialization-race]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]
---
# Is Message Bridge Kafka Endpoint Lazy Initialization Safe Under Parallel Solace Consumption?

The incident attributes `workerPool must be specified` failures to concurrent first use of a lazily initialized Apache Camel Kafka endpoint after changing from one Solace route to eight routes sharing a Kafka destination.

The source provides an observed exception and a plausible execution model, but does not establish the deployed Camel version, Kafka component version, endpoint lifecycle implementation, or a reproduction.

## Questions to resolve

- Which Apache Camel and Camel Kafka component versions ran in `fmrp1` and `fmrp2`?
- Is the shared `KafkaEndpoint` configured for lazy startup, and how is endpoint startup synchronized?
- Can the failure be reproduced with simultaneous first sends from multiple Solace routes and `.parallelProcessing()`?
- Does eager endpoint initialization, startup sequencing, or endpoint isolation eliminate the failure?
- What concurrency and startup-load tests demonstrate safe behavior?
- Did any deployed fix address the `workerPool` failure, and was it validated in both environments?

The unsupported claim that more than ten consumers makes failure nearly certain should not be used as an operational threshold without measured failure-rate evidence.