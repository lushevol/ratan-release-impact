---
type: concept
title: Nostro Account Normalization
created: 2026-08-24
updated: 2026-08-24
tags: [nostro-static-data, account-number, normalization, integration, razor, rdm]
related: [nostro-static-golden-source, nostro-record-composite-uniqueness, ratan-versus-razor-nostro-representation, nostro-stamping, rdm, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Nostro SSI/Nostro Static Golden Source.md"]
---

# Nostro Account Normalization

## Definition

Nostro account normalization is the controlled transformation of account-number representations between NAMS, RDM, RAZOR, and other FMO consumers. The source shows that equivalent accounts may contain currency codes, country information, spaces, suffixes, or replacement characters in different systems.

## Observed representations

| NAMS | RAZOR | Difference |
| --- | --- | --- |
| 15209909601AED | 15 2099096 01 | Currency +space |
| 5000408097 | DK4920005000408097 | Account info |
| 0100001846001 | HU 39120010080000184600100004 | Account info +suffix |
| 600-392027 | IL510126000000000392027 | Account info + replace '-' to '000000' |

## Required contract

The requirement identifies RDM as the place where FMO data massaging may occur, but does not define a canonical contract. A complete contract should specify:

1. The authoritative source value.
2. The canonical normalized value.
3. Each consumer-specific representation.
4. Whether country and currency prefixes are semantic data or formatting.
5. Whether spaces, hyphens, padding, and suffixes can be removed or transformed.
6. How original values are retained for audit and reconciliation.
7. How matching handles multiple representations of the same account.

Normalization must not be confused with identity resolution. A formatted account number may contain information that cannot safely be discarded.