---
type: concept
title: Payment Accounting Flow
tags: [cash-settlement, payment-accounting, platform-ownership, routing]
related: [aspire, ebbs, keystone, nostro-account-scope]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting.md"]
---
# Payment Accounting Flow

## Definition

A payment accounting flow describes which accounting platform owns the processing or recording of a cash-settlement payment for a given market and Nostro-account scope.

## Operating models

### Before Keystone

eBBS owns all Nostro accounts for CN, SG, IN, MY, AG, and UK. Aspire owns all Nostro accounts for HK, TW, and TH.

### Post Keystone

eBBS continues to own all Nostro accounts for CN, SG, IN, MY, AG, and UK. For HK, eBBS owns Main Nostro and Aspire owns Suspense. Aspire continues to own all Nostro accounts for TW and TH.

## Design implication

Platform ownership is not equivalent to market ownership in the post-Keystone model. HK must be routed using both the market and the account category. Treating HK as wholly assigned to either [[aspire]] or [[ebbs]] would lose the account-level distinction.

The source does not define the detailed transaction-routing algorithm, accounting journal behavior, effective-date rule, or exception handling.