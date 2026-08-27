---
type: project
title: 2025 Cash Settlement Roadmap
status: active
owner: ""
start_date: 2025-01-20
target_date: 2025-12-31
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, migration, roadmap, re-platforming]
related: ["cash-settlement-re-platforming", "cashflow-migration", "ratan", "murex-2-11", "aspire", "fmrp", "auto-netting", "standard-settlement-instructions", "pre-rule-migration", "ops-team", "dev-team"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/2025 Target.md"]
---
# 2025 Cash Settlement Roadmap

## Status Qualification

The project is marked `active` to represent its status in the March 2025 source, which identifies Sprint 3 as the current sprint. This is a historical status rather than confirmation that the project remained active through 2026. The latest production status requires verification.

## Objective

Move cash-settlement processing from [[murex-2-11]] into the Strategic Cash Settlements stack identified as [[ratan]], while supporting accounting, SSI behavior, operational readiness, product onboarding, and transitional integrations.

## Scope

The source associates the roadmap with:

- UK cashflow migration, including Precious Metals
- Three geographic cashflow-migration tranches
- Accounting integration with [[aspire]]
- CN LNBR
- UK Prime PM and Rates
- CN CCS and CFETS-related work
- Hefei Branch Rollout
- UK E-Precious and PM NDF
- Global Rates FRA
- FXO
- Prime CPN
- FXU
- Swap Agent Day2
- [[auto-netting]]
- Strategic One Stop SSI stamping
- [[iso-20022-mx]] onboarding
- Keystone

Several initiatives are listed without dates, owners, dependencies, or acceptance criteria.

## Migration Tranches

### Tranche 1

Targeted for Q2 2025:

- BANGKOK
- TAIPEI
- OBU TAIPEI
- HONG KONG
- SCS HK

Associated work includes static-data setup, accounting design and implementation, UAT, reconciliation, SSI selection, Vostro SI Settlement Means, and dashboard and blotter coverage.

### Tranche 2

Targeted for Q2 2025:

- MAURITIUS
- DUBAI
- JAKARTA
- MANILA
- TOKYO
- JOBURG
- PHILIP FCU
- DIFC
- NEWYORK

The source does not explain whether Tranche 2 is concurrent with or dependent on Tranche 1.

### Tranche 3

Targeted for Q3 2025:

- JERSEY_BR

## Dependencies

- Murex rules such as suppression and netting must be reviewed and configured in RATAN as part of [[pre-rule-migration]].
- NDS Auto Netting for SG is described as dependent on Murex.
- RATAN-to-Murex release-status synchronization remains part of sprint work.
- SSI selection and stamping behavior must align across cashflows and trades.
- Tranche 1 requires static data, accounting, UAT, reconciliation, and Vostro settlement-means updates.
- The [[ops-team]] and [[dev-team]] are expected to review UAT cases and participate more closely.

## Risks

- Roadmap targets may be mistaken for verified production deliveries.
- The Murex pre-rule inventory and RATAN parity status are not documented.
- Tranches 1 and 2 share a Q2 target without stated sequencing.
- Several annual initiatives have no dates or owners.
- The project includes production database-growth and performance concerns without quantitative results.
- Work item `6473089` may affect [[maker-checker-segregation]], but its control rationale is not documented.
- The UK Prime PM milestone contains conflicting apparent go-live dates, tracked in [[what-was-the-uk-prime-pm-go-live-date]].

## Reported Delivery Evidence

The source labels seven Sprint 2 items as `RELEASED`, including a 5,000-cashflow load capability, dashboard auto refresh, DB usage enhancement, an NSTP display change, an ND IRS trade lookup fix, a Stella Prime SI hierarchy change, and BIC Netting for Prime cashflow.

These item-level assertions do not demonstrate completion of the overall roadmap.

## Success Criteria Requiring Confirmation

The source does not define project-wide success criteria. Useful criteria to obtain include:

- Production migration and sign-off for each entity and tranche
- Verified parity for suppression, netting, and other pre-rules
- Reconciled accounting outputs through Aspire
- Validated SSI selection and stamping behavior
- UAT sign-off from business, OPS, and Dev participants
- Measured throughput, latency, reliability, and database growth
- Retirement or formally approved long-term coexistence of Murex dependencies

## Retrospective

No completion retrospective is available because the source does not establish that the project was completed.