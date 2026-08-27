---
type: query
title: What Is the Authoritative LMS Routing Policy for Jersey, ZHENGZHOU, and TAEYUAN?
created: 2026-08-22
updated: 2026-08-22
tags: [lms, routing, jersey, zhengzhou, taeyuan]
related: [lms, jersey, zhengzhou, taeyuan, entity-onboarding-static-data-controls]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch3  Static data go live checklist.md"]
---
# What Is the Authoritative LMS Routing Policy for Jersey, ZHENGZHOU, and TAEYUAN?

## Question

What source of truth, configuration, owner, and test evidence govern LMS routing for the Tranche 3 entities?

## Evidence

ADO story `9920605` records the intended policy:

- [[jersey]] must not flow to [[lms]];
- [[zhengzhou]] must flow to LMS; and
- [[taeyuan]] must flow to LMS.

The source does not identify the LMS configuration location, operational owner, or test outcome.

## Information needed

- Authoritative routing specification;
- implemented filter configuration;
- integration and negative-test results; and
- accountable owner for production routing changes.