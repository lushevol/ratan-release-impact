---
type: query
title: Are the Tranche 3 Suppression Rule Configurations Deployed and Validated in Production?
created: 2026-08-22
updated: 2026-08-22
tags: [tranche-3, suppression, uat, production-readiness]
related: [cashflow-suppression-vs-swift-suppression, payment-and-cashflow-suppression-governance, fmrp, jersey, release-readiness-attestation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch3  Static data go live checklist.md"]
---
# Are the Tranche 3 Suppression Rule Configurations Deployed and Validated in Production?

## Question

Were the listed UAT suppression rules promoted to production, validated, approved, and made recoverable?

## Evidence

The source identifies these UAT rule IDs:

- `7374420229233111040` for deliverable-currency SWIFT suppression;
- `7369258354199584768` for metal-currency cashflow suppression; and
- `7369288575163731968` for the `Non FMRP entities` cashflow-suppression rule, including Jersey FMID `400910415`.

No production rule IDs, deployment records, test results, approval evidence, or rollback procedures are supplied.

## Information needed

- Production rule identifiers and effective dates;
- deployment and change records;
- test evidence for suppression behaviour and rule precedence;
- confirmation that `SAUDI` remained unchanged; and
- rollback or reversal procedure.