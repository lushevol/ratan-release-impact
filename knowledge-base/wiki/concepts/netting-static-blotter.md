---
type: concept
title: Netting Static Blotter
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, static-data, manual-rule, blotter]
related: [beneficiary-bic-netting, netting-key-eligibility, netting-resultant-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/03 Beneficiary BIC Netting.md"]
---
# Netting Static Blotter

The netting static blotter is the operational surface identified in the Beneficiary BIC Netting requirements for creating manual netting rules.

A manual rule that is live is expected to place cashflows satisfying its conditions into:

- cashflow state `WAITING`
- cashflow sub-state type `Pending Netting`

Those cashflows may subsequently be selected for [[beneficiary-bic-netting]], subject to [[netting-key-eligibility]].

## Deprecated rule-refresh behaviour

A struck-through scenario proposed that disabling or updating an existing manual rule would remove `Pending Netting` from affected cashflows. Because the requirement is deprecated, it must not be used as current behaviour or as a rule-refresh contract.

The source does not define rule fields, activation controls, effective dating, precedence, refresh timing, or audit requirements.