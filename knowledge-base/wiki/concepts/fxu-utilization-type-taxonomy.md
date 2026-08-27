---
type: concept
title: FXU Utilization Type Taxonomy
created: 2026-08-23
updated: 2026-08-23
tags: [fxu, utilization, util-type, mvp, phase-2]
related: [fxu, ratan, fxu-ratan-utilization-response-contract, partial-and-pastdue-utilization-accounting, utilization-status-lifecycle, what-is-the-authoritative-fxu-util-type-enumeration-and-validation-precedence]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Util Response ACK NACK.md"]
---
# FXU Utilization Type Taxonomy

`Util_Type` is the request classification used by [[ratan]] to select utilization validation rules. The source uses `UTIL`, `REV`, `PADU`, `EARLY`, `PART`, `FULL`, and `VDATE`, including combinations such as `FULL, UTIL`, `FULL, REV`, and `PADU-%-REV`.

## Documented Scope

For MVP, RATAN explicitly rejects requests containing:

- `REV` — reverse utilization;
- `PADU` — past-due utilization;
- `EARLY` — early utilization; and
- `PART` — partial utilization.

The implied supported path is full standard utilization, subject to the remaining validations. The document contains Phase 2 rules for reversal, past-due reversal, non-full classifications, and `MISSING_INFO`; it does not confirm their delivery.

## Timing and Amount Rules

The intended date predicates require `EARLY` before payment date, `PADU` after payment date, and `VDATE` on payment date. `FULL, UTIL` must match `Ratan.Remaining_Amount`. Separate Phase 2 reversal checks compare full-reversal and reversal amounts.

The authoritative enumeration, token grammar, legal combinations, and rule priority are unknown. This is tracked in [[what-is-the-authoritative-fxu-util-type-enumeration-and-validation-precedence]].