---
type: query
title: What Is the Current Korea Settlement Onboarding and Contact Routing Status?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, korea, settlements, onboarding, contact-routing, data-quality]
related: [ratan, ratan-settlement-contact-routing, in-country-ops, korea-accounting-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Settlements Ops Contacts.md"]
---
# What Is the Current Korea Settlement Onboarding and Contact Routing Status?

## Open Question

Is `SCB SEOUL*SEL` / FMID `10036645` currently onboarded for settlement, and which operational contacts are authoritative?

## Evidence

The source contains two records for the same profile:

- `SOUTH KOERA` / `SCB SEOUL*SEL` / `10036645` states: “Not Onboarded yet for Settlement.”
- `KOREA` / `SCB SEOUL*SEL` / `10036645` lists `Control_Korea@sc.com`, `DOK_settle@sc.com`, `DOK_conf@sc.com`, and `JiHoon.Yang@sc.com` under In Country Ops.

This is a document-level contradiction. It does not establish the actual current onboarding state.

## Required Resolution

Confirm the current settlement onboarding status and authoritative contact list with the accountable settlement operations owner. Record an effective date and replacement process for the obsolete record, if any.

This contact-routing question must not be used to infer behavior of [[korea-accounting-reconciliation]] or other accounting integrations.