---
type: query
title: What Is the Authoritative FXU Util Type Enumeration and Validation Precedence?
created: 2026-08-23
updated: 2026-08-23
tags: [fxu, ratan, utilization, util-type, validation]
related: [fxu, ratan, fxu-utilization-type-taxonomy, fxu-ratan-utilization-response-contract, utilization-status-lifecycle, partial-and-pastdue-utilization-accounting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Util Response ACK NACK.md"]
---
# What Is the Authoritative FXU Util Type Enumeration and Validation Precedence?

The source uses `UTIL`, `REV`, `PADU`, `EARLY`, `PART`, `FULL`, `VDATE`, and `PADU-%-REV`, but does not define a canonical enumeration, composition grammar, or parsing model.

It also does not specify which NACK must be returned when a request fails multiple validations. This is material because MVP-rejection rules coexist with Phase 2 eligibility, amount, and timing rules.

## Required Resolution

Confirm:

1. valid `Util_Type` tokens and permitted combinations;
2. MVP versus Phase 2 availability and current implementation status;
3. canonical cashflow-state and sub-state values; and
4. deterministic validation ordering and NACK precedence.