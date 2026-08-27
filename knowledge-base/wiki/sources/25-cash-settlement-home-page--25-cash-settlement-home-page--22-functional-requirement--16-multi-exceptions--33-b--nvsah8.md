---
type: source
title: Bulk Process for Multi Exceptions
authors: []
year: 2024
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/2298013"
venue: "Cash Settlement Home Page functional requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, cashflows, multi-exceptions, bulk-processing, functional-requirement]
related: [cash-settlement-home-page, bulk-cashflow-processing, multi-exception-bulk-eligibility, cashflow-bulk-submit-and-approve, cashflow-filtering, cashflow-blotter, murex, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Process for Multi Exceptions.md"]
---
# Bulk Process for Multi Exceptions

## Summary

This functional requirement proposes bulk processing for multiple cashflows with exceptions in the [[entities/cash-settlement-home-page]]. The capability is intended to reduce the operational effort of processing cashflows individually, particularly during periods of high volume.

Bulk operations are subject to controls requiring selected cashflows to share the same Value Date, Booking Entity, and Counterparty. Processing eligibility is also intended to be configurable through NSTP rules and restricted to whitelisted exception types.

The requirement defines two state-dependent actions:

- **Bulk Submit** for cashflows in `WAITING - pending operator`.
- **Bulk Approve** for cashflows in `WAITING - pending verification`.

The relevant bulk action is displayed only when all selected cashflows have the required pending sub-state. Both operations require a preview containing eligible and ineligible items before execution. Bulk Submit additionally requires a process-result view.

## Problem Statement

The source states that teams spend considerable time processing cashflows one by one, especially when transaction volume is high. Bulk processing is proposed to allow users to process multiple cashflows at the same time.

## Operational Controls

The proposed controls are:

1. Selected cashflows must have the same Value Date, Booking Entity, and Counterparty.
2. Bulk processing is permitted only for whitelisted exceptions.
3. Exception eligibility should be configurable in NSTP rules.
4. An exception configured with `N` is considered ineligible for bulk processing.

The source does not define the complete NSTP configuration schema or the authoritative meanings of `Yes`, `N`, and `NA`.

## Exception Eligibility List

The source includes the following structured exception list. Its column layout is ambiguous in the original requirement; the displayed values are retained as supplied.

| Exception | Bulk processing allow | Bulk processing not allowed |
|---|---:|---:|
| Adhoc Netting Client | Yes | |
| Adhoc Netting FMCODE | Yes | |
| Adhoc Netting FMID | Yes | |
| Adhoc_Netting | Yes | |
| Bad Business Day | Yes | |
| CHINA FDL Client | Yes | |
| China Precious Metal | Yes | |
| CORP Client | Yes | |
| GSAM Client | Yes | |
| India Adhoc Netting | Yes | |
| India SCF | Yes | |
| Murex 2.11 CRD CDS product | Yes | |
| Murex 2.11 CRD RTRS product | Yes | |
| Murex COM SWP/FWD | Yes | |
| Murex IRS | Yes | |
| Net Cashflow | Yes | |
| Pending Affirmation | Yes | |
| Settled as gross | Yes | |
| Structure Trade | Yes | |
| WHT Clients | Yes | |
| WHT FMCODE | Yes | |
| DVP | | Yes |
| Manual Deliver | | Yes |
| AmendmentError | | Yes |
| Portfolio reassignment | | Yes |
| CCS: Check Validation Status | | Yes |
| ReInstate | | Yes |
| Previously Netted | | Yes |
| NetOverAmend | | Yes |
| Withdrawal on component | | Yes |
| Murex 2.11 Strategy CCS_DVP | | Yes |
| Murex 2.11 Strategy PAR FWD DVP | | Yes |
| Reversal | | Yes |
| Rebook | | Yes |
| reversal | | Yes |
| ReBook | | Yes |
| DVP Strategy | | Yes |
| LEI required | | Yes |
| Back Value Date | | Yes |
| Stella_Corp_CCS | | Yes |
| Missing Vostro | | NA |
| Missing Nostro | | NA |
| Secondary Vostro | Yes | NA |
| Multiple Vostro | | NA |
| High Value Payment | | Yes |

The exception taxonomy requires clarification before it can be treated as an authoritative production eligibility matrix. Potential duplicates include `Reversal`/`reversal`, `Rebook`/`ReBook`, and variants of `Adhoc Netting`. The meaning of `NA` is not specified.

## Cashflow Multi-Selection

The bulk control must validate that selected cashflows share:

- Counterparty
- Booking Entity
- Value Date

If these values are not the same, the bulk operation is disabled.

Bulk Submit is available when the selected cashflows are in `WAITING - pending operator`. Bulk Approve is available when the selected cashflows are in `WAITING - pending verification`. Bulk Submit and Bulk Approve appear only when all selected cashflows have the corresponding pending sub-state.

The requirement does not specify whether mixed-state selections are rejected, automatically partitioned, or handled through another UI response.

## Bulk Submit Preview

The Bulk Submit preview must provide:

1. Exception summary.
2. Cashflow summary containing:
   - Trade ID
   - Cashflow ID
   - Counterparty
   - Entity
   - Currency
   - Amount
   - Value Date
   - Pay/Receive
   - Exception
3. Not eligible exception summary.
4. Not eligible cashflow detail.
5. Affirmation details.

## Bulk Approve Preview

The Bulk Approve preview must provide:

1. Exception summary.
2. Cashflow summary containing:
   - Trade ID
   - Cashflow ID
   - Counterparty
   - Entity
   - Currency
   - Amount
   - Value Date
   - Pay/Receive
   - Affirmation Email ID
   - Exception
3. Not eligible exception summary.
4. Not eligible cashflow detail.
5. Affirmation Email ID.

## Process Result

Bulk Submit requires a process-result view after execution. The source does not define whether results are reported per cashflow or per batch, nor does it specify success and failure statuses, retry behavior, error messages, audit information, or partial-success handling. Equivalent result requirements for Bulk Approve are not stated.

## Maker/Checker Proposal

The solutioning section proposes changing pending affirmation to maker/checker. The requirement does not define the replacement states, role responsibilities, separation-of-duty rules, mapping from `Pending Affirmation`, or whether the change applies to all exceptions or only bulk processing.

This proposal should therefore be treated as an unresolved design direction rather than an approved workflow model. It relates to [[concepts/cashflow-bulk-submit-and-approve]] and existing confirmation and authorization controls.

## Source References

- User story: [Azure DevOps work item 2298013](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/2298013)
- Technical design: [Confluence page 3048144376](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3048144376)
- Referenced attachments:
  - `attachments/MicrosoftTeams-image.png`
  - `attachments/image2024-7-17_10-55-14.png`
  - `attachments/image2024-5-20_11-48-31.png`
  - `attachments/image2024-5-20_11-48-53.png`
  - `attachments/image2024-5-20_11-38-25.png`

## Evidence and Limitations

The requirement provides strong evidence for the intended selection controls, action names, workflow sub-states, and preview fields. It is incomplete or ambiguous regarding:

- Authoritative exception eligibility.
- The semantics of `Yes`, `N`, and `NA`.
- Canonical exception naming.
- Mixed-state and partially eligible selections.
- Atomic versus per-cashflow processing.
- Partial success and retry behavior.
- Maker/checker workflow semantics.
- Bulk Approve result handling.

The linked Azure DevOps work item and Confluence technical design should be reviewed before establishing an authoritative decision or implementation contract.