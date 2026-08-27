---
type: query
title: What Is the Operational Recovery Process for Uber DLT Records?
created: 2026-08-24
updated: 2026-08-24
tags: [dlt, operations, replay, incident-management, uber, kafka]
related: [kafka-persistent-retry-and-dlt-recovery, uber-inbound-message-idempotency-and-error-state, tdsx-uber-message-listener]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[group", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[group]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]
---
# What Is the Operational Recovery Process for Uber DLT Records?

Uber DLT handling creates visible incomplete work: inbound and group-message records are `ERROR`, the group is `PENDING`, and downstream cashflow is not sent. The source does not define how this work is owned, diagnosed, corrected, replayed, or closed.

## Questions to Resolve

- Which team owns alert response and remediation for Uber DLT records?
- What are the topic retention period, access controls, dashboards, alert thresholds, and recovery SLA?
- What data correction must occur before replay?
- Who is authorized to replay, and what approval or audit record is required?
- Does replay use the original message, a new event, or a controlled application workflow?
- How does replay reconcile `major_version` and `New`/`Withdrawal` state?
- What control prevents duplicate downstream cashflow publication?
- When is a `PENDING` group moved to a final state after successful remediation?

## Outcome Needed

A runbook and automated observability contract are needed to make DLT a recoverable operational state rather than a durable backlog of unresolved business failures.