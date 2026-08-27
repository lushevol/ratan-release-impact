---
type: concept
title: Resultant Cashflow Hard Blocker Propagation
created: 2026-08-23
updated: 2026-08-23
tags: [resultant-cashflow, netting, hard-blocker, swap-agent, ratan]
related: [swap-agent-hard-blocker, ratan-cash-settlement-netting-service, ratanone-rule-service, what-is-the-current-swap-agent-hard-blocker-configuration, settlement-day-2]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/[Deprecated", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/[Deprecated] Hard Blocker Tech Analysis.md"] Hard Blocker Tech Analysis.md"] Hard Blocker Tech Analysis.md"]
---
# Resultant Cashflow Hard Blocker Propagation

Resultant cashflow hard-blocker propagation is the historical design for retaining component-level Swap Agent eligibility after cashflows are netted.

A resultant cashflow is identified by a non-empty `Cashflow__Netting_Id`. Rather than re-evaluating direct component fields, the final documented rule evaluates the derived field:

```text
Cashflow__Component_Strategy_Payment_Hard_Blocker
```

The field is expected to contain token values such as:

```text
SWAP_AGENT#Coupon
SWAP_AGENT#Interim MTM
```

The resultant rule uses comma-delimited token boundary matching, so a single matching component marker should trigger the hard blocker.

## Service responsibility

[[ratan-cash-settlement-netting-service]] is documented as enriching resultant cashflows during netting. The source states that only IRS cashflows can perform net-over-net and therefore the requirement considers only single component cashflows when setting relevant resultant attributes.

FMRP1 test notes show that resultants containing matching components were blocked, while resultants composed only of non-matching components were not. At least one blocked resultant was successfully unnetted.

## Contract inconsistency

The source is internally inconsistent about the final field contract:

- The final rule and service notes use `Cashflow__Component_Strategy_Payment_Hard_Blocker`.
- The migration configures `Instrument_Common.Component_Murex_Product_Strategy` and `Cashflow.Component_Payment_Type`.
- The XML XPath mappings target `hardBlockerComponentMurexStrategy` and `hardBlockerComponentPaymentType`.
- An implementation note also mentions `hardBlockerComponentType`.

The deprecated evidence does not show the canonical transformation or confirm which representation was deployed. This must be resolved before using the rule as implementation guidance; see [[what-is-the-current-swap-agent-hard-blocker-configuration]].