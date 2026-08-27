---
type: source
title: "MX2.11 Decommissioning — Cash Settlement STP Driven by Affirmation and Confirmation Status"
tags: [cash-settlement, stp, nstp, trade-affirmation, trade-confirmation, mx2-11, auto-netting]
related: [affirmation-confirmation-driven-settlement-stp, fixing-cashflow-stp, fx-swap-leg-independent-stp, ratan, ratan-one, tds3-api, inter-entity-netting, clearing-swift-suppression]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/Affirmation   Confirmation Status driving Settlement STP.md"]
authors: []
year: 2026
url: ""
venue: ""
---

# MX2.11 Decommissioning — Cash Settlement STP Driven by Affirmation and Confirmation Status

## Summary

This business workflow defines how Trade Affirmation Status, Trade Confirmation Status, and Cashflow Affirmation Status influence settlement release and STP/NSTP outcomes during the MX2.11 decommissioning context.

The proposed design is agnostic to the Bank-versus-Corporate client segment. Where NSTP is required, the workflow should use product-level or individual-client parameters rather than generic client-segment rules.

The matrix is not a complete approved implementation specification. Several entries describe current behavior, proposed target behavior, or controls requiring verification.

## Core observations

- Ordinary gross and trade cashflows generally require complete trade affirmation or full confirmation matching for STP.
- Economics-level affirmation or matching is generally insufficient for STP.
- Cashflow affirmation may provide an alternative cashflow release path, but the matrix labels that path `Manual Affirm`; the canonical semantics remain unresolved.
- FX SWAP near and far legs should be evaluated independently according to product type and tenure.
- DEPO payments may remain held until receipt of funds is confirmed, including an overnight confirmation condition for China Day1.
- Fixing cashflows have separate requirements involving full matching and completion of fixing.
- Internal FXMM/derivative trades may qualify for STP when generated through an external venue where the trade is matched, such as Trianna or SCALE.
- Inter-entity derivative STP depends on a proposed `validated` status following TCG reconciliation controls based on SABRE and TDS3 data; the control design requires verification.
- Islamic Trades remain an unresolved current-state versus target-state topic.
- Self-executed trades for negative-affirmation clients may use confirmation dispatch without matching, subject to Legal review of NCA requirements.
- Netting STP may depend on S2B NG, external venue validation, client-specific auto-netting configuration, a predefined cutoff, and fully affirmed or fully matched underlying trades. Precedence and failure behavior require further analysis.
- Clearing trades are currently suppressed in MX2.11, while the target state remains to be agreed.

## Status distinctions

The workflow distinguishes among:

- **Trade Affirmation Status:** whether trade economics or the complete trade has been affirmed.
- **Trade Confirmation Status:** whether trade economics or the complete trade has been matched.
- **Cashflow Affirmation Status:** whether RATAN considers a cashflow affirmed.
- **Fixing completion:** whether a fixing-dependent cashflow has completed its fixing prerequisite.
- **External venue validation:** whether an external venue or reconciliation control has established eligibility for STP.
- **Settlement release:** whether a cashflow may proceed to settlement, which is not necessarily equivalent to automated STP.

## Source matrix

The source table is reproduced below, retaining its irregular header structure and original wording.

