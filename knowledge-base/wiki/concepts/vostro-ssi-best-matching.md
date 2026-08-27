---
type: concept
title: Vostro SSI Best Matching
created: 2026-08-23
updated: 2026-08-23
tags: [Vostro, SSI, best-matching, settlement, cashflow-migration]
related: [ssi, ssi-plus, ssi-plus-es-api, fmrp, ssi-stamping, vostro-nostro-ssi-selection, bau-versus-uk-vostro-ssi-best-matching, multi-entity-cash-settlement-compatibility, what-defines-a-uk-specific-vostro-branch]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Vostro SSI Best Matching - UK Cashflow Migration.md"]
---
# Vostro SSI Best Matching

Vostro SSI best matching selects one settlement instruction from multiple candidates returned by [[entities/ssi-plus-es-api]].

## Conditional Algorithms

### BAU

The existing BAU sequence is:

1. Retain the most granular `CFI_Code` match.
2. Apply branch hierarchy and default-status priority.
3. Prefer country-specific primary, Global primary, country-specific secondary, and Global secondary in that order.

BAU applies to `CN`, including `HEFEI`, `SG`, `IN`, `MY`, `AG`, `EG`, `NP`, and `SA`, and also applies when the original source system is `LOANIQ`.

### UK Cashflow Migration

The migration sequence is:

1. If a UK-specific branch Vostro exists, remove all `Global` candidates. If only Global candidates exist, retain them.
2. Retain the most granular `CFI_Code` match.
3. Prefer `Is_Default_SSI = True`.

This ordering means a branch-specific SSI can be selected even when a Global SSI has a more granular product code.

## Worked Result

Given the requirement’s sample candidates, the new algorithm removes Global SSIs, removes the less-specific `******` product match, and then selects SSI ID `001` over secondary SSI ID `002`.

## Scope Boundary

The new algorithm is not a universal replacement for BAU. The current implementation’s non-BAU branch includes `UK`, `HK`, `TW`, and `TAIPEI`, while new entities and products such as `Prime` and `Global Rates` require separate assessment.

## Unresolved Semantics

The requirement leaves the following semantics open:

- What qualifies as a UK-specific branch.
- How every CFI wildcard pattern is ranked.
- How ties between multiple primary SSIs are resolved.
- What fallback is used when no candidate survives.

These questions are tracked in [[queries/what-defines-a-uk-specific-vostro-branch]].