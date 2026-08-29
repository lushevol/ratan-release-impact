---
type: source
title: NDS Auto Netting Functional Requirement
authors: []
year: 2024
url: ""
venue: "Cash Settlement Home Page"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, NDS, auto-netting, RATAN, Murex]
related: [ratan, murex-2-11, murex, nds-auto-netting, nds-netting-key, pending-nds-netting, net-resultant-cashflow, nds-duplicate-payment-prevention, cashflow-logical-model, duplicate-payment-prevention, cashflow-exception-handling, confirmation-match-driven-settlement, murex-to-ratan-rule-replication, tds3, nds, nds-fixing, ndirs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/NDS Auto Netting.md"]
---

# NDS Auto Netting Functional Requirement

## Summary

This functional requirement defines the migration of NDS cashflow auto-netting from Murex 2.11 to RATAN. RATAN is expected to scan eligible cashflows every 30 minutes and combine them into a net resultant cashflow using a composite key containing Booking Entity, Counterparty, value date, currency, and NID.

The document covers product scope, status and exception gating, Group Blotter processing, resultant cashflow generation, event handling, and test scenarios for amendments, cancellations, re-fixing, and duplicate payments.

## Target operating model

- Murex 2.11 must stop performing NDS netting.
- RATAN becomes the auto-netting engine.
- Component cashflows wait in `WAITING` status with the `Pending NDS Netting` exception.
- RATAN scans cashflows every 30 minutes.
- The value-date scope is today, tomorrow, and the day after, using business days.
- Component cashflows must pass through the Group Blotter without becoming stuck in normal processing.
- A net resultant may be manually netted with other product cashflows while it remains unreleased.
- Confirmation-match status for both components and resultants must follow MX2.11 logic.

## Product scope

The stated typology scope is:

`NDS`, `NDS Fixing`, `NDIRS`, `NDCF`, `NDFRA`, `ND CDS Fixing`, `ND CDS`, and `ND-Convert`.

USD generated from NDS Fixing for ND IRS is intended to settle straight-through in the deliverable currency and is excluded from netting. Other qualifying NDS-related cashflows, including ND CCS scenarios, are expected to wait for auto-netting.

## Eligibility and data derivation

The source defines the netting key as:

- Booking Entity
- Counterparty
- Same value date
- Currency
- NID

The solutioning conditions are:

- Value date is within `[Today, Today+2 business day]`.
- Main status is `WAITING`.
- The cashflow has a pending exception.
- The pending exception contains `Pending NDS Netting`.
- The relevant NSTP rule is live when auto-netting runs.

The technical mapping is:

| Field | Path | Source |
| --- | --- | --- |
| 1 | `Cashflow.ND_Parent_Trade_Id` | `userDefinedField: NID` | Murex |
| 2 | `Cashflow.ND_Parent_Typology` | If current cashflow typology is `NDS Fixing`, query `Instrument_Common.Source_System_Instrument_Type` with `Source_System_Internal_Trade_Id = ND_Parent_Trade_Id`. `Source_System_Instrument_Type` takes the last data with separator `"|"`. | TDS3 |
| 3 |  |  |  |

TDS3 may not yet have received the relevant Murex data. In that case, RATAN may receive an empty `ND_Parent_Typology`; the source does not define the retry, exception, or routing policy for this condition.

## Net resultant cashflow generation

The source-defined mapping is preserved below.

| Logical model field | Generation Logic | Comment |
| --- | --- | --- |
| Data_Flow.Unique_Identifier_Message_Id | UUID | |
| Execution_Date_Time | latest time stmap | |
| Cashflow.Cashflow_Id | fix length 12: 'N' + 11 numeric | |
| Cashflow.Cashflow_Event_Type | pre-config: New | |
| Cashflow.Cashflow_State | pre-config: QUEUED | |
| Cashflow.Cashflow_Affirmation_Status | pre-config: Unaffirmed | |
| Cashflow.Cashflow_Sub_State | pre-config: Blank | |
| Cashflow.Cashflow_Sub_State_Updater | pre-config: Blank | |
| Cashflow.Cashflow_Sub_State_Type | pre-config: Blank | |
| Cashflow.Payment_Type | pre-config: Blank | |
| Cashflow.Netting_Id | UUID | |
| Family | Inherit from component cashflow if the values are same, empty if value are different | |
| Group | Inherit from component cashflow if the values are same, empty if value are different | |
| Type | Inherit from component cashflow if the values are same, empty if value are different | |
| Typology | Inherit from component cashflow if the values are same, empty if value are different | |
| Strategy | Inherit from component cashflow if the values are same, empty if value are different | |
| Trade_Id | Inherit from component cashflow if the values are same, empty if value are different | |
| Taxonomy | Inherit from component cashflow if the values are same, empty if value are different | |
| CFI Code | Same with NDS cashflow (the one whose typology is not NDS Fixing) | |
| Settlement Method | Pre-config: GROSS | |
| Delivery Method | Pre-config: CASH | |
| Cashflow.Payment_Type | Pre-config: NDS Fixing Netting | |
| Parent_Trade_Id | NA | |
| Trade_State | pre-config: TOBESENT | |
| Cashflow.Cashflow_Version | Pre-Config: 0 | |
| Cashflow.Cashflow_Business_Version | Pre-Config: 0 | |
| Cashflow.FMO_Comment | Pre-config: Blank | |
| Cashflow.FMO_Comment_Updater | Pre-config: Blank | |
| Cashflow.FMO_Comment_Timestamp | Pre-config: Blank | |
| Data_Flow.Data_Publication_Date_Time | Latest timestamp | |
| Other Attributes | Copy from first cashflow | |

The table contains two definitions for `Cashflow.Payment_Type`: blank and `NDS Fixing Netting`. The authoritative value requires confirmation.

## Event handling

Before resultant release:

- An amendment or re-fixing automatically un-nets the resultant. Reversal and replacement cashflows enter the next auto-netting cycle.
- A cancellation automatically un-nets the resultant. The original becomes cancelled and a replacement waits for the next cycle. If no replacement arrives, it may remain in `WAITING` for Operations investigation.

After resultant release:

- Amendment and re-fixing reversals and replacements are held as NSTP with `REVERSAL` and `REBOOK` exceptions for manual handling.
- Cancellation holds the component reversal. System or manual un-netting is not allowed after payment release.

## Testing findings

Cases 18–23 identify duplicate-payment weaknesses:

- Non-economic trade-reference changes can generate a second NDS Fixing payment.
- Manually booked additional FXD trades can create duplicate payments.
- A duplicate payment can remain eligible under the same or a changed NID.
- In case 21, RATAN nets the duplicate into the resultant and produces an incorrect amount.
- In post-release scenarios, duplicate payments may be STP while the original payment is already released.

These cases show that matching by status and NID is not sufficient to establish economic uniqueness. [[nds-duplicate-payment-prevention]] should therefore be treated as a release-blocking control rather than an optional enhancement.

## Open design questions

- What is the precedence between NDIRS-specific STP and generic NDS Fixing pending-netting rules?
- How should RATAN handle an empty parent typology returned because of TDS3 latency?
- Is NID stable across non-economic amendments and trade-reference changes?
- Must a netting group be processed atomically?
- Which `Payment_Type` value is authoritative?
- What ordering defines the “first cashflow” used for copied attributes?
- Has the case 21 wrong-amount outcome been remediated and accepted?

## Related wiki pages

This source extends murex to ratan rule replication with NDS-specific eligibility, scheduling, resultant-field mapping, and duplicate-payment evidence. It also provides requirements relevant to cashflow exception handling, cashflow logical model, and confirmation match driven settlement.