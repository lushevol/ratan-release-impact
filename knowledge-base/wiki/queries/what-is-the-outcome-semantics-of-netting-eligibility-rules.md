---
type: query
title: What Is the Outcome Semantics of Netting Eligibility Rules?
created: 2026-08-23
updated: 2026-08-23
tags: [netting, eligibility, static-data, open-question]
related: [netting-eligibility-static-data, nstp-rule-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data.md"]
---
# What Is the Outcome Semantics of Netting Eligibility Rules?

The supplied CN Day1 rule is:

```text
Entity.Counterparty_SCI_FMID==400202766&&Cashflow.Netting_Id==null
```

The source labels this as a Netting Eligibility Rule but does not state whether a match means that the cashflow is eligible for netting, ineligible for netting, or requires exception routing.

## Evidence Needed

Confirm the rule outcome in the UI, service contract, or production decision trace. The answer should also define behavior when optional dimensions such as Portfolio, Product Type, or Currency are blank.