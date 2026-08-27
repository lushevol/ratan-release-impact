---
type: concept
title: RATAN Netting Rule Check
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, settlement, netting, eligibility, pending-netting]
related: [ratan, auto-netting-rule-configuration, nds-netting, irs-fix-leg-floating-leg-netting, ccil-netting, beneficiary-bic-netting, inter-entity-netting, netting-mechanism-precedence]
sources: ["RATAN - 51358/RATAN/RATAN -Core Function/RATAN-Settlement  4_Netting Rule Check.md"]
---
# RATAN Netting Rule Check

A RATAN netting rule check is the classification and validation activity applied to cashflows in `Pending Netting` before they are consolidated through an applicable netting path.

The available source identifies NDS, IRS, configured auto-netting rules, CCIL, Beneficiary BIC, bilateral, and inter-entity netting as categories considered by this function. It does not establish whether these paths are mutually exclusive, evaluated in sequence, or governed by a complete common decision tree.

## Explicit precedence

[[beneficiary-bic-netting]] is stated to take priority over bilateral manual netting. No broader priority model is documented.

## Inter-entity validation

For [[inter-entity-netting]], the rule check includes currency, value-date, amount, opposite-direction, and reciprocal booking-entity/counterparty mapping checks. See [[inter-entity-cashflow-pre-match]].

## Scope limitations

This concept does not treat NDS, IRS, CCIL, or inter-entity rules as interchangeable. Each has distinct stated behavior and unresolved eligibility details. The full precedence model remains tracked in [[netting-mechanism-precedence]].