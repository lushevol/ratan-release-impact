---
type: concept
title: Global and Branch-Specific SSI Scope
tags: [ssi, branch-scope, global-ssi, cashflow, re-stamping]
related: [ssi-stamping, ssi-stamping-notification, cfi-code-ssi-granularity-matching, ssi-stamping-product-mapping]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/SSI Notification Flow.md"]
---
# Global and Branch-Specific SSI Scope

## Definition

Branch scope controls which cashflows are considered for SSI re-stamping after a `New`, `Amend`, or `Re-active` SSI+ event.

The source distinguishes a branch-specific SSI from a `Global` SSI. `Global` is a scope-expansion value, not merely another branch identifier.

## Rules

- A branch-specific SSI is matched only against cashflows stamped to the specific branch.
- A `Global` SSI is matched against both:
  - Cashflows stamped with `Global`.
  - Cashflows stamped with a specific branch SSI.

The branch fields are:

| Data source | Logical model field |
| --- | --- |
| Cashflow | `Entity.Booking_Entity_SCI_FMCODE` |
| SSI data | `Settlement_Instruction.BranchId_Murex3Id` |

## Example

| Branch from SSI event | Branches from assigned SSI |
| --- | --- |
| `SCB LONDON*LDN` | `SCB LONDON*LDN` |
| `Global` | All |

The requirement does not define whether “All” refers to every branch value in the data store or to a governed branch catalogue. That scope boundary should be confirmed before implementation.