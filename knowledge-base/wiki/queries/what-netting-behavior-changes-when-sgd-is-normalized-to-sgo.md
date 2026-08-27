---
type: query
title: What Netting Behavior Changes When SGD Is Normalized to SGO?
tags: [open-question, netting, currency-normalization, grouping, irs, auto-netting]
related: [currency-alias-normalization, netting-service, irs-cashflow-processing, irs-counterpart-leg-matching, nds-cashflow-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Online Offline currency conversion solution.md"]
created: 2026-08-24
updated: 2026-08-24
---
# What Netting Behavior Changes When SGD Is Normalized to SGO?

What changes in validation, manual netting, IRS processing, auto-netting, trigger-time calculation, and grouping when `settlementCurrency` is normalized from `SGD` to `SGO`?

## Affected Areas Identified by the Source

The Netting Service proposal names:

```text
CashFlowRepository.getCashFlowQueryResults(...)
NettingService.processIRSNetting(...)
NettingService.getWaitingAnotherLegCashflowByTrade(...)
AutoNettingRuleCheckService.generateAutoNettingCashflow(...)
AutoNettingRuleCheckService.caculateNettingTriggerTime(...)
AutoNettingCashflow.generateGroupKey(...)
```

## Evidence Needed

- Whether `settlementCurrency` participates in IRS counterpart-leg selection or matching.
- Validator behavior for `SGD`, `SGO`, and mixed representations.
- Whether group keys differ after normalization and how existing groups are handled.
- The impact on netting eligibility, trigger times, and re-netting.
- Manual-netting visibility of the transformed currency.
- Verification that `caculateNettingTriggerTime(...)` is the exact implementation identifier rather than a documentation typo.