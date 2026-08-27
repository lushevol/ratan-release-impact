---
type: source
title: "Settlement Day 2 SAL Hard-Blocker UAT Self-Testing Evidence"
authors: []
year: 2025
url: ""
venue: "FMO Post Trade Portal UAT and self-testing evidence"
created: 2026-08-22
updated: 2026-08-22
tags: [settlement-day-2, sal, swap-agent, nstp, hard-blocker, uat, self-testing, cash-settlement]
related: [sal-swap-agent-hard-blocker, nstp-hard-blocker-bulk-eligibility, maker-checker-hard-blocker-operational-levels, cashflow-auto-netting, manual-cashflow-netting, pending-auto-netting-state, netting-resultant-cashflow, netting-resultant-cashflow-lifecycle, auto-netting-resultant-nstp, clearing-resultant-swift-suppression, fmo-post-trade-portal, swap-agent, murex, nstp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Self testing evdience.md"]
---
# Settlement Day 2 SAL Hard-Blocker UAT Self-Testing Evidence

## Scope

This source records UAT and self-testing evidence for a Settlement Day 2 NSTP hard-blocker requirement in the [[entities/fmo-post-trade-portal|FMO Post Trade Portal]]. The tested scope covers SAL and `SWAP_AGENT` cashflows, manual and automatic netting, resultant cashflows, maker-checker workflows, bulk operations, and release or suppression actions.

Testing evidence is reported for 2025-09-12 through 2025-09-19, 2025-10-16, and 2025-10-31. The evidence consists primarily of test-case tables, screenshots, cashflow identifiers, resultant identifiers, rule identifiers, and observed UI messages. The screenshots were not independently inspected during ingestion.

## Authoritative rule expression recorded in the evidence

```text
(Cashflow__Netting_Id == null || Cashflow__Netting_Id == "") &&
Instrument_Common__Murex_Product_Strategy == "SWAP_AGENT" &&
(Cashflow__Payment_Type == "Coupon" || Cashflow__Payment_Type == "Interim MTM")
```

The rule was associated with SAL netting rules and an NSTP hard-blocker rule. Reported rule identifiers include:

- `7351574062254944256`
- `7351573889412694016`
- `7372077796809277440`
- `7297966779679870976`
- `7386290080661438464`
- `7301223423860588544`
- `7207921566096560128`

## Findings

### Hard-blocked payment types

The evidence repeatedly shows that a cashflow with `Murex_Product_Strategy = "SWAP_AGENT"` and payment type `Coupon` or `Interim MTM` receives the `Hard block Swap Agent` exception. The UI displays the exception in red and reports:

> This is a Swap Agent Coupon or Interim MTM cashflow, can't be released from Ratan

The rule applies to source cashflows and, in tested same-type netting scenarios, to the resulting netting cashflow.

### Netting and release are separate controls

Different-payment-type combinations were rejected during manual netting. Tested examples included:

- `SWAP_AGENT` `Coupon` with `SWAP_AGENT` `Interim MTM`
- `SWAP_AGENT` `Interim MTM` with `SWAP_AGENT` `Initial Notional`
- `SWAP_AGENT` `Coupon` with `RECALC` `Coupon`
- `SWAP_AGENT` `Interim MTM` with `SWAP_AGENT` `Final Notional`

For same-payment-type cases, two cashflows could be netted and a resultant could be generated, but the resultant then hit the hard blocker and could not follow the prohibited release or approval path. The evidence therefore does not support the statement that the hard blocker prevents all netting creation.

### Role-dependent maker-checker behavior

Under maker-controlled configurations, maker submission was rejected. Under checker-only configurations, the maker could submit because the exception was not visible or actionable at maker level, while checker approval was rejected. Maker-checker configurations retained the release restriction.

### Bulk processing

A hard-blocked cashflow was not eligible for bulk submission whether `Bulk Eligible` was enabled or disabled. A separate item without the hard-blocker exception could continue through the normal bulk workflow.

### Payment-type exclusions

`SWAP_AGENT` cashflows with `Initial Notional` or `Final Notional` did not hit the tested hard-blocker rule and were released through the tested process. This evidence is specific to the recorded predicate and does not establish a universal policy for all future rule versions.

### Resultant and exception handling

Resultants with the hard blocker could also show exceptions such as Missing Vostro, Missing Nostro, or Pending Affirmation. The source reports that release or approval remained blocked, while actions including unnetting, Swift suppression, manual failure, reinstatement, hold/unhold, and cashflow suppression were tested as available in relevant scenarios.

### Auto-netting

For SAL `SWAP_AGENT` Coupon or Interim MTM cashflows, the tested auto-netting flow moved source cashflows from `WAITING` with sub-state `Pending Auto Netting` to `Netted` and created a resultant with payment type `SAL MTM Netting`. When automatic Swift suppression was configured, the resultant was reported as `SWIFT_SUPPRESSED`. When the auto Swift suppression rule was disabled, the resultant was still created but hit the NSTP hard blocker.

### Configuration regression

The tests confirmed that a non-hard-blocker NSTP rule could still be created with maker-checker configuration. Brief regression checks reported successful operation for BIC Netting, CCIL Netting, Bilateral Netting, bulk submit, and bulk approve.

## Representative identifiers

The evidence includes the following representative test objects:

- Cashflows: `M00121810310`, `M00121810311`, `M00202510185`, `M00202510186`, `M00121833333`, `M00121844444`
- Resultants: `N00000047171`, `N00000047172`, `N00000047177`, `N00000050647`, `N00000050650`

These identifiers are test-data references and should not be treated as production configuration.

## Evidence limitations

The evidence is moderate to strong for the tested workflows but has several limitations:

- Most observations are screenshot references rather than machine-readable logs or API responses.
- Some test rows are incomplete or inconsistently numbered.
- Later test rounds do not repeat the full predicate.
- UAT1 and UAT2 used different environments and data.
- The complete action authorization matrix is not established.
- The precedence between hard-blocker exceptions and automatic Swift suppression remains unresolved.
- The relationship between `SAL`, `SWAP_AGENT`, and `SAL MTM Netting` is implied rather than formally specified.
- The self-testing material does not establish formal sign-off status.

## Related wiki topics

See [[sal-swap-agent-hard-blocker]] for the rule behavior, [[nstp-hard-blocker-bulk-eligibility]] for bulk safeguards, and [[maker-checker-hard-blocker-operational-levels]] for operational-level differences. The unresolved authorization and lifecycle questions are tracked in [[what-is-the-authoritative-sal-hard-blocker-action-matrix]].