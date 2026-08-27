---
type: query
title: What Does C&R Mean in Murex Trade and Cashflow Events?
created: 2026-08-23
updated: 2026-08-23
tags: [murex, terminology, cashflow-lifecycle, event-ordering, cancellation]
related: [murex, ratan, what-is-the-authoritative-murex-cancellation-removal-cashflow-sequencing-and-correlation-model, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--15-deprecated-docs--28-m--1b3wu0h]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Murex Trade & Cashflow Events.md"]
---
# What Does C&R Mean in Murex Trade and Cashflow Events?

## Question

What does `C&R` formally mean in the Murex trade and cashflow-event process, and what does `C&R Removal` reverse or remove?

## Why it matters

The deprecated source uses `C&R` and `C&R Removal` in scenarios involving repeated events, out-of-order cashflow receipt, and trade-ID reversion to `T1`. Without an authoritative definition, `C&R` cannot safely be equated with cancellation, correction, rebooking, reversal, withdrawal, or another lifecycle action.

## Information required

- The expanded term and formal Murex event name.
- Preconditions and state transitions for `C&R` and `C&R Removal`.
- Cashflow creation, withdrawal, reversal, and replacement behavior for each event.
- The identifiers and versions that correlate repeated `C&R` events and removal events.
- Whether the term is Murex-native, an interface-specific abbreviation, or local operational shorthand.

## Evidence and boundary

The source supplies no definition. This query exists to prevent unsupported lifecycle interpretations in [[what-is-the-authoritative-murex-cancellation-removal-cashflow-sequencing-and-correlation-model]].