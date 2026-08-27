---
type: concept
title: Cashflow Accounting Stamping
created: 2026-08-23
updated: 2026-08-23
tags: [accounting, cashflow, static-data, stamping, cash-settlement]
related: [ebbs, aspire, settlement-integration-static-data-readiness, cashflow-accounting-eligibility, accounting-feed-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Accounting & Recon.md"]
---

# Cashflow Accounting Stamping

## Definition

Cashflow accounting stamping is the planned association of cashflows with underlying accounting-relevant static data before accounting entries are generated.

The source describes this as:

> Accounting stamping ( cashflow VS underlying static data)

## Scope

The requirement applies separately to:

- Aspire accounting for Hong Kong and Taiwan.
- EBBS accounting for the United Kingdom, Singapore, and India.

The source does not identify the required attributes or source-of-truth system. Possible accounting attributes must not be inferred as confirmed requirements.

## Dependency

Accounting-entry generation depends on the availability and quality of the underlying static data. The source marks `EBBS Account` static data as not requiring new build, but does not confirm its completeness, ownership, or readiness.

This is related to [[settlement-integration-static-data-readiness]], but the source does not establish that the same controls or data model apply.
