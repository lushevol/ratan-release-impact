---
type: concept
title: Message Topic Consolidation
tags: [messaging, topics, migration, routing, cash-settlement]
related: [message-bridge, domain-owned-message-filtering, message-header-propagation, message-bridge-filtering-vs-domain-service-filtering, ratan, tds3, murex, scbml]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message Bridge Filters.md"]
---
# Message Topic Consolidation

Message topic consolidation is the proposed combination of target message topics as part of removing business filters from [[message-bridge|Message Bridge]].

## Proposed Topic Scope

The source identifies the following topic combinations:

1. `TDS3_All_Trade_Message_Process_In`, `Confirmation_Orchestration_Process_In`, `TDS3_Trade_Murex_Message_Process_In`, `TDS3_Trade_Message_Process_In`
2. `Settlement_Orchestration_Process_In`, `Cash_Settlement_Group_Message_Inbound`
3. `Settlement_Ssi_Notification_Event_In`, `Settlement_Ssi_Notification_Event_In_RT_Decom`
4. `Settlement_Cashflow_Status_In`, `Cash_Settlement_Cashflow_Status_In`
5. `Settlement_Receiver_Ack_Nack_In`, `Cash_Settlement_Receiver_Ack_Nack_In`

The scope includes [[tds3|TDS3]] and [[murex|Murex]]-related trade messages, as well as cash-settlement orchestration, SSI notification, cashflow-status, and receiver acknowledgment flows.

## Required Compatibility Checks

A combined topic must be validated for:

- payload and schema compatibility;
- ordering and replay requirements;
- retention and dead-letter behavior;
- consumer-group capacity;
- access-control boundaries;
- observability and operational ownership;
- service-specific filtering semantics.

The source proposes these combinations but does not provide compatibility evidence, migration order, rollback steps, or consumer acceptance criteria. Therefore, topic consolidation remains a proposed migration item rather than an approved contract change.