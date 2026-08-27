---
type: concept
title: Settle as Gross Maker/Checker Workflow
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, settlement, maker-checker, exceptions, gross-settlement]
related: [ratan, multi-exception-resolution-handling, netting-exception-recovery]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Service - GUI & API intergration.md"]
---
# Settle as Gross Maker/Checker Workflow

**Settle as Gross** is a maker/checker route that allows Settlement Ops to stop waiting for netting and process eligible cashflows as gross.

## Eligibility

The maker can initiate the action for cashflows in `WAITING` with either:

- `Pending Netting / Pending Operator`
- `Pending Another Leg / Pending Operator`

## Approval path

1. A Settlement Ops maker selects **Settle as Gross**.
2. The cashflow remains `WAITING` but moves to `Pending Exception / Pending Verification/Operator`.
3. RATAN generates a checker-only `Settle As Gross` exception, alongside any other applicable exceptions.
4. An exception-fix checker approves the multiple exceptions.
5. The cashflow becomes `READY`.

The `Settle As Gross` exception is not visible to the exception-fix maker.

## Unresolved rejection path

The requirement says a checker who does not agree may perform ad hoc netting on grossed cashflows. It does not define a rejection event, intermediate state, exception disposition, or whether the maker request must first be rejected. This remains an incomplete workflow boundary.