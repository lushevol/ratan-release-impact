---
type: concept
title: Netting Exception Recovery
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, exception-management, recovery, maker-checker]
related: [bilateral-netting, cashflow-hold-and-unhold, failed-cashflow-reinstatement, settlement-method-update, netting-withdrawal-timing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/01 Bilateral Netting.md"]
---
# Netting Exception Recovery

The bilateral-netting requirement demonstrates several exception paths that preserve or restore eligibility for later netting.

## Recovery paths

| Action | Intermediate state | Restored or resulting state |
|---|---|---|
| Manual Fail followed by Reinstate | `FAIL / NA` | `WAITING / Pending Netting` |
| Hold followed by Unhold | `Hold / NA` | `WAITING / Pending Netting` |
| Swift Suppression rejected by Checker | `WAITING / Swift Suppression` | `WAITING / Pending Netting` |
| Cashflow Suppression rejected | `WAITING / Cashflow Suppression` | `WAITING / Pending Netting` |
| Settle As Gross | `WAITING / Pending Netting` | `WAITING / Pending Exception`, `Settlement Method='Gross'` |

After restoration, the applicable cashflows can be selected for bilateral netting, subject to the normal eligibility key and state validations.

## Settle As Gross

Settle As Gross removes one cashflow from the netting population by changing its settlement method to `Gross`. The other eligible cashflows can still be netted into a bilateral-netting resultant.

## Scope

These transitions are specific to the scenarios in this bilateral-netting requirement. They should not be treated as universal contracts for all failure, hold, or suppression workflows without corroborating requirements.