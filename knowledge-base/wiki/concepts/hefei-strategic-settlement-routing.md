---
type: concept
title: Hefei Strategic Settlement Routing
created: 2026-08-22
updated: 2026-08-22
tags: [hefei, strategic-routing, cashflow-suppression, razor, ratan]
related: [hefei-branch, 2025-hefei-branch-onboarding, cashflow-suppression, settlement-message-routing, razor, ratan, what-is-the-hefei-razor-ratan-routing-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Hefei Branch Onboarding.md"]
---
# Hefei Strategic Settlement Routing

The Hefei onboarding checklist places China in a strategic-flow entity whitelist implemented through a [[cashflow-suppression]] rule.

## Whitelists in the checklist

- Legacy flow: `EG`, `NP`, `SAUDI`, `LOANIQ`
- Strategic flow: `CN`, `SG`, `MY`, `IN`, `UK`, `DE`

As a China branch, [[hefei-branch]] is within the stated strategic-flow country scope.

## Routing boundary

The checklist describes configuration that will “send to RAZOR or handle in RATAN,” and states that RATAN generates SWIFT and accounting in that described model. It does not specify the transaction attributes, precedence rules, or authoritative configuration that selects [[razor]] versus [[ratan]].

This routing statement must not be generalized to all transactions for all entities in the listed countries. The unresolved decision logic is tracked in [[what-is-the-hefei-razor-ratan-routing-rule]].