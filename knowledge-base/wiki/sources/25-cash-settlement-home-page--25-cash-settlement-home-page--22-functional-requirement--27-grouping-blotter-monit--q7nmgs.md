---
type: source
title: Grouping Blotter Monitoring
authors: []
year: 2024
url: ""
venue: "Cash Settlement Home Page Functional Requirement"
tags: [cash-settlement, group-blotter, monitoring, operational-workflow]
related: [cash-settlement-home-page, group-blotter, grouped-cashflow-monitoring, group-pending-monitoring, group-pending-validation-monitoring, pending-trade-validation-investigation, murex-ratan-trade-id-synchronization-gap, manual-cashflow-push-from-group-blotter]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Grouping Blotter Monitoring.md"]
---
# Grouping Blotter Monitoring

## Summary

This functional-requirement document describes operational monitoring and investigation of grouped cashflows from the [[cash-settlement-home-page]]. It defines two dashboard indicators:

- **Group Pending**: expected cashflows have not been fully received.
- **Group Pending Validation**: cashflows are waiting for trade or market-event validation.

Selecting a non-zero dashboard count opens a filtered [[group-blotter]] tile for investigation.

The document describes intended operational behavior supported by UI screenshots and worked examples. It does not establish a formal API, status contract, service-level agreement, or measured production outcome.

## Group Pending monitoring

When the **Group Pending** count is not zero, the user selects the dashboard tag and opens the Group Blotter with `Status = PENDING`.

The investigation flow is:

1. Use the original trade ID to retrieve all underlying payments.
2. Inspect the `Pending Reason`.
3. Confirm the expected number of payments and identify any missing payment ID.
4. Check the missing payment in [[murex-2-11]].
5. Contact the Murex 2.11 PSS team if the payment was not delivered to [[ratan]].
6. Follow the applicable Murex 2.11 DOI to push the missing payment to RATAN.
7. Confirm that the pending exception clears after the missing payment is delivered.

The worked example uses payment IDs `108185597` and `108185598`. Both payments were generated from the same market event and were expected to be sent together. `108185597` reached RATAN, while `108185598` was not pushed from Murex. The received payment remained `PENDING` because the grouped payment set was incomplete.

This demonstrates [[grouped-cashflow-completeness]]: receipt of one payment does not make the group complete.

## Group Pending Validation monitoring

When the **Group Pending Validation** count is not zero, the user selects the dashboard tag and opens the Group Blotter with cashflows in `Pending Trade Validation`.

Payments with an imminent value date, such as the following day, should receive particular attention. The document does not define an exact priority cutoff or escalation SLA.

### Murex: matching trade ID, validation incomplete

If the trade ID in RATAN matches the trade ID in Murex but the trade has not been validated, Settlement Ops may approach MO to perform the validation. This may be particularly important when a client requests payment affirmation.

This is a validation-ownership issue rather than a trade-correlation mismatch.

### Murex: trade-ID divergence after a non-economic amendment

The document gives the following example:

- RATAN trade ID: `96502251`
- Murex amended trade ID: `96522715`

Murex performed a non-economic amendment, changing the trade ID from `96502251` to `96522715`. The new trade ID was validated, but it was not synchronized to RATAN. The source attributes this to a known Murex limitation.

Because the cashflow remains associated with the older RATAN trade ID, the user must manually push the cashflow from the Group Blotter to the [[cashflow-blotter-functional-scope|Cashflow Blotter]]. This is covered by [[murex-ratan-trade-id-synchronization-gap]] and [[manual-cashflow-push-from-group-blotter]].

The stated limitation should be corroborated against authoritative Murex-RATAN integration documentation before being treated as a general system invariant.

### Stella: trade not validated

For [[stella]], a cashflow may remain in `Pending Trade Validation`. The user checks the trade blotter using the same trade ID and major version. If the trade state is `TOBESENT`, the user should approach MO to validate the trade.

This path is specific to the Stella workflow and should not be generalized as Murex behavior.

## Monitoring objectives

The document positions the Group Blotter as an exception-oriented operational interface for monitoring:

- Cashflows not fully received.
- Cashflows expected in a subsequent feeding batch.
- Cashflows stuck in Murex workflow.
- Cashflows pending market-event or trade validation.
- Trade IDs that are not synchronized between Murex 2.11 and RATAN.

The dashboard-to-worklist navigation is:

```text
Cash Settlement Home Page dashboard
        ↓ select a non-zero group counter
Group Blotter
        ↓ apply the relevant status filter
Pending group records
```

## Evidence and limitations

The source includes screenshot references for dashboard counters, Group Blotter filters, payment details, Murex investigation, trade validation, and manual cashflow pushing. The screenshots themselves are not available in the extracted text, so exact UI labels, columns, and controls cannot be independently verified.

The document does not define:

- The grouping key for underlying payments.
- The complete derivation rules for `Group Pending` and `Group Pending Validation`.
- The complete pending-reason catalogue.
- The meaning of `major version`.
- The precise Murex DOI procedure.
- Ownership and escalation SLAs.
- Audit, approval, duplicate-prevention, or reversibility controls for manual pushes.
- The exact relationship between trade validation, market-event validation, and payment affirmation.
- The conditions for automatic exception closure.

## Referenced screenshot files

The source references these attachments:

- `image2024-8-14_14-31-40.png`
- `image2024-8-13_22-38-8.png`
- `image2024-8-13_22-40-8.png`
- `image2024-8-13_22-42-54.png`
- `image2024-8-13_22-56-54.png`
- `image2024-8-14_14-49-42.png`
- `image2024-8-14_15-8-2.png`
- `image2024-8-14_15-15-41.png`
- `image2024-8-14_15-43-56.png`
- `image2024-8-14_15-45-4.png`
- `image2024-8-14_15-46-50.png`
- `image2024-8-14_15-50-56.png`
- `image2024-8-14_15-52-22.png`
- `image2024-8-14_16-28-37.png`
- `image2024-8-14_16-27-45.png`