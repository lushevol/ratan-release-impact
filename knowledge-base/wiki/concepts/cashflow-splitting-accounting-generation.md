---
type: concept
title: Cashflow Splitting Accounting Generation
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-splitting, accounting, suppression, child-cashflow, EBBS]
related: [cashflow-splitting, ratan-accounting-service, ebbs, ratan, uat-test-case]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT/Cashflow Splitting UAT For EBBS.md"]
---
# Cashflow Splitting Accounting Generation

This concept describes the tested relationship between a child cashflow action and accounting information generation in the EBBS cashflow-splitting flow.

## Tested rule

| Child outcome or action | Accounting information in the tested flow |
|---|---|
| Partial release | Generated |
| `swift_suppress` | Generated |
| `cashflow_suppress` | Not generated |
| Child failure | Generated |

The rule is supported by four passing manual-split scenarios for gross cashflows. It is an observed UAT behavior, not a complete accounting specification.

## Automatic flows

The UAT also passed for:

- Automatic splitting of a gross cashflow where all children were released and accounting information was generated.
- Automatic distribution over a net resultant cashflow where all children were released.

The source does not state whether accounting information is generated once per child, once per parent, or once per eligible accounting event.

## Validation artifact

Accounting behavior was checked using records in [[entities/ratan-accounting-service]], specifically the `ratan_accounting_request_task` table. The source provides a query but no result set or payload contents. Consequently, the evidence does not independently verify request counts, field values, or the contents of `request_info`.

## Boundaries

`swift_suppress` and `cashflow_suppress` must be treated as distinct actions. The child-failure result must not be generalized to all RATAN failure or AutoFail states until the exact tested state and workflow are confirmed.