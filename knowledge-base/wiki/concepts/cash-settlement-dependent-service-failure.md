---
type: concept
title: Cash Settlement Dependent-Service Failure
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, dependency, service-failure, techfail, kafka]
related: [cash-settlement-exception-handling, synchronous-kafka-to-camunda-orchestration, ssi-stamping-service, static-data-service, bpsi, dqsl, query-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md"]
---
# Cash Settlement Dependent-Service Failure

A dependent-service failure can block cashflow processing and require coordinated restoration and operational reprocessing.

## Common Ratan services

The source lists SSI, Rule, Netting, Static Data, and other common Ratan services as dependencies whose outage can move cashflows to `QUEUED+Pending Exception`. RATAN PSS identifies the failure, restores the service or external dependency, and notifies OPS to use `ReInstate`.

For [[ssi-stamping-service]], this is a broad Ratan operational failure rule and does not replace SSI-specific exception lifecycle behaviour documented in [[adhoc-ssi-exception-lifecycle]].

## BPSI via DQSL

[[bpsi]] is accessed through [[dqsl]] for booking-entity and counterparty FMCODE information. If the dependency is unavailable before FMCODE retrieval, the source states that Razor cannot continue and the cashflow may become technically failed. The recovery path is dependency restoration followed by reinstatement.

If the failure occurs after FMCODE retrieval, the source records `GSAM client Unknown` and `CORP client Unknown` NSTP exceptions instead. Whether this should instead be treated as a technical failure remains unresolved.

## Kafka recovery boundary

For Camunda, Lifecycle Service, and Murex adaptor outages, the stated recovery design is to withhold Kafka commit so the message remains available for later redelivery. This mechanism is specific to those named service paths; it is not documented as a general retry contract for all dependencies.