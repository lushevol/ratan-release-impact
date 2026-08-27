---
type: source
title: Ratan and Razor (MX-FXCASH)-40630
authors: [Yunzhe Ta, Junying Jiang, Pengpeng Li, Jie Cai]
year: 2026
url: ""
venue: Internal Confluence documentation
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, razor, mx-fxcash, cash-settlement, fx-replication, interface-40630]
related: [ratan, mx-fxcash, ratan-razor-mx-fxcash-interface, ratan-fx-replication, ratan-fxu-utilization-integration, what-is-the-relationship-between-razor-mx-fxcash-and-fxu, what-is-the-authoritative-ratan-fxu-mx-fxcash-40630-interface-contract, 5-ratan--17-ratan-interfaces--28-ratan-and-fxumx-fxcash-40630--hwa4i8]
sources: ["RATAN/RATAN -Interfaces/Ratan and Razor (MX-FXCASH)-40630.md"]
---
# Ratan and Razor (MX-FXCASH)-40630

## Summary

This reviewed internal interface summary describes data feeds between [[ratan]] and Razor, identified in the document as `MX-FXCASH`. It provides country scope for eight feed categories and explicitly defines two directional flows:

- RATAN sends `BOOKED` FX Spot, Forward, and Swap trade and event messages to MX-FXCASH for FX replication.
- MX-FXCASH sends eligible-payment status updates to RATAN through the BCS settlement flow.

The source is an interface inventory and high-level flow summary, not a complete implementation contract. It does not define endpoints, authentication, payload schemas, delivery guarantees, retries, monitoring, support ownership, or reconciliation procedures.

## Governance

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| @Yunzhe Ta @Junying Jiang | 2026-02-02 | @Yunzhe Ta @Pengpeng Li @Jie Cai | 2026-03-25 | |

The source states that status should be changed to Published after review, but the recorded Status field is blank.

## Feed Inventory and Scope

| Data Feed | Countries in scope |
| --- | --- |
| Cashflows feed | London, Singapore, Hong Kong, Jersey , Egypt & China 30 Branches |
| Payment status messages | London, Singapore, Hong Kong, Jersey, Egypt & China 30 Branches |
| ACK/NACK | London, Singapore, Hong Kong, Jersey, Egypt & China 30 Branches |
| Cashflow Affirmation messages | London, Singapore, Hong Kong, Jersey, Egypt & China 30 Branches |
| Cashflow Failed status | London, Singapore, Hong Kong, Jersey, Egypt & China 30 Branches |
| Trade & Event messages | China 30 Branches & UK, HK, Taiwan, Germany, Malaysia, Singapore, Thailand, Philippines, India, Sri Lanka, Bangladesh |
| Utilization request | Egypt, Nepal, Saudi |
| Utilization response ACK/NACK | Egypt, Nepal, Saudi |

The introductory wording says RATAN “extracts/receives” data from Razor (MX-FXCASH). However, the documented end-to-end flows establish that direction must be assessed per feed rather than inferred from that statement.

## Explicit End-to-End Flows

### Trade STP / FX replication

`Ratan -> MX-FXCASH`

RATAN sends trade and event messages to MX-FXCASH as an FX-replication flow. The stated selection condition is a trade in `BOOKED` status.

- Products: FX Spot, Forward, Swap
- Message format: `SCBML V4.0`

This is evidence for the Razor/MX-FXCASH path of [[ratan-fx-replication]] only. It does not establish that all RATAN replication targets use the same status filter, products, or format.

### BCS settlement flow

`MX-FXCASH -> Ratan`

MX-FXCASH sends payment-status messages to RATAN for eligible payments.

- Statuses: `Released`, `Settled`, `Netted`, `Split`, `CCPNetted`
- Exclusions: `UTIL` trades; reversal and resultant payments for `SPLIT` and Netting events
- Message format: `SCBML V4.0`
- Size limit: `2M`

The source does not define eligible payments or the unit, scope, or enforcement point of the `2M` limit.

### FXU flow

The source refers readers to the RATAN–FXU documentation for utilization flows. It records utilization request and utilization-response ACK/NACK scope only for Egypt, Nepal, and Saudi; it does not provide protocol, direction, payload, or lifecycle details. See [[ratan-fxu-utilization-integration]].

## Referenced Specifications

- [RATAN - 51358](https://confluence.global.standardchartered.com/display/RZPSS/RATAN+-+51358)
- [FM Derivatives Replatforming RATAN - FMRP - Service Specs](https://confluence.global.standardchartered.com/display/FMEDMI/FM+Derivatives+Replatforming+RATAN+-+FMRP+-+Service+Specs)
- [RAZOR Cash Settlement Processing Guide](https://confluence.global.standardchartered.com/display/Razor/RAZOR+Cash+Settlement+Processing+Guide)
- [Requirements-12 entities FX replication](https://confluence.global.standardchartered.com/display/DSP/Requirements-12+entities+FX+replication)
- [RATAN and FXU](https://confluence.global.standardchartered.com/display/PSS/RATAN+and+FXU)
- [RATAN - OLA](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA)

## Limitations and Open Points

Connection details, interface team contact, known issues, and troubleshooting steps are blank. The source also leaves unspecified the direction and contracts for the cashflow, generic ACK/NACK, cashflow-affirmation, and cashflow-failed-status feeds.

The document title uses Razor (MX-FXCASH), whereas an existing related source is titled “Ratan and FXU (MX-FXCASH) 40630.” The relationship among Razor, MX-FXCASH, and [[fxu]] remains unresolved; see [[what-is-the-relationship-between-razor-mx-fxcash-and-fxu]].