---
type: query
title: What Is the Authoritative Trade Confirmation Correlation Key by Source System?
created: 2026-08-23
updated: 2026-08-23
tags: [confirmation, correlation, trade-id, versioning, open-question]
related: [murex-2-11, stella, cdu-lake, ratan, trade-event-id-lineage, trade-cashflow-reference-linkage, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--15-deprecated-docs--53-c--1d13ogn]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Copy of Trade Confirmation & Cashflow STP - Deprecated.md"]
---
# What Is the Authoritative Trade Confirmation Correlation Key by Source System?

A deprecated requirement specifies `Trade_ID` only for Murex 2.11 confirmation notifications and `Trade_Id + Trade Major Version` for Stella notifications.

Validate the active correlation key, whether versions are required or populated for each source, and how amendments, cancellations, revives, and late events are prevented from applying confirmation status to the wrong cashflow generation.