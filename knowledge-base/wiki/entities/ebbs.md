---
type: entity
title: EBBS
created: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/2026 Entity Onboarding - new branch setup in Vietnam.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - FXO.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - Korea Cashflow Migration.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - HK & TW.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - Prime Day 2.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/UBER regression - round 2.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Accounting & Recon.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - EBBS Accounting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Korea Accounting Recon - RATAN- TLM.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS)/AutoDVP UAT testing.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities/04 Go live checklist for Manual Entities-Overall.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall/Tranche1.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall/Tranche2.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Nostro SSI/Nostro Static Golden Source.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Settlement Accounting for Aspire Tech design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - OLTP.md", "RATAN/RATAN -Interfaces/Ratan and EBBS 14147.md"]
tags: ["accounting", "settlement", "system", "integration", "downstream-system", "ebbs", "cash-settlement", "fmrp", "regression", "ratanone", "payment-accounting", "accounting-platform", "Keystone", "payment-processing", "posting", "bridge-account", "Nostro", "transaction-message", "payment-platform", "notification", "rta", "auto-dvp", "reference-data", "configuration", "tranche-1", "ledger", "nostro-static-data", "reconciliation", "feed", "unverified", "ratan"]
related: ["vietnam-ifc-branch", "ratan", "solace", "settlement-accounting", "entity-branch-onboarding", "aspire", "fmrp", "cashflow-accounting-release", "cashflow-migration", "korea-settlement-accounting", "korea", "keystone-hk", "cash-settlement-accounting-routing", "f2b-hk-tw-milestone-checklist", "fmrp-prime-uk-uat-drop-2", "reconciliation", "ratan-one", "ebbs-settlement-accounting", "regression-failure-triage", "cashflow-fail-and-reinstatement", "bcdf", "bridge-account", "cashflow-accounting-stamping", "entity-based-eod-feeding", "single-payment-realtime-accounting-feeding", "cashflow-accounting-eligibility", "accounting-feed-reconciliation", "keystone", "payment-accounting-flow", "nostro-account-scope", "ebbs-payment-accounting-integration", "accounting-posting-lifecycle", "oltp", "ebbs-accounting-message-mapping", "korea-accounting-reconciliation", "auto-dvp", "ebbs-rta-notification", "auto-dvp-ebbs", "ebbs-rta-notification-validation", "ebbs-settlement-posting-configuration", "manual-entity-go-live-static-data-controls", "ebbs-accounting-configuration", "go-live-readiness-for-manual-entity-settlement", "ebbs-posting-configuration", "what-are-the-final-qatar-release-cutoff-and-ebbs-configurations", "nostro-static-golden-source", "nostro-account-taxonomy", "nostro-record-composite-uniqueness", "razor", "fileit", "accounting-feed-withdrawal-as-reversal", "value-date-accounting-feed-cutoff", "oltp-accounting", "ebbs-vs-oltp-accounting-flow", "accounting-task-retry-exclusion", "cash-settlement-accounting-service", "ratan-ebbs-accounting-feed", "what-is-the-canonical-ratan-to-ebbs-interface-contract"]
updated: 2026-08-24
---

# EBBS

EBBS (also rendered as `eBBS` and `Ebbs`) has documented roles in cash-settlement accounting, posting configuration, Nostro ledger-account reference data, settlement-accounting integration, and the [[ratan]] accounting-feed interface.

## Identity and naming

The RATAN interface overview uses `EBBS` in its title and opening description, `eBBS` in narrative text, and `Ebbs` in its data-flow line. This page uses **EBBS** as the provisional canonical name.

The authoritative product name and ownership require confirmation.

## Accounting and settlement-accounting roles

### Korea OLTP baseline and retry handling

The *Korea Accounting - OLTP* technical design describes EBBS as the existing downstream settlement-accounting target and the baseline for the Korea OLTP design.

According to that design:

- EBBS requests are held in `request_info` as EBBS-format JSON.
- When no response is received, or when responses are `TXN99999` or `TEC0004`, the EBBS retry process resends messages three times at four-minute intervals.
- Korea OLTP tasks are explicitly excluded from this retry policy.

### Proposed settlement-accounting feed

The *Settlement Accounting for Aspire Tech design* names EBBS as the target of event-driven feed generation in its proposed settlement-accounting design.

That design does not establish whether EBBS is:

- a downstream system;
- a feed format or channel; or
- another name for [[aspire]].

It also leaves the Aspire-versus-EBBS database representation unresolved.

## RATAN accounting-feed interface

The RATAN interface overview identifies EBBS as a downstream accounting-message consumer. [[ratan]] is intended to feed payment-accounting entries to EBBS in real time through [[solace]], using JSON messages.

Within [[ratan-ebbs-accounting-feed]], EBBS is the receiving system in the stated route:

```text
Ratan → Central Solace → eBBS
```

The source associates EBBS with a multi-location scope, although its supplied list mixes countries, cities, and possible booking entities. It does not establish EBBS deployment topology, supported entities, interface ownership, or production status.

### Open contract questions

The RATAN interface overview does not document:

- a message schema;
- Solace destination configuration;
- delivery semantics;
- a reconciliation process; or
- operational support details.

See [[what-is-the-canonical-ratan-to-ebbs-interface-contract]] and [[what-is-the-authoritative-ebbs-country-or-booking-entity-scope]].

## Accounting and posting configuration

The Tranche 2 manual-entity settlement checklist identifies EBBS as the accounting and posting system used for bridge-account and transaction-code configuration.

The checklist lists bridge accounts and posting branches or codes for:

- Bahrain
- Qatar
- Uganda
- Ghana
- Nigeria

The checklist explicitly states that Qatar requires double confirmation. The recorded Qatar account must therefore not be treated as final approval. See [[ebbs-posting-configuration]].

## Role in the Nostro model

EBBS is the ledger-account domain used to consolidate Nostro entries from multiple systems or departments for applicable countries.

The proposed NAMS/RDM mapping includes `Ledger Account Number_EBBS`, with example value `HK7251800192082CNY238`.

The Nostro static-data source states that RAZOR stores an EBBS account number in `TABLE#DATA#SITRN_DBF`.

A key unresolved question in the Nostro model is whether one Nostro account can map to multiple EBBS ledger accounts. The centralized model must define the cardinality, ownership, and uniqueness implications of that relationship.
