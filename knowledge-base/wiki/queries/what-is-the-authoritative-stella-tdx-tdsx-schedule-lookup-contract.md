---
type: query
title: What Is the Authoritative Stella TDX TDSX Schedule Lookup Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [Stella, TDX, TDSX, TDS3, IRS, API]
related: [tdsx, stella, pending-another-leg-status, irs-fixed-floating-leg-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/IRS Fix Leg & Floating leg payment handling.md"]
---
# What Is the Authoritative Stella TDX TDSX Schedule Lookup Contract?

The requirement refers to TDX for cashflow-count comparison, TDSX as the schedule API, and TDS3 in the FMRP booking lineage. It does not establish whether these names identify separate systems, datasets, or interfaces.

## Questions to Resolve

- Which system is authoritative for IRS payment-schedule lookup?
- What endpoint, authentication, availability, timeout, and retry requirements apply?
- Is the bypass condition a payment date found on only one leg, absent from both legs, or another test?
- How are time zones, business-day adjustments, duplicate dates, and amended schedules normalized?
- What should RATAN do if the lookup fails or returns incomplete schedule data?

Resolution is required because an incorrect schedule interpretation may either block valid standalone cashflows or permit incomplete IRS schedules to settle.