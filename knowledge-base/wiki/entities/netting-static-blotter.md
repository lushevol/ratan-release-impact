---
type: entity
title: Netting Static Blotter
created: 2026-08-22
updated: 2026-08-23
tags: [netting, static-data, configuration, cash-settlement, blotter]
related: [auto-netting-rule-management, cashflow-auto-netting, cash-settlement-home-page, pending-auto-netting-state, bilateral-netting, bilateral-netting-eligibility, ccil-manual-netting, ccil-netting-eligibility-key, cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Business user case testing.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/01 Bilateral Netting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/02 CCIL Netting.md"]
---
# Netting Static Blotter

## Role

The Netting Static Blotter is a static-data interface and configuration surface for creating and maintaining netting rules. The source versions describe its use in auto-netting, manual bilateral-netting, and manual CCIL-netting contexts.

## Auto-netting configuration

In the auto-netting business user cases, the Netting Static Blotter is used to create, activate, update, disable, and inspect auto-netting rules for [[cashflow-auto-netting]].

The tested configuration responsibilities include:

- Netting type, including bilateral, CCIL, and BIC scenarios.
- Netting date and time, such as `VD-1 9:00` and `VD 09:00`.
- STP level, including `NSTP_MAKER_CHECKER` and `NSTP_CHECKER_ONLY`.
- Eligibility predicates involving SCI FMIDs, settlement method, counterparty BIC-netting flags, products, and empty netting IDs.

The auto-netting testing source reports the following behavior:

- Creating a new rule can refresh existing cashflows into `WAITING / Pending Auto Netting`.
- Updating a rule appears to refresh only cashflows matching the updated rule.
- Disabling a rule removes the `Pending Auto Netting` sub-state.

The update and disablement findings are qualified because their evidence is incomplete or affected by automated triggers.

Rule identity also appears to constrain aggregation: cashflows assigned to different rules are not combined even when other attributes match. See [[cross-rule-netting-isolation]] and [[netting-scenario-priority]].

## Manual bilateral-netting configuration

In the bilateral-netting business user case, the Netting Static Blotter is described as the configuration surface used to create and maintain manual netting rules.

A manual netting rule must be live before eligible cashflows can be netted. The rule establishes the conditions under which cashflows may participate in the operation.

That source does not define:

- The complete rule schema.
- Rule versioning or effective dates.
- Whether changes are reevaluated against already-booked cashflows.
- The behavior of disabling or updating a rule after cashflows enter `Pending Netting`.

The proposed “Manual Netting Refresh” scenario is struck through and marked `Confirm`; it is therefore not an active acceptance criterion.

## Manual CCIL-netting configuration

In the CCIL acceptance cases, the Netting Static Blotter is the interface where manual netting rules are created and made live.

According to the CCIL source, a live manual rule causes qualifying cashflows to enter `WAITING` with sub-state `Pending Netting`.

The CCIL source includes struck-through historical cases concerning:

- Rule disablement.
- Rule updates.
- CCIL-versus-Bilateral-rule precedence.

Those historical cases are not active requirements. See [[what-is-the-authoritative-ccil-netting-rule-precedence-and-refresh-behavior]].
