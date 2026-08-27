---
type: query
title: What Is the FMRP Murex Fix-Flag File Correlation and Retry Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [Murex, FMRP_MUREX_FIX_FLAG, file-processing, idempotency, reconciliation]
related: [murex-pending-fixing-flag-processing, murex, pending-another-leg-status]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/IRS Fix Leg & Floating leg payment handling.md"]
---
# What Is the FMRP Murex Fix-Flag File Correlation and Retry Contract?

`FMRP_MUREX_FIX_FLAG` provides `FLOW_ID;WAIT_FIX` updates for cashflows blocked by `Fixing Unknown`. The source specifies target-status eligibility but does not define the operational integration contract.

## Questions to Resolve

- Does `FLOW_ID` identify the RATAN cashflow, Murex cashflow, message flow, or another object?
- What makes a file row idempotent?
- How are duplicate, conflicting, delayed, or missing rows handled?
- What ordering is required between a fixed-leg reversal and its net resultant?
- What audit and reconciliation records are required for ignored or failed rows?

Resolution is required to prevent an unresolved provisional cashflow from remaining indefinitely blocked or being processed out of order.