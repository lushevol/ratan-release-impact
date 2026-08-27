---
type: concept
title: Booking System Event During Group-Message Movement
tags: [cash-settlement, group-message, booking-system-event, message-movement, regrouping]
related: [cashflow-economic-and-non-economic-amendment-classification, cashflow-blotter, grouping-blotter, static-data-synchronization, request-id-based-sync-correlation, per-destination-sync-status-tracking]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Economic Amendment Fields.md"]
---
# Booking System Event During Group-Message Movement

## Definition

The Cash Settlement design requires `bookingSystemEvent` to be set while moving group messages from `sourceMsgs` to `targetMsgs`. This makes event assignment part of the regrouping operation rather than a separate presentation-only transformation in the [[cashflow-blotter]].

## Processing boundary

The relevant operation is:

```text
sourceMsgs -> targetMsgs
```

At this boundary, the implementation should:

1. Determine whether the amendment is economic, non-economic, or a key-field change.
2. Apply the corresponding `bookingSystemEvent`.
3. Move the group message to the target collection.
4. Preserve the event value through downstream processing and retries.

The source identifies the event outcomes as:

```text
Amendment
NonEcoAmend
NonEcoAmend_Replace
```

## Consistency requirements

Paired withdrawal and new cashflows should have consistent event semantics. The movement operation should also define behavior for:

- Partial movement success.
- Retries and duplicate processing.
- Source and target messages being processed by different attempts.
- Persistence or downstream emission of `bookingSystemEvent`.
- Correlation of the movement with group and cashflow identifiers.

These concerns may intersect with [[static-data-synchronization]], [[request-id-based-sync-correlation]], and [[per-destination-sync-status-tracking]], although the source does not define a complete synchronization or retry protocol.

## Related routing rule

The BAU note introduces `dedicatedChange` and states that it may drive processing into `nopair` first. The design does not clarify whether `nopair` changes only pairing behavior or also overrides the assigned `bookingSystemEvent`.
