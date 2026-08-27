---
type: source
title: SSI Notification Flow
authors: []
year: 2026
url: ""
venue: "Functional Requirement"
tags: [ssi, ssi-stamping, notification, cashflow, settlement-instruction]
related: [ssi-plus, ssi, ssi-stamping, ssi-stamping-notification, cfi-code-ssi-granularity-matching, global-and-branch-specific-ssi-scope, what-is-the-authoritative-ssi-cfi-granularity-matching-rule, what-is-the-authoritative-ssi-restamping-state-transition]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/SSI Notification Flow.md"]
---
# SSI Notification Flow

## Summary

This functional requirement defines how cashflows are identified for SSI re-stamping after an [[entities/ssi-plus]] lifecycle event. It distinguishes creation or change events (`New`, `Amend`, and `Re-active`) from deletion or deactivation events (`Delete` and `De-active`).

Refresh eligibility depends on the SSI event, cashflow status, sub-status, and exception. The source gives special treatment to cashflows in `Pending Operator`, while equivalent `Pending Verification` cases are excluded.

## Re-stamping eligibility matrix

| Case ID | SSI+ Event | Cashflow Status | Sub Status | Cashflow Exceptions | Eligible for SSI Refresh | Logic to identify the impacted cashflows |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | New/Amend/Re-active | WAITING | Pending Operator | Missing Vostro | Y | Re-stamp when the SSI and cashflow match on Counterpart, Currency, CFI Code, and Branch ID. If re-stamping raises an exception, set the sub-status to `Pending Operator` and require Maker input again. |
| 2 | New/Amend/Re-active | WAITING | Pending Verification | Missing Vostro | N | — |
| 3 | New/Amend/Re-active | WAITING | Pending Operator | Multi Vostro | Y | — |
| 4 | New/Amend/Re-active | WAITING | Pending Verification | Multi Vostro | N | — |
| 5 | New/Amend/Re-active | WAITING | Pending Operator | Nostro vs Vostro Mismatch | Y | — |
| 6 | New/Amend/Re-active | WAITING | Pending Verification | Nostro vs Vostro Mismatch | N | — |
| 7 | New/Amend/Re-active | WAITING | — | Adhoc SI | N | — |
| 8 | New/Amend/Re-active | WAITING | Pending Operator | Secondary Vostro | Y | — |
| 9 | New/Amend/Re-active | WAITING/READY | NA+NA | Good System Assigned Vostro | Y | — |
| 10 | Delete/De-active | WAITING | Pending Operator | Multi Vostro | Y | Re-stamp if the deleted SSI is one of the Multi SSI causing the exception. |
| 11 | Delete/De-active | WAITING/READY | NA+NA | Good System Assigned Vostro | Y | Re-stamp if the deleted SSI is assigned to the cashflow. |

The source does not define the meaning of `NA+NA`, the behavior of unlisted statuses, or whether `Multi Vostro` and `Multi SSI` are synonymous.

## Query logic for `New/Amend/Re-active`

The impacted cashflow scope is narrowed by four matching dimensions.

| Matching dimension | Cashflow logical model field | SSI logical model field |
| --- | --- | --- |
| Counterparty FMID | `Entity.Counterparty_SCI_FMID` | `Settlement_Instruction.Counterparty_SCI_FMID` |
| Currency | `Cashflow.Payment_Currency` | `Settlement_Instruction.Payment_Currency` |
| CFI Code | `Instrument_Common.CFI_Code` | `Settlement_Instruction.CFI_Code` |
| Branch ID | `Entity.Booking_Entity_SCI_FMCODE` | `Settlement_Instruction.BranchId_Murex3Id` |

Counterparty FMID and currency are compared between the notification and the cashflow. CFI Code uses the source's wildcard and granularity examples rather than simple literal equality; see [[concepts/cfi-code-ssi-granularity-matching]]. Branch matching depends on whether the SSI is branch-specific or `Global`; see [[concepts/global-and-branch-specific-ssi-scope]].

### CFI examples

| SSI CFI | Cashflow CFI | Good to pick up cashflow? |
| --- | --- | --- |
| `*R****` | `SRXXXX` | Yes |
| `*F****` | `JFXXXX` | Yes |
| `******` | `SRXXXX` | Yes |
| `SRF***` | `SRXXXX` | No |

The stated requirement is that the SSI CFI must be at a higher or equal granular level than the cashflow CFI. The formal wildcard predicate is not specified.

### Branch scope

| Branch from SSI event | Branches from assigned SSI |
| --- | --- |
| `SCB LONDON*LDN` | `SCB LONDON*LDN` |
| `Global` | All |

A branch-specific SSI limits the lookup to cashflows stamped to that branch. A `Global` SSI expands the lookup to cashflows stamped with `Global` and cashflows stamped with a specific branch SSI.

## Query logic for `Delete/De-active`

Deletion and deactivation use SSI identity rather than the four-attribute comparison.

1. Read the SSI ID from the notification at `Settlement_Instruction.SSI_Id`.
2. Compare that SSI ID with cashflows.
3. Re-stamp a `Multi Vostro` cashflow if the deleted SSI is one of the multiple SSIs causing the exception.
4. Re-stamp a `Good System Assigned Vostro` cashflow if the deleted SSI is the SSI stamped to that cashflow.

## Re-stamping exception behavior

If an exception occurs during re-stamping, the cashflow sub-status becomes `Pending Operator`. The Maker must provide input again. The requirement does not specify whether the original exception is retained, which fields are recalculated, or whether a second notification is emitted.

## Scope and limitations

The source does not define an event payload schema, API or queue contract, retry behavior, idempotency guarantees, or the formal meanings of `Re-active` and `De-active`. It also does not specify the complete CFI hierarchy or wildcard algorithm.

The phrase “same values” should therefore be interpreted as field-specific matching: exact or scoped matching for FMID, currency, and branch, and pattern or granularity matching for CFI Code. This interpretation is tracked in [[queries/what-is-the-authoritative-ssi-cfi-granularity-matching-rule]].