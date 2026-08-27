---
type: source
title: Bulk Processing for Multi Exception Demo
created: 2026-08-23
updated: 2026-08-23
tags: [functional-requirement, cashflow, bulk-processing, nstp, ratan-one, maker-checker]
related: [bulk-cashflow-exception-processing, cashflow-bulk-eligibility, bulk-processing-cohort-controls, pending-affirmation-bulk-processing, what-is-the-authoritative-bulk-cashflow-eligibility-evaluation-and-revalidation-rule, what-is-the-bulk-processing-partial-success-concurrency-and-retry-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Processing for Multi Exception Demo.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Bulk Processing for Multi Exception Demo

## Summary

This functional requirement and demo outline describes a proposed RATAN ONE workflow for processing multiple cashflows with NSTP exceptions through the [[cashflow-blotter]]. Its stated objective is to reduce the operational effort of processing high cashflow volumes individually.

Bulk operations are constrained by two controls:

- Selected cashflows must share the same Value Date, Booking Entity, and Counterparty.
- Every exception associated with a payment must be configured as bulk eligible; one non-eligible exception makes the payment ineligible.

The workflow uses an eligibility preview before bulk submit or approve. The preview compares exceptions with the latest rule configuration, separates cashflows into eligible and not eligible sections, and permits all-or-partial selection from the eligible section. `Pending Affirmation` is bulk eligible but requires manual affirmation details that apply only to selected cashflows carrying that exception.

The source specifies maker-checker submit, approve, and reject actions with expected real-time result and status refresh behavior. It explicitly demonstrates partial success during approval when another user has processed an item offline. It does not provide execution results: every `Ready for Testing` field is blank.

## Functional Requirements

1. Users maintain bulk eligibility for NSTP exceptions through `FMO_BR_APR` and `FMO_BR_MKR`.
2. Bulk processing is limited to cashflows with the same Value Date, Booking Entity, and Counterparty.
3. A preview opens when the user starts bulk submit or bulk approve.
4. The preview compares each cashflow exception against the latest rule configuration and divides cashflows into eligible and not eligible sections.
5. No action is available for the not eligible section.
6. Users may select all eligible cashflows or a subset.
7. `Pending Affirmation` cashflows require manual affirmation details; those details apply only to the relevant Pending Affirmation cashflows.
8. Submit, approve, and reject are intended to show results and refresh cashflow statuses in real time.

## Bulk Eligibility Catalogue

The following catalogue is preserved verbatim from the source. `Reversal` and `reversal` remain separate entries, and `Rebook` appears twice.

| **Bulk processing allow** | **Bulk processing not allowed** |
| --- | --- |
| Adhoc Netting Client | DVP |
| Adhoc Netting FMCODE | Manual Deliver |
| Adhoc Netting FMID | AmendmentError |
| Adhoc_Netting | Portfolio reassignment |
| Bad Business Day | CCS: Check Validation Status |
| CHINA FDL Client | ReInstate |
| China Precious Metal | Previously Netted |
| CORP Client | NetOverAmend |
| GSAM Client | Withdrawal on component |
| India Adhoc Netting | Murex 2.11 Strategy CCS_DVP |
| India SCF | Murex 2.11 Strategy PAR FWD DVP |
| Murex 2.11 CRD CDS product | Reversal |
| Murex 2.11 CRD RTRS product | Rebook |
| Murex COM SWP/FWD | reversal |
| Murex IRS | Rebook |
| Net Cashflow | DVP Strategy |
| Pending Affirmation | LEI VA |
| Settled as gross | Back Value Date |
| Structure Trade | Stella_Corp_CCS |
| WHT Clients | Missing Vostro |
| WHT FMCODE | Missing Nostro |
| Secondary Vostro | Multiple Vostro |
|  | High Value Payment |
|  | NSTP |
|  | Above Threshold |
|  | Murex STP_HOLD |
|  | CCY NSTP |
|  | Murex SLT |
|  | CS Linked IRS |
|  | NDS Fixing |
|  | INO IRS |
|  | XAU |
|  | FI Client - PoU Check |
|  | Multi SSI |

## Demo Scope

The planned demo covers configuration inspection, same-cohort selection, mixed eligibility preview, bulk submit, bulk approval with partial success, and a single-submit fallback for a remaining `Pending Affirmation` cashflow.

The demo does not include a bulk-reject scenario, independent tests for differing Counterparty or Value Date, authorization-boundary testing, configuration change handling, or completed test evidence.

## Status and Limitations

This is a requirement and demo plan, not evidence of deployment or successful testing. It does not define:

- The action-time revalidation rule after preview.
- Payment-to-cashflow eligibility scope and cardinality.
- Per-cashflow partial-success outcomes, error codes, retries, or transaction semantics.
- Concurrency, locking, idempotency, or version-conflict handling.
- Required affirmation fields, validation, audit data, or checker edit permissions.
- A measurable definition of real-time status refresh.

See [[bulk-cashflow-exception-processing]], [[cashflow-bulk-eligibility]], and [[bulk-processing-cohort-controls]].