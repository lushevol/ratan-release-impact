---
type: source
title: F2B Milestone Checklist - HK and TW
authors: []
year: 2026
url: ""
venue: "Functional requirement and onboarding checklist"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, f2b, hk, tw, onboarding, functional-requirements, testing]
related: [fmrp-china-cash-settlement, fmrp, ratan, murex, stella, ssi-stamping, ssi-selection-hierarchy, swift-mt-mx-integration, iso-20022-mx, cashflow-suppression, auto-netting, cashflow-migration, markitwire, ebbs, aspire, cdups, keystone-hk, irs-interest-auto-netting, pending-another-leg, murex-to-ratan-rule-replication, sgo-currency-handling, cash-settlement-accounting-routing, is-nd-ccs-in-scope-for-f2b-hk-tw]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - HK & TW.md"]
---

# F2B Milestone Checklist - HK and TW

## Purpose and evidence status

This document defines functionality required for development and functionality to be tested for F2B milestone onboarding in Hong Kong and Taiwan. It is a scope and acceptance-checklist baseline, not a test execution report. It provides no author, approval status, final sign-off, pass/fail evidence, defect references, or production-readiness determination.

The checklist contains items that are in scope, excluded, dependent on another drop, or awaiting clarification. Migration activities use a separate test pack.

## Functional scope

### SSI and Nostro processing

The onboarding must support:

- SSI auto-stamping hierarchy, including old-versus-new hierarchy behavior.
- CFI-code selection.
- `FEDWIRE` and `CASH` settlement methods.
- Single-agent and two-agent processing. Three-agent processing is not supported.
- Trade SSI stamping to CDUPS through XML and product-based flows.
- Default Nostro auto-stamping.
- Automatic SSI attachment for IRS, CCS, and Loan Depo.
- Correct CFI-code capture for IRS, CCS, and Loan Depo.
- Automatic attachment of the correct Nostro.

HK/TW follows the UK SSI hierarchy model: `Country Specific + Global Product` takes priority over `Global Entity + Product Specific`.

### Grouping and settlement queue

The expected operational flow is:

```text
Group Pending Validation
        |
        | validation
        v
Settlement Queue
```

No cashflow should remain stuck in `Group Pending`. A cashflow may remain in `Group Pending Validation` before validation; after validation it should flow to the Settlement Queue.

Cashflow Blotter fields introduced for Murex flows are explicitly outside this onboarding scope, including `LIEN`, `Pending Fixing`, `Duplicate NDS`, `LTID`, `Structure ID`, `NID`, `Commodity Flag`, and `Alpha Clearing`.

### SWIFT and MX generation

Required MT output coverage includes:

```text
MT103
MT202
MT103+202COV
MT210
FlipMT202
MT192
MT292
MT604
MT605
MT692
```

Required ISO 20022 output references include:

```text
Pacs.008.001.08  -> MT103
Pacs.009.001.08  -> MT202 and MT202COV
Camt.056.001.08 -> MT192 and MT292
camt.057        -> MT210
```

Acceptance criteria are that the cashflow moves to `SETTLED` and SWIFT generation succeeds for the specified messages. The checklist does not define message schemas, complete field-level validation, negative tests, or the precise conditions under which a cashflow may become `SETTLED`.

Configuration considerations include:

- Booking Entity FMID.
- Booking Entity SWIFT BIC.
- Field 53 SWIFT BIC for LCY and Over Account.
- Field 58 SWIFT BIC for Flip MT202.
- Branch-code mapping.
- Other branch-specific SWIFT requirements.

See [[swift-mt-mx-integration]] and [[iso-20022-mx]] for related message and format requirements.

### Accounting generation

The accounting scope includes:

- EBBS real-time feeds.
- ASPIRE integration.
- End-of-day feeds.
- Nostro and Over Account data for Keystone (HK) routed to EBBS.
- Suspense data routed to ASPIRE.
- Transition from the Aspire-to-EBBS operating model.
- Historic cashflows and events on past-value cashflows after cutover.
- Special CNH logic, which must be checked with Balaji.

The acceptance criterion is no accounting errors. The source does not provide accounting mappings, transaction types, reconciliation evidence, or exception-handling procedures. See [[cash-settlement-accounting-routing]].

### Booking models, products, and allocation

RFR Booking Model and Swap Agent are not in scope. `FWD_START_SWAP` is also out of scope according to Candice.

ND currency handling for ND CCS and ND IRS is identified as applicable to HK/TW. ND IRS is explicitly in scope and should behave like normal IRS. The scenarios also mention NDIRS and NDCCS initial cashflows being held as `pending another leg`, with all legs tagged and automatically netted. Story `8244494 [Stella] ND CCS Auto Netting` is identified as available for drop 2; the current F2B boundary for ND CCS therefore requires clarification. See [[is-nd-ccs-in-scope-for-f2b-hk-tw]].

Markitwire IRS and CCS allocation is in scope for drop 2. Cashflows for the ALOC name are not STP'd. Allocation support must not be interpreted as automatic STP for allocated cashflows.

### Netting

The checklist requires:

