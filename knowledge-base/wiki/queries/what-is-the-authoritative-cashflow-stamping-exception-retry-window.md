---
type: query
title: What Is the Authoritative Cashflow Stamping Exception Retry Window?
created: 2026-08-24
updated: 2026-08-24
tags: [SSI, cashflow, retry, recency-window, open-question]
related: [ssi-change-notification-re-stamping, cashflow, eventual-consistency-for-cashflow-exceptions-and-swift-status]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design/SSI Stamping Implementation(SCBML).md"]
---
# What Is the Authoritative Cashflow Stamping Exception Retry Window?

The documented impact queries restrict records with `updated_at >= current_date - 6`. The source does not explain why the window is six days or whether it is a business-date, calendar-date, or timestamp-based boundary.

## Questions to resolve

- Why are records older than six days excluded?
- Is the window aligned with payment-date ranges or operational settlement procedures?
- Should the predicate use a timestamp and explicit timezone?
- What happens to an unresolved exception after the window expires?
- Is the six-day value configurable?