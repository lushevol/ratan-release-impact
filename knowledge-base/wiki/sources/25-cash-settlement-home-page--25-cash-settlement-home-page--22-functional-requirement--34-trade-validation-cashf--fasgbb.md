---
type: source
title: RATAN Settlement Control on Trade Validation
authors: []
year: 2024
url: ""
venue: "Functional Requirement"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, trade-validation, RATAN, Murex-2-11, Stella, cashflow-blotter]
related: [ratan, stella, murex-211, mo, trade-validation-cashflow-gating, ratan-group-blotter-event-completeness, manual-cashflow-blotter-push-exception, does-manual-ratan-blotter-push-bypass-trade-validation, what-is-the-authoritative-trade-validation-status-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/RATAN Settlement Control on Trade Validation.md"]
---
# RATAN Settlement Control on Trade Validation

## Summary

This functional requirement describes trade-validation controls for cashflow ingestion into the RATAN cashflow blotter. Current CN flows from Stella and Murex 2.11 send cashflows without checking trade validation. From 10 August, the proposed interim control requires cashflows for SG, MY, and IN to enter the RATAN blotter only after trade validation; CN remains on the current BAU process. A September 2024 Stella/CDU auto-validation enhancement for SCF and LoanDepo is marked TBC.

Manual intervention remains necessary when validation is unavailable on value date or when cashflows are delayed, cancelled before feeding, or held while a related event is missing. The requirement states that this manual process remains until trade migration is complete.

## Validation workflow

| Timeline | MO Workflow | Settlements Workflow | Mitigation Control | Settlement Manual Action with Trade Validation |
| --- | --- | --- | --- | --- |
| Current CN Flow - STELLA | MO validates Stella CN trades in RATAN | Cashflow push to cashflow blotter without validation check | Payments will not STP since the trade is not matched; the Settlements team performs cashflow affirmation with the counterparty before releasing the payment | No |
| Current CN Flow - MX2.11 | MO validates trades in Murex 2.11 | Cashflow push to cashflow blotter without validation check | Payments will not STP since the trade is not matched; the Settlements team performs cashflow affirmation with the counterparty before releasing the payment | No |
| Flow 29th July to 10th Aug (SG/MY/IN/CN) | No changes to process | All entities follow current CN BAU | Same as current CN BAU | No |
| From 10th Aug | No changes to process | Cashflows flow to the RATAN cashflow blotter only after validation for SG/MY/IN; CN cashflows follow current BAU | — | Monitor cashflows for trades not validated and manually push them to the cashflow blotter when trade validation is unavailable on value date |
| Sep 2024 (TBC) | Stella/CDU enhancement: auto-validation for SCF and LoanDepo | Cashflows flow to the RATAN cashflow blotter only after validation | — | Intended reduction in manual touch for Stella cashflows |
| Until Trade Migration | — | — | — | Manual action is required to push cashflows for exception cases when the trade is not validated |

## Group blotter functionality

The production group blotter is explicitly described as independent of Trade Validation Status. Its stated purposes are:

- Ensure that all cashflows belonging to a market event are received, including reversal and rebook events, CCS interest pay/receive flows, CCS initial notional payments, and initial notional plus first-period interest payments.
- Compare withdrawals and new cashflows after the full group arrives to identify non-economic amendments.
- Reduce operations effort for reversal and rebook handling.

This establishes separate control dimensions for trade validation and event-group completeness.

## Manual grouping-blotter scenarios

### Cashflow stuck in the Murex workflow

The requirement reports 46 cashflows over the preceding four months in which a cashflow was expected to reach RATAN but remained stuck in the Murex workflow or left a group waiting for a related event.

| Trade Event | Payment ID | Reversal & Rebook | Value Date | Date Sent to RATAN | RATAN Status | Manual Monitoring & Push Action |
| --- | ---: | --- | --- | --- | --- | --- |
| New Booking | 103916452 | — | 2024-06-25 | 2024-06-17 | NSTP | — |
| C&R | 106649728 | Reversal of 103916452 | 2024-06-25 | 2024-06-24 | Pending in blotter waiting for 106649729 | Manually push to Cashflow Blotter |
| Rebook | 106649729 | Rebook of 103916452 | 2024-06-25 | 2024-06-25 | — | — |

### Cashflow cancelled before feeding to RATAN

| Trade Event | Payment ID | Murex Payment Status | Reversal & Rebook | Value Date | Date Sent to RATAN | RATAN Status | Manual Monitoring & Push Action |
| --- | ---: | --- | --- | --- | --- | --- | --- |
| New Booking | 106267096 | INIT | — | 2024-06-13 | NA | NA | — |
| — | 106267099 | SNTR | — | 2024-06-13 | 2024-06-13 | Pending in blotter waiting for 106267096 | Manually push to Cashflow Blotter |
| C&R | 106267096 | CNCL | — | 2024-06-13 | NA | — | — |

### Non-economic amendments

The requirement reports 200 Murex 2.11 non-economic amendments for H1 entities SG/MY/IN/CN over three months and 2,000 for all entities over three months. The source example is structurally malformed, so the relationships between all trade, payment, and cashflow identifiers cannot be treated as authoritative.

The reliable elements of the example are:

- New booking trade `92060188` has Murex status `CHCK`.
- RATAN shows cashflow `M00101912951`, associated with payment `101912951`, as a new cashflow pending validation and expecting trade `92060188`.
- The cashflow is marked `NSTP`.
- Related non-economic C&R, status update, validation, and confirmation events include trade `92060252` with statuses `CHCK`, `VALD`, and `COMP`.

## Evidence and limitations

The document contains no named author, document date, version, approval status, implementation reference, or canonical status dictionary. The reported volumes are useful operational indicators but lack extraction and reconciliation definitions. The September auto-validation enhancement is explicitly tentative. The requirement does not define the accepted validation statuses, trade-to-cashflow matching key, manual-push authorization, audit trail, monitoring SLA, or migration exit criteria.

## Related wiki pages

The distinction between validation gating and group completeness is developed in [[concepts/trade-validation-cashflow-gating]] and [[concepts/ratan-group-blotter-event-completeness]]. The exception process is documented in [[concepts/manual-cashflow-blotter-push-exception]]. Open status and override questions are tracked in [[queries/does-manual-ratan-blotter-push-bypass-trade-validation]] and [[queries/what-is-the-authoritative-trade-validation-status-model]].