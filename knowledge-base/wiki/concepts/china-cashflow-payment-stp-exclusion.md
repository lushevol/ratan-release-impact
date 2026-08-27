---
type: concept
title: China Cashflow Payment STP Exclusion
created: 2026-08-24
updated: 2026-08-24
tags: [china-settlement, murex-211, payment-stp, cashflow-routing, exclusion]
related: [cn-settlement-murex-211-integration, murex-ratan-bidirectional-cashflow-integration, cashflow-suppression-rules, nstp-rule-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 Delivery Plan.md"]
---
# China Cashflow Payment STP Exclusion

The CN Settlement delivery plan contains a requirement to exclude China cashflows from `Murex2.11 Payment STP` and to disable or exclude them from the BAU payment queue.

The Payment STP exclusion appears twice in the plan: once for Q4 Sprint 15 and again for Q1 2023 Sprint 1 under `RATAN-10678`. The plan does not explain whether these entries represent separate environments, rework, a follow-on release, or replacement scope.

The source does not define:

- the rule that identifies a China cashflow;
- where exclusion is enforced;
- the handling of excluded cashflows; or
- routing-rule precedence against other STP or suppression controls.

Do not infer those details from this requirement. They are tracked by [[what-is-the-final-china-cashflow-exclusion-rule-for-murex-211-payment-stp]].