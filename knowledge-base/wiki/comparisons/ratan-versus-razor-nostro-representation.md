---
type: comparison
title: Ratan versus Razor Nostro Representation
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, razor, nostro, terminology, data-format]
related: [ratan, razor, nostro-centralization, nostro-stamping, nostro-notification-and-refresh]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Centralization.md"]
---
# Ratan versus Razor Nostro Representation

## Evidence-based comparison

| Aspect | Ratan | Razor |
|---|---|---|
| Settlement terminology | Uses `NOS` | Uses `Nostro` |
| Explicitly named query impacts | Cashflow or trade stamping query; accounting query | Not specified in the source |
| Expected centralization impact | Integrate with and consume Nostro data from `SSI+` | Affected by data-format standardization; exact integration path is not specified |
| Notification behavior | Not specified beyond the general TP-system requirement | Not specified |
| Migration behavior | Historical cashflow treatment is unresolved | Not specified |

## Interpretation

The source establishes a terminology difference but does not establish equivalent data models, query paths, or service ownership. `NOS` and `Nostro` should not be normalized in implementation until the canonical value and compatibility rules are approved.

The source supports a direct scope statement for `Ratan`, but only a terminology and data-format impact statement for `Razor`.

## Open comparison points

- Whether `NOS` and `Nostro` are semantic equivalents.
- Whether either system retains a local Nostro cache.
- Whether both systems consume the same `SSI+` contract.
- Whether notification refresh and deletion handling are implemented consistently.
- Whether portfolio-to-Nostro mapping is shared with `RFI stamping`.
