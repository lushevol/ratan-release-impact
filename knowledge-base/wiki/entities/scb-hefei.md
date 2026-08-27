---
type: entity
title: SCB Hefei
created: 2026-08-22
updated: 2026-08-22
tags: [booking-entity, china, hefei, cash-settlement, swift, ebbs]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--38-04-onboardingentity-pr--27yb0b, swift-network, swift-service, ebbs, murex-211, cash-settlement-home-page, does-hefei-ssi-propagate-as-a-global-murex-ssi, is-hefei-bridge-account-560100000001910205-approved]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/China Hefei Branch Setup.md"]
---
# SCB Hefei

SCB Hefei, also described as China Hefei Branch, is a proposed booking and settlement entity being onboarded to the Cash Settlement Home Page ecosystem.

## Identifiers

- Booking Entity FMID: `401053411`
- Booking Entity FMCODE: `SCB CHINA*HFI`
- Booking Entity BIC / SWIFT sender BIC: `SCBLCNSXHFI`
- Branch code: `73`
- EBBS branch code: `73`

## SWIFT Routing

For Hefei-generated SWIFT messages:

- Sender BIC: `SCBLCNSXHFI`
- Field 53 BIC for LCY and Over-Account flows: `SCBLCNSXGMO`
- Field 58 in Flip MT202: `SCBLCNSXGMO`

The source assumes that no other Hefei-specific SWIFT requirement exists. This remains an assumption requiring downstream confirmation and message-level validation with [[swift-network]] and [[swift-service]].

## Settlement and Static Data

Hefei is expected to follow China Head Office currency release timing and EBBS transaction-code behavior. The proposed bridge account is `560100000001910205`, but it is marked TBC by Balaji; it must not be treated as approved configuration until confirmation and posting validation are available. See [[is-hefei-bridge-account-560100000001910205-approved]].

Existing Global SSIs are intended to be selected automatically. Branch-specific SSIs are limited to `SUPPRESSXX` Nostro auto-debit flows and Over-Account clients. The stated risk is that a Hefei SSI may propagate to [[murex-211]] as a Global SSI, contrary to the intended branch-specific scope.

## Required Enablement

- LMS entity-list update
- SWIFT BIC and branch mapping
- EBBS accounting setup
- Cashflow Blotter and Dashboard dropdown inclusion in [[cash-settlement-home-page]]
- Nostro and Vostro static-data setup
- SWIFT suppression rules for SCB Hefei as counterparty plus FCY
- UAT and regression testing

The onboarding evidence is summarized in [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--38-04-onboardingentity-pr--27yb0b]].