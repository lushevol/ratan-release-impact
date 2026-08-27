---
type: entity
title: LOANIQ
created: 2026-08-22
tags: [booking-system, legacy-flow, settlement, LoanIQ, testing, LMS, source-system, loan-management, settlement-affirmation, cashflow-source, fmrp, ratan, cashflow, Stella, loans, liquidity-management]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Derivative Settlement Affirmation - Email Automation.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/High Value Payment Control - RATAN.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Source Stack Flow Name in LMS Feed.md", "RATAN/RATAN -Interfaces/Ratan and LMS 50686.md"]
related: ["ratan", "stella", "tds3", "tag-20-logic", "ssi-selection-hierarchy", "has-loanid-been-used-intentionally-in-the-ssi-hierarchy", "lms", "settlement-integration-static-data-readiness", "affirmation-email-scope-configuration", "fmrp", "fmsgw", "razor", "ratan-high-value-payment-control", "source-stack-flow-name-propagation", "netting-resultant-stack-derivation", "ratan-lms-liquidity-cashflow-feed", "lms-country-and-entity-scope"]
updated: 2026-08-25
---
# LOANIQ

LOANIQ, also styled as LoanIQ in the 2023-Q4 Analysis and the derivative settlement-affirmation requirement, is identified as a legacy booking-system flow in the RATAN onboarding checklist. It is also identified as an original trade source system for `FMRPSTELLA-LOANIQ` cashflows routed through Stella.

LOANIQ is also a cashflow source or product flow within the RATAN high-value payment-control scope and is listed as a source system for the RATAN-to-LMS liquidity-management cashflow feed.

## Role and Settlement Flow

According to the 2023-Q4 Analysis, LoanIQ was a Day 1 release and system-integration-testing dependency for term-loan cashflows.

The onboarding checklist documents the settlement flow as:

```text
LOANIQ -> STELLA -> TDS3 -> RATAN ONE
```

LOANIQ uses `LOANIQ` as its source-system identity and `LQ` as the Field 20 prefix for the documented source-system and Tag 20 agreement.

### FMRPSTELLA-LOANIQ Stack

The source-stack-flow requirement reports the following under confirmed Proposal 1 for `FMRPSTELLA-LOANIQ` cashflows:

- The stack-flow value is `FMRPSTELLA-LOANIQ`.
- The settlement process is FMRP.
- Swift and accounting are handled by RATAN.
- The LMS source value is `FMRPSTELLA-LOANIQ`.
- The Tag20 prefix is `LQ`.
- A netting resultant tested with this stack was sent to LMS with the same source value.

That source reports no withdrawal-event test for LOANIQ cashflows. It also states that the exact formatting of the hyphenated value requires confirmation.

The `FMRPSTELLA-LOANIQ` stack description comes from the source-stack-flow requirement and should be kept distinct from the onboarding checklist's documented `LOANIQ -> STELLA -> TDS3 -> RATAN ONE` flow.

## RATAN-to-LMS Liquidity-Management Feed

The RATAN and LMS interface source lists LOANIQ as a source system for the RATAN-to-LMS liquidity-management cashflow feed.

The associated loan feed categories are:

- `XQTXXX` — term loan
- `XQRXXX` — revolving loan
- `XQXXXX` — default loan

### Country Scope

The same source lists the LOANIQ scope as:

```text
UK, SG and HK
```

That source does not state a LOANIQ-specific SAIL-LMS exclusion.

## Onboarding and Routing Relevance

LOANIQ is treated separately from the strategic flow in workflow routing. Its SSI-hierarchy exception is uncertain because the onboarding checklist states `LOANID old logic` while other relevant sections state `LOANIQ`. See [[has-loanid-been-used-intentionally-in-the-ssi-hierarchy]].

The GUI SWIFT-query table identifies `LQ + Branch Code + Cashflow ID` as the LOANIQ Tag 20 format, but names BLADE/S2BX/CFETS as the SWIFT message source. This discrepancy requires confirmation.

## Settlement-Affirmation Scope

According to the derivative settlement-affirmation email-automation requirement, LoanIQ is listed as a configurable cashflow source for RATAN publishing criteria.

That requirement explicitly excludes SLT-CUST and Loan-related cashflows from the derivative settlement-affirmation email scope. This exclusion is stated for the affirmation-email scope and does not alter the onboarding, term-loan settlement-flow, FMRPSTELLA-LOANIQ stack, RATAN-to-LMS liquidity-feed, or high-value payment-control claims above.

## High-Value Payment Control

According to the high-value payment-control requirement, LOANIQ is treated as part of the [[fmrp]] flow.

It is therefore included in the FMRP/LOANIQ requirements for:

- USD-equivalent blotter visibility.
- Amount filtering.
- FMSGW STP/NSTP and user-attribution data.
- RATAN authorization-profile changes.

The high-value payment-control solution must align with [[razor]]. The requirement does not separately define LOANIQ-specific thresholds, interface variations, or affirmation-control behavior.

## Q4 2023 Testing

According to the 2023-Q4 Analysis, SIT started on 2023-11-08. Testing encountered an FMID mapping issue from TDS3, and manually updated sample messages were used to verify LMS and RAZOR integration while the issue remained under investigation.

Subsequent testing included:

- Storing the LOANIQ ledger id for the RATAN EOD process.
- Enabling the `is_netting` flag in an NSTP rule.
- Updating the source-system filter condition for STELLA cashflow-status updates.
- Updating the NSTP rule for structure trades.
- Aligning field values with the STELLA team.

The basic term-loan flow passed on 2023-11-24. This was evidence of progress, not proof of complete release readiness.

The source-stack-flow requirement separately reports that a netting resultant using the `FMRPSTELLA-LOANIQ` stack was sent to LMS with the same source value. It does not report a withdrawal-event test for LOANIQ cashflows.

## Related Pages

- [[ratan]]
- [[stella]]
- [[tds3]]
- [[tag-20-logic]]
- [[ssi-selection-hierarchy]]
- [[has-loanid-been-used-intentionally-in-the-ssi-hierarchy]]
- [[lms]]
- [[settlement-integration-static-data-readiness]]
- [[affirmation-email-scope-configuration]]
- [[fmrp]]
- [[fmsgw]]
- [[razor]]
- [[ratan-high-value-payment-control]]
- [[source-stack-flow-name-propagation]]
- [[netting-resultant-stack-derivation]]
- [[ratan-lms-liquidity-cashflow-feed]]
- [[lms-country-and-entity-scope]]