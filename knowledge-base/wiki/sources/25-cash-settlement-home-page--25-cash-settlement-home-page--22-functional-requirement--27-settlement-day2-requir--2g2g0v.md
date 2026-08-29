---
type: source
title: Settlement Day 2 Cashflow Auto Netting Functional Requirement
authors: []
year: 2025
url: ""
venue: Internal functional requirement
created: 2026-08-22
updated: 2026-08-22
tags: [settlement-day-2, cashflow-auto-netting, netting-static, acceptance-criteria]
related: [cashflow-auto-netting, auto-netting-rule-management, auto-netting-datetime-calculation, business-calendar-relative-netting-time, pending-auto-netting-state, cross-rule-netting-isolation, netting-type-derivation, netting-resultant-cashflow, netting-un-net-lifecycle, clearing-resultant-swift-suppression, irs-net-over-net, ratan, cash-settlement-home-page, netting-static-blotter, data-ops, fmmis, what-is-the-authoritative-auto-netting-priority-order, how-are-pending-auto-netting-cashflows-reconciled-after-rule-changes, what-is-the-canonical-auto-netting-stp-level-enums, what-is-the-clearing-swift-suppress-resultant-semantics, should-vd-netting-on-holidays-be-adjusted]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting.md"]
---
# Settlement Day 2 Cashflow Auto Netting Functional Requirement

This functional requirement defines Settlement Day 2 auto-netting rules configured through the [[cash-settlement-home-page]] and executed by [[ratan]]. It aims to automate the grouping and netting of rule-eligible cashflows, with an unverified expected operational saving of one hour per day.

Related ADO work items:

- https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469617
- https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/2300383
- https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/9442080

## Scope and controls

[[data-ops]] users may create, update, and disable auto-netting static rules in the [[netting-static-blotter]]. Other users have read-only access. The blotter must distinguish manual and auto rules through a `Rule Type` field.

Rules can include booking entity FM code, Murex product taxonomy, FMRP product catalogue, currency, payment type, counterparty, Counterparty BIC, and additional entity, product, typology, strategy, hierarchy, and currency-pair conditions.

The source specifies these validations:

- A rule with Booking Entity as its only condition is rejected: `Rule Creation not allowed with Booking Entity Alone`.
- A CCIL rule requires `Settlement method == CCIL`.
- A BIC rule requires `Counterparty_SCI_BIC_Net_Flag == "Y"`.
- Rules without `(Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")` receive a warning that netting resultants may not be excluded.
- Rules without a booking entity receive a soft warning that they apply to all SCB booking locations.
- Updating a rule's netting type requires confirmation.

## Netting type mappings

The source defines the following mappings verbatim.

| Netting Type | Netting Key | Netting Resultant Field | Description |
| --- | --- | --- | --- |
| Bilateral Netting | `[Entity.Booking_Entity_SCI_FMID, Entity.Counterparty_SCI_FMID, Cashflow.Cashflow_Currency, Cashflow.Cashflow_Payment_Date]` | `{"Cashflow__Payment_Type":"Bilateral Netting"}` | Bilateral Netting |
| CCIL Netting | `[Entity.Booking_Entity_SCI_FMID, Cashflow.Cashflow_Currency, Cashflow.Cashflow_Payment_Date]` | `{"Entity__Counterparty_SCI_FMID":"400021949", "Entity__Counterparty_SCI_FMCODE":"CLEARING CORP*MMB", "Settlement_Method":"Cash", "Cashflow__Payment_Type":"CCIL Netting"}` | Netting of CCIL cashflows, need to include *Settlement method =="CCIL" and Counterparty SCI FMID<>400021949* |
| BIC Netting | `[Entity.Booking_Entity_SCI_FMID, Cashflow.Cashflow_Currency, Cashflow.Cashflow_Payment_Date, Entity.Counterparty_SCI_BIC_Net_Flag, Entity.Counterparty_SCI_BIC_Code]` | `{"Cashflow__Payment_Type":"Ben BIC Netting"}` | Netting based on Counterparty BIC need to include *Counterparty_SCI_BIC_Net_Flag == "Y"* |
| SAL MTM Netting | `[Entity.Booking_Entity_SCI_FMID, Entity.Counterparty_SCI_FMID, Cashflow.Cashflow_Currency, Cashflow.Cashflow_Payment_Date, Cashflow.Cashflow_Payment_Type]` | `{"Cashflow__Payment_Type":"SAL MTM Netting"}` | Netting of MTM Cashflows of Swap Agent Limited |
| SAL Coupon Netting | `[Entity.Booking_Entity_SCI_FMID, Entity.Counterparty_SCI_FMID, Cashflow.Cashflow_Currency, Cashflow.Cashflow_Payment_Date, Cashflow.Cashflow_Payment_Type]` | `{"Cashflow__Payment_Type":"SAL Coupon Netting"}` | Netting of Coupon Cashflows of Swap Agent Limited |
| Clearing_Swift_Suppress | `[Entity.Booking_Entity_SCI_FMID, Entity.Counterparty_SCI_FMID, Cashflow.Cashflow_Currency, Cashflow.Cashflow_Payment_Date]` | `{"Cashflow__Payment_Type":"Bilateral Netting"}` | Single cashflow which hit the auto netting rule but no other cashflow to net with will be reinstate to the main flow |

