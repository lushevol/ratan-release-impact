---
type: stakeholder
title: Front Office
created: 2026-08-24
updated: 2026-08-24
tags: [front-office, murex-211, trade-lifecycle, cashflow]
related: [murex-211, ratan, trade-validation-cashflow-gating, non-economic-cashflow-amendment-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/UAT test cases - Murex 2.11 booking.md"]
---
# Front Office

Front Office (FO) is an operational role in the Murex 2.11 trade lifecycle. The source assigns FO responsibility for booking trades, moving trade statuses, modifying trades, performing C&R, removing market events, cancelling trades, and initiating payment publication to RATAN.

FO actions create or alter the trade and cashflow lineage that [[entities/ratan]] evaluates. Validation may be performed through an FO/MO workflow, depending on the scenario.

The source does not identify named individuals, a formal team owner, or approval controls for FO actions.