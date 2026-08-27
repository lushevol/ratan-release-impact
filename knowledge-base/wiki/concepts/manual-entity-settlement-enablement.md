---
type: concept
title: Manual-Entity Settlement Enablement
created: 2026-08-22
updated: 2026-08-23
tags: [settlement, manual-entities, ratan, murex, settlement-day-2, cash-settlement, entity-configuration, static-data, uat]
related: [ratan, cash-settlement-home-page, settlement-day-2, cashflow-auto-netting, settlement-suppression-exceptions, manual-entity-static-data-onboarding, ratan-cashflow-lifecycle-state-machine, cashflow-lifecycle-versioning, cashflow-suppression-rule, qatar-slate-one-llc-doh-gbs, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--1lzh700]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/01 Enabling Settlement for Manual Entities.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/003 QATAR SLATE ONE LLC DOH(GBS).md"]
---
# Manual-Entity Settlement Enablement

## Definition and evidence boundaries

The existing on-disk version describes manual-entity settlement enablement as the controlled migration of cashflows from manual payment processing to Ratan-managed settlement. It states that the source concerns entities that sent cashflows from Murex 2.11 into Ratan while cashflow settlement was suppressed.

The newly generated version identifies the topic as the apparent subject of a Settlement Day 2 functional requirement. It states that, based on the filename alone, the requirement concerns allowing settlement processing for a category of entities described as manual.

The newly generated version further characterizes manual-entity settlement enablement as covering the configuration and processing needed to settle cashflows for entities managed through manual settlement procedures.

These versions differ in their available source evidence:

- The existing on-disk version presents detailed scope, controls, entities, and rollout information attributed to the source.
- The newly generated version states that detailed requirements were not available from its source extraction and derives the concept solely from [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--1lzh700]].
- The newly generated UAT-source version records a Qatar-specific suppression path for [[qatar-slate-one-llc-doh-gbs]].

## Enablement model

According to the existing on-disk version, enablement is selective: it permits eligible cashflows to proceed through settlement, but does not remove all NSTP, suppression, accounting, Swift, or downstream-feed controls.

The existing on-disk version defines the implementation question as whether each cashflow independently satisfies:

1. Entity scope and settlement eligibility.
2. Required static-data availability.
3. Applicable NSTP rules.
4. Cashflow-suppression exceptions.
5. Swift and accounting controls.
6. Downstream LMS requirements.

Under that version's interpretation, this layered model prevents enablement from being treated as universal payment release.

## Processing boundaries

The existing on-disk version distinguishes settlement enablement from the following controls and processes:

- **Cashflow suppression:** A cashflow may remain suppressed because of entity, counterparty, currency, product, or internal-deal rules.
- **Swift generation:** Membership in `STRATEGIC_FM_LIST` controls whether Swift generation is considered; `SLATE_QFC` remains suppressed and is excluded.
- **EBBS accounting:** Accounting requires separate bridge-account, posting-branch, transaction-code, and timezone configuration.
- **LMS delivery:** LMS feed eligibility is independent of settlement suppression.
- **SSI stamping:** Manual entities follow the UK SSI model and do not belong in `NON_UK_ENTITY_LIST`.
- **Lifecycle processing:** Rule changes can affect cashflow lifecycle states and the treatment of previously suppressed or pending cashflows.

## Entity scope

The existing on-disk version identifies the active scope as:

- BAHRAIN
- DOHA
- KENYA
- ZAMBIA
- UGANDA
- TANZANIA
- GHANA
- NIGERIA
- SRI LANKA
- FCBUSLANKA
- HANOI
- KARACHI
- DHAKA

It identifies `SLATE_QFC` as a deliberate exception: it remains cashflow-suppressed while still feeding LMS.

According to the existing on-disk version, Botswana is historical scope only and was replaced by Qatar after the Botswana branch closure.

## Qatar SLATE UAT suppression path

The newly generated version based on the UAT confirmation for [[qatar-slate-one-llc-doh-gbs]] describes a special path:

- The `SLATE` cashflow is intended to be cashflow suppressed.
- Consequently, the remaining settlement static data is described as unnecessary.
- Only the [[cashflow-suppression-rule]] is required.

This UAT statement should be treated as a case-specific exception or negative-path interpretation within the enablement workflow. It does not replace the normal static-data requirements for other manual entities or cashflows.

The exact meaning of “rest of static” and the formal conditions and identifier for the Cashflow Suppression rule remain unresolved. See [[what-static-data-is-skipped-when-cashflow-is-suppressed]].

## Rollout

The existing on-disk version groups the work into two broad tranches:

| Tranche | Entities |
|---|---|
| Tranche 1 | Bangladesh, Tanzania, Sri Lanka, Pakistan, Kenya, Vietnam, and Zambia |
| Tranche 2 | Nigeria, Ghana, Qatar, Bahrain, and Uganda |

That version states that the source tracks UAT, CPT, static-data signoff, and post-go-live issues, but does not establish that every entity reached production go-live.

## Unconfirmed behavior

The newly generated version states that its available source evidence does not establish:

- what qualifies an entity as manual;
- whether enablement is global, product-specific, environment-specific, or user-specific;
- whether configuration, a user interface, an API, or a database record controls enablement;
- whether approval, authorization, audit, or segregation-of-duties controls apply;
- which settlement statuses or workflows become available;
- how the capability interacts with automated settlement, netting, DVP, messaging, or accounting;
- how failure, disablement, or rollback is handled.

Per the newly generated version, the concept must not be generalized to automated entities or to specific systems such as Ratan without supporting source text.