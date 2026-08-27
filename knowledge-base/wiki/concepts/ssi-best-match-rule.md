---
type: concept
title: SSI Best-Match Rule
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, vostro, cfi, fallback, settlement-method]
related: [trade-ssi-stamping, ratan, ssi-product-template-mapping, adhoc-ssi-workflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade SSI Stamping - Product templates.md"]
---

# SSI Best-Match Rule

The SSI best-match rule selects the most specific Vostro instruction available for a trade lookup.

## Matching sequence

1. Derive the initial CFI from the product or SCBML.
2. Refactor the CFI using wildcards for positions `213456`.
3. Query the requested CFI and progressively broader parent patterns.
4. Select the first available Vostro using this precedence:
   - Exact CFI.
   - Parent CFI.
   - `******`.

## Settlement-method normalization

| Trade value | Query value |
|---|---|
| `CASH` | `(CASH,FEDWIRE)` |
| `GROSS` | `(CASH,FEDWIRE)` |
| Other value | `(Other Value, CASH,FEDWIRE)` |

The source states that this behavior is aligned with cashflow SSI stamping, but the selected trade SSI must not be treated as inherited by cashflow stamping.