- IRS interest auto netting.
- Fixed cashflows to wait as `pending another leg`.
- Automatic netting after the floating leg is received.
- Re-fixing to break the previous netting and create new netting using the latest cashflow.
- Cross-product netting between IRS and CCS separately from STELLA and other Murex cashflows.

BIC Netting, NDS Auto Netting, Principal + Interest Netting, and DVP are not applicable to HK/TW. The NDS row nevertheless describes USD generation and holding the first leg in RATAN as `pending another leg`; this note should not be treated as a current acceptance criterion until clarified.

### Business rules and suppression

The onboarding requires expected NSTP behavior, including adding new entities where SCB entities are counterparties that bypass NSTP and where SCB entities are booking entities. The following rules are excluded according to Candice:

```text
PRC_SCBHK_SGEI
PRC_USD_SGEI
PRC_SGE_SWP
PRC_HOC_SGE_SWP
PRC_HOSGE_N_IMA
```

Murex rules must be replicated for STELLA cashflows. SWIFT suppression must cover expected cases such as auto-debit by agent and shared Nostros with another entity. Murex interface filters that exclude certain auto-suppression counterparties must be converted into RATAN suppression rules because STELLA does not have the same filter.

Client Clearing Portfolios cashflows must be automatically suppressed. See [[murex-to-ratan-rule-replication]] and [[cashflow-suppression]].

### Migration and configuration

Murex-to-FMRP migration must address:

- Duplicate-payment prevention.
- Cutover handling.
- New functions and changes.
- Historical data.
- ISO migration.
- Near-value cashflows.
- Events on past-value cashflows after cutover.

A separate migration test pack is used. Related requirements are captured in [[cashflow-migration]].

Other configuration notes include:

- BCS-versus-strategic-routing entity whitelists.
- Routing selected entities to RAZOR or handling them in RATAN, where RATAN generates SWIFT and accounting.
- Loan Depo configured as `Pending Fixing`.
- Non-ISO-to-ISO and precious-currency mapping.
- `SGO` producing SWIFT and accounting as `SGD`.
- No SWIFT or accounting failure for `SGO`.
- Automatic SGO Nostro and Vostro attachment.
- New branch or product entries in Cashflow Blotter and Dashboard GUI dropdowns.
- No Vostro SSI Input Screen changes.
- No rounding changes.
- Settlement accounting configuration row marked “No changes”.

## Authoritative acceptance wording

The following checklist statements are retained as acceptance criteria pending refinement into executable test cases:

```text
- SSI is Auto Attached for IRS, CCS, Loan Depo
- Correct CFI code is captured for IRS, CCS, Loan Depo
- Correct nostro is auto attached
- No Cashflows get stuck as Group Pending
- Cashflows are stuck as Group Pending Validation prior to Validation & when validated they flow to Settlement Queue
- Cashflow moves to SETTLED status
- Swift Generated successfully for MT103, 202, MT103+202COV, MT210, FlipMT202, MT192, MT292, MT604, MT605, MT692
- No Accounting Errors
- ND IRS in scope. Behavior same as normal IRS.
- Verify SSI Stamping for IRS/CCS different CFI Code
- Verify all legs get tagged as Pending another leg and get auto netted
- Initial cashflow should be stopped as pending another leg for NDIRS/NDCCS
- available for drop 2
- Allocation in scope - available for drop 2
- Fixed cashflow waiting as pending another leg & auto netted post floating leg received
- Re-fixing breaks the previous netting and does re-netting with latest cashflow
- Net cashflows between IRS, CCS separately of STELLA with other Murex cashflow
- NSTP is triggered as expected
- Murex Rules are replicated to work on STELLA cashflows
- Swift Suppression done for expected cases
- Client Clearing Portfolios cashflows are auto suppressed
- SGO currency generates swift and accounting as SGD
- No Swift / Accounting failure for SGO
- SGO Nostro & Vostro are auto attached
```

## Explicit exclusions

| Area | Scope |
|---|---|
| RFR Booking Model | Not in scope |
| Swap Agent | Not in scope |
| BIC Netting (Manual) | Not applicable |
| NDS Auto Netting | Not applicable, subject to clarification of adjacent behavior |
| Principal + Interest Netting | Not applicable |
| DVP | Not applicable |
| Vostro SSI Input Screen | Not applicable |
| Rounding | Not applicable |
| `FWD_START_SWAP` | Not in scope |
| Murex Cashflow Blotter fields | Not in scope |
| Named NSTP rules | Excluded according to Candice |

## Open implementation questions

- Is ND CCS part of the F2B HK/TW milestone or only drop 2?
- What are the authoritative EBBS and ASPIRE routing rules for each accounting event?
- Which Murex rules must be replicated for STELLA, and what are the precedence and exceptions?
- What conditions transition each flow type to `SETTLED`?
- Which separate migration test pack is authoritative?
- Does “Settlement Accounting — No changes” refer only to branch/account configuration, rather than the accounting operating-model migration?
- What are the monitoring, timeout, retry, and remediation rules for grouping and settlement-queue transitions?

The checklist should be converted into an executable test matrix with product, booking model, source and target system, currency, settlement method, SSI hierarchy, CFI code, agent count, expected state transitions, SWIFT message, accounting destination, suppression expectation, evidence, result, defect reference, owner, and approval status.