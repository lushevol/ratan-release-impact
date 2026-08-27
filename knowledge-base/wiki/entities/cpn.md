---
type: entity
title: CPN
created: 2026-08-23
updated: 2026-08-23
tags: [cpn, cash-settlement, netting, service]
related: [cpn-service, cpn-netting, cpn-netting-reversal-cashflow, netting-resultant-cashflow, entities/stella, entities/cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CPN Tech Design - Draft for now.md"]
---
# CPN

CPN is the netting process or service identified in the draft technical design for Cash Settlement. It evaluates or processes CPN-eligible cashflows, creates netting resultants, updates component states, performs automatic un-netting after trade events, and creates reversal cashflows when a released resultant must be cancelled.

## Responsibilities described in the draft

- Associate selected components with a Netting ID such as `N001`.
- Move netted components to `Netted` and remove them from the Cashflow Blotter.
- Create a queued resultant cashflow.
- Support resultant `Netting Review` and checker approval.
- Automatically un-net prior netting when a newer component version is created.
- Create a reversal cashflow such as `C106` for a released resultant such as `C105`.

The source uses both `CPN` and `CPN Service`. The exact boundary between the process name and the application service is not formally defined.