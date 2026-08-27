---
type: query
title: What Defines a UK-Specific Vostro Branch?
created: 2026-08-23
updated: 2026-08-23
tags: [SSI, Vostro, UK-cashflow-migration, branch-configuration, open-question]
related: [vostro-ssi-best-matching, bau-versus-uk-vostro-ssi-best-matching, ssi-plus-es-api, multi-entity-cash-settlement-compatibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Vostro SSI Best Matching - UK Cashflow Migration.md"]
---
# What Defines a UK-Specific Vostro Branch?

## Question

Should “UK-specific Vostro” mean any non-`Global` value in `BranchId_Murex3Id`, or should it mean membership in an approved UK branch or entity configuration?

## Evidence

The worked example treats `SCB LONDON*LDN` as UK-specific and drops all `Global` SSIs when that value is present. The requirement does not state whether other branch values qualify, whether branch classification is configured, or whether the rule applies to all non-Global branches.

## Why It Matters

The answer determines which candidates are removed before product hierarchy filtering. An overly broad non-Global rule could cause an unrelated branch-specific SSI to suppress a valid Global fallback. An overly narrow rule could leave Global SSIs eligible when UK-specific instructions should take precedence.

## Required Resolution

Define:

- The authoritative branch or entity configuration source.
- Whether `SCB LONDON*LDN` is an example or an exhaustive value.
- The behavior when multiple branch-specific values are present.
- The fallback when only Global SSIs are returned.
- Whether the rule is also intended for current `HK`, `TW`, and `TAIPEI` flows.