---
type: concept
title: Nostro Account Scope
tags: [cash-settlement, payment-accounting, Nostro, account-routing]
related: [payment-accounting-flow, aspire, ebbs, keystone]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting.md"]
---
# Nostro Account Scope

## Definition

Nostro Account Scope is the account dimension used by the payment-accounting ownership matrix to qualify platform responsibility within a market.

## Values in the source

- `All` — Used for eBBS across CN, SG, IN, MY, AG, and UK, and for Aspire across TW and TH. The source does not define which account categories are included.
- `Main Nostro` — The HK account scope assigned to eBBS after Keystone.
- `Suspense` — The HK account scope assigned to Aspire after Keystone.

## Routing significance

Before Keystone, HK is assigned entirely to Aspire under `All`. After Keystone, HK is split between eBBS and Aspire by account category:

- HK Main Nostro → eBBS
- HK Suspense → Aspire

This distinction is part of the [[payment-accounting-flow]] model and should be preserved in implementation and reconciliation logic.

## Clarifications required

The source does not establish whether Main Nostro and Suspense are account classes, accounting treatments, routing destinations, or operational labels. It also does not state whether `All` includes suspense, transit, omnibus, or other account categories.