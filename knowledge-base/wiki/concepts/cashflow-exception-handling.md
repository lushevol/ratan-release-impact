---
type: concept
title: Cashflow Exception Handling
tags: [cashflow, exceptions, blotter, nacks, settlement]
related: [cash-settlement, cashflow-status-handling, reconciliation, swift-status-reconciliation]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes.md"]
---
# Cashflow Exception Handling

Cashflow exception handling covers the detection, visibility, filtering, approval, reversal, rebooking, and downstream processing of settlement exceptions.

The 2024 scope includes COM-status consumption from TDS3, maker/checker affirmation, bulk approval, NACK handling from FMSRE/AMH, withdrawal after released netting, reversal and rebook, non-economic changes, and SCPAY SSI validation.

The UK/Germany scope additionally requires exceptions to be displayed in the cashflow blotter and filtered by exception type. NACK handling depends on downstream integration, including FM Swift Gateway and Razor/FMSGW-related components.