---
type: entity
title: AKHQ
created: 2026-08-23
updated: 2026-08-23
tags: [AKHQ, Kafka, testing, operations]
related: [kafka, mock-settlement-test-data-generation, fmo-post-trade-portal]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Mock testing data userguide.md"]
---

# AKHQ

AKHQ is the Kafka web interface used by the mock settlement-data procedure.

## Role in testing

Testers use AKHQ to:

- Select a target environment such as `dev`, `uat1`, or `uat2`.
- Search for `Cash_Settlement_Group_Message_Inbound`.
- Inspect and copy an existing cashflow message.
- Modify `trackingId` and `cashflowId`.
- Produce the modified message back to the Kafka topic.

The guide uses this URL:

http://uklvadapp1340.uk.dev.net:9090/ui/uat-2/topic?search=group&topicListView=HIDE_INTERNAL&page=1

A successful producer notification is treated as message-production confirmation. It is not, by itself, evidence of downstream cashflow creation or settlement completion.
