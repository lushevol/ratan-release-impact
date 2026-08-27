---
type: concept
title: Cash Settlement Exception Handling
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, exception-handling, operations, cashflow, lifecycle]
related: [cashflow-reinstatement-and-replay, cash-settlement-ola-break-monitoring, cash-settlement-dependent-service-failure, cashflow-blotter, adhoc-ssi-exception-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md"]
---
# Cash Settlement Exception Handling

Cash Settlement exception handling is an operational control model that associates each processing failure with a lifecycle state, monitoring signal, accountable support team, and recovery action.

## State and recovery distinctions

- `ERROR` represents invalid or missing upstream data. The stated resolution is trade amendment rather than automatic retry.
- `QUEUED+Pending Exception` represents processing blocked by an unavailable Ratan service or dependent system. After recovery, OPS can use `ReInstate`.
- `FAILED` is used for Razor NACK handling. OPS can reinstate the cashflow or manually book it in [[oscar]].
- `READY+Pending Ack` is used for Ratan-to-Razor OLA breaks and may require operational replay.
- `RELEASED SETTLED` can still require a Ratan-to-Murex status write-back replay if the Murex acknowledgement breaks its OLA.

The source uses `TechFail`, `TechFailed`, and `QUEUED+Pending Exception` in related technical-failure contexts, but does not define their canonical relationship. This ambiguity is tracked in [[what-is-the-canonical-cash-settlement-exception-state-machine]].

## Operational control loop

1. Detect the failure through service monitoring, ITRS, IMS, a log signature, or database investigation.
2. Establish which system or dependency failed.
3. Restore the affected Ratan service or external dependency.
4. Notify the accountable operational team.
5. Choose the appropriate recovery mechanism: data amendment, Kafka redelivery, `ReInstate`, message replay, status replay, or manual booking.
6. Verify the resulting lifecycle status and relevant ACK/NACK history.

[[cashflow-blotter]] is a central operational surface for reinstatement and replay, while database history provides investigation evidence.

## Scope

The source explicitly assigns different recovery behaviour to different subject systems. Kafka commit suppression applies to specified Ratan service outages, including Camunda, Lifecycle Service, and the Murex adaptor. It must not be assumed for all failures involving [[murex]], [[razor]], [[bpsi]], or [[dqsl]].