---
type: query
title: What Is the Authoritative COV SWIFT Status Display Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, swift, fmsgw, cov, status-display, ambiguity]
related: [fmsgw-deletion-driven-cashflow-settlement, fmsgw, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--198hh9i]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow status sync with FMSGW deletion.md"]
---
# What Is the Authoritative COV SWIFT Status Display Rule?

The requirement defines `Check in FMSGW` as the condition where MT103 and MT202 COV receive different FMSGW response values.

However, a business use case says that when both messages receive a deleted response, the SWIFT status should show `Check in FMSGW`. This is ambiguous if both deletion values are identical.

## Decision Needed

Define the UI/display rule for all COV response combinations:

- identical allowed terminal statuses;
- different allowed terminal statuses;
- allowed terminal status plus error;
- pending, absent, or unrecognized response.

The answer should distinguish the display indicator from the independent cashflow settlement rule defined in [[fmsgw-deletion-driven-cashflow-settlement]].