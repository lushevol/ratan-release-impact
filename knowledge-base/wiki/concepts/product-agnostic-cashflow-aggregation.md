---
type: concept
title: Product-Agnostic Cashflow Aggregation
created: 2026-08-22
updated: 2026-08-24
tags: [cash-settlement, cashflow, aggregation, netting, product-agnostic]
related: [normalized-payment-schedule, 2026-brp-q3-ratansett-product-agnostic-aggregation, ratan, fmrp-flow, irs-interest-auto-netting, ccs-auto-netting, cross-product-netting, netting-over-netting, how-will-normalized-payment-schedule-aggregation-coexist-with-irs-and-ccs-auto-netting, normalized-payment-schedule-completeness-check, netting-service, cashflow, strategic-cashflow, what-is-the-authoritative-auto-aggregation-completeness-and-idempotency-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Product Agnostic Aggregation Design.md"]
---
# Product-Agnostic Cashflow Aggregation

Product-agnostic cashflow aggregation is a proposed capability to combine eligible cashflows through a common mechanism rather than mechanisms limited to particular product taxonomies.

The functional-requirement draft proposes the capability for [[ratan]] and intends it to rely on [[normalized-payment-schedule]]. It responds to limitations of existing IRS Netting and ccs auto netting, which that draft describes as supplementary aggregation mechanisms bounded to IRS and CCS taxonomies.

The technical-design source describes the approach more specifically as determining aggregation readiness from normalized payment-schedule legs rather than product-specific cashflow interpretation. Under that design, [[normalized-payment-schedule]] calculates the expected number of eligible legs for a cashflow’s currency and payment date. [[netting-service]] compares that expected count with eligible received cashflow records having the same `tradeId`, currency, and payment date.

## Intended aggregation readiness rule

According to the technical-design source, automatic aggregation should not occur while the number of expected schedule legs exceeds the number of eligible received cashflows. In that condition, the cashflow is intended to enter a “pending another leg” outcome.

## Scope distinction

This concept concerns aggregation of cashflows. The functional-requirement source does not establish that it is equivalent to:

- Cross-product netting.
- Netting over netting.
- Replacement of all existing netting mechanisms.
- Aggregation of every cashflow or taxonomy in FMRP Flow.

Coexistence with IRS Netting and CCS Auto Netting remains unresolved in the functional-requirement source. Without explicit precedence and duplicate-prevention controls, parallel mechanisms could produce inconsistent or duplicate aggregation outcomes.

## Motivating limitation

The functional-requirement draft identifies a specific IRS scenario in which a trade’s second leg has multiple cashflows, a model said not to be supported by current IRS Netting. That source references ADO Story 15005868 but does not provide detailed expected behavior.

## Design limitations and unresolved controls

The technical-design source defines only a count comparison between expected schedule legs and eligible received cashflows. It does not establish:

- One-to-one leg identity.
- Duplicate protection.
- Amendment handling.
- Version correlation.
- A safe response when the received count exceeds the expected count.

Therefore, the technical-design source indicates that an explicit idempotency and reconciliation contract is required before the approach can be relied upon for settlement processing.