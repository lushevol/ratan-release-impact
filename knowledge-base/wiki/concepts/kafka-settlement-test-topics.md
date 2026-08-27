---
type: concept
title: Kafka Settlement Test Topics
created: 2026-08-23
updated: 2026-08-23
tags: [Kafka, topics, message-routing, settlement-testing]
related: [kafka, cdu, tds3, mock-settlement-test-data-generation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Mock testing data userguide.md"]
---

# Kafka Settlement Test Topics

The mock testing guide identifies distinct Kafka topics for cashflow input, trade input, confirmation-status input, and trade-event publication.

## Topic mapping

```text
Cash_Settlement_Group_Message_Inbound:
  Used as the source and destination topic when cloning a cashflow message.

TDS3_Trade_Message_Process_In:
  Receive Trade

CDU_Trade_Confirmation_Process_In:
  Receive confirmation status

Trade_Service_Trade_Events:
  Publish event
```

## Interpretation

The topic names indicate a separation between trade receipt, confirmation-status receipt, and event publication. The guide does not identify the owning services or explicitly state that producing to `CDU_Trade_Confirmation_Process_In` guarantees publication to `Trade_Service_Trade_Events`.

Complete schemas, message headers, keys, ordering requirements, status values, and success evidence are not provided.
