---
type: query
title: Who Owns the Tactical Ratan CCIL Client Static Data and Its Retirement?
created: 2026-08-22
updated: 2026-08-22
tags: [CCIL, Ratan, static-data, ownership, Murex-2-11, decommissioning, open-question]
related: [ccil-non-guaranteed-client-static-data, ccil-settlement-method-stamping, ratan, murex-2-11, configuration-driven-onboarding]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CCIL Netting.md"]
---
# Who Owns the Tactical Ratan CCIL Client Static Data and Its Retirement?

## Question

Which team owns the accuracy, approval, maintenance, audit evidence, and retirement of the tactical Ratan copy of Murex 2.11 non-guaranteed CCIL client static data?

## Known Facts

The source states that:

- Murex 2.11 logical static data is the current source for the client list.
- Ratan copies and maintains the list as local logical static data.
- The tactical copy is expected to be discarded after Murex 2.11 decommissioning.
- There is no clear ownership for the Murex 2.11 CCIL static data.
- Permanent FMID additions can require a CR, UAT, and release process lasting weeks.
- Temporary NSTP rules can be used for newly onboarding clients, with manual Nostro verification and manual SWIFT suppression.

## Required Resolution

Identify the authoritative golden source, data owner, operational approver, quality controls, change and rollback process, Murex 2.11 decommission date, retirement trigger, and migration plan. The BAU policy allowing additional FMIDs on a pre-tested NSTP rule without new UAT should also have documented risk acceptance and monitoring.