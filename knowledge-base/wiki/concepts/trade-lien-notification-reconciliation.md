---
type: concept
title: Trade Lien Notification Reconciliation
created: 2026-08-23
updated: 2026-08-23
tags: [lien, notification, reconciliation, tds3, cashflow-reprocessing]
related: [ratan, tds3, murex, lien-driven-cashflow-nstp, cashflow-lifecycle-state-machine, what-is-the-authoritative-parent-trade-id-scbml-path-for-lien-correlation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Lien Settlement Process - Cashflow Migration/RATAN Cashflow Process with Lien - Function Specs.md"]
---
# Trade Lien Notification Reconciliation

Trade lien notification reconciliation addresses out-of-order arrival between Murex cashflows and TDS3 trade updates.

RATAN initially queries TDS3 when it receives a cashflow. If the cashflow arrives before the corresponding lien-bearing trade update, it may initially have no **“LIEN on Trade”** exception. A later TDS3 trade notification is intended to identify cashflows through original trade ID and trigger corrective processing.

The source specifies that `WAITING` cashflows with `Sub Status Type == 'Pending Exception'`, and `HOLD` or `READY` cashflows, should be reprocessed when lien is present and the exception is missing.

Only `VALD` and `COMP` notifications are consumed “by priority” in the stated design. The source does not define the ordering between these statuses or the disposition of other notifications. Therefore, the requirement provides eventual correction rather than evidence of instantaneous NSTP protection.