---
type: decision
title: "Adopt Boolean Resultant Hard-Blocker Marker"
status: proposed
deciders: []
date: 2026-08-22
supersedes: ""
created: 2026-08-22
updated: 2026-08-22
tags: [hard-blocker, resultant-cashflow, swap-agent, netting, nstp]
related: [swap-agent-coupon-interim-mtm-hard-blocker, resultant-hard-blocker-stamping, ratan-cash-settlement-netting-service, ratanone-rule-service, ratan-rule-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker Tech Design.md"]
---
# Adopt Boolean Resultant Hard-Blocker Marker

## Context

The source presents two designs for enforcing the `SWAP_AGENT` Coupon and Interim MTM release restriction. Option 1, which encoded component strategy and payment details in a combined string and used regex matching in the resultant rule, is struck through. Option 2 uses a boolean marker, `Cashflow__Is_Hard_Blocker`, plus pre-netting validation.

The source clearly identifies Option 2 as the selected design, but it does not provide formal approval evidence or an accountable decision record. This decision remains proposed pending confirmation.

## Proposed decision

Use a boolean resultant marker propagated as `scb:isHardBlocker`, `Cashflow__Is_Hard_Blocker`, and `EnhancedFact.Cashflow__Is_Hard_Blocker`.

Combine this with request-level validation that rejects `SWAP_AGENT` `Coupon` or `Interim MTM` cashflows when they are netted with a different payment type, and use the `HARD_BLOCKER` exception category to prevent NSTP submit and approve release actions.

## Consequences

- Resultant rules remain simple and do not need to parse component strings.
- The restriction is enforced both before incompatible netting and at later NSTP release steps.
- The implementation requires coordinated changes to [[ratan-cash-settlement-netting-service]], [[ratanone-rule-service]], [[ratan-rule-service]], and rule-engine database configuration.
- The marker must remain correctly populated for all in-scope netting paths.
- The decision does not establish NDS endpoint applicability or deployment status.