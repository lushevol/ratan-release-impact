---
type: concept
title: RATAN-Razor (MX-FXCASH) Interface
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, razor, mx-fxcash, cash-settlement, trade-stp, fx-replication, scbml]
related: [ratan, mx-fxcash, fxu, ratan-fx-replication, ratan-fxu-utilization-integration, what-is-the-relationship-between-razor-mx-fxcash-and-fxu, 5-ratan--17-ratan-interfaces--31-ratan-and-razor-mx-fxcash-40630--y3x7oc]
sources: ["RATAN/RATAN -Interfaces/Ratan and Razor (MX-FXCASH)-40630.md"]
---
# RATAN-Razor (MX-FXCASH) Interface

The RATAN-Razor (MX-FXCASH) interface is a set of cash-settlement, payment-status, trade/event, and utilization-related feeds involving [[ratan]] and `MX-FXCASH`. The source uses “Razor (MX-FXCASH)” as the counterpart designation but does not define whether Razor and MX-FXCASH are distinct systems or alternative names.

## Defined Directional Flows

### Outbound Trade STP

RATAN sends FX trade and event messages to MX-FXCASH for [[ratan-fx-replication]].

- Direction: `Ratan -> MX-FXCASH`
- Trade condition: `BOOKED`
- Products: FX Spot, Forward, Swap
- Format: `SCBML V4.0`

These details apply to this specific Razor/MX-FXCASH path and must not be generalized to other RATAN FX-replication integrations.

### Inbound BCS Payment Status

MX-FXCASH sends payment-status updates to RATAN.

- Direction: `MX-FXCASH -> Ratan`
- Statuses: `Released`, `Settled`, `Netted`, `Split`, `CCPNetted`
- Population: eligible payments
- Excluded population: `UTIL` trades and reversal/resultant payments for `SPLIT` and Netting events
- Format: `SCBML V4.0`
- Stated size limit: `2M`

“Eligible payments” and the unit and application of the `2M` limit are not defined in the source.

## Feed Scope

Cashflow, payment-status, ACK/NACK, cashflow-affirmation, and cashflow-failed-status feeds are scoped to London, Singapore, Hong Kong, Jersey, Egypt, and China 30 Branches.

Trade and event messages have a different scope: China 30 Branches, UK, HK, Taiwan, Germany, Malaysia, Singapore, Thailand, Philippines, India, Sri Lanka, and Bangladesh.

Utilization request and utilization-response ACK/NACK are listed only for Egypt, Nepal, and Saudi. Their detailed design is delegated to [[ratan-fxu-utilization-integration]].

## Contract Boundaries

The source establishes high-level feed inventory, limited scope, and the two explicit flows above. It does not establish payload fields, endpoints, authentication, transport, sequencing, retries, failure handling, reconciliation, monitoring, or support ownership.

The direction of cashflow, generic ACK/NACK, affirmation, and failed-status feeds is not explicitly stated. The relationship among Razor, [[mx-fxcash]], and [[fxu]] is tracked in [[what-is-the-relationship-between-razor-mx-fxcash-and-fxu]].