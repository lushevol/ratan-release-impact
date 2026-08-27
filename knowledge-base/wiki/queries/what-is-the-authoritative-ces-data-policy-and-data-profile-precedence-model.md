---
type: query
title: What Is the Authoritative CES Data Policy and Data Profile Precedence Model?
created: 2026-08-24
updated: 2026-08-24
tags: [ces, data-policy, data-profile, precedence, access-control, governance]
related: [ces, data-policy-and-data-profile-precedence, ratan-data-entitlement]
sources: ["RATAN/RATAN -Interfaces/Ratan and CES 55508.md"]
---
# What Is the Authoritative CES Data Policy and Data Profile Precedence Model?

The source states only that Data Profile rules take precedence over Data Policy rules “as a general rule.” It provides an illustrative Korea/GB scenario but no formal evaluation policy.

## Questions

- Are Data Profile grants always able to override Data Policy restrictions?
- How are explicit denies evaluated against grants?
- Do rule specificity, user location, entity hierarchy, time windows, or policy priority affect precedence?
- Which roles can create, approve, and audit Data Policy and Data Profile overrides?
- What evidence records the effective entitlement decision for a user?

The required formal model should clarify the control boundary described in [[data-policy-and-data-profile-precedence]].