---
type: source
title: Hold UnHold — Cash Settlement Functional Requirement
authors: [Jill Du]
year: 2026
url: ""
venue: Internal functional requirement
tags: [cash-settlement, ratan, hold, unhold, authorization, cashflow-lifecycle]
related: [ratan, cash-settlement-home-page, cashflow-hold-and-unhold, cashflow-hold-unhold-authorization, failed-cashflow-status, cashflow-event-versioning, cashflow-withdrawal-and-new, what-actions-are-authoritatively-permitted-while-a-cashflow-is-on-hold, what-is-the-authoritative-hold-unhold-status-restoration-and-eligibility-matrix, how-are-unhold-authorization-limits-calculated-for-non-usd-and-bulk-cashflows]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Hold UnHold.md"]
---
# Hold UnHold — Cash Settlement Functional Requirement

This requirement specifies a proposed RatanOne/Ratan capability for settlement users to place cashflows on HOLD before cutoff and later UNHOLD them. The document is marked as reviewed by business owners, but does not state an approval outcome.

## Ownership and delivery roles

- Document owner: Jill Du
- Product Owner: Dinesh, Arockia
- Business Owners: K Thirunavukarasu; Cordelia Sumita; Thomas, David George
- Developer: Yang3, Chen
- QA: Ma, Shimeng; Wang, Elena

## Requirement summary

The feature introduces `HOLD` as a main cashflow status, with sub-status type `Cashflow Hold` and sub-status `Pending Verification`. HOLD is intended to stop further ordinary processing, while UNHOLD restores the status held immediately before HOLD and resumes processing.

Each HOLD and UNHOLD action creates a new Ratan cashflow version. Both actions require comments and may be submitted in bulk.

HOLD is stated to be available after any status except `RELEASED`, `NET`, or `SPLIT`. UNHOLD is restricted by profile, Maker/Checker role, self-approval prevention, and a USD operations authorization limit.

The source cites the [Status Machine - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/Status+Machine) as a reference for status semantics.

## User action matrix

| Source Cashflow Status | Source Sub Status Type | Source Sub Status | HOLD Action | HOLD Target Cashflow Status | HOLD Target Sub Status Type | HOLD Target Sub Status | UNHOLD Action | UNHOLD Target Cashflow Status | UNHOLD Target Sub Status Type | UNHOLD Target Sub Status |
|---|---|---|---|---|---|---|---|---|---|---|
| QUEUED | N/A | N/A | Hold | HOLD | Cashflow Hold | Pending Verification | Unhold | QUEUED | N/A | N/A |
| Pending Exception | N/A | Hold | HOLD | Cashflow Hold | Pending Verification | Unhold | QUEUED | Pending Exception | N/A |
| WAITING | Pending Another Leg | Pending Verification | Hold | HOLD | Cashflow Hold | Pending Verification | Unhold | WAITING | Pending Another Leg | Pending Verification |
| Pending Netting | Pending Verification | Hold | HOLD | Cashflow Hold | Pending Verification | Unhold | WAITING | Pending Netting | Pending Verification |
| Pending Exception | Pending Verification/Operator | Hold | HOLD | Cashflow Hold | Pending Verification | Unhold | WAITING | Pending Exception | Pending Verification/Operator |
| Reversal_Rebook | Pending Verification | Hold | HOLD | Cashflow Hold | Pending Verification | Unhold | WAITING | Reversal_Rebook | Pending Verification |
| READY | N/A | N/A | Hold | HOLD | Cashflow Hold | Pending Verification | Unhold | READY | N/A | N/A |

## Actions listed as available from HOLD

| Action allowed after 'HOLD' status | Status after action |
|---|---|
| Adhoc SSI | 'WAITING' |
| Netting | move to new lifecycle |
| Un-Net | move to new lifecycle |
| Swift Suppression - Maker/Checker | move to End status 'SWIFT SUPPRESSED' |
| Cashflow Suppression - Maker/Checker | move to End status 'CASHFLOW SUPPRESSED' |
| Unhold | revert back to the previous status before HOLD |

## Illustrative version histories

### Hold and UNHOLD by different users

| User ID | Business Event | Cashflow ID | Cashflow Event | Cashflow Version (Ratan) | Cashflow Status | Sub Status Type | Sub Status |
|---|---|---|---|---:|---|---|---|
|  | New | C101 | New | 1 | WAITING | Pending Another Leg | Pending Verification |
| AAA | Rantan Hold | C101 | Hold | 2 | HOLD | Cashflow Hold | Pending Verification |
| BBB | Ratan Unhold | C101 | Unhold | 3 | WAITING | Pending Another Leg | Pending Verification |

### Value date passed

| Day | User ID | Business Event | Cashflow ID | Cashflow Event | Cashflow Version (Ratan) | Cashflow Status | Sub Status Type | Sub Status |
|---|---|---|---|---|---:|---|---|---|
| VD-5 |  | New | C101 | New | 1 | WAITING | Pending Another Leg | Pending Verification |
| VD-5 | AAA | Ratan Hold | C101 | HOLD | 2 | HOLD | Cashflow Hold | Pending Verification |
| VD EOD | BBB | Ratan Unhold disabled as the cashflow status FAILED is not eligible for UNHOLD | C101 | FAIL | 3 | FAILED |  |  |

The source states that a failed cashflow is handled by the fail process and defines EOD as before China business hour 7pm.

### Trade amendment retains HOLD

| Business event | Cashflow ID | Cashflow Event | Cashflow Version (Ratan) | Cashflow Status | Sub Status Type | Sub Status |
|---|---|---|---:|---|---|---|
| New | C101 | New | 1 | WAITING | Pending Exception | Pending Verification |
| Rantan Hold | C101 | HOLD | 2 | HOLD | Cashflow Hold | Pending Verification |
| Trade amendment | C101 | Withdrawal (same reference) | 3 | Cancelled | N/A | N/A |
| C102 | New (new reference) | 4 | HOLD | Cashflow Hold | Pending Verification |

### Held cashflow withdrawal

| User ID | Business event | Cashflow ID | Cashflow Event | Cashflow Version (Ratan) | Cashflow Status | Sub Status Type | Sub Status |
|---|---|---|---|---:|---|---|---|
|  | New | C101 | New | 1 | WAITING | Pending Exception | Pending Verification |
| AAA | Rantan Hold | C101 | New | 2 | HOLD | Cashflow Hold | Pending Verification |
|  | Withdrawal | C101 | Withdrawal | 3 | CANCELLED | N/A | N/A |

### Authorization-limit example

| User ID | Business event | Cashflow ID | Cashflow Event | Cashflow Version (Ratan) | Cashflow Status | Sub Status Type | Sub Status | Amount |
|---|---|---|---|---:|---|---|---|---:|
|  | New | C101 | New | 1 | WAITING | Pending Another Leg | Pending Verification | 1000 |
| AAA | Ratan Hold | C101 | Hold | 2 | HOLD | Cashflow Hold | Pending Verification | 1000 |
| BBB (under profile BOC, which allowed operation amount is 100) | Ratan Unhold disabled after the system checks the profile amount limitation |  |  |  |  |  |  |  |

## Interpretation limits

This is a functional requirement, not implementation evidence. It contains unresolved tensions: HOLD is said to stop SSI stamping and other processing, yet Adhoc SSI, Netting, Un-Net, and both suppression actions are listed as permitted from HOLD. The source-status matrix also uses inconsistent main-status and sub-status representations. See [[what-actions-are-authoritatively-permitted-while-a-cashflow-is-on-hold]] and [[what-is-the-authoritative-hold-unhold-status-restoration-and-eligibility-matrix]].