---
type: entity
title: ratan_cashflow_message_io
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, kafka, message-audit, cashflow]
related: [cashflow, group-management-service, ratan-cashflow-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Group Management Service - Non-Eco Amendment Technical Design.md"]
---
# ratan_cashflow_message_io

`ratan_cashflow_message_io` is a proposed logical audit table for inbound and outbound Kafka messages associated with cashflow processing. It stores message headers, payload content, direction, and an aggregate message key in the form `tradeId|majorVersion|cashflowId`.

The source supplies no types, constraints, message-retention policy, payload protection requirements, or correlation semantics.

| Column name | Column description | Sample Value |
| --- | --- | --- |
| id | primary key |  |
| header | kafka message header |  |
| content | kafka message payload |  |
| direction | message inbound or outbound | IN OUT |
| message_key | message aggregate id, tradeId\|majorVersion\|cashflowId | 15700093\|1\|M00017700002 |
| version | technical version |  |
| created_at |  |  |
| updated_at |  |  |