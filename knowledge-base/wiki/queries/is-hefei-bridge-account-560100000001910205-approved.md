---
type: query
title: Is Hefei Bridge Account 560100000001910205 Approved?
created: 2026-08-22
updated: 2026-08-22
tags: [hefei, ebbs, bridge-account, settlement-accounting, approval]
related: [scb-hefei, ebbs, cash-settlement-entity-onboarding, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--38-04-onboardingentity-pr--27yb0b]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/China Hefei Branch Setup.md"]
---
# Is Hefei Bridge Account 560100000001910205 Approved?

## Question

Has Balaji confirmed bridge account `560100000001910205` for SCB Hefei, and has the resulting [[ebbs]] settlement-accounting configuration been validated?

## Evidence

The source lists bridge account `560100000001910205` for Hefei settlement accounting, but marks it “TBC by Balaji.” It specifies EBBS branch code `73` and instructs that the EBBS transaction code should follow China.

## Acceptance Evidence Needed

- Confirmation from the accountable approver that the account is correct and active.
- The effective configuration in the relevant EBBS environment.
- Posting tests showing branch code `73`, the inherited China transaction-code behavior, and correct bridge-account treatment.
- UAT and regression evidence covering normal and exception settlement flows.

Until this evidence is recorded, the bridge account remains proposed rather than production-approved.