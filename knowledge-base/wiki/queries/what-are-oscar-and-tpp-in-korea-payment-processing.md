---
type: query
title: What Are OSCAR and TPP in Korea Payment Processing?
tags: [korea, payments, oscar, tpp, operational-risk]
related: [korea, korea-settlement-localization, cash-settlement, ratan-settlement]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Korea Migration Functional Analysis.md"]
---
# What Are OSCAR and TPP in Korea Payment Processing?

## Question

What do OSCAR and TPP denote, and what is the approved control model for manually handling Korea OUR payments, TPP cases, and decimal differences?

## Evidence

The source states that OUR payments and TPP-related cases may be manually keyed by OSCAR. It does not define whether OSCAR is a system, team, or user role. It also does not define TPP, identify the affected payment types, or describe approval, audit, reconciliation, or exception controls.

## Resolution needed

Confirm:

- the identity and responsibility represented by OSCAR;
- the meaning of TPP;
- the exact payment and decimal-difference scenarios;
- whether manual entry is temporary or permanent;
- maker/checker, audit, reconciliation, and duplicate-payment controls;
- the required owner and go-live acceptance evidence.

Until resolved, the manual process should be treated as a potential operational-risk item rather than an approved target-state design.