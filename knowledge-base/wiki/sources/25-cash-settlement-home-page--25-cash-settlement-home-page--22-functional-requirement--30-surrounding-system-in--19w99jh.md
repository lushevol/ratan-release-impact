---
type: source
title: Ratan and Stella Cashflow Integration
authors: []
year: 2022
url: ""
venue: "Cash Settlement Home Page functional requirement"
tags: [cashflow, Stella, Ratan, FMRP, post-trade, integration]
related: [stella, ratan, fmrp, fmrp-stella, fmrp-cashflow-responsibility-split, cashflow-lifecycle-state-model, cashflow-business-and-message-versioning, payment-date-versus-value-date, cashflow-netting-and-auto-un-netting, released-settled-amendment-control, cashflow-version-concurrency-control, nstp-rule-routing]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Ratan & Stella cashflow integration.md"]
---

# Ratan and Stella Cashflow Integration

## Summary

This functional and design requirement proposes a target FMRP integration in which [[entities/stella]] generates cashflows from trade business events while [[entities/ratan]] owns post-trade materialization, lifecycle processing, netting, payment processing, and settlement-status propagation.

The proposal was developed in the context of China entity onboarding and Murex decommissioning. It is an architecture proposal and scenario walkthrough rather than evidence of an approved implementation, production behavior, or formal acceptance test.

## Target responsibility split

Stella is proposed to:

- Generate `New`, `Amendment`, and `Cancellation` cashflow events from trade business events.
- Generate a new `Business Version` when the trade-processing system changes the cashflow.
- Default generated cashflows to `Projected`.
- Generate both theoretical and known cashflows and send them to Ratan.
- Replicate post-trade `Released` and `Settled` status updates for downstream visibility and amendment controls.

Ratan is proposed to:

- Materialize persisted projected cashflows.
- Move cashflows through post-trade lifecycle states.
- Apply NSTP processing and FMO maker/checker controls.
- Generate netting resultant cashflows.
- Perform auto un-netting after relevant amendments.
- Maintain `Payment Date` independently from Stella’s `Value Date`.
- Send generated Swift messages to FMSRE and process Razor settlement responses.

## Proposed lifecycle

The principal lifecycle described by the source is:

```text
Projected → Queued → Pending → Validated → Released → Settled
```

The stated ownership and triggers are:

```text
Projected → Queued : Ratan moves the cashflow status to 'Queued' on VD-5.
Queued → Pending : 'Pending' is used for NSTP criteria such as NSTP Review/CPN/SSI Exception.
Pending → Validated : Cashflow moves to 'Validated' after FMO resolves the NSTP criteria.
Validated → Released : Swift message is generated and sent to FMSRE.
Released → Settled : Swift message has been sent to the Swift network.
```

The source also lists additional Stella status-moving actions:

```text
1. Projected → Released
2. Projected → Netted
3. Netted → Projected
4. Netted → Released
5. Netted → Settled
```

The relationship between these direct transitions and the principal lifecycle is unresolved. They may represent exceptional, replicated, or asynchronous states rather than an alternative formal state machine.

## Version model

| Field | Managed by | Starting value | Increment rule | Reset rule |
|---|---|---:|---|---|
| Business Version | FMRP Stella | 0 | Increases from amendment/withdrawal events | Not specified |
| Cashflow Version | FMRP Stella | 0 | Increases when a new cashflow message is generated, such as a status update | Not specified |
| Ratan Minor Version | Ratan | 0 | Increases for Ratan internal activities, workflow, and FMO GUI actions | Reset to 0 when a new business version is populated by Stella |

The stated duplicate-filtering key is:

```text
Cashflow Id
Business Version
Status_Update Event
```

The first scenario uses `Payment Version` where later scenarios use `Ratan Minor Version`. The source does not establish whether these are aliases or separate fields.

## Representative new-trade processing

| Event | Action By | Cashflow Status | Sub Status Type | Sub Status | Business Version | Cashflow Version | Payment Version |
|---|---|---|---|---|---:|---:|---:|
| Payment persistence | Stella | Projected |  |  | 0 | 0 | 0 |
| Materialization | Ratan | Queued |  |  | 0 | 0 | 1 |
| NSTP | Ratan | Pending | NSTP Release | Pending Operator | 0 | 0 | 2 |
| NSTP | Ratan | Pending | NSTP Release | Pending Verification | 0 | 0 | 3 |
| Validation | Ratan | Validated |  |  | 0 | 0 | 4 |
| Razor return Released status | Ratan | Released |  |  | 0 | 0 | 5 |
| Razor return Settled status | Ratan | Settled |  |  | 0 | 0 | 6 |

For the final two rows, Ratan consumes Razor status messages and updates the cashflow status. Stella separately receives `Released` and `Settled` status updates. The source states that a separate process should guarantee successful status propagation to Stella, with an exception ticket generated when a technical or functional failure occurs.

## Netting

