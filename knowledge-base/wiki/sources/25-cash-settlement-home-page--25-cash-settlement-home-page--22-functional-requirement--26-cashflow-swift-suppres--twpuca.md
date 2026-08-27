---
type: source
title: Cashflow Swift Suppression
authors: []
year: 2023
url: "https://confluence.global.standardchartered.com/display/DSP/Function+Flow"
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, ratan, swift, suppression, accounting, maker-checker]
related: [ratan, razor, oscar, amh, cashflow-suppression, swift-suppression, suppression-maker-checker-workflow, suppression-rule-management, cashflow-status-lifecycle, cashflow-amendment-supersession, cashflow-accounting-eligibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Swift Suppression.md"]
---
# Cashflow Swift Suppression

This functional requirement defines automated and manual suppression capabilities in the Ratan STP/NSTP workflow.

It distinguishes:

- **Cashflow Suppression**, for cases where neither payment nor settlement accounting is required.
- **Payment Suppression**, for cases where payment is not required.
- **Swift Suppression**, the operational status model specified later in the requirement, where SWIFT generation is bypassed but accounting continues through [[razor]].

The relationship between Payment Suppression and Swift Suppression is not explicitly defined. See [[is-payment-suppression-the-same-as-swift-suppression]].

## Automation and rule administration

Static-data rules drive automatic Cashflow Suppression and Swift Suppression as a single-level workflow; matching cashflows do not require a per-cashflow Maker/Checker approval.

Cashflow Suppression rules can use pre-defined fields for NSTP rule definition, including a stated example to suppress cashflows booked with unsupported entities. Rule creation and deletion require Maker/Checker control.

Payment Suppression requires a dedicated UI tile and backend rule type, while sharing the Cashflow Suppression rule-creation and deletion process. The field schema, matching semantics, precedence, and effective-date rules are not specified. See [[what-is-the-authoritative-suppression-rule-schema-and-precedence-model]].

## Manual status transitions

### Cashflow Suppression

| Source cashflow status | Source sub-status type | Source sub-status | Action | Target cashflow status | Target sub-status type | Target sub-status |
|---|---|---|---|---|---|---|
| PROJECTED | NA | NA | Maker | WAITING | Cashflow Suppression | Pending Verification |
| WAITING | Exclude (Cashflow Suppression, Undo Cashflow Suppression, Swift Suppression, Undo Swift Suppression) | Any | Maker | WAITING | Cashflow Suppression | Pending Verification |
| READY | NA | NA | Maker | WAITING | Cashflow Suppression | Pending Verification |
| WAITING | Cashflow Suppression | Pending Verification | Checker Approve | CASHFLOW SUPPRESSED | NA | NA |
| WAITING | Cashflow Suppression | Pending Verification | Checker Reject | Rollback status | Rollback status | Rollback status |

### Undo Cashflow Suppression

| Source cashflow status | Source sub-status type | Source sub-status | Action | Target cashflow status | Target sub-status type | Target sub-status |
|---|---|---|---|---|---|---|
| CASHFLOW SUPPRESSED | NA | NA | Maker | WAITING | Undo Cashflow Suppression | Pending Verification |
| WAITING | Undo Cashflow Suppression | Pending Verification | Checker Approve | QUEUED | NA | NA |
| WAITING | Undo Cashflow Suppression | Pending Verification | Checker Reject | CASHFLOW SUPPRESSED | NA | NA |

### Swift Suppression

| Source cashflow status | Source sub-status type | Source sub-status | Action | Target cashflow status | Target sub-status type | Target sub-status |
|---|---|---|---|---|---|---|
| PROJECTED | NA | NA | Maker | WAITING | Swift Suppression | Pending Verification |
| WAITING | Exclude (Cashflow Suppression, Undo Cashflow Suppression, Swift Suppression, Undo Swift Suppression) | Any | Maker | WAITING | Swift Suppression | Pending Verification |
| READY | NA | NA | Maker | WAITING | Swift Suppression | Pending Verification |
| WAITING | Swift Suppression | Pending Verification | Checker Approve | SWIFT SUPPRESSED | NA | NA |
| WAITING | Swift Suppression | Pending Verification | Checker Reject | Rollback status | Rollback status | Rollback status |

### Undo Swift Suppression

| Source cashflow status | Source sub-status type | Source sub-status | Action | Target cashflow status | Target sub-status type | Target sub-status |
|---|---|---|---|---|---|---|
| SWIFT SUPPRESSED | NA | NA | Maker | WAITING | Undo Swift Suppression | Pending Verification |
| WAITING | Undo Swift Suppression | Pending Verification | Checker Approve | QUEUED | NA | NA |
| WAITING | Undo Swift Suppression | Pending Verification | Checker Reject | SWIFT SUPPRESSED | NA | NA |

A Checker rejection of a suppression action uses an unspecified “Rollback status.” An approved undo transitions to `QUEUED`, rather than restoring the original `PROJECTED` or `READY` status.

## Value-date constraint

Manual un-suppression is permitted only until value date.

For Cashflow Suppression, payment and accounting required after value date must be handled through [[oscar]]. For Payment Suppression, payment required after value date must be handled through [[amh]] / [[oscar]]. The document does not define cutoff time, timezone, calendar, validation mechanics, or exception authorization.

## SWIFT SUPPRESSED accounting requirement

On value date, by EOD, [[ratan]] must send cashflows in `SWIFT SUPPRESSED` status to [[razor]]. Razor must bypass SWIFT generation and run accounting using that status.

After value-date accounting EOD:

- A cancellation is sent for reversal-accounting-entry generation.
- An amendment sends the withdrawn original for reversal accounting and the replacement cashflow for a new accounting entry.

## Accounting user cases

| Action | Sent to Razor | System date | Cashflow ID | Cashflow Event | Cashflow Status | Currency | Amount | Value Date | Accounting Date | Accounting Entry | Swift Value Date | Swift generation |
|---|---|---|---|---|---|---|---:|---|---|---|---|---|
| SWIFT SUPPRESSED Cashflow sent to Razor on VD | Y | 8th May | C101 | New | SWIFT SUPPRESSED | USD | 100 | 8th May | 8th May | Y |  | N |

| Action | Sent to Razor | System date | Cashflow ID | Cashflow Event | Cashflow Status | Currency | Amount | Value Date | Accounting Date | Accounting Entry | Swift Value Date | Swift generation |
|---|---|---|---|---|---|---|---:|---|---|---|---|---|
| SWIFT SUPPRESSED Cashflow sent to Razor on VD | Y | 8th May | C101 | New | SWIFT SUPPRESSED | USD | 100 | 8th May | 8th May | Y |  | N |
| Trade Cancellation post accounting EOD | Y | 9th May | C101 | Withdrawal | SWIFT SUPPRESSED | USD | 100 | 8th May | 9th May | Y(Reversal) |  | N |

| Action | Sent to Razor | System date | Cashflow ID | Cashflow Event | Cashflow Status | Currency | Amount | Value Date | Accounting Date | Accounting Entry | Swift Value Date | Swift generation |
|---|---|---|---|---|---|---|---:|---|---|---|---|---|
| SWIFT SUPPRESSED Cashflow sent to Razor on VD | Y | 8th May | C101 | New | SWIFT SUPPRESSED | USD | 100 | 8th May | 8th May | Y |  | N |
| Trade Amendment | Y | 9th May | C101 | Withdrawal | SWIFT SUPPRESSED | USD | 100 | 8th May | 9th May | Y(Reversal) |  | N |
| Trade Amendment | Y | 9th May | C102 | New | SWIFT SUPPRESSED | USD | 200 | 8th May | 9th May | Y |  | N |

| Action | Sent to Razor | System date | Cashflow ID | Cashflow Event | Cashflow Status | Currency | Amount | Value Date | Accounting Date | Accounting Entry | Swift Value Date | Swift generation |
|---|---|---|---|---|---|---|---:|---|---|---|---|---|
| SWIFT SUPPRESSED Cashflow sent to Razor on VD | Y | 8th May | C101 | New | SWIFT SUPPRESSED | USD | 100 | 8th May | 8th May | Y |  | N |
| Trade Amendment | Y | 9th May | C101 | Withdrawal | SWIFT SUPPRESSED | USD | 100 | 8th May | 9th May | Y(Reversal) |  | N |
| Trade Amendment | Y | 9th May | C102 | New | READY | USD | 200 | 8th May | 9th May | Y |  | Y |