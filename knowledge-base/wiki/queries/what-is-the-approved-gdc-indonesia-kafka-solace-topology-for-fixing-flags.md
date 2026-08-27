---
type: query
title: What Is the Approved GDC-Indonesia Kafka-Solace Topology for Fixing Flags?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, gdc, indonesia, kafka, solace, message-bridge, fixing-flag]
related: [message-bridge, kafka, solace, indonesia-pending-fixing-flag-relay, indonesia-ratan-data-residency-isolation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Fixing Flag Process in Indonesia.md"]
---
# What Is the Approved GDC-Indonesia Kafka-Solace Topology for Fixing Flags?

The draft describes a logical route from GDC Kafka to an FM Solace topic and from an Indonesian FM Solace queue to Kafka. It does not define the physical or operational topology.

Approval is needed for Kafka clusters and topic names, Solace topic and queue names, subscriptions, ownership, ACLs, encryption, persistence, delivery semantics, retry and replay, monitoring, alerting, reconciliation, and the data-residency basis for cross-domain message forwarding.