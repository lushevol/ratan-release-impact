---
type: source
title: Cash Settlement Home Page — Settlement Day 2 Cashflow Splitting
created: 2026-08-22
updated: 2026-08-22
tags: [functional-requirement, settlement-day-2, cashflow-splitting, ratan, fmrp]
related: [cashflow-splitting, nostro-threshold-auto-splitting, split-child-processing-exclusions, split-cashflow-swift-annotation, nostro-threshold-static, is-manual-splitting-of-irs-aggregation-resultants-in-day-1-scope, what-is-the-authoritative-nostro-threshold-auto-split-allocation-algorithm, what-is-the-approved-withdrawal-and-accounting-behavior-after-split-child-release]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting.md"]
authors: []
year: 2025
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469617"
venue: "Functional requirement"
---
# Cash Settlement Home Page — Settlement Day 2 Cashflow Splitting

This functional requirement defines Settlement Day 2 cashflow splitting for [[ratan]] and [[fmrp]]. It supports user-directed payment allocation and automatic distribution of qualifying SCB pay cashflows to meet Nostro Agent payment thresholds. The stated expected benefit is approximately one hour less manual work per day.

The requirement received user sign-off to proceed on 2025-08-26. Its displayed ADO identifier is inconsistent: the rendered text refers to work item `64695`, while the link target refers to `6469617` and is followed by trailing text `64`.

## Day 1 scope

Only FMRP cashflows are in scope. BCS, LOANIQ, EG, NP, and SA are excluded because payment generation is routed through [[razor]]. EG, NP, and SA may be included if they migrate to FMRP before go-live.

The capability comprises:
- [[cashflow-splitting]] for manual parent-to-child allocation.
- [[nostro-threshold-auto-splitting]] before SWIFT generation.
- Parent–child traceability through `Cashflow.Splitting_Id`.
- Exclusion of split children from netting and IRS processing through [[split-child-processing-exclusions]].

## Review history

| # | Date | Status |
| --- | --- | --- |
| 1 | 2025-08-07 | Requirement reviewed; official email sign-off was being collected. |
| 2 | 2025-08-26 | Previous-version updates reviewed; user sign-off to proceed recorded. |

## Manual action eligibility

| User action | Condition |
| --- | --- |
| Split Cashflow | Cashflow State in ("~~PROJECTED~~", "WAITING", "READY") and Netting Is is empty and Splitting Id is empty and Cashflow Event Type = "New" and Trade Original Source System Name <>'LOANIQ' |
| Amend Split Amount | Cashflow State in ("WAITING") and Splitting Id Exists |
| Un-Split | Splitting Id is not null and and Cashflow Event Type = "New" and Cashflow State NOT IN ('RELEASED','SETTLED') |

`PROJECTED` is struck through in the requirement and therefore appears to have been removed from split eligibility. The exact meaning of “Netting Is” is not defined.

## Required identifiers and query field

```text
Cashflow.Splitting_Id
```

```text
with S prefix and length as 12
sample: S00123456789
```

## Settlement instruction lookup sample

```text
Settlement_Instruction.BranchId_Murex3Id in ("SCB LONDON*LDN","Global") //booking fmcode
Settlement_Instruction.Payment_Currency in ("USD") //payment currency
Settlement_Instruction.Counterparty_SCI_FMID in ("401064447") //counterparty fmid
Settlement_Instruction.SSI_Status in ("Active","New","Update")
```

## Nostro Threshold Static fields

| Field | Requirement |
| --- | --- |
| Booking Entity FMID | Optional; soft warning if absent. Used by backend matching. |
| Booking Entity FM CODE | Optional; soft warning if absent. Reference-only for users. |
| Nostro Agent | Optional; derived from 53 correspondent SWIFT in Nostro static; validate 8 or 11 characters. |
| Currency | Mandatory; quick-search list plus manual entry. |
| Threshold | Mandatory; no decimals. |
| Amount | Mandatory; no decimals; validation: less than Threshold and limitation. |
| Limitation | Mandatory; no decimals; validation: less than Threshold. |
| Duplicate key | Booking Entity + Nostro Agent + Currency. |

The source does not define whether “Amount ... less than Threshold and limitation” means less than both fields or only a separate limitation rule.

## Auto-split SWIFT annotation

```text
/REC/Split of {CCY} {Parent amount}
```

| Message type | Field |
| --- | --- |
| MT103 / MT103Cov | Field 70 only |
| MT202 / MT202Cov / MT202Flip | Field 72 |
| MT605 / MT210 | Out of scope |

Existing stamped content is shifted to later lines; the final line is discarded if all positions are occupied. For INR, after LEI handling, split content occupies line 3.

## Integration and lifecycle highlights

- The parent enters `SPLIT`; this status is written back to Stella but not Murex.
- Child `RELEASED`, or `SETTLED` without prior release, is written back to Murex in the specified cases.
- `SPLIT` produces no accounting entry and must not transition to `FAILED`.
- Successful unsplit sets children to `DEAD`, reinstates the parent, and holds it with an `Un-Split` exception.
- Any auto-split exception returns the cashflow to `READY` with sub-status `Pending Exception`.
- Blade requires a hard blocker for `SPLIT`; DQSL must expose `Cashflow.Splitting_Id`.
- TLM, EBBS, Aspire, RATAN EOD, SSDR, CIS, and FMMIS have linkage or status/manual-touch consumption requirements.

## Material unresolved issues

The requirement conflicts on whether manual splitting of IRS aggregation resultants is supported in Day 1. It also references an unavailable `Auto Split Samples.xlsx` for the core allocation logic, leaving child-count, residual, limitation, tie-break, and rollback behavior unspecified. Withdrawal and accounting behavior after release of a split child remains unsettled.