Cross-rule netting is prohibited. The effective grouping key must contain the netting-type key and an immutable unique rule identifier, such as `Rule_ID`. Cashflows assigned to different rules must not be netted together even when their ordinary grouping values match.

## Timing

A rule specifies a value-date-relative offset and a minute-precision netting time, defaulting to `00:00`. The system calculates the execution date against the cashflow currency calendar.

| Cashflow | Currency | Payment Date | Date from Netting Static | Auto netting date | Calendar context |
| --- | --- | --- | --- | --- | --- |
| C1 | SGD | 1st Apr. 2025 (Tuesday) | VD-1 | 20250328 (Last Friday) | SGD holiday on 2025/03/31 |
| C2 | CNY | 1st Apr. 2025 (Tuesday) | VD-1 | 20250331 (Monday) | Working day |
| C3 | CNY | 7th Apr. 2025 (Monday) | VD-1 | 20250406 (Sunday) | CNY working weekend |
| C4 | GBP | 21st Apr. 2025 (Holiday) | VD | 20250421 (Holiday) | Payment date is a holiday |

A later review requests a `VD-2` option. The source does not conclusively establish whether a `VD` date that is a non-working day should ever be adjusted.

## Lifecycle and scheduler behavior

A cashflow matching an auto-netting rule enters:

```text
Cashflow_Status = WAITING
Cashflow sub state type = Pending Auto Netting
```

At or after the calculated netting time, the scheduled job nets multiple eligible cashflows. Components become `NETTED`; the resultant is affirmed, receives the configured STP/NSTP treatment, and can be released from RATAN.

A single matching cashflow is released from `Pending Auto Netting` with the rule's configured STP treatment. It must not be marked `settleAsGross`; if reinstated, it can match the rule again.

Cashflows arriving after the nominal netting time remain eligible for `Pending Auto Netting` and are processed when the scheduled job runs. This supersedes the earlier proposal for a configurable post-netting-time action.

Auto-netting with affirmation must be recorded as:

```text
action = 'Net'
user = "System"
```

Pending auto-netting supports the ordinary pending-netting actions, including manual fail/reinstate, hold/unhold, SWIFT suppression and verification, cashflow suppression and confirmation, and manual netting. Resultants support un-net before release.

## Resultant and withdrawal behavior

Resultants inherit specified parent attributes, including DVP settlement method, LIEN, and Commodity Flag. Ordinary net-over-net is prohibited, with a stated exception for auto-netting over an IRS netting resultant.

If a component is withdrawn after auto-netting, the resultant is automatically un-netted and becomes `DEAD`; the withdrawn component becomes `CANCELLED`; remaining components return to `WAITING / Pending Auto Netting` and may be netted again.

## Review findings and unresolved points

The document records scope reviews between 2025-04-14 and 2025-07-16. It confirms a requested priority sequence of SAL MTM, SAL Coupon, Clearing_Swift_Suppress, CCIL, BIC, then Bilateral Netting.

Several requirements remain internally unresolved:

- Detailed requirements and AC-011 through AC-015 require automatic refresh after rule creation, update, disablement, or conversion, while a later clarification specifies no automatic historical refresh.
- One rule-overlap rule applies netting-type priority first and latest creation only for ties; other text says the latest-created rule always wins.
- `NSTP_MAKER_CHECKER`, `NSTP_CHECKER_ONLY`, and `FULL_STP` are defined, but acceptance examples also use `MAKER_ONLY`.
- `Clearing_Swift_Suppress` has a bilateral resultant payment-type mapping despite later review language requiring SWIFT suppression for resultants and certain single-cashflow cases.
- [[fmmis]] is mentioned as a potential consumer or query client, but initial-scope integration is not confirmed.

See what is the authoritative auto netting priority order, how are pending auto netting cashflows reconciled after rule changes, what is the canonical auto netting stp level enums, what is the clearing swift suppress resultant semantics, and should vd netting on holidays be adjusted.