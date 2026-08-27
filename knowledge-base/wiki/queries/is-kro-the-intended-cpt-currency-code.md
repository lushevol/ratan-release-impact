---
type: query
title: Is KRO the Intended CPT Currency Code?
created: 2026-08-22
updated: 2026-08-22
tags: [cpt, currency, korea, configuration, open-question]
related: [chg1016055, ratan-settlement-korea, cash-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md"]
---
# Is KRO the Intended CPT Currency Code?

## Question

Is `KRO` the intended production identifier in the Korea CPT pair, or does it represent a configuration error or internal code requiring documentation?

## Recorded Configuration

```yaml
EG_TBFX_CPTY_FMID: 401039206
CPT_ENTITY_LIST: 10036645
CPT_PAIRS: USD^1|KRO^1
CPT_END_DATE: 2026-08-24
```

The value must remain recorded as `KRO` unless authoritative evidence confirms a correction.

## Evidence Needed

- The approved CPT configuration specification.
- The internal currency or product-code dictionary.
- Confirmation from the business or configuration owner.
- Production behavior showing how `KRO` is interpreted.
- Any defect, waiver, or correction record associated with the value.