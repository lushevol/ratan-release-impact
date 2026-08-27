---
type: concept
title: Cashflow Economic and Non-Economic Amendment Classification
tags: [cash-settlement, cashflow, amendment, economic-fields, non-economic-amendment]
related: [booking-system-event-during-group-message-movement, cashflow-blotter, grouping-blotter, what-is-the-authoritative-economic-amendment-classification-rule]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Economic Amendment Fields.md"]
---
# Cashflow Economic and Non-Economic Amendment Classification

## Definition

Cashflow amendment classification determines the `bookingSystemEvent` assigned when a trade or group message is amended. The classification distinguishes economic changes from non-economic changes and further separates standard non-economic amendments from amendments requiring replacement behavior.

The source examples use three event values:

- `Amendment` — an economic field changed.
- `NonEcoAmend` — a non-economic amendment where release or manual-touch conditions are satisfied and key fields are unchanged.
- `NonEcoAmend_Replace` — a non-economic amendment requiring replacement behavior, including unreleased or untouched cashflows and examples with key-field changes.

## Classification signals

The design considers:

1. Whether an economic field changed.
2. Whether a key field changed, with `Swap Agent Id` as the example.
3. Whether the cashflow was manually touched.
4. Whether the cashflow was released.
5. Trade-event context such as refixing.
6. `majorVersion` and the presence or absence of `preGroup` in the refixing edge case.

The examples indicate that economic changes map to `Amendment`. They also indicate that a key-field change can result in `NonEcoAmend_Replace` even when the cashflow was manually touched. This suggests that key-field changes may take precedence over manual-touch status, but the source does not provide a formal precedence algorithm.

## Paired cashflows

Withdrawal and new cashflows are shown as pairs:

- C01 and C04: `NonEcoAmend_Replace`
- C02 and C05: `NonEcoAmend`
- C03 and C06: `Amendment`
- C07 and C08: `NonEcoAmend_Replace`

The design does not state whether each cashflow is classified independently or whether the event is computed once and inherited by the paired cashflow.

## Refixing behavior

The source contains conflicting refixing guidance. An earlier note classifies C02 and C03 as `NonEcoAmend`, while a later annotation classifies them as `Amendment` when an economic field changes during refixing under the stated major-version conditions:

- `majorVersion = 1`: classify as `Amendment` when the economic field changed during refixing.
- `majorVersion > 1` and no `preGroup`: classify as `Amendment`.

The authoritative rule remains unresolved and is tracked in [[what-is-the-authoritative-economic-amendment-classification-rule]].

## Relationship to processing

Classification is not only a display decision in the [[cashflow-blotter]]. The event must be assigned while group messages move between `sourceMsgs` and `targetMsgs`, as described in [[booking-system-event-during-group-message-movement]]. The implementation must preserve consistent classification across paired messages and retry paths.
