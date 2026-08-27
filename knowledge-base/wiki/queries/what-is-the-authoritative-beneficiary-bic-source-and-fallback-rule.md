---
type: query
title: What Is the Authoritative Beneficiary BIC Source and Fallback Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [beneficiary-bic, netting, data-governance, murex, ratan]
related: [beneficiary-bic-netting, paystp-net-table]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Beneficiary BIC Netting/Beneficiary BIC Netting Demo.md"]
---
# What Is the Authoritative Beneficiary BIC Source and Fallback Rule?

## Question

Which system is authoritative for the Beneficiary BIC used by Beneficiary BIC Netting, and what must happen when that BIC is missing, invalid, stale, or inconsistent across sources?

## Why this is open

The proposal makes Swift BIC the primary Ratan UDT criterion while identifying missing Swift BIC capture in [[murex]] as an existing operational problem. It also includes an unclear reference to BIC, `MXR`, and [[sci]].

The source does not define whether Ratan should source BIC from Murex, SCI, MXR, a Ratan static, or another source. It provides no fallback, remediation, precedence, validation, or ownership rule.

## Required decision outputs

- Canonical BIC source and permitted fallback sources.
- BIC formatting and validation standard.
- Precedence rule for conflicting values.
- Missing-BIC behavior: block, gross-settle, exception-route, or another outcome.
- Data-remediation owner and service-level expectation.
- Audit and reconciliation requirements.