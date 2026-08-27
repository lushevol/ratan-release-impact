---
type: concept
title: Netting on Netting
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, netting, controls, ktlo]
related: [auto-netting, maker-checker-segregation, settlement-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/2025 backlog.md"]
---
# Netting on Netting

Netting on Netting refers to applying another netting operation to obligations or payments that have already been netted.

## Proposed Control

ADO 6473084 proposes blocking Netting on Netting, with an explicit exception for netting on IRS Fixed + Floating auto-netted payments.

This is a narrowly scoped backlog requirement. It should not be generalized into either a universal prohibition or unrestricted support for repeated netting.

## Related Backlog Items

The same source includes several related [[auto-netting]] items:

- Auto Netting for Swap Agent Clearing Payment.
- NDS Auto Netting for SG.
- Removal of BIC netting tagging after “settle as gross.”
- Permission for the user who performed netting to act as Checker.
- A warning where net resultant cancellation requires manual Swift cancellation.

The checker exception may create tension with strict [[maker-checker-segregation]], but the source does not explain which controlled action the Checker approves or what compensating controls apply.