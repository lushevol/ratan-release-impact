---
type: comparison
title: BAU Versus UK Vostro SSI Best Matching
created: 2026-08-23
updated: 2026-08-23
tags: [SSI, Vostro, BAU, UK-cashflow-migration, comparison]
related: [vostro-ssi-best-matching, ssi-stamping, multi-entity-cash-settlement-compatibility, ssi-plus-es-api]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Vostro SSI Best Matching - UK Cashflow Migration.md"]
---
# BAU Versus UK Vostro SSI Best Matching

| Aspect | BAU | UK cashflow migration |
| --- | --- | --- |
| Candidate retrieval | One SSI+ ES API query | One SSI+ ES API query |
| First selection filter | Product hierarchy | Branch-specific versus Global |
| Second selection filter | Branch hierarchy and primary/secondary status | Product hierarchy |
| Final selection filter | Included with branch/default ranking | Prefer `Is_Default_SSI = True` |
| Primary scope | `CN`, `SG`, `IN`, `MY`, `AG`, `EG`, `NP`, `SA`, and original source system `LOANIQ` | Current `else` branch, including `UK`, `HK`, `TW`, and `TAIPEI` |
| Global handling | Compared after product filtering | Dropped whenever a UK-specific branch exists |
| Example outcome | BAU can retain a Global candidate after product filtering | New logic selects SSI ID `001` for the supplied sample |

## Key Behavioral Difference

The algorithms differ in ordering. BAU evaluates product specificity before branch specificity. The migration algorithm evaluates branch specificity first, so a branch-specific candidate is protected from elimination by a more granular Global product match.

The migration algorithm should therefore be documented and tested as a conditional variant rather than merged into the canonical BAU rule.