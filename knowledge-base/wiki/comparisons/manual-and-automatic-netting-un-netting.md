---
type: comparison
title: Manual and Automatic Netting Un-Netting
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, un-netting, lifecycle, comparison]
related: [bilateral-netting, netting-resultant-cashflow-lifecycle, netting-withdrawal-timing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/01 Bilateral Netting.md"]
---
# Manual and Automatic Netting Un-Netting

The source defines two distinct ways to reverse a netting relationship.

| Aspect | Manual un-netting | Automatic un-netting |
|---|---|---|
| Trigger | User selects a resultant and chooses `Un-Net Cashflow` | A component is withdrawn while the resultant is neither `SETTLED` nor `RELEASED` |
| User interaction | Component details are displayed; user selects `Un-Net all Cashflow` | No explicit user un-net action is specified |
| Resultant state | N1 becomes `DEAD` | N1 becomes `DEAD` |
| Component outcome | Components return to `WAITING / Pending Netting` | Withdrawn component becomes `CANCELLED`; remaining components return to `WAITING / Pending Netting` |
| Further processing | Components may be netted again | Remaining components may be netted into a new resultant, such as N2 |
| Authorization and audit | Not defined beyond the stated UI action | Not defined |

The source does not establish parity for audit events, user attribution, checker approval, or resultant lineage.