```markdown
| Product | Trade Affirmation Status CDU PS | Trade Confirmation Status CDU PS | Cashflow Affirmation Status RATAN | Comments |
| --- | --- | --- | --- | --- |
| **Method** | **Product** | **Unaffirmed** | **Economics Affirmed** | **Full Affirmed** | **Unconfirmed** | **Economics** **Matched** | **Matched** | **Unaffirmed** | **Affirmed** | |
| Gross | FX - Cash, Tom, Spot | **NSTP** | **NSTP** | **STP** | **NSTP** | **NSTP** | **STP** | **NSTP** | **Manual Affirm** | Release Cashflow if Trade is Full Affirmed or Matched (or) Cashflow is Affirmed |
| FX - FORWARD | **NSTP** | **NSTP** | **STP** | **NSTP** | **NSTP** | **STP** | **NSTP** | **Manual Affirm** | |
| FX SWAP | Near and Far Leg should independently follow the STP workflow based upon the product type / tenure |
| DEPO | **NSTP** | **NSTP** | **STP** | **NSTP** | **NSTP** | **STP** | **NSTP** | **Manual Affirm** | Hold payment until receipt of funds is confirmed (O/N for China Day1) |
| LOAN | **NSTP** | **NSTP** | **STP** | **NSTP** | **NSTP** | **STP** | **NSTP** | **Manual Affirm** | |
| **All Derivatives Products** - Trade Cashflows | **NSTP** | **NSTP** | **STP** | **NSTP** | **NSTP** | **STP** | **NSTP** | **Manual Affirm** | |
| **All Derivative Products**- Fixing Cashflows including IRS / NDF | **NSTP** | **NSTP** | **NSTP** | **NSTP** | **NSTP** | **NSTP** | **NSTP** | **STP if Confirmation is Fully Matched + Fixing is done** | - STP if underlying Trade must be Full Matched + Fixing completed (i.e., NSTP if Trade is Fully Affirmed + Fixed). - Currently Fixing cashflows are STP for some of the products without cashflow affirmation |
| FXMM/Derivatives - **Internal trades** **requiring payment** | STP if the generation is triggered by external venue (example: prime services are matched in Trianna / SCALE) |
| Derivatives - Inter Entity | STP if trade is in a 'validated' status on the back of reconciliation done by TCG <<Controls at TCG based on SABRE TDS3 recon via ONEVALUATIONS view to be verified>> |
| Islamic Trades | ** NSTP **<<Current state / target state to be reviewed as a separate exercise>> |
| Self Executed Trades by Clients Negative Affirmation Clients | Release payment based on Confirmation Dispatch and no matching required <<<Engage Legal to challenge NCA requirement for Self executed trades>>> |
| Netting - FX / Derivatives | STP if the netting is 1) triggered by client (S2B NG) or 2) Validated from an external venue 3) STP for specific clients based on auto netting at a predefined netting cutoff provided underlying trades are fully Affirmed / fully Matched <<<Further analysis required to define the logic>>> |
| Clearing Trades | <<Currently being suppressed in MX2.11, target state to be agreed>> |
```

## Unresolved points

- The canonical column schema and status vocabulary require confirmation.
- The relationship between `Cashflow Affirmed`, `Manual Affirm`, automated release, and STP is unclear.
- The fixing-cashflow products that currently bypass cashflow affirmation are not identified.
- The required DEPO state transition after receipt of funds is unspecified.
- The TCG `validated` status and its SABRE/TDS3/ONEVALUATIONS control chain require verification.
- The Legal and NCA position for self-executed negative-affirmation trades remains unresolved.
- Netting trigger precedence, failure handling, and underlying-trade eligibility require definition.
- The target state for clearing trades after MX2.11 decommissioning is not agreed.

## Related wiki context

This source extends [[concepts/auto-netting-rule-check]], [[concepts/auto-netting-datetime-calculation]], [[concepts/inter-entity-netting]], [[concepts/inter-entity-cashflow-pre-match]], [[concepts/clearing-swift-suppression]], and [[concepts/clearing-resultant-swift-suppression]]. It also provides workflow context for [[entities/ratan]], [[entities/ratan-one]], and [[entities/tds3-api]].

---

---FILE: wiki/concepts/affirmation-confirmation-driven-settlement-stp.md---
---
type: concept
title: Affirmation and Confirmation-Driven Settlement STP
tags: [stp, nstp, settlement, trade-affirmation, trade-confirmation, cashflow-affirmation]
related: [26-auto-netting-page-md-files--164-cash-settlement-home-page-cash-settlement-home-page-mx211-decomm-cash-settle--1d21pqc, ratan, ratan-one, last-mile-payment-check, auto-netting-rule-check]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- MX2.11 Decomm - Cash Settlement Business Workflow -- Affirmation   Confirmation Status driving Settlement STP.md"]
---

# Affirmation and Confirmation-Driven Settlement STP

## Definition

Affirmation and confirmation-driven settlement STP is the decisioning model that determines whether a cashflow can be released automatically, held for NSTP handling, or sent for manual affirmation based on trade and cashflow statuses.

The model separates:

- Trade affirmation status from trade confirmation status.
- Economics-level status from full-trade status.
- Cashflow affirmation from automated settlement release.
- Generic product rules from product-, venue-, and client-level exceptions.

## General rule

For the ordinary gross and derivative trade-cashflow categories covered by the source:

