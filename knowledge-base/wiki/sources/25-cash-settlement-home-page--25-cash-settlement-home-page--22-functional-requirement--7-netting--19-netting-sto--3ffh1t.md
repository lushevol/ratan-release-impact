---
type: source
title: Netting Story Board — Ratan and S2BNG
tags: [cash-settlement, netting, ratan, s2bng, functional-requirements]
related: [ratan, s2bng, ratan-s2bng-netting-eligibility, net-to-gross-workflow, netting-release-control, component-amendment-netting-exception, netting-client-configuration, net-id-reconciliation-matching]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Story Board.md"]
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
---
# Netting Story Board — Ratan and S2BNG

This storyboard records intended functional requirements for cashflow netting in [[ratan]] and [[s2bng]]. It separates Ratan-only requirements from functions shared by both platforms. It is requirements evidence, not confirmation of implementation, approved workflow sequencing, or a complete lifecycle specification.

The accompanying attachment is `Netting Story Board - Ratan S2BNG.pdf`.

## Ratan-only requirements

Ratan requires FMO maker/checker profiles and limits, manual release of net cashflows through maker/checker controls, and consumption of netting information from [[gtss]].

Net-to-Gross requests from Netting Clients must go to [[nstp]]. Ratan must also support CLS netting and inter-entity netting through [[lcm]].

For reconciliation, [[tlm]] must auto-match many trades to one cashflow by a common Net ID for Bridge suspense reconciliation.

The source states that no net or un-net action is allowed on a Released cashflow (`Razor>FMSRE`). This is described as a soft block, with an incremental posting still pending.

## Shared Ratan and S2BNG requirements

[[fmo-users]] must be able to select two or more cashflows for ad hoc gross-cashflow netting. Net cashflows must be displayed, filterable in the cashflow blotter, drillable to component trades, and represented in the audit trail. The solution must support un-netting and re-netting.

For Default Netting Clients, the net amount must be shown by default, with an option to drill down into trades.

Cashflows can be netted only while unreleased. A DVP deal must not be moved into netting. Cashflows generated through Split are eligible for netting.

A component-trade amendment affecting an unreleased net cashflow must create an exception. Users must manually review and accept the new net cashflow before release.

Net cashflow SI amendment is permitted before release. Netting success or failure must be notified on screen.

## Eligibility rules

The storyboard defines a client-classification-specific identity key, with shared matching dimensions:

| Client classification | Identity match | Required shared matches |
|---|---|---|
| GIVE UP CLIENTS | Same SWIFT BIC | Currency, SCB Entity, value date, settlement method, and product at CFI-code level |
| NON GIVE UP | Same FMID | Currency, SCB Entity, value date, settlement method, and product at CFI-code level |

See [[ratan-s2bng-netting-eligibility]]. These rules are scoped to Ratan/S2BNG and must not be assumed to replace [[ccil-netting-eligibility-key]] or [[bilateral-netting-eligibility]].

## Configuration and workflow requirements

The source requires client-level configuration for product at the lowest CFI-code level, instrument currency, and auto-netting batch timing by FMID or LEI. Netting-set validation must send an affirmation email, and clients must be able to manage notification preferences.

[[cadm]] is proposed as the client-data source, but this is explicitly marked TBC.

Net-to-Gross requests for UK and US Netting Clients must trigger [[tcrm]]. A configurable threshold must determine when TCRM approval is required. The sequencing of TCRM and Ratan's NSTP routing is not specified.

## FX-leg handling

One leg of an FX trade can be independently netted, but the other leg must follow settlement method `NET`. The source does not state whether the second leg must join a netting set or only inherit the settlement-method value.

## Open requirement tensions

The document says both that netting can occur “within and across Products” and that eligibility requires the same product at CFI-code level. It also restricts shared netting to the same SCB Entity while listing Ratan inter-entity netting through LCM.

These tensions are tracked in what is the ratan s2bng cross product netting rule and how does lcm inter entity netting coexist with the same scb entity rule.