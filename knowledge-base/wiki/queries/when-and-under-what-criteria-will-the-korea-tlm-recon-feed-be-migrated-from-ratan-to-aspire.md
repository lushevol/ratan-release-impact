---
type: query
title: When and Under What Criteria Will the Korea TLM Reconciliation Feed Be Migrated from RATAN to Aspire?
created: 2026-08-23
updated: 2026-08-23
tags: [Korea, TLM, RATAN, Aspire, migration, reconciliation, open-question]
related: [korea-accounting-reconciliation, ratan, tlm, aspire]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Korea Accounting Recon - RATAN- TLM.md"]
---
# When and Under What Criteria Will the Korea TLM Reconciliation Feed Be Migrated from RATAN to Aspire?

## Question

The requirement describes the RATAN-to-TLM API as an interim solution and references Feature `11898201` for a future `OLTP > ASPIRE > TLM` route. The source does not define the migration criteria or decommissioning plan for the interim feed.

## Evidence

The stated rationale is that Aspire cannot meet the Korea release timeline. The future feature is titled `TLM-KR-Onboard the recon from OLTP>ASPIRE>TLM (Decomm from RATAN to TLM)`.

## Required resolution

Confirm the target API and data contract, ownership of reconciliation records, cutover and rollback criteria, parallel-run requirements, production acceptance evidence, and the conditions under which the RATAN-to-TLM integration may be decommissioned.