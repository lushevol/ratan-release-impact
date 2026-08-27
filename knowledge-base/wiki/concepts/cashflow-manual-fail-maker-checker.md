---
type: concept
title: Cashflow Manual Fail Maker-Checker Control
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, manual-fail, maker-checker, segregation-of-duties, audit]
related: [cash-settlement-home-page, bulk-cashflow-manual-fail, cashflow-pre-fail-state-restoration, fmo-ops-manual-fail-profiles, maker-checker-ssi-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Bulk Fail.md"]
---
# Cashflow Manual Fail Maker-Checker Control

## Purpose

The maker-checker control prevents one user from submitting and approving the same cashflow manual-fail request. It applies to both bulk manual fail and the existing single-cashflow manual fail action.

## Workflow

1. A maker selects one or more eligible cashflows.
2. The maker enters a mandatory comment and submits the manual-fail request.
3. Each selected cashflow moves to `WAITING / Pending Manual Fail / Pending Verification`.
4. A different user acts as checker.
5. The checker enters a mandatory comment and approves or rejects the request.
6. Approval moves the cashflow to `FAILED / NA / NA`; rejection restores the pre-fail state.

## Segregation of duties

The maker cannot act as checker for the same request. For the maker, the `Confirm Manual Fail` action is disabled and shows:

```text
For Cashflow XXX , Maker and checker cannot be the same account
```

The requirement compares this behavior with the control used for Swift suppression, but it does not establish that the two workflows share the same implementation or authorization rules.

## Comment control

Comments are mandatory at both stages:

- The maker must provide a comment to submit manual fail.
- The checker must provide a comment to approve or reject.

The source does not define comment length, character restrictions, retention, or whether a bulk comment is stored once per request or separately for each cashflow.

## Authorization

The listed profiles are documented in [[entities/fmo-ops-manual-fail-profiles]]. The source does not specify whether all profiles can perform both maker and checker actions.
