---
type: concept
title: Ratan Cashflow ID Management
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, cashflow-id, normalization, netting, split]
related: [ratan, stella, murex-2-11, mxcash, concurrency-safe-id-allocation, ratan-cash-settlement-netting, cash-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/LifeCycle/Cashflow & Payment cashflow id management.md"]
---
# Ratan Cashflow ID Management

Ratan cashflow ID management distinguishes imported cashflows from cashflows created by Ratan processing.

## Identifier formats

- [[stella]] IDs are preserved when supplied as 12-character values.
- [[murex-2-11]] IDs use `M` followed by a zero-padded numeric source value, for a total of 12 characters.
- [[mxcash]] Razor IDs use `R` followed by a zero-padded numeric source value, for a total of 12 characters.
- Netting-result IDs use `N` plus an 11-digit auto-incrementing value.
- Split-result IDs use `S` plus an 11-digit auto-incrementing value.

The prefix is therefore both a format component and a source or lifecycle indicator. It must not be interpreted as a general transformation rule for systems not named in the requirement.

## Uniqueness boundary

The requirement states that cashflow IDs must be unique across Ratan services and processes. It also requires concurrency consideration for manual and automatic netting or split requests.

No mechanism is specified for sequencing, persistence, failure recovery, or validation of malformed inputs. [[concurrency-safe-id-allocation]] describes the control objective, while [[how-is-ratan-cashflow-id-uniqueness-enforced]] tracks the unresolved implementation decision.