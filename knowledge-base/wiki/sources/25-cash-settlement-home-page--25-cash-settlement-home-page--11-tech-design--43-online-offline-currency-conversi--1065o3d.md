---
type: source
title: Online Offline Currency Conversion Solution
authors: []
year: 2026
url: ""
venue: Internal technical design
tags: [currency-normalization, netting, group-management, sgd, sgo]
related: [currency-alias-normalization, currency-normalization-layer-ownership, which-service-owns-sgd-to-sgo-normalization, what-is-the-authoritative-sgd-to-sgo-mapping-scope, what-netting-behavior-changes-when-sgd-is-normalized-to-sgo, netting-service, irs-cashflow-processing, nds-cashflow-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Online Offline currency conversion solution.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Online Offline Currency Conversion Solution

This technical design proposes two alternative locations for normalizing the currency alias `SGD` to `SGO` before downstream cash-settlement processing and delivery. It does not document an approved decision, implementation, owner, test evidence, or delivery plan.

## Requirement

The stated outcome is to map `SGD` to `SGO` before downstream processing and delivery so that consumers use a consistent currency code.

The source does not define the authority, business scope, effective date, reverse-mapping behavior, or audit treatment for the `SGD → SGO` mapping.

## Solution 1: Group Management Standardization

This option places the conversion rule in [[group-management]], within the [[standardization-module]]. A new command would be registered in `UberHandlerBeanConfig` and executed before currency-dependent standardization commands.

```text
From StandardizationCommand, default getOrder() is 1, so the new currency command should use an earlier order (commonly 0).
```

Proposed change points:

```text
Add one new command class under domain/standardize.
Register the command in standardizationCommands(...) in UberHandlerBeanConfig.
No external API contract changes.
```

The source identifies a material risk: downstream consumers and manual netting may not observe the converted currency. Therefore, a Group Management-local transformation does not by itself establish that all intended consumers receive `SGO`.

The stated estimates are development: Medium; testing/validation: High.

## Solution 2: Netting Service Normalization

This option places the conversion rule in [[netting-service]]. It proposes rewriting `CashFlowQueryResult.settlementCurrency` after cashflow retrieval, then applying the same representation in manual netting, validation, grouping, IRS, and auto-netting paths.

| Covered logic | Proposed change point |
| --- | --- |
| Manual Netting, validators, and grouping | `CashFlowRepository.getCashFlowQueryResults()` |
| IRS | `NettingService.getWaitingAnotherLegCashflowByTrade()` |
| Auto-netting | `ruleCheck()` |

```text
Invoke normalization immediately after cashFlowApiClient.getCashFlowsV2(...) returns in CashFlowRepository.
Normalize CashFlowQueryResult.settlementCurrency before downstream grouping/validation logic.
```

Named proposed touchpoints:

```text
CashFlowRepository.getCashFlowQueryResults(...)
NettingService.processIRSNetting(...)
NettingService.getWaitingAnotherLegCashflowByTrade(...)
AutoNettingRuleCheckService.generateAutoNettingCashflow(...)
AutoNettingRuleCheckService.caculateNettingTriggerTime(...)
AutoNettingCashflow.generateGroupKey(...)
```

The source calls out validator verification for different currencies and a potentially broad change surface. In particular, changing `AutoNettingCashflow.generateGroupKey(...)` may affect group identity and therefore grouping or netting outcomes. The source does not specify compatibility rules for historical cashflows, cached results, persisted group keys, or mixed `SGD` and `SGO` inputs.

The stated estimates are development: Low; testing/validation: Medium. These estimates conflict with the same option's stated “many changes,” “High development cost,” and high testing-cost risks.

## Open Design Implications

Neither alternative proves that all downstream consumers receive the normalized value. The design needs confirmation of:

- the authoritative owner and scope of `SGD → SGO`;
- whether the original source code must be retained alongside the normalized code for audit and delivery;
- whether [[irs-cashflow-processing]] or counterpart-leg matching depends on `settlementCurrency`;
- the effect of normalization on manual-netting visibility, validators, grouping, and auto-netting;
- idempotency for already-normalized `SGO` values; and
- a reconciled, evidence-based effort estimate before planning.

See [[currency-alias-normalization]], [[currency-normalization-layer-ownership]], and [[what-netting-behavior-changes-when-sgd-is-normalized-to-sgo]].