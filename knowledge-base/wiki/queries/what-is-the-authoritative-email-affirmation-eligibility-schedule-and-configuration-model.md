---
type: query
title: What Is the Authoritative Email Affirmation Eligibility, Schedule, and Configuration Model?
created: 2026-08-23
updated: 2026-08-23
tags: [affirmation, email, scheduling, eligibility, configuration, cashflow]
related: [email-based-cashflow-affirmation, affirmation-driven-cashflow-release, ratan, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--vhh9uf]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation.md"]
---
# What Is the Authoritative Email Affirmation Eligibility, Schedule, and Configuration Model?

The requirement suggests `VD -1` as a possible email-dispatch time but does not approve it or define alternatives.

The authoritative design must determine:

- Eligible booking entities, cashflow types, payment-date windows, statuses, and exception codes.
- Whether gross and netted resultant cashflows have distinct eligibility rules.
- Scheduling across time zones, regional calendars, settlement cutoffs, and resend windows.
- Whether rules, templates, recipients, and sender properties are hard-coded or dynamically configured.
- Ownership, authorization, maker-checker controls, audit history, and effective-dating for configuration changes.
- Whether a cashflow may be included in more than one email batch.

Until resolved, no particular `VD -1` schedule or eligibility rule should be treated as implemented behavior.