Ratan identifies component cashflows, assigns them a `Netting ID`, changes their status to `Netted`, and creates a resultant cashflow. The resultant proceeds independently through NSTP, validation, Swift generation, and settlement.

| Event | Cashflow ID | Amount | Source System | Cashflow Status | Netting ID | Update to Stella | Business Version | Cashflow Version | Ratan Minor Version |
|---|---|---:|---|---|---|---|---:|---:|---:|
| Netting(Component) | C101 | 100 | Stella | Netted | N001 | Y | 0 | 0 | 3 |
| Netting(Component) | C102 | 200 | Stella | Netted | N001 | Y | 0 | 0 | 3 |
| Netting(Resultant) | C103 | 300 | Ratan | Queued | N001 | N | 0 | 0 | 0 |
| NSTP(Netting Resultant) | C103 | 300 | Ratan | Pending | N001 | N | 0 | 0 | 1 |
| Validation(Netting Resultant) | C103 | 300 | Ratan | Validated | N001 | N | 0 | 0 | 2 |
| Swift Generation(Netting Resultant) | C103 | 300 | Ratan | Released | N001 | N | 0 | 0 | 3 |
| Settle(Netting Resultant) | C103 | 300 | Ratan | Settled | N001 | N | 0 | 0 | 4 |
| Component Cashflow update | C101 | 100 | Stella | Released | N001 | Y | 0 | 1 | 4 |
| Component Cashflow update | C102 | 200 | Stella | Released | N001 | Y | 0 | 1 | 4 |
| Component Cashflow update | C101 | 100 | Stella | Settled | N001 | Y | 0 | 2 | 5 |
| Component Cashflow update | C102 | 200 | Stella | Settled | N001 | Y | 0 | 2 | 5 |

The design introduces auto un-netting when an amendment affects a netted cashflow. It does not fully specify atomicity, locking, retry behavior, or the authoritative status relationship between component and resultant cashflows.

## Withdrawal and New

For an amendment after `Released` or `Settled`:

- FO amendment is blocked.
- MO may amend the trade.
- Stella emits a `Withdrawal` event for the original cashflow and a new cashflow event for the amended amount.
- Ratan must process the withdrawal before the new event.
- The original payment may require reversal messages such as `MT292/MT192`.
- The replacement payment may use `MT202/MT103`.

The source explicitly states:

```text
There's system control the Withdrawal event(C101) must be proceeded prior to the new event(C102)
```

Identifiers vary across examples, including `C101`, `C102`, `P102`, and `P103`; these should not be treated as a canonical identifier contract.

## Value Date and Payment Date

The proposed design preserves Stella’s original `Value Date` and adds a post-trade-managed `Payment Date`.

| Event | Cashflow Status | Value Date | Payment(Settlement) Date | Update to Stella |
|---|---|---|---|---|
| Cashflow Persistence | Projected | 9/30/2022 |  | N |
| Materialization | Queued | 9/30/2022 |  | N |
| NSTP | Pending | 9/30/2022 |  | N |
| Failed Process | Failed | 9/30/2022 |  | N |
| Payment Date update from Ratan GUI | Queued | 9/30/2022 | 10/3/2022 | N |
| NSTP | Pending | 9/30/2022 | 10/3/2022 | N |
| Validation | Validated | 9/30/2022 | 10/3/2022 | N |
| Swift Generation | Released | 9/30/2022 | 10/3/2022 | Y |
| Settle | Settled | 9/30/2022 | 10/3/2022 | Y |

`Payment Date` is intended to drive Swift message generation with the updated settlement date. The source does not define its type, timezone, nullability, audit requirements, edit permissions, or behavior after release.

## Concurrency and exception cases

The source describes two stale-update scenarios:

1. Stella amends a cashflow while Ratan is releasing it. Ratan’s status update can fail because Stella has advanced the version. The proposed correction sends the original and amendment to Razor, where C&R produces reversal and replacement Swift messages.
2. Stella amends a cashflow while Ratan is netting it. Ratan may read current versions, but submission is rejected after Stella increments the cashflow version. The source asks whether netting can be transactional and automatically reversed but does not resolve the design.

These cases motivate optimistic concurrency, version-aware deduplication, and explicit recovery semantics.

## Open design questions

- Which system is authoritative for each lifecycle status?
- Are `Payment Version` and `Ratan Minor Version` the same field?
- What is the formal state machine for `Failed`, `Netted`, `Suppressed`, and reversal states?
- What is the canonical cashflow identifier lineage for withdrawal/new and resultant flows?
- Are netting and un-netting atomic across component and resultant cashflows?
- What protocol rejects stale Ratan actions and defines retries?
- Does `Payment Date` drive all relevant Swift settlement-date fields?
- What does `Update to Stella` mean: replication, acknowledgement, or settlement notification?
- How are failed status propagations ticketed and reconciled?
- Can FO and MO permissions be enforced at every amendment entry point?
