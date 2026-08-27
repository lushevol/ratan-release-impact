---
type: query
title: What Is the Canonical CCIL Netting Status Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [CCIL, netting, status, NSTP, cashflow-lifecycle]
related: [ccil-netting, rule-service, settlement-method-driven-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/CCIL Netting Design.md"]
---
# What Is the Canonical CCIL Netting Status Contract?

The source uses two status expressions for apparently related purposes:

```text
Waiting+IsNettingEligible
```

for the rule-service result, and:

```text
waiting+pending netting
```

for frontend CCIL-netting eligibility.

It is not established whether these expressions represent the same state, separate fields, or a lifecycle transition. The canonical field names, allowed values, transition rules, and API representation should be documented before the frontend and service implementations are aligned.