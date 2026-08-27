---
type: project
title: Hong Kong Physical Gold Settlement
status: planned
owner: ""
start_date: ""
target_date: ""
created: 2026-08-22
updated: 2026-08-22
tags: [hkcs, gold-settlement, hau, settlement-day-2]
related: [hau, xau, hau-currency-onboarding, settlement-day-2, should-lms-convert-hau-to-xau, does-hau-require-swift-message-customization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative/Onboarding for HAU currency.md"]
---
# Hong Kong Physical Gold Settlement

The Hong Kong Physical Gold Settlement initiative is the recorded business context for onboarding [[hau]] into RATAN ONE Settlement Day 2 processing.

## Recorded delivery scope

The source identifies static-data, account-setup, frontend, SWIFT, LMS, accounting, Razor, and netting-rule assessment work. Delivery is traceable to nine Azure DevOps stories and feature branches in the accounting service, SWIFT service, and database repository.

## Status limitation

This page uses `planned` because the source does not provide evidence of completed pull requests, successful pipelines, deployment, release approval, or production validation. It does record UAT1 configuration and one generated HAU SWIFT message.

## Key dependencies

Production readiness depends on decisions or verification for HAU holiday and cut-off handling, LMS mapping to or from [[xau]], SWIFT customization and downstream acceptance, accounting-message suppression, frontend currency selection, and netting-rule treatment.