---
type: concept
title: Inter-Entity Netting
tags: ["inter-entity-netting", "auto-netting", "legal-entity", "cash-settlement", "settlement-day-2", "UAT", "cashflow-matching"]
related: ["auto-netting", "cash-settlement", "financial-field-classification", "pending-auto-netting-state", "netting-resultant-cashflow", "netting-eligibility-rules", "auto-netting-datetime-calculation", "netting-un-net-lifecycle", "netting-resultant-cashflow-lifecycle", "released-resultant-amendment-handling", "irs-resultant-cashflow-netting", "nostro-static-validation", "clearing-resultant-swift-suppression", "settlement-suppression-exceptions", "ratan", "lms", "irs", "fmo-post-trade-portal", "direction-dependent-prematch-key", "auto-netting-rule-check", "settlement-day-2", "ratan-cash-settlement-netting-service", "is-inter-entity-netting-resultant-counterparty-selection-deterministic"]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting/Inter Entity Netting - UAT.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting/Inter Entity Netting Design.md"]
---

# Inter-Entity Netting

Inter-entity netting concerns the matching of eligible cashflows across different legal or booking entities. The UAT evidence describes eligible cashflows being automatically combined into settlement resultants through the fmo post trade portal and [[ratan]].

The design source describes the matching model more specifically as matching reciprocal cashflows between two entities. A `Pay` cashflow from one entity is matched with a corresponding `Receive` cashflow from the counterparty when their direction-dependent composite keys resolve to the same value.

## Design matching model

The design demonstrates three core matching conditions:

- The entity and counterparty positions are reversed between reciprocal `Pay` and `Receive` cashflows.
- The amount must match exactly.
- Matching is performed against a composite `PreMatchKey`.

For example, cashflow 1, in which `400906330` pays `7` an amount of `100`, matches cashflow 4, in which `7` receives from `400906330` an amount of `100`.

The design also shows that duplicate keys do not automatically cause every cashflow to match. Cashflows 5 and 6 share `7-400906330-200`, but only cashflow 5 is marked as matched. The source does not define the ordering or tie-breaker used to determine which duplicate is selected.

The design does not establish the authoritative rules for:

- Duplicate-key selection.
- One-to-one versus aggregate matching.
- Amount normalization.
- Currency eligibility.
- Value-date eligibility.
- Downstream processing after matching.

These questions should be tracked with is inter entity netting resultant counterparty selection deterministic.

## Processing scope and participating services

The design identifies ratan cash settlement netting service and three other services as participating in the feature. It identifies Cashflow Enrichment as the stage that sets the USD transferred amount before the [[auto-netting-rule-check]] performed by the Auto Netting Job.

The design source does not establish whether a match:

- Creates a [[netting-resultant-cashflow]].
- Suppresses the source cashflows.
- Changes lifecycle status.
- Qualifies records for a later processing stage.

The UAT provides evidence for these downstream behaviors in its tested scenarios, but does not establish that the design description resolves all of the open matching questions.

## Scope and status evidence

The 2024 changes source contains separate evidence about scope and an upstream indicator:

- The Nepal/Saudi/Egypt scope lists **Inter Entity Netting** under **Netting**, with a dependency on Murex 2.11 logic, but leaves the item unchecked.
- SCI separately lists an **Inter Entity** indicator as `Not Required` and `CLOSED`.

These entries may describe different concerns: the inter-entity netting capability itself and an upstream indicator field. The source does not establish whether the capability was implemented, deferred, or excluded.

The UAT provides tested behavior for the scenarios below. It does not confirm the complete Day 1 entity scope, so the tested observations should not be treated as a complete authoritative policy.

## UAT eligibility evidence

The UAT demonstrates the following tested exclusions and requirements:

- Non-USD cashflows are not eligible.
- USD cashflows above USD 100,000 are not eligible.
- Cashflows belonging to an out-of-scope entity are not eligible.
- An eligible cashflow must have an eligible counterpart before a netting resultant can be created.

## UAT matching modes

Successful matching was demonstrated through:

1. Exact FMID matching.
2. Backend static mapping where FMIDs were not exact.
3. BIC-based rule conditions after the inter-entity rule was updated.

The exact precedence between these mechanisms remains unresolved.

## UAT processing lifecycle

A matching component cashflow first enters `Pending auto netting`. This is an intermediate state, not a guarantee that netting will occur. Depending on the available counterpart and operational events, a pending cashflow can:

- Become `NETTED` and contribute to a new netting resultant.
- Be sent as gross when no eligible counterpart is available.
- Be cancelled after a withdrawal.
- Return to processing after an un-net or amendment.
- Be sent as gross after the rule is disabled.

A cashflow received after the configured netting date/time may be processed in a later cycle. The UAT expected subsequent processing every 30 minutes and observed separate resultants for separate batches after retest.

## Gross fallback

According to the UAT, gross settlement is the fallback when the opposite-side cashflow is:

- Not received in RATAN.
- Suppressed by a cashflow suppression rule.
- Suppressed by a SWIFT suppression rule.
- Otherwise unavailable for matching.

The observed sequence is that the available side enters `Pending auto netting`, remains unmatched, and is ultimately sent as gross.

## Netting versus payment release

Netting eligibility and resultant release are separate controls. In one UAT test, matching and netting succeeded but the net parent could not initially be released because the required [[nostro-static-validation]] was missing. Updating the nostro static allowed the test to pass.

## Withdrawal and amendment behavior

The UAT lifecycle depends on payment release:

- **Pending before netting:** A withdrawal directly cancels the cashflow.
- **Netted but not released:** A withdrawal or amendment can un-net the existing resultants, cancel or exclude the affected component, and trigger replacement processing or new resultants.
- **One side released:** Existing resultants remain unchanged; the affected component can remain in a waiting state.
- **Both sides released:** Existing released resultants remain unchanged.

This is a “rebuild before release, preserve after release” behavior. Further detail is captured in [[netting-un-net-lifecycle]] and [[released-resultant-amendment-handling]].

## Rule disablement and rollback

Disabling the inter-entity netting rule provides a rollback path for pending flows. Pending cashflows are sent as gross after the rule is disabled. Cashflows already netted and their generated resultants are isolated from the later configuration change and remain unaffected.

This distinction should be preserved in operational rollback procedures.

## IRS interaction

The UAT also tested [[irs]] cashflows. IRS aggregation resultants `N00000148696` through `N00000148699` were moved to `DEAD`, and their component cashflows were re-netted into `N00000148700` and `N00000148701`.

This confirms the observed interaction but does not establish the complete precedence model between IRS aggregation and inter-entity netting.

## Operational exceptions

Manual un-netting of one side was tested and passed, including cases where a withdrawal had already been received. These scenarios are explicitly described as not expected in BAU. They document recovery and exception behavior rather than the canonical automatic lifecycle.

## Evidence limitations

The UAT contains an obsolete Scenario 13 that is both marked passed and declared invalid after a withdrawal-event-handling change. It should not be used as evidence for current behavior.

Initial failures in Scenarios 6, 10, and 11 were attributed to temporary environment issues and passed after retest. LMS confirmations are incomplete across the scenario set.