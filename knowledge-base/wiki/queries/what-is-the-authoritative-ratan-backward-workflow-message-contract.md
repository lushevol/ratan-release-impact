---
type: query
title: What Is the Authoritative Ratan Backward Workflow Message Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, message-contract, Ratan, Razor, open-question]
related: [backward-workflow-design, cashflow-status-write-back, netted-and-gross-cashflow-status-update, razor, stella, murex-2-11, ratan-cashflow-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Backward Workflow Design.md"]
---
# What Is the Authoritative Ratan Backward Workflow Message Contract?

## Question

What is the complete and authoritative contract for settlement-status messages sent from Razor to Ratan and then synchronized to STELLA or Murex2.11?

## Known Evidence

The source identifies `ACK/NACK`, `RELEASED`, and `SETTLED` as Razor outcomes. It provides Ratan-to-Adaptor payloads for:

- Netted updates containing multiple cashflow IDs and a populated `Cashflow__Netting_Id`.
- Gross updates containing one cashflow ID and an empty `Cashflow__Netting_Id`.

Ratan is described as the owner of cashflow status updates and downstream synchronization.

## Unresolved Questions

1. What do `ACK` and `NACK` acknowledge?
2. Are `RELEASED` and `SETTLED` ordered state transitions?
3. Can `RELEASED` or `SETTLED` arrive out of order or be repeated?
4. Should a gross `Cashflow__Netting_Id` be `null` or `""`?
5. Must every cashflow ID belong to the supplied netting ID?
6. Is a netted batch atomic, partially successful, or independently retried?
7. How are duplicate, stale, and late messages handled?
8. Which Ratan service performs the state update?
9. What transport, endpoint, topic, authentication, and versioning rules apply?
10. What is the STELLA integration path and payload?
11. What exact Adaptor and Murex2.11 contract is defined in the referenced external design?
12. Are downstream updates synchronous or asynchronous, and what are their retry and idempotency guarantees?

## Evidence Gaps

The supplied document does not include the external Murex design, a STELLA interface specification, or operational behavior for retries and failures. Resolution requires the referenced `CN Settlement - Murex2.11 Technical Design`, the relevant Ratan service contract, and downstream interface documentation.
