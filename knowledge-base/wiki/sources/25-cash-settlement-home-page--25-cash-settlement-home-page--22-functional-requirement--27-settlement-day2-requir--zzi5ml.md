---
type: source
title: High Value Payment Control - RATAN
created: 2026-08-23
updated: 2026-08-23
tags: [functional-requirement, settlement-day-2, high-value-payment, ratan, fmsgw]
related: [ratan, fmsgw, bcs, fmrp, loaniq, ratan-high-value-payment-control, stp-nstp-and-last-user-message-contract, what-is-the-final-stpflag-and-lastuser-contract-between-ratan-and-fmsgw, what-is-the-final-fmrp-cashflow-affirmation-authorization-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/High Value Payment Control - RATAN.md"]
authors: []
year: 2026
url: ""
venue: Internal functional requirement
---
# High Value Payment Control - RATAN

This functional requirement defines proposed RATAN enhancements that provide FMSGW with value-routing and approval-relevant information. It covers BCS, FMRP, and LOANIQ cashflows. The documented scope includes BCS, LOANIQ, and FMRP; the Korea ENSIS flow is excluded.

The requirement is a design and scope artifact. It does not provide implementation evidence, final FMSGW payment thresholds, or production approval evidence.

## Core control model

FMSGW is expected to distribute payment messages into queues according to payment-amount thresholds, with different approval levels for each queue. RATAN is expected to supply additional data supporting that process.

For FMRP/LOANIQ, RATAN must:

- Display each cashflow's USD equivalent in the Cashflow Blotter.
- Support USD-equivalent filtering both through an additional custom-filter condition and directly in the blotter.
- Send STP/NSTP information and user attribution to FMSGW.
- Apply the specified RATAN profile authorization limits.
- Update affected production user profiles as part of the release after PO confirmation.

The proposed routing and authorization design is documented in [[ratan-high-value-payment-control]].

## BCS and FMRP/LOANIQ scope distinction

| Requirement | FMRP Solution | BCS Solution | Comments |
| --- | --- | --- | --- |
| Display 'High Value' exception in Cashflow detail | Already in BAU | Will not be built | |
| View 'USD' equivalent in the Cashflow Blotter | New field will be added in the cashflow blotter, but solution should not rely on users creating custom filters | Will not be build | |
| Ability to view filter options based on different cashflow thresholds | New field will be added in the cashflow blotter | Will not be built | |
| Apply Authorization Limits for Checker Actions | Already in BAU | 1. Authorize limit build will leverage FMRP existing static – static blotter & limit 1. NSTP Checker Approval ![image-2026-8-11_10-5-52.png](attachments/image-2026-8-11_10-5-52.png) 2. Cashflow Affirmation - add auth limit check for single level "update affirmation statuus" for the initial release (scheduled in Sep) - - need to check if can change this to maker/checker process, raise another ADO to track. ![image-2026-8-11_10-1-53.png](attachments/image-2026-8-11_10-1-53.png) 3. Failed Cashflow Release - 1. ~~remove release failed cashflow option (OPS is using this in BAU)~~ 2. add the profile limt for checker approval ![image-2026-8-11_10-1-11.png](attachments/image-2026-8-11_10-1-11.png) | |
| Send STP/NSTP Flag to FMSGW | STP/NSTP flag – taken as NSTP as long as cashflow has user manual touch | Same as FMRP | - pending @Arockia Dinesh @Deepak K to confirm on exact actions vs values |
| Send Last Checker FMID to FMSGW | - Send last Checker PSID for all actions where there is maker+checker. - Send Maker PSID for all actions where there is single level (example: Affirmation) | Same as FMRP | |

The USD-equivalent display and filtering features must not be generalized from FMRP/LOANIQ to [[bcs]], where the source explicitly excludes them.

## Proposed FMRP/LOANIQ message fields

The proposed Swift-header interface is described in [[stp-nstp-and-last-user-message-contract]]:

- `stpFlag`: `Y` for STP and `N` for NSTP.
- An NSTP cashflow is proposed to mean an exception closed by a user; other flows are STP.
- Failed/reinstated actions and comments are proposed to be excluded from NSTP determination.
- `lastUser`: user bank ID, blank when `stpFlag` is `Y`.
- For maker/checker actions, RATAN sends the last checker PSID; for a single-level action, it sends the last maker PSID.
- An automatically distributed or split child cashflow derives STP/NSTP status from its parent.

The source simultaneously records these field definitions as pending confirmation. In particular, it does not establish that a user bank ID and PSID are the same identifier. See [[what-is-the-final-stpflag-and-lastuser-contract-between-ratan-and-fmsgw]].

## RATAN profile limits

| **Profile** | **Current Limit** | **TOBE Limit (USD)** | **Remarks** |
| --- | --- | --- | --- |
| FMO_OPS_BOC | < 30 Million | <30 Million | |
| FMO_OPS_BO | < 100 Million | < 100 Million | |
| FMO_OPS_BOS | < 300 Million | < 500 Million | Change to 500 Million |
| FMO_OPS_BOL | < 1 Billion | < 1 Billion | |
| FMO_OPS_BOM | < 4 Billion | < 4 Billion | |
| ~~FMO_OPS_BOSM~~ | | ~~< 4 Billion~~ | ~~New Profile (band4), same view access as FMO_OPS_BOM~~ ~~to be confirmed if this still required~~ |

Only `FMO_OPS_BOS` is intended to change, from less than USD 300 million to less than USD 500 million. `FMO_OPS_BOSM` is not required. Development is to extract the current live-user list, and Deepak K is to confirm affected users' target profiles before production release.

## Cashflow affirmation

For BCS, the source records confirmation on 2026-08-13 that an authorization-limit check must be added to the single-level update-affirmation-status action. A possible later maker/checker enhancement is to be tracked separately.

For FMRP, the control remains unresolved as of 2026-08-21. Anna must choose between removing update affirmation from the cashflow-list view or applying an authorization-limit check to that action. See [[what-is-the-final-fmrp-cashflow-affirmation-authorization-control]].

## Scope and dependencies

- [[bcs]], [[fmrp]], and [[loaniq]] are in scope.
- Korea ENSIS is out of scope.
- If Korean cashflows later migrate to the RATAN/FMRP flow, [[murex]] would need to send additional data and ENSIS would need to support the process.
- The FMRP/LOANIQ implementation must align with [[razor]].
- The source does not specify numerical FMSGW queue thresholds or a DEF Rule-to-queue mapping.