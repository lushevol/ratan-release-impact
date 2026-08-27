---
type: concept
title: Netting Scenario Priority
created: 2026-08-22
updated: 2026-08-22
tags: [netting, scenario, precedence, static-data]
related: [cpn-netting, ad-hoc-cashflow-netting, cashflow-lifecycle-state-machine, ccs-auto-netting, beneficiary-bic-based-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CPN Business Scenario.md"]
---
# Netting Scenario Priority

Scenario priority determines which netting treatment applies when a cashflow satisfies more than one scenario.

The source gives the following examples:

- CLS Netting has priority `1`.
- Ad-hoc Netting has priority `3`.
- A cashflow qualifying for both is treated as CLS Netting.
- Auto Netting is assigned priority `0`.

These examples imply the following convention:

```text
Lower numeric value = higher precedence
```

Under that interpretation, Auto Netting precedes CLS Netting, which precedes general netting and ad-hoc netting. The source does not provide a complete authoritative ordering for all scenarios, including BIC, inhouse, CCIL, DVP, tenure-based, and currency-pair-based netting.

Priority selection should occur before the cashflow is routed into the corresponding NSTP or gross workflow. The selected scenario must remain visible to operations and be auditable, particularly when a static eligibility rule and a client-requested ad-hoc operation overlap.

The term “higher priority” is ambiguous because it could refer to either a larger numeric value or greater precedence. The numeric convention should be confirmed before implementation.
