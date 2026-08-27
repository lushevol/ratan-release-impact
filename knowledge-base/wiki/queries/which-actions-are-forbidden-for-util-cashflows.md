---
type: query
title: Which Actions Are Permanently Forbidden for UTIL Cashflows?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, utilization, action-gating, authorization, fxu]
related: [fxu-cashflow-utilization, util-settlement-method, cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case.md"]
---
# Which Actions Are Permanently Forbidden for UTIL Cashflows?

The FXU test case requires the following actions to be removed or made unavailable for `Util` cashflows:

- Netting
- Swift suppress
- Cashflow suppress
- Fail
- Update affirmation
- Early release
- Hold
- Settle As Gross

The source does not define the enforcement boundary or scope of this rule.

## Questions

1. Is the canonical settlement-method value `Util` or `UTIL`?
2. Does action gating depend only on settlement method, or also on cashflow status?
3. Does the restriction apply to every status or only to `Ready` cashflows?
4. Are actions hidden, disabled, or rejected by backend authorization?
5. Do APIs and batch operations enforce the same restrictions as the blotter UI?

The answer should be aligned with the authorization and action model of [[cashflow-blotter]].