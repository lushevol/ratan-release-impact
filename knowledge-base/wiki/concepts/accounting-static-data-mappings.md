---
type: concept
title: Accounting Static Data Mappings
tags: [payment-accounting, static-data, reference-data, ebbs, ratan]
related: [ebbs-payment-accounting-integration, ebbs, ratan, razor, sci, murex]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - EBBS Accounting.md"]
---
# Accounting Static Data Mappings

Accounting generation depends on reference data maintained or queried by RATAN and related systems.

## Mapping categories

- Entity FMID to posting branch.
- Posting branch and debit/credit direction to transaction code.
- Entity FMID to eBBS Bridge account.
- Non-ISO currency label to ISO currency code.
- CIS external codes used by the UK accounting-suppression exception.
- Narrative inputs from trade, cashflow, counterparty, portfolio, and FXU data.

The source includes mappings for entities across China, Singapore, India, Malaysia, the United Kingdom, Germany, Mauritius, the United Arab Emirates, Indonesia, the Philippines, Japan, South Africa, the United States, Nepal, Saudi Arabia, Egypt, and Hong Kong.

## Currency rules

The source gives special treatment to `CNH`. For Singapore CNH, the original `CNH` value is retained. For several countries, including the United Kingdom and Hong Kong, CNH is also retained; for specified country codes such as CN, MY, IN, and DE, conversion to ISO `CNY` is performed.

## Governance risk

The requirement does not identify the authoritative system of record, effective-dating model, approval owner, or reconciliation process for these mappings. Historical corrections and strikethrough values in the source make controlled reference-data governance essential.