---
type: entity
title: PAYSTP_NET
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, configuration, static-data]
related: [beneficiary-bic-netting, bic-net-eligibility-flag, ratan, murex, sci]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Beneficiary BIC Netting.md"]
---
# PAYSTP_NET

`PAYSTP_NET` is the configuration table used to determine or support eligibility for Beneficiary BIC netting.

## Role

The table is referenced by both the Murex BAU process and the proposed [[entities/ratan]] workflow. Its fields are expected to support filtering by entity, value date, counterparty, and other settlement attributes.

The requirement states that `PAYSTP_NET` must be configurable by users. This is intended to reduce the risk that newly onboarded give-up counterparties are omitted from BIC-netting eligibility because static data is not updated promptly.

## Relationship to Beneficiary BIC data

The Beneficiary BIC itself is sourced from [[entities/sci]], using the BIC where `mediumUsage='MXR'`. The source does not define precedence when `PAYSTP_NET` and SCI contain conflicting or incomplete data.

## Operational risks

Incorrect or delayed `PAYSTP_NET` configuration can result in:

- Counterparties being excluded from BIC netting.
- Settlement amount mismatches.
- Cashflows being manually netted through competing queues.
- Suppression and manual payment through OSCAR.
- Increased operational and reconciliation risk.

## Governance questions

The source does not specify the configuration owner, approval process, audit history, effective-dating model, or validation rules for user changes. These controls should be defined before implementation.