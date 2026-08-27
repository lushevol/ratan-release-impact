---
type: concept
title: CPN Netting
created: 2026-08-22
updated: 2026-08-23
tags: [cpn, netting, China, RATAN, Murex, FMRP, cashflow, settlement, maker-checker]
related: [ratan, razor, murex-2-11, stella, sci, cpn-netting-scope, ad-hoc-cashflow-netting, cashflow-netting, netting-resultant-cashflow-lifecycle, netting-resultant-cashflow, force-gross-review, cpn-netting-reversal-cashflow, automatic-un-netting-on-trade-market-events, netting-withdrawal-timing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CPN Business Scenario.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CPN Tech Design - Draft for now.md"]
---
# CPN Netting

CPN netting combines eligible component derivative cashflows into a CPN-generated resultant cashflow. The CPN Business Scenario describes it as a proposed China-focused process in [[ratan]], while the CPN Tech Design describes the component and resultant cashflow lifecycle.

## China Day 1 boundary

The CPN Business Scenario states that China Day 1 is deliberately narrower than the future cross-platform CPN vision.

- China Day 1 does not include [[razor]] cashflows.
- It covers derivative products currently supported outside Mx2.11.
- For products that remain in [[murex-2-11]], the existing CPN static table is enriched to add China as an eligible entity.
- Eligible Mx2.11 cashflows are sent at MLS level into [[ratan]] rather than [[razor]].
- Clients absent from the CPN static table remain gross in Mx2.11. A manual queue is proposed for pushing selected cashflows to RATAN for ad-hoc CPN netting.
- Automated execution of CPN netting is outside Day 1 scope. The Tech Design distinguishes this from automated eligibility identification: eligibility may be identified automatically, but selection and execution of netting remain manual in the described workflow.

## Eligibility

For products moving to FMRP, the CPN Business Scenario proposes that RATAN apply the following eligibility hierarchy:

1. SCI flag.
2. RATAN static table keyed by counterparty, currency, and product: `Ctp | ccy | product`.
3. Currency-exclusion static table.

The exact precedence and fallback behavior should be reconciled with the authoritative FMRP eligibility rules.

### Eligibility status terminology

The CPN Business Scenario states that a normally netting-eligible cashflow is held as:

```text
Cashflow Status: Pending
Sub Status: Pending Netting
```

The CPN Tech Design instead states that eligible components are marked `Pending` with sub-status type `CPN Netting`. These source descriptions use different sub-status terminology and should remain distinct pending confirmation of the canonical status model.

The CPN Business Scenario states that a non-eligible cashflow follows the gross path:

```text
Cashflow Status: Validated
Sub Status: Pending Release
```

## Manual and ad-hoc netting

In the Tech Design workflow, FMO Ops manually selects eligible components in the Cashflow Blotter.

The Tech Design also describes ad-hoc netting over a mixed set of `Projected`, `Queued`, `Pending`, and `Validated` components. This is broader than its summary action matrix, which lists ad-hoc netting only for `Projected/Queued` components.

Separately, the CPN Business Scenario states that an ad-hoc client request may include otherwise gross cashflows, including CCS, provided that the cashflows:

- have not been released or settled; and
- satisfy the common validation key.

## Lifecycle

The CPN Tech Design describes the following lifecycle:

1. CPN Eligibility Checking identifies eligible cashflows.
2. Eligible components are marked `Pending` with `CPN Netting` sub-status type.
3. FMO Ops selects components in the Cashflow Blotter.
4. Components receive a shared Netting ID, move to `Netted`, and become hidden from the GUI.
5. CPN Service creates a queued resultant.
6. Settlement Workflow changes the resultant to `Pending` / `Netting Review`.
7. A checker approves the resultant, changing it to `Validated` / `Reviewed`.
8. The resultant may progress to `Released` and `Settled`.

### Components and resultants

Components are retained as historical cashflows with updated versions and a Netting ID. While `Netted`, they are filtered from subsequent settlement tasks and are not visible in the Cashflow Blotter.

The resultant is a separate cashflow with its own status, version, review, release, settlement, un-netting, and reversal lifecycle.

### Explicit exclusions

The Tech Design explicitly states that:

- Netting an existing resultant, or “net of net,” is unsupported.
- Partial un-netting is unsupported.

## SSI stamping

The CPN Business Scenario proposes using the settlement instruction of the first component cashflow for the resultant. The source does not define how component cashflows are ordered or what occurs when their settlement instructions differ. This rule requires implementation confirmation before it can be considered canonical.

## Future scope

The CPN Business Scenario identifies cross-netting between FXMM, RAZOR FX, RAZOR ALM, [[stella]], and Mx2.11 as a future requirement. It should not be inferred as part of China Day 1.