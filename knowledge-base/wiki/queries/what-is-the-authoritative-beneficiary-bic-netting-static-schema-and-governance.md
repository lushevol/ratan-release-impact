---
type: query
title: What Is the Authoritative Beneficiary BIC Netting Static Schema and Governance?
created: 2026-08-23
updated: 2026-08-23
tags: [beneficiary-bic, netting, static-data, maker-checker, governance]
related: [beneficiary-bic-netting, paystp-net-table]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Beneficiary BIC Netting/Beneficiary BIC Netting Demo.md"]
---
# What Is the Authoritative Beneficiary BIC Netting Static Schema and Governance?

## Question

What fields, ownership, maker-checker process, effective dating, synchronization controls, audit history, and data-quality checks govern Beneficiary BIC netting eligibility static?

## Evidence

The source proposes rule maintenance through `FMO_BR_MKR` and `FMO_BR_APR` and provides one example record with Entity Code, product-classification fields, and BIC.

It does not provide a complete schema or governance model. The reported operational context also identifies delayed UDF-table updates and missing PAYSTP_NET Table entries as risks, making static-data control material.

## Required decision outputs

- Complete eligibility-static schema and field definitions.
- Unique key and duplicate-record handling.
- Owner, maker, checker, and approver roles.
- Effective dates, expiry dates, and emergency-change process.
- Source-system synchronization and reconciliation controls.
- BIC validation and reference-data standards.
- Audit history, reporting, and operational monitoring.