- `Economics Affirmed` generally results in `NSTP`.
- `Full Affirmed` generally qualifies for `STP`.
- `Economics Matched` generally results in `NSTP`.
- `Matched` generally qualifies for `STP`.
- An unaffirmed cashflow generally results in `NSTP`.
- An affirmed cashflow is shown as `Manual Affirm`, so it must not automatically be interpreted as STP.

The source also states that a cashflow may be released when the trade is fully affirmed, the trade is matched, or the cashflow is affirmed. This creates an unresolved distinction between release eligibility and the processing mode used to achieve release.

## Scope boundaries

These general rules do not automatically apply to:

- Fixing cashflows.
- FX SWAP legs.
- DEPO payment holds.
- Internal trades generated through external venues.
- Inter-entity trades with validated reconciliation status.
- Negative-affirmation client workflows.
- FX and derivative netting.
- Clearing trades currently suppressed in MX2.11.

Client-segment neutrality is a design principle, not evidence that every client has identical parameters. Exceptions should be expressed through product or individual-client configuration.

## Operational implications

Settlement services should preserve the source status dimensions rather than collapsing them into a single affirmation flag. Rule evaluation should identify whether the outcome is:

1. Automatically eligible for STP.
2. Eligible for release but requiring manual affirmation.
3. NSTP because a complete affirmation, confirmation, or other prerequisite is absent.
4. Subject to a product-specific hold or external validation.

This concept complements [[concepts/last-mile-payment-check]] but is not equivalent to it: status-driven STP eligibility is an upstream decisioning concern, while the last-mile check concerns downstream payment readiness.

## Evidence and limitations

The source is a business workflow and contains irregular table headers, unresolved target-state statements, and controls marked for verification. The rules should therefore be treated as documented business intent or current-state evidence until implementation and approval records confirm the canonical behavior.

---

---FILE: wiki/concepts/fixing-cashflow-stp.md---
---
type: concept
title: Fixing Cashflow STP
tags: [fixing-cashflow, stp, nstp, derivatives, irs, ndf]
related: [26-auto-netting-page-md-files--164-cash-settlement-home-page-cash-settlement-home-page-mx211-decomm-cash-settle--1d21pqc, affirmation-confirmation-driven-settlement-stp, netting-type-derivation, resultant-hard-blocker-stamping]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- MX2.11 Decomm - Cash Settlement Business Workflow -- Affirmation   Confirmation Status driving Settlement STP.md"]
---

# Fixing Cashflow STP

## Definition

Fixing cashflow STP is settlement automation for derivative cashflows whose eligibility depends on completion of a fixing in addition to trade affirmation or confirmation status.

The source explicitly separates fixing cashflows, including IRS and NDF, from ordinary derivative trade cashflows.

## Documented target condition

The source indicates that a fixing cashflow may be STP when:

- The underlying trade is fully matched.
- The fixing is completed.
- The applicable cashflow conditions are satisfied.

It also records the formulation: `NSTP if Trade is Fully Affirmed + Fixed`, indicating that full affirmation plus fixing completion is not necessarily sufficient for the target STP path.

## Current-state qualification

The source states that some fixing cashflows are currently STP without cashflow affirmation. It does not identify the affected products or establish whether this is approved target-state behavior.

Accordingly, the following must remain separate:

- The proposed target rule requiring full matching and fixing completion.
- Current product-specific behavior that may bypass cashflow affirmation.
- Any future approved implementation matrix.

## Processing consequence

A fixing-complete flag must not by itself qualify a cashflow for STP. The rule must evaluate fixing completion together with the relevant underlying trade confirmation and product configuration.

This concept must not be generalized to ordinary derivative trade cashflows, whose matrix entries use different affirmation and confirmation outcomes.

## Open control questions

The source leaves unresolved which products currently bypass cashflow affirmation, whether full matching is mandatory for every fixing product, and how fixing completion is represented and propagated to settlement decisioning.

---

---FILE: wiki/concepts/fx-swap-leg-independent-stp.md---
---
type: concept
title: FX SWAP Leg-Independent STP
tags: [fx-swap, stp, settlement, near-leg, far-leg]
related: [26-auto-netting-page-md-files--164-cash-settlement-home-page-cash-settlement-home-page-mx211-decomm-cash-settle--1d21pqc, affirmation-confirmation-driven-settlement-stp, netting-type-derivation]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- MX2.11 Decomm - Cash Settlement Business Workflow -- Affirmation   Confirmation Status driving Settlement STP.md"]
---

# FX SWAP Leg-Independent STP

## Definition

FX SWAP leg-independent STP is the rule that the near leg and far leg of an FX SWAP are evaluated independently for settlement automation.

The source states that each leg should follow the STP workflow based on its product type and tenure.

## Decision model

The settlement decision for each leg should consider:

- The product classification applicable to the leg.
- The leg's tenure.
- Trade affirmation status.
- Trade confirmation status.
- Cashflow affirmation status where applicable.
- Any product-specific hold, cutoff, or exception parameter.

A trade-level FX SWAP outcome should not replace the individual settlement outcomes of its near and far legs.

## Boundary

The source does not provide a complete near-leg/far-leg status matrix or specify whether the two legs share any common blocking condition. Implementation details therefore require confirmation before this concept is used as an authoritative algorithm.

---

---FILE: wiki/entities/mx2-11.md---
---
type: entity
title: MX2.11
tags: [settlement-platform, legacy-system, decommissioning, cash-settlement]
related: [26-auto-netting-page-md-files--164-cash-settlement-home-page-cash-settlement-home-page-mx211-decomm-cash-settle--1d21pqc, clearing-swift-suppression, affirmation-confirmation-driven-settlement-stp]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- MX2.11 Decomm - Cash Settlement Business Workflow -- Affirmation   Confirmation Status driving Settlement STP.md"]
---

# MX2.11

## Role

MX2.11 is the legacy processing context referenced in the cash settlement workflow and its decommissioning activities.

## Documented state

The source states that Clearing Trades are currently being suppressed in MX2.11. The target treatment after decommissioning has not been agreed.

MX2.11 should therefore be treated as evidence of current-state behavior, not as the authority for the future clearing-trade workflow.

---

---FILE: wiki/entities/cdu-ps.md---
---
type: entity
title: CDU PS
tags: [trade-status, affirmation, confirmation, settlement]
related: [26-auto-netting-page-md-files--164-cash-settlement-home-page-cash-settlement-home-page-mx211-decomm-cash-settle--1d21pqc, affirmation-confirmation-driven-settlement-stp]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- MX2.11 Decomm - Cash Settlement Business Workflow -- Affirmation   Confirmation Status driving Settlement STP.md"]
---

# CDU PS

## Role

CDU PS is the status domain or component identified as the source of Trade Affirmation Status and Trade Confirmation Status in the settlement STP matrix.

## Status dimensions

The source distinguishes:

- Unaffirmed
- Economics Affirmed
- Full Affirmed
- Unconfirmed
- Economics Matched
- Matched

These statuses are used alongside RATAN Cashflow Affirmation Status to determine STP, NSTP, or Manual Affirm outcomes.

## Qualification

The source does not define CDU PS's system ownership, interface, or canonical enum names. Those details require confirmation before implementation-level use.

---

---FILE: wiki/entities/tcg.md---
---
type: entity
title: TCG
tags: [reconciliation, controls, inter-entity-trades, settlement]
related: [26-auto-netting-page-md-files--164-cash-settlement-home-page-cash-settlement-home-page-mx211-decomm-cash-settle--1d21pqc, sabre, tds3-api, onevaluations, inter-entity-netting, inter-entity-cashflow-pre-match]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- MX2.11 Decomm - Cash Settlement Business Workflow -- Affirmation   Confirmation Status driving Settlement STP.md"]
---

# TCG

## Role

TCG is the control or reconciliation function referenced for validating inter-entity derivative trades.

## Documented workflow

The source proposes that an inter-entity trade can qualify for STP when it is in `validated` status following reconciliation performed by TCG. The proposed control chain uses SABRE and TDS3 reconciliation data and the ONEVALUATIONS view.

The source marks the TCG controls as requiring verification. `validated` must therefore be treated as a proposed or conditional status rather than an authoritative STP decision until confirmed.

---

---FILE: wiki/entities/sabre.md---
---
type: entity
title: SABRE
tags: [reconciliation, controls, inter-entity-trades]
related: [26-auto-netting-page-md-files--164-cash-settlement-home-page-cash-settlement-home-page-mx211-decomm-cash-settle--1d21pqc, tcg, tds3-api, onevaluations]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- MX2.11 Decomm - Cash Settlement Business Workflow -- Affirmation   Confirmation Status driving Settlement STP.md"]
---

# SABRE

## Role

SABRE is referenced as part of the reconciliation basis used by TCG to validate inter-entity derivative trades.

## Qualification

The source does not specify SABRE's interface, ownership, or authoritative data model. Its relationship to TDS3 and TCG remains subject to control-design verification.

---

---FILE: wiki/entities/onevaluations.md---
---
type: entity
title: ONEVALUATIONS
tags: [valuation, reconciliation, controls, inter-entity-trades]
related: [26-auto-netting-page-md-files--164-cash-settlement-home-page-cash-settlement-home-page-mx211-decomm-cash-settle--1d21pqc, tcg, sabre, tds3-api]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- MX2.11 Decomm - Cash Settlement Business Workflow -- Affirmation   Confirmation Status driving Settlement STP.md"]
---

# ONEVALUATIONS

## Role

ONEVALUATIONS is the view referenced for verifying the TCG control design supporting inter-entity derivative reconciliation.

## Qualification

The source does not establish whether ONEVALUATIONS is an operational decisioning interface, a reporting view, or only a verification surface. Its authoritative role is not established.

---

---FILE: wiki/entities/s2b-ng.md---
---
type: entity
title: S2B NG
tags: [netting, client-triggered-netting, stp, external-system]
related: [26-auto-netting-page-md-files--164-cash-settlement-home-page-cash-settlement-home-page-mx211-decomm-cash-settle--1d21pqc, auto-netting-rule-check, auto-netting-datetime-calculation]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- MX2.11 Decomm - Cash Settlement Business Workflow -- Affirmation   Confirmation Status driving Settlement STP.md"]
---

# S2B NG

## Role

S2B NG is identified as a client-triggered netting venue or system.

## Settlement relevance

The source lists client-triggered netting through S2B NG as one possible condition for STP for FX and derivative netting.

This is a candidate condition rather than a complete rule. The source does not define precedence against external venue validation, client-specific auto-netting configuration, cutoff timing, or underlying trade status.

---

---FILE: wiki/entities/trianna.md---
---
type: entity
title: Trianna
tags: [external-venue, trade-matching, internal-trades, settlement]
related: [26-auto-netting-page-md-files--164-cash-settlement-home-page-cash-settlement-home-page-mx211-decomm-cash-settle--1d21pqc, affirmation-confirmation-driven-settlement-stp]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- MX2.11 Decomm - Cash Settlement Business Workflow -- Affirmation   Confirmation Status driving Settlement STP.md"]
---

# Trianna

## Role

Trianna is cited as an example external venue where prime-services trades may be matched.

## Settlement relevance

For internal FXMM or derivative trades requiring payment, the source proposes STP when generation is triggered by an external venue and the relevant trade is matched there, with Trianna given as an example.

This condition applies to the specified internal-trade workflow and should not be generalized to all internal or inter-entity trades.

---

---FILE: wiki/entities/scale.md---
---
type: entity
title: SCALE
tags: [external-venue, trade-matching, internal-trades, settlement]
related: [26-auto-netting-page-md-files--164-cash-settlement-home-page-cash-settlement-home-page-mx211-decomm-cash-settle--1d21pqc, affirmation-confirmation-driven-settlement-stp]
created: 2026-08-22
updated: 2026-08-22
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- MX2.11 Decomm - Cash Settlement Business Workflow -- Affirmation   Confirmation Status driving Settlement STP.md"]
---

# SCALE

## Role

SCALE is cited as an example external venue where prime-services trades may be matched.

## Settlement relevance

The source proposes that internal FXMM or derivative trades requiring payment may qualify for STP when generation is triggered by an external venue and the relevant trade is matched there.

The source does not define SCALE's interface or provide an approved implementation rule.

---

---FILE: wiki/log.md---
## 2026-08-22 ingest | MX2.11 Decommissioning — Cash Settlement STP Driven by Affirmation and Confirmation Status

- Added the source summary and documented the affirmation, confirmation, cashflow, fixing, inter-entity, netting, and clearing workflow distinctions.
- Added pages for [[affirmation-confirmation-driven-settlement-stp]], [[fixing-cashflow-stp]], and [[fx-swap-leg-independent-stp]].
- Added entity pages for MX2.11, CDU PS, TCG, SABRE, ONEVALUATIONS, S2B NG, Trianna, and SCALE.
- Recorded unresolved cashflow affirmation, fixing-cashflow, inter-entity validation, netting precedence, Legal/NCA, and clearing target-state questions.