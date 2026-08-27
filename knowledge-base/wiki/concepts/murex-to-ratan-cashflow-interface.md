---
type: concept
title: Murex-to-Ratan Cashflow Interface
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, cashflow, settlement, mq, lifecycle]
related: [murex, ratan, ratan-one, mxml-to-scbml-conversion, murex-flow-group-batch-handling, event-driven-component-cashflow-status-management, what-is-the-authoritative-murex-cashflow-publication-window]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Ratan MxML- SCBML Adaptor ( Entity CN, SG, IN, MY).md"]
---
# Murex-to-Ratan Cashflow Interface

The Murex 2.11 to Ratan interface publishes one MxML payment message per cashflow through MQ. The Ratan MxML-SCBML Adaptor converts the message into Ratan’s SCBML cashflow representation.

## Status handoff

The documented Murex 2.11–Ratan lifecycle is:

```text
Murex INIT
  → Murex publishes to Ratan
  → Murex SNTR
  → Ratan acknowledges receipt
  → Ratan RELEASED
  → Murex RSLR
```

Ratan `SETTLED` is explicitly not synchronized back to Murex. Therefore, Murex `RSLR` should not be interpreted as proof that the cashflow reached final Ratan settlement.

## Publication model

The interface distinguishes:

- scheduled publication for existing cashflows on weekdays; and
- immediate publication for newly booked cashflows whose value date falls within the configured future window.

The exact future-window rule is unresolved because the source describes both nine calendar days and seven business days. See [[what-is-the-authoritative-murex-cashflow-publication-window]].

## Scope boundary

Murex is the payment-event producer and Ratan is the receiving settlement platform. Murex product-level auto-netting of swap legs occurs before cashflows are transmitted to Ratan and is separate from Ratan-side netting processes.

## Reconciliation implication

Because final `SETTLED` status is absent from the feedback path, operational reconciliation requires a Ratan-side source for final-settlement confirmation. The interface design alone does not define the reconciliation process.