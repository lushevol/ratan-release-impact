---
type: query
title: What Is the Development MQ Topology for Murex-RATAN Inbound and Outbound Connectivity?
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, ratan, mq, development-environment, messaging]
related: [cn-settlement-murex-211-integration, murex-ratan-bidirectional-cashflow-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 Delivery Plan.md"]
---
# What Is the Development MQ Topology for Murex-RATAN Inbound and Outbound Connectivity?

## Question

Why did development inbound and outbound connectivity require two MQ sets when only one was applicable, and what topology or workaround was ultimately used?

## Evidence

The delivery plan records a Q4 Sprint 14 workflow task for development MQ connectivity. Its dependency note states: “Require 2 set of MQ for Dev but only one is applicable.”

## Unknowns

- The intended inbound and outbound MQ topology.
- Why one of the two required MQ sets was not applicable.
- Whether the limitation affected development, SIT, or production design.
- Any compensating control, shared queue, or sequencing mechanism.

## Needed evidence

Obtain MQ architecture diagrams, environment configuration, delivery notes, and SIT execution records.