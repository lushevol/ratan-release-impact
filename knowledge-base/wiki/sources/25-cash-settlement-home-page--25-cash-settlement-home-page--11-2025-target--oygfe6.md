---
type: source
title: 2025 Cash Settlement Target
authors: []
year: 2025
url: "https://confluence.global.standardchartered.com/display/FMRP/2025+High+Level+Backlog"
venue: "Standard Chartered Confluence"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, roadmap, migration, re-platforming, 2025]
related: [cash-settlement-2025-roadmap, cash-settlement-re-platforming, cashflow-migration, ratan, murex-2-11, aspire, fmrp, auto-netting, standard-settlement-instructions, ssi-selection-hierarchy, ssi-stamping, pre-rule-migration, maker-checker-segregation, iso-20022-mx, what-was-the-uk-prime-pm-go-live-date]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/2025 Target.md"]
---
# 2025 Cash Settlement Target

## Summary

This internal roadmap records planned cash-settlement migrations, integrations, product onboarding, operational improvements, and sprint work for 2025. It identifies [[ratan]] as the strategic target for cash-settlement processing migrated from [[murex-2-11]] and divides the broader [[cashflow-migration]] into three geographic tranches.

The plan extends beyond migration. It includes accounting integration with [[aspire]], FMRP business initiatives, Auto Netting, SSI-related work, ISO 20022 MX onboarding, branch rollout, new-product support, database housekeeping, performance testing, and operational readiness.

The document appears to represent a point-in-time plan maintained during Sprint 3 of Q1 2025, approximately 3–14 March 2025. It must not be treated as evidence that every annual target or milestone was delivered.

## Evidence Status

The source mixes several kinds of status:

- Annual targets without dates
- Dated or quarter-level milestones
- Sprint commitments
- Checked work items
- Items explicitly labeled `RELEASED`
- Undated backlog entries

The `RELEASED` label supports a release claim only for the individual item carrying that label. Checked boxes without that label may indicate completion within the planning document, but the source does not define whether that means development completion, UAT completion, deployment, or production release.

No release notes, deployment records, UAT sign-offs, production metrics, named owners, or acceptance criteria accompany the status assertions.

## Strategic Direction

The roadmap describes a transition from [[murex-2-11]] to the Strategic Cash Settlements stack, identified as [[ratan]]. Related work includes static-data setup, accounting, SSI behavior, UAT, reconciliation, dashboard and blotter coverage, release-status synchronization, performance, and production database management.

The presence of Murex-dependent work and RATAN-to-Murex status updates indicates a coexistence period rather than an immediately complete one-way replacement.

## Yearly Target

- UK Cashflow migration from Murex 2.11 to RATAN
- Continuous Migration of Murex 2.11 cash settlements into Strategic Cash Settlements stack (RATAN) with 3 tranches - Tranche 1: BANGKOK, TAIPEI,OBU TAIPEI, HONG KONG, SCS HK - Tranche 2: MAURITIUS, DUBAI, JAKARTA, MANILA, TOKYO, JOBURG, PHILIP FCU, DIFC, NEWYORK - Tranche 3: JERSEY_BR
- Accounting with integration to Aspire
- FMRP business initiative - CN LNBR - UK Prime migration for PM and Rates - CN CCS Trade migration
- Hefei Branch Rollout
- Prime CPN
- FXO
- Swap Agent Day2
- FXU
- Auto Netting
- Strategic One Stop SSI stamping
- ISO 20022 MX onboarding
- Keystone

## Milestones

| Date | Milestone |
| --- | --- |
| 20 Jan 2025 | 430500 UK Cashflow Migration Go live (Murex Cash Settlements Migration 2024 including Precious Metals) |
| 22 Feb 2025 | 6469299 CN LNBR Go live (RATAN is Ready) |
| 3 Mar 2025 | 6469316 F2B: UK Prime PM Go Live (24 Feb Go Live) |
| 8 Mar 2025 | 6469344 F2B: CN CCS [CFETS 08 Mar] & Trade Migration [Aug] |
| Apr 2025 | F2B: UK Prime Rates Go Live |
| Apr 2025 | Hefei Branch Rollout |
| Q2 2025 | F2B: UK E-Precious +** PM NDF** + Trade Migration |
| Q2 2025 | Tranche 1 cashflow migration |
| Q2 2025 | Tranche 2 cashflow migration |
| Q2/Q3 2025 | F2B: Desk and Entity Setup (HK, TW, IN, LK, BD, SG, MY, TH, VN, UK) |
| Q3 2025 | F2B: Global Rates New Product (FRA) |
| Aug 2025 | CN CCS Trade Migration |
| Oct 2025 | F2B: FXO Go Live |
| Q3 2025 | Tranche 3 cashflow migration |
| | Prime CPN |
| | FXU |
| | Swap Agent Day2 |
| | Auto Netting |
| | Strategic One Stop SSI stamping |
| | Keystone |

The CN CCS entry contains two distinct events: a CFETS go-live associated with 8 March 2025 and a trade migration planned for August 2025. These should be tracked separately.

The UK Prime PM entry contains both 3 March 2025 and 24 February 2025 as apparent go-live dates. The canonical production date remains unresolved in [[what-was-the-uk-prime-pm-go-live-date]].

## Q1 2025 Sprints

| | Sprint | Sprint-0 (1.20-1.31) | Sprint-1（2.3-2.14) | Sprint-2 (2.17-2.28) | Sprint-3(3.3-3.14) (Current Sprint) | Sprint-4(3.17-3.28) | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | UK Post Care & Enhancement | F2B: Drop 4.0: CN Loan Depo Go Live | - [x] (RELEASED) Load 5k cashflows | 7177438 Data entitlement for TW/CN | | |
| 2 | | | UK Post Care - | - [x] (RELEASED) Dashboard auto refresh | 7477339 SSI Selection hierarchy - Tranche 1 to follow UK | | |
| 3 | | | Tranche 1 static data setup | - [x] (RELEASED) DB Usage enhancement | 6469344 CN CCS Go live [CFETS] | | |
| 4 | | | Tranche 1 Accounting design | - [x] (RELEASED) NSTP not displayed on cashflows | 6473089 Allow user who did netting to act as Checker | |
| 5 | | | | - [x] (RELEASED) ND IRS issue - Trade ID looked up RAZOR trade | 6472953 Enable NDS Auto Netting for SG (Dependency on Murex) | |
| 6 | | | | - [x] (RELEASED) SI hierarchy to follow new model for Stella Prime payments | Moving H1 entities to H2 model - Code & Config [32 MD] | |
| 7 | | | | - [x] (RELEASED) 7489431 [BIC Netting] Enable for Prime cashflow | 7147811 Tranche 1 - Update Vostro SI Settlement Means values | | |
| 8 | | | | - [x] UK Prime Rates Performance Testing | 7506417 Add entities to Dashboard & Blotter | | |
| 9 | | | | - [x] Tranche 1 UAT support on data loading/recon | 7402405 RATAN->Murex RELEASE Status Update Issue Fix - by batch | | |
| 10 | | | | | 7523847 [Trade SSI Stamping] Sync Up UK Prime trade SSI stamping best match with cashflow | | |
| 11 | | | | 7378233 MT605 Issue | | |
| 12 | | | | Tranche 1 Accounting implementation/UAT | | |
| 13 | | | | 7402457 housekeeping for Prod DB - Excessive growth in database space | | |
| 14 | | | | 7177927 fileIt setup | | |

## Reported Sprint 2 Releases

The source explicitly labels the following items as `RELEASED`:

- Load 5k cashflows
- Dashboard auto refresh
- DB Usage enhancement
- NSTP not displayed on cashflows
- ND IRS issue - Trade ID looked up RAZOR trade
- SI hierarchy to follow new model for Stella Prime payments
- `7489431` BIC Netting enabled for Prime cashflow

These assertions apply only to the named items. They do not establish completion of [[ratan]], [[auto-netting]], a migration tranche, or the full [[cash-settlement-2025-roadmap]].

## Migration Scope

The planned [[cashflow-migration]] scope is grouped as follows:

- **Tranche 1, targeted for Q2 2025:** BANGKOK, TAIPEI, OBU TAIPEI, HONG KONG, SCS HK
- **Tranche 2, targeted for Q2 2025:** MAURITIUS, DUBAI, JAKARTA, MANILA, TOKYO, JOBURG, PHILIP FCU, DIFC, NEWYORK
- **Tranche 3, targeted for Q3 2025:** JERSEY_BR
- **Separate F2B desk and entity setup, targeted for Q2/Q3 2025:** HK, TW, IN, LK, BD, SG, MY, TH, VN, UK

The source does not state whether Tranches 1 and 2 were intended to run concurrently or sequentially.

## Operational Warnings

The source records the following warnings verbatim:

1. Review pre rules in Murex like suppression, netting, which are all supposed to be setup in RATAN
2. UAT cases should be reviewed more carefully from OPS/Dev team, we should get ourselves closely involved in the progress

These warnings identify [[pre-rule-migration]] and UAT participation by the [[ops-team]] and [[dev-team]] as operational-readiness concerns.

## Key Dependencies and Risks

### Rule parity

Suppression, netting, and other Murex pre-rules were expected to be configured in RATAN. The source does not inventory those rules or confirm parity testing.

### SSI behavior

Work involving [[standard-settlement-instructions]] includes the Tranche 1 selection hierarchy, Vostro SI Settlement Means, Stella Prime payment hierarchy, trade SSI stamping, and Strategic One Stop SSI stamping.

### Transitional coexistence

NDS Auto Netting for SG is explicitly dependent on Murex. Another item addresses batch-level RATAN-to-Murex release-status updates. The intended duration and end state of these dependencies are not provided.

### Operational control

Work item `6473089` proposes allowing a user who performed netting to act as Checker. The source does not explain whether this complies with [[maker-checker-segregation]], applies only to limited cases, or retains another approval control.

### Capacity and maintainability

The roadmap addresses loading 5,000 cashflows, UK Prime Rates performance testing, DB usage, dashboard refresh, and excessive production database growth. It does not provide measurable throughput, latency, reliability, or storage results.

## Limitations

The source does not provide:

- Named owners or deciders
- Formal acceptance criteria
- Detailed architecture
- Actual SSI selection rules
- A Murex pre-rule inventory
- Production deployment evidence
- UAT sign-off records
- Performance measurements
- Incident or defect metrics
- Current status after March 2025
- Definitions for CPN, FXO, FXU, NDS, NSTP, ND IRS, PM, PM NDF, CN LNBR, CN CCS, H1/H2 model, `fileIt`, or SCS HK