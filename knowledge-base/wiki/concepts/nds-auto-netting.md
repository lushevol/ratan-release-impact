---
type: concept
title: NDS Auto Netting
created: 2026-08-22
updated: 2026-08-22
tags: [NDS, auto-netting, RATAN, cash-settlement]
related: [ratan, murex-2-11, nds-netting-key, pending-nds-netting, net-resultant-cashflow, nds-duplicate-payment-prevention, cashflow-blotter-action-eligibility, confirmation-match-driven-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/NDS Auto Netting.md"]
---
# NDS Auto Netting

NDS Auto Netting is the proposed RATAN process for aggregating eligible NDS-related component cashflows into a single net resultant cashflow.

Murex 2.11 is required to stop performing NDS netting. RATAN scans every 30 minutes, compared with the current two-hour Murex cycle, for cashflows whose value dates fall on today, tomorrow, or the next business day.

Eligibility requires the composite [[concepts/nds-netting-key]], `WAITING` status, and the live `Pending NDS Netting` exception. Components must pass through the Group Blotter before entering the netting workflow.

The process is reversible before resultant release. After release, reversals and replacements are held for manual Operations handling, and un-netting is prohibited.