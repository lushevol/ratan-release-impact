---
type: source
title: Economic Amendment Fields
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page technical design"
tags: [cash-settlement, economic-amendment, cashflow-blotter, booking-system-event, FMRP-8.0]
related: [cashflow-economic-and-non-economic-amendment-classification, booking-system-event-during-group-message-movement, what-is-the-authoritative-economic-amendment-classification-rule, cashflow-blotter, grouping-blotter, cash-settlement-platform]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Economic Amendment Fields.md"]
---
# Economic Amendment Fields

## Scope

This technical design note defines how the Cash Settlement application classifies economic and non-economic amendments in the Cashflow Blotter and assigns the corresponding `bookingSystemEvent`. The design applies to group-message processing and paired withdrawal/new cashflows.

The primary referenced work item is [Story 12659039 [FMRP 8.0] G10 & FXO New Eco Fields](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/12659039/?view=edit). The note also references [RFI Nostro stamping based on Portfolio](https://confluence.global.standardchartered.com/display/DSP/RFI+Nostro+stamping+based+on+Portfolio).

## Amendment classification examples

| Trade Id | Cashflow Id | Business Event | Amount (economic field change) | Swap Agent Id (key field change) | CF blotter Status | Expected Booking System Event | Case Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T01 | C01 | Withdrawal | 100 USD |  | New Waiting, no manual touch | `NonEcoAmend_Replace` | Non-economic amendment; not manually touched and not released |
| T01 | C02 | Withdrawal | 200 CNY |  | Released | `NonEcoAmend` | Non-economic amendment; post-release; key fields unchanged |
| T01 | C03 | Withdrawal | 300 JPY |  | Waiting | `Amendment` | Economic amendment |
| T01 | C04 | New | 100 USD |  | NA | `NonEcoAmend_Replace` | Paired with C01; non-economic amendment; not manually touched and not released |
| T01 | C05 | New | 200 CNY |  | NA | `NonEcoAmend` | Paired with C02; non-economic amendment; manually touched; key fields unchanged |
| T01 | C06 | New | 400 JPY |  | NA | `Amendment` | Paired with C03; economic amendment |
| T01 | C07 | Withdrawal | 500 EUR | MTM/Coupon | New Waiting, user manual touch | `NonEcoAmend_Replace` | Non-economic amendment with manual touch and key-field change |
| T01 | C08 | New | 500 EUR | Coupon | NA | `NonEcoAmend_Replace` | Paired with C07; non-economic amendment with key-field change |

The source includes the note: “manual touched check not required if 3 matched.” The meaning of “3 matched” is not defined.

## Refixing edge case

| Trade Event | Trade Id | Lien Monitoring | Major Version | Count | Batch ID | Cashflow ID | Business Event | Composite match fields |
| --- | --- | --- | ---: | ---: | --- | --- | --- | --- |
| Booking | T01 | Yes | 1 | 1 | b01 | C01 | N | `ccy+direction+vd+fmid+cptyid+amt+method = ABC` |
| Fixing | T01 | Yes | 1 | 1 | b02 | C02 | N | `ABC` |
| Refixing | T01 | Yes | 1 | 2 | b03 | C02 | W | `ABC` |
| Refixing | T01 | Yes | 1 | 2 | b03 | C03 | N | `ABC` |

The fixing-stage Cashflow Blotter status is:

```text
Waiting + Pending Exception + Submitted
```

The pre-development note states that C02 and C03 will be tagged as `NonEcoAmend`. A later annotation gives the following intended behavior:

1. When `majorVersion = 1`, check the cashflow only and classify it as `Amendment` because an economic field changed during refixing.
2. If `majorVersion > 1` and `preGroup` does not exist, classify it as `Amendment`.

The source does not establish whether the later annotation is approved or implemented.

## Implementation requirement

The code-level requirement is:

```text
Set bookingSystemEvent while moving groupMessages from sourceMsgs to targetMsgs
```

The classification should therefore be applied at the source-to-target group-message movement boundary. Paired cashflows should receive consistent event semantics, and retry or partial-move handling must not leave inconsistent `bookingSystemEvent` values.

## BAU routing note

The source adds the following BAU note:

```text
add dedicatedChange, if dedicatedChange will drive into nopair first
```

The interaction between `dedicatedChange`, `nopair` routing, pairing, and `bookingSystemEvent` is not specified.

## Open questions

- What are the complete names and definitions of the new G10 and FXO economic fields?
- What are the “3 matched” conditions that remove the manual-touch check?
- Does a key-field change always force `NonEcoAmend_Replace`?
- What is the precedence among economic change, key-field change, manual touch, release state, and trade-event type?
- Is the later refixing rule authoritative over the pre-development `NonEcoAmend` behavior?
- Does `dedicatedChange` affect only pairing, or also `bookingSystemEvent`?
- Is classification calculated independently for paired cashflows or inherited across the pair?
- What happens when movement from `sourceMsgs` to `targetMsgs` partially succeeds?
- Are `bookingSystemEvent` values persisted, emitted downstream, or both?

This source extends the behavior documented for the [[cashflow-blotter]] and [[grouping-blotter]] within the [[cash-settlement-platform]]. The unresolved classification questions are tracked in [[what-is-the-authoritative-economic-amendment-classification-rule]].
