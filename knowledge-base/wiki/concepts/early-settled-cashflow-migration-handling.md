---
type: concept
title: Early-Settled Cashflow Migration Handling
tags: [cashflow, migration, duplicate-payment, settled-status, cn]
related: [cn-trade-migration, murex-2-11, stella, ratan, lms, razor, oscar, cashflow-status-lifecycle, cashflow-netting-and-un-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Trade Migration - Settlement Process.md"]
created: 2026-08-23
updated: 2026-08-23
---
# Early-Settled Cashflow Migration Handling

An early-settled overlap arises when a cashflow with a future value date is paid through Murex 2.11 before a migration weekend, then recreated from the migrated trade in Stella. Without a migration control, the Stella cashflow can be processed as a new payment in Ratan.

## Preferred approach

The source prefers moving the matching Stella cashflow from `PROJECTED` to `SETTLED` in a batch status-only operation. This marks the Stella representation as economically settled without processing a second payment.

Required guardrails are:

- the migration programme supplies the eligible cashflow-ID list;
- the operation is status-only;
- no message is sent to [[razor]];
- no SWIFT message is generated; and
- only the matching overlap cashflows are updated.

This is a functional proposal, not confirmation of an implemented control.

## Amendment behaviour

The source contrasts this approach with suppression. With synthetic `SETTLED` status, a later amendment can create a withdrawal for the prior 100 and a new cashflow for 120. Ratan is expected to net these to a new payment of 20.

The example does not prove universal netting eligibility or test coverage. Individual recall and resettlement may still require [[oscar]] and [[settlement-ops]].

## Downstream caveat

A migration-control `SETTLED` status does not necessarily mean that payment was initiated through the current Stella/Ratan/Razor path. [[lms]] treatment of this distinction remains unresolved.