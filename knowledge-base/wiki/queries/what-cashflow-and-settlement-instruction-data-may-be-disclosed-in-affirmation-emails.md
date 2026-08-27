---
type: query
title: What Cashflow and Settlement Instruction Data May Be Disclosed in Affirmation Emails?
created: 2026-08-23
updated: 2026-08-23
tags: [email, data-privacy, settlement-instructions, beneficiary-account, cashflow, masking]
related: [email-based-cashflow-affirmation, sci, murex, cashflow-auto-netting, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--vhh9uf]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation.md"]
---
# What Cashflow and Settlement Instruction Data May Be Disclosed in Affirmation Emails?

The candidate affirmation-email payload includes beneficiary account numbers, beneficiary bank BICs, and beneficiary correspondent BICs. The source only suggests partial account-number masking, for example `XXX XXX 51869`, without defining a security or privacy policy.

The authoritative requirement must determine:

- Final mandatory and optional fields.
- Whether `Booking_Entity_SCI_FMCODE` and `Counterparty_SCI_FMCODE` are displayed as raw FMCODEs or converted display names.
- The required handling of netted resultant cashflows, including literal `Net` for Trade ID and optional or blank fields.
- Account-number masking format and whether BIC values may be disclosed.
- Recipient entitlement, email encryption, template access, retention, and audit requirements.
- Data classification and applicable privacy controls.
- The canonical capitalization and field paths for settlement-instruction attributes.

No sensitive settlement-instruction data should be assumed approved for email distribution based solely on the draft mapping.