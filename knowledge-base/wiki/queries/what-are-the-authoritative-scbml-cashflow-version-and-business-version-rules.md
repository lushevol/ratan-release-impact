---
type: query
title: What Are the Authoritative SCBML Cashflow Version and Business Version Rules?
created: 2026-08-23
updated: 2026-08-23
tags: [query, scbml, cashflow-version, business-version, lifecycle]
related: [scbml, cashflowinfo, cashflow-lifecycle-supersession-and-audit-history, cashflow-amendment-supersession]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/SCBML Template.md"]
---
# What Are the Authoritative SCBML Cashflow Version and Business Version Rules?

## Question

What is the intended relationship among `Cashflow_Version`, `Cashflow_Business_Version`, `Cashflow_Minor_Version`, `cashflowVersion`, and `businessVersion`?

## Evidence

Both supplied templates use the following mapping:

```xml
<scb:cashflowVersion
    th:text="${CashFlowInfo.Cashflow__Cashflow_Business_Version}">
</scb:cashflowVersion>
<scb:businessVersion
    th:text="${CashFlowInfo.Cashflow__Cashflow_Version}">
</scb:businessVersion>
```

The Withdrawal template additionally contains literal fallback values `0` and sets `cashflowMinorVersion` to `2`, while the New template leaves `cashflowMinorVersion` empty.

## Resolution needed

Confirm:

- Whether the apparent reversal of similarly named fields is intentional.
- The increment rules for business and technical versions.
- The meaning of minor version `2` for Withdrawal.
- Whether literal element content is fallback data or actual output.
- How versions identify amendment, withdrawal, supersession, and audit history.
