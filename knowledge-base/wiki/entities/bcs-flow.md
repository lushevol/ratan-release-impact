---
type: entity
title: BCS Flow
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, bcs, cashflow, settlement, production-support]
related: [ratan-ktlo-tracker, ratan-transient-failure-recovery, strategic-flow, razor]
sources: ["RATAN/RATAN -KTLO Tracker/RATAN -KTLO Tracker.md"]
---
# BCS Flow

BCS Flow is a RATAN processing-flow variant identified in the KTLO tracker as a recurring source of exception-replay work involving Razor responses.

## Operational Issues

The tracker reports approximately two BCS-related exception-replay tickets per week. PSS currently informs and instructs Ops to replay affected cashflows manually. STORY 8502031 concerns cashflow `006226593174`, which was caught by a RATAN auto-fail job.

GENERIC TASK 8565961 describes a BCS/Strategic Flow case in which RATAN cannot process a Razor response because it arrives before the expected processing point. The source supports an early-arrival or ordering failure as a reported operational symptom, but does not define the complete state machine or confirm the root cause.

## Proposed Direction

Automatic retry or replay, improved exception-blotter self-service, and clearer handling of status write-back are proposed areas of work. The tracker also mentions discussion of a possible migration from BCS Flow to [[entities/strategic-flow|Strategic Flow]] with a target of 2026. This is a preliminary discussion rather than an approved migration decision or delivery commitment.

## Source

See [[ratan-ktlo-tracker]] for the ticket references and evidence limitations.