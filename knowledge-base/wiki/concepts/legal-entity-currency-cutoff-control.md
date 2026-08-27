---
type: concept
title: Legal-Entity-Currency Cutoff Control
created: 2026-08-23
updated: 2026-08-23
tags: [cutoff, cashflow, swift, settlement-operations, static-data]
related: [new-currency-onboarding-static-data-readiness, ratan, settlement-ops]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/New Currency Onboarding Checklist.md"]
---
# Legal-Entity-Currency Cutoff Control

A legal-entity-currency cutoff is RATAN static data that controls a cashflow's release date and time.

```text
Legal Entity/Currency
```

When a cashflow is posted after the configured cutoff, SWIFT generation begins. At that point, Settlement Ops can no longer change the cashflow.

The source does not specify the cutoff time zone, inclusive/exclusive boundary semantics, behavior where no configuration is found, applicable product and lifecycle scope, or override and repair controls.