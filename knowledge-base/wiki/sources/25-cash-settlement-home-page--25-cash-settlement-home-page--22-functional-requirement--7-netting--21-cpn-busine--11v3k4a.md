---
type: source
title: "Cash Settlement Home Page — Functional Requirement — Netting — CPN Business Scenario"
authors: []
year: 2022
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, netting, cpn, functional-requirement, China]
related: [cpn-netting, netting-resultant-cashflow-lifecycle, netting-scenario-priority, cashflow-blotter-netting-workflow, ad-hoc-cashflow-netting, maker-checker-settlement-control, cashflow-lifecycle-state-machine, ratan, razor, murex-2-11]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CPN Business Scenario.md"]
---
# Cash Settlement Home Page — Functional Requirement — Netting — CPN Business Scenario

## Summary

This functional requirement describes cashflow netting scenarios for settlement FXMM and derivatives, with particular emphasis on China Day 1 CPN processing. Netting is treated as a non-straight-through processing (NSTP) workflow in RATAN. Eligible cashflows remain available for manual or scheduled netting, while ordinary gross cashflows proceed through validation and release-cutoff processing.

The central validation key is:

```text
Booking Entity + Counterparty + Currency + Value Date
+ Cashflow Status not in Released or Settled
```

A valid request produces a netting resultant cashflow, assigns a shared `Netting ID` to the resultant and its components, marks the components as `Netted`, and routes the resultant to Checker review. Maker and Checker must be different user IDs.

## China Day 1 CPN scope

China Day 1 excludes RAZOR cashflows and focuses on derivative products currently supported outside Mx2.11.

- Products remaining in Mx2.11 use an enriched CPN static table. China is added as a CPN-eligible entity, and eligible cashflows are fed at MLS level into RATAN rather than RAZOR.
- Clients absent from the Mx2.11 CPN static table are expected to settle gross in Mx2.11, but a Murex manual queue may push selected cashflows into RATAN for ad-hoc CPN netting.
- Products moving to FMRP use a RATAN eligibility hierarchy:
  1. SCI flag.
  2. RATAN static table keyed by `Ctp | ccy | product`.
  3. Currency-exclusion static table.
- Cross-netting across FXMM, RAZOR FX, RAZOR ALM, Stella, and Mx2.11 is future scope rather than China Day 1 behavior.

## Netting scenarios

| # | Netting type | China scope | Scenario priority | Cross-product | Identifier or source |
|---:|---|:---:|---:|:---:|---|
| 1 | GROSS | Y | - | n/a | No netting scenario |
| 2 | Netting based on client request | Y | - | Y | Client request before release |
| 3 | Clients defined as Ad-hoc Netting in static data | N | 3 | Y | Ad-hoc Netting Table |
| 4 | General Netting across derivative products | Y | 2 | Y | Mx2.11 CPN table or RATAN rules |
| 5 | CPN Netting across FXMM and derivatives | N | - | - | Future requirement |
| 6 | CFETS Netting | Y | - | - | Bilateral-netting-like affirmation |
| 7 | BIC-Based Netting | N | - | - | SCI BIC source |
| 8 | CLS Netting | N | 1 | - | SCI flag |
| 9 | Inhouse Netting (LCM) | N | - | - | RAZOR/LCM flag |
| 10 | CCIL Netting | N | - | - | India-specific |
| 11 | Combination of Netting | N | - | - | Relevant flags |
| 12 | Tenure-Based Netting | N | - | - | Relevant flags |
| 13 | Currency-pair-Based Netting | N | - | - | RATAN netting table |
| 14 | Auto Netting | Y | 0 | N | Client static list and scheduled time |

The examples imply that a lower numeric priority value has higher precedence: Auto Netting `0` precedes CLS `1`, which precedes general netting `2` and ad-hoc netting `3`. The source does not explicitly confirm this convention.

## Worked netting example

For Shanghai, JP Morgan, USD, and value date `10/20/2022`:

| Cashflow | Direction | Amount | Product |
|---|---|---:|---|
| C101 | Pay | 100 | IRS |
| C102 | Receive | 150 | IRS |
| C103 | Pay | 200 | Loan/Deposit |
| C104 | Receive | 200 | Loan/Deposit |

Signed calculation:

```text
Pay     = 100 + 200 = 300
Receive = 150 + 200 = 350
Result  = Receive 50
```

The resultant product is taken from the first component cashflow, IRS in this example. The source proposes using the first component’s settlement instruction for SSI stamping.

## Representative lifecycle

| Cashflow type | Cashflow ID | Netting ID | Status | Sub status |
|---|---|---|---|---|
| Netting component | C101 | N101 | Netted | — |
| Netting component | C102 | N101 | Netted | — |
| Netting component | C103 | N101 | Netted | — |
| Netting component | C104 | N101 | Netted | — |
| Netting resultant | C105 | N101 | Pending | Netting Review |
| Accepted resultant | C105 | N101 | Validated | Pending Release |

A released cashflow, including one whose SWIFT message has been generated and sent to FMSRE, cannot be included in netting.

## Operational requirements

- The cashflow blotter must refresh automatically when queried cashflows change.
- DQSL query results should no longer be limited to only hundreds of cashflows in one batch; the target behavior is an unlimited or appropriately paginated result set.
- Release-cutoff configuration must support general and ad-hoc thresholds by legal entity and currency.
- RAZOR supports FX DVP gross processing, but DVP netting is not currently supported and remains a payment lake consideration.
- For derivatives, DVP applies only to commodity derivatives. Such payments are NSTP and manually released after bullion confirmation.
- The Checker must be able to inspect the components associated with a resultant through the shared `Netting ID`.

## Source ambiguities

The document contains an early example showing a resultant amount of `150`, while the detailed worked examples calculate `Receive 50`. The latter is consistent with the Pay/Receive calculation and should be treated as the more reliable example.

Status terminology also varies between scenario tables and detailed workflow steps. The exact rejection/reversion transitions, deterministic ordering for “first cashflow” SSI selection, cutoff race handling, and numeric priority convention remain to be confirmed.
