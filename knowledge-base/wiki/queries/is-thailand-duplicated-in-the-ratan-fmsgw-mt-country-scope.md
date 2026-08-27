---
type: query
title: Is Thailand Duplicated in the RATAN-FMSGW MT Country Scope?
tags: [ratan, fmsgw, mt, country-scope, documentation-quality, open-question]
related: [ratan-fmsgw-settlement-messaging, fmsgw, swift, what-is-the-authoritative-ratan-fmsgw-interface-contract]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and FMSGW 54949.md"]
---
# Is Thailand Duplicated in the RATAN-FMSGW MT Country Scope?

## Question

Is the second `TH` in the RATAN MT real-time message country list intentional, or is it a documentation duplication?

## Evidence

The source records the MT scope as:

```text
CN, MY, IN, SG, UK, DE, HK, TH, TW, US , ID, JP, MU, PH, UAE, ZA, TH
```

The MX scope records:

```text
MU, UK, CN, UAE, HK, SG, ZA, TW, MY, PH, TH, ID, IN, US, JP, DE
```

Both rows contain the same 16 unique country codes after duplicate removal. The source provides no explanation for the repeated `TH` in the MT row and does not identify country-specific routes, message variants, legal entities, or settlement products that could justify two entries.

## Required Resolution

Confirm the canonical country scope from an authoritative routing, rollout, or interface specification. Until then, represent the MT scope verbatim while treating the duplicate as unresolved documentation ambiguity.