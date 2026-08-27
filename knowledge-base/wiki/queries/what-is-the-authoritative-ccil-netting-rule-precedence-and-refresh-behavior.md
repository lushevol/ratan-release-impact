---
type: query
title: What Is the Authoritative CCIL Netting Rule Precedence and Refresh Behavior?
created: 2026-08-23
updated: 2026-08-23
tags: [ccil, netting, rules, static-data, pending-netting]
related: [ccil-manual-netting, ccil-netting-eligibility-key, netting-static-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/02 CCIL Netting.md"]
---
# What Is the Authoritative CCIL Netting Rule Precedence and Refresh Behavior?

## Open Question

How do disabling or editing a live manual netting rule affect cashflows already in `Pending Netting`, and which rule prevails when CCIL and Bilateral rules both match?

## Historical Evidence Only

The source contains two struck-through cases:

- A rule-disable/update case expecting existing qualifying cashflows to lose the `Pending Netting` sub-state.
- A CCIL-versus-Bilateral-rule case suggesting that a CCIL rule should take precedence when both rules match.

Because both cases are struck through, they are not active requirements and cannot establish production behavior.

## Needed Resolution

Obtain a current rule-engine specification or approved acceptance case that defines rule refresh timing, re-evaluation of queued cashflows, precedence ordering, and audit behavior for rule changes.