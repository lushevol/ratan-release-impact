---
type: concept
title: Cashflow Suppression Rules
created: 2026-08-22
updated: 2026-08-23
tags: [cashflow, suppression, business-rules, migration, ratan, static-data]
related: [murex, ratan, stella, cashflow-status-handling, strategic-routing, nstp-rule-routing, cashflow-amendment-maker-checker-control, receive-only-swift-suppressed-cashflow, swift-suppressed-lms-feed-contract, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - FXO.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data.md"]
---
# Cashflow Suppression Rules

Cashflow suppression rules are configurable predicates over cashflow-level attributes that prevent selected cashflows from proceeding through normal downstream settlement processing.

The Static Data source assigns rule ownership to `FMO_BR_MKR` and `FMO_BR_APR` and requires Maker/Checker control for rule creation, update, and deletion.

## Rule Coverage

The Static Data source's documented 2024 Drop 2 inventory includes rules covering:

- Legal-entity and counterparty combinations.
- Booking portfolios such as `AGENCY_BARCLAYS`, `AGENCY_BKCREDIT`, `AGENCY_BKMACRO`, `AGENCY_EASTFORT`, `AGENCY_SCBHK`, and `AGENCY_SINOPAC`.
- Murex 2.11 counterparty labels.
- `XVA-Premium` and `Yearly-PL-Sweep` trade purposes.
- Port-to-port cashflows where booking and counterparty FMIDs are equal.
- Non-FMRP entities, with explicit exclusions and `Trade_Original_Source_System_Name!=LOANIQ`.
- `NonEcoAmend` reversal and rebook cashflows.
- No-settlement products `CDS_SCH`, `Loan_ACBS_Rep`, and `Loan_EBBS_Rep`.

## Murex-to-RATAN Requirement

The FXO checklist states that the [[murex]]-to-[[ratan]] cashflow interface contains filter logic that excludes auto-suppression counterparties. Corresponding RATAN suppression rules must be configured so that the same cashflows can be suppressed for [[stella]] flows.

This FXO checklist requirement concerns preserving source-side suppression behavior during migration. It does not establish that all Murex filters should be reproduced without review.

The FXO checklist also associates entity whitelists with cashflow suppression and with routing flows either to [[razor]] or to RATAN. Suppression and routing should therefore be treated as distinct rule concerns.

## Migration Scope

The Static Data source explicitly states that no Swift Suppression Rule is required for cashflow migration Day 1. This does not establish that Swift suppression is unnecessary for later migrations or business-as-usual processing.

Existing behavior for Swift-suppressed receipts is covered by [[receive-only-swift-suppressed-cashflow]] and [[swift-suppressed-lms-feed-contract]].

## Rule Design and Governance

A complete rule design should distinguish:

- Suppression from routing.
- Counterparty rules from booking-entity rules.
- Global rules from branch- or product-specific rules.
- Rule precedence when whitelist and suppression conditions overlap.
- Operational override and audit requirements.

The Static Data source notes that the rules contain long FMID and shortcode lists, inconsistent labels, and scientific-notation identifiers. An executable implementation should therefore rely on an authoritative export with ownership, effective dates, version history, and conflict-resolution semantics.

The FXO checklist does not enumerate the affected counterparties or identify the authoritative rule owner.