---
type: query
title: What Is the Authoritative FMRP Field 20 Prefix Mapping?
created: 2026-08-24
updated: 2026-08-24
tags: [fmrp, razor, lms, swift, field-20, mapping]
related: [lms, razor, ratan, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/LMS Feed.md"]
---
# What Is the Authoritative FMRP Field 20 Prefix Mapping?

The source contains a material contradiction for the China go-live flow:

- The narrative says BLADE/S2BX/CFETS populate `FMRP` to LMS and RAZOR generates the SWIFT field 20 prefix `MX`.
- The mapping table says the same `FMRP` source value maps to prefix `DV`.

The authoritative value must be confirmed before the mapping is used for payment-message generation.

## Related mappings

| Booking system | LMS source value | Narrative prefix | Table prefix |
| --- | --- | --- | --- |
| SABRE EQ | `STELLA` | `EQ` | `EQ` |
| LOANIQ | `LOANIQ` | `LQ` | `LQ` |
| BLADE/S2BX/CFETS | `FMRP` | `MX` | `DV` |

## Evidence needed

Confirm the intended value with the owners of RAZOR field 20 generation and the China go-live configuration, then update the source requirement and implementation mapping consistently.