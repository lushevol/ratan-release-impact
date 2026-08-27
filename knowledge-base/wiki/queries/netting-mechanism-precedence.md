---
type: query
title: What Is the Complete RATAN Netting Mechanism Precedence?
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, netting, precedence, eligibility, settlement]
related: [ratan-netting-rule-check, beneficiary-bic-netting, nds-netting, irs-fix-leg-floating-leg-netting, ccil-netting, inter-entity-netting, auto-netting-rule-configuration]
sources: ["RATAN - 51358/RATAN/RATAN -Core Function/RATAN-Settlement  4_Netting Rule Check.md"]
---
# What Is the Complete RATAN Netting Mechanism Precedence?

The available source lists seven RATAN netting categories but documents only one ordering: Beneficiary BIC Netting has higher priority than bilateral manual netting.

## Questions to resolve

- Are the listed categories mutually exclusive or may one cashflow satisfy multiple paths?
- What is the evaluation order for NDS, IRS, configured auto-netting rules, CCIL, Beneficiary BIC, bilateral, and inter-entity netting?
- Are any categories hard overrides based on product, market, counterparty, or legal entity?
- What status, audit record, or exception is produced when rules conflict?

A complete precedence matrix is needed before the list can be treated as an implementation decision tree.