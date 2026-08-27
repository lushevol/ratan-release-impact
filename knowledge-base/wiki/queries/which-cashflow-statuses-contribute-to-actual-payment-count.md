---
type: query
title: Which Cashflow Statuses Contribute to Actual Payment Count?
created: 2026-08-22
updated: 2026-08-22
tags: [cashflows, lifecycle, payment-completeness, auto-netting]
related: [expected-payment-count-for-auto-netting, cashflow-auto-netting, ratan-cashflow-lifecycle-state-machine, cashflow-logical-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Product Agnostic model to identify all cashflows for a specific value date to support Auto Aggregation.md"]
---
# Which Cashflow Statuses Contribute to Actual Payment Count?

The source illustrates Actual Payment Count as the number of cashflows present in a netting group, but does not define which cashflow statuses qualify.

## Questions

Should Actual Payment Count include or exclude cashflows that are:

- pending;
- held;
- suppressed;
- failed;
- cancelled;
- reinstated; or
- identified as duplicates?

## Impact

The answer determines whether the completeness gate in [[expected-payment-count-for-auto-netting]] is consistent with the authoritative [[ratan-cashflow-lifecycle-state-machine]] and avoids netting an operationally ineligible set.