---
type: query
title: What Is the Authoritative FXU Settlement-Method Transition Matrix?
tags: [fxu, settlement-method, specification-gap, validation]
related: [settlement-method-update, fx-utilization, fxu-utilization-validation, fxu, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--20-fxu-technical-design--okbgq5, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--20-fxu-technical-design--13-fxu-tes--1jiarro]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case/FXU Phase2 Test Case.md"]
---
# What Is the Authoritative FXU Settlement-Method Transition Matrix?

The Phase 2 test case describes a bidirectional settlement-method change involving `GROSS` and `UTIL`, but explicitly records only:

```text
GROSS <=> ""
```

`UTIL` appears as an eligible current settlement method under a separate status rule, but the source does not state its permitted target value or values.

## Questions to Resolve

- Is `UTIL` changed to `GROSS`, blank, or both?
- Can `GROSS` change directly to `UTIL`?
- Can blank change directly to `UTIL`?
- Is a target settlement-method value selected by the user, inferred by the UI, or determined by backend logic?
- Do status and taxonomy eligibility rules constrain only the current value, or also the requested target value?

## Evidence Needed

Confirm the transition matrix against the authoritative [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--20-fxu-technical-design--okbgq5]], API contract, UI specification, or executable acceptance tests. Do not infer `UTIL` transitions solely from the Phase 2 eligibility predicate.