---
type: query
title: What Are the Authoritative Trade Validation Status Mappings?
created: 2026-08-24
updated: 2026-08-24
tags: [query, trade-validation, status-model, Stella, Murex-2-11, TDS3, RATAN]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--34-trade-validation-cashf--mg1utu, trade-validation-gated-cashflow-visibility, trade-major-version-cashflow-correlation, cashflow-lifecycle-state-model, fmrp-cashflow-status-synchronization, fmrp-murex-cashflow-status-synchronization, scbml-cashflow-payload]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process.md"]
---
# What Are the Authoritative Trade Validation Status Mappings?

## Question

What is the canonical definition of a validated trade across cashflow SCBML, Stella parent-trade lookups, Murex 2.11 parent-trade lookups, and TDS3 validation messages?

## Evidence from the requirement

The document lists the following accepted values:

- Cashflow SCBML: Murex `VALD` and `CONFIRMED`; other sources `SENT`, `ECONAFFIRMED`, `AFFIRMED`, `ECONCONFIRMED`, `CONFIRMED`, and `NONCONFIRMED`.
- Stella parent trade: `TOBESENT` with `Validate`, or `SENT`, `ECONAFFIRMED`, `AFFIRMED`, `ECONCONFIRMED`, `CONFIRMED`, and `NONCONFIRMED`.
- Murex parent trade: `VALD` or `COMP`.

## Ambiguities to resolve

The source does not explain whether `NONCONFIRMED` is intentionally treated as validated, whether `TOBEVALIDATED` is an intermediate state excluded from the accepted set, or whether `COMP` means validation completion rather than validation. It also uses inconsistent field headings around the Murex status table.

The authoritative answer should specify state values, required action combinations, source-system scope, version semantics, and behavior for unknown or out-of-order statuses.