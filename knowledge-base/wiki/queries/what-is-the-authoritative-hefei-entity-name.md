---
type: query
title: What Is the Authoritative Hefei Entity Name?
created: 2026-08-22
updated: 2026-08-22
tags: [hefei, entity-data, static-data, identifiers]
related: [hefei-branch, 2025-hefei-branch-onboarding, murex-2-11, ebbs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Hefei Branch Onboarding.md"]
---
# What Is the Authoritative Hefei Entity Name?

The checklist uses multiple values that may refer to the same branch in different contexts:

- `Hefie`
- `Heifei`
- `HEFEI`
- `SCB CHINA*HFI`

`HEFEI` is explicitly the Murex 2.11 entity name, and `SCB CHINA*HFI` is explicitly a legal-entity value. The document does not establish whether `Hefei` is the approved business name, nor whether the apparent spelling variants are source errors or system-specific identifiers.

## Evidence needed

- Approved legal-entity and branch master-data records.
- The canonical name for operational documentation.
- Confirmation that FMID `401053411` and branch code `73` resolve to the same entity in Murex, SWIFT, EBBS, and GUI configuration.
- Correction or preservation guidance for the `Hefie` and `Heifei` variants.