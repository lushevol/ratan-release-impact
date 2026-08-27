---
type: concept
title: Non-ISO-to-ISO Currency Mapping
created: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall/Tranche1.md"]
tags: ["currency", "ratan", "reference-data", "normalization", "iso", "settlement"]
related: ["ratan", "manual-entity-go-live-static-data-controls", "what-is-the-authoritative-nigeria-ngb-ngn-rounding-and-mapping-sequence", "manual-entity-settlement-enablement", "go-live-readiness-for-manual-entity-settlement"]
updated: 2026-08-23
---

# Non-ISO-to-ISO Currency Mapping

Non-ISO-to-ISO currency mapping normalizes or converts an internal or local input currency code to its ISO equivalent before downstream RATAN settlement processing.

## Stated mappings

The go-live checklist states that the following mappings need to be added on the RATAN side:

- `NGB → NGN` for Nigeria.
- `PKO → PKR` for Pakistan.

Both mappings are described as absent from the current RATAN mapping list.

For Pakistan, the Tranche 1 source records a 2026-01-20 confirmation from Cordelia Sumita K Thirunavukarasu that `PKO → PKR` did not exist in the current mapping list and needed to be added.

## Status and evidence limitations

The sources express required configuration changes but do not provide implementation, deployment, validation, or test evidence. The status of both mappings remains unverified from these sources alone.

## Nigeria rounding ambiguity

Nigeria has unresolved rounding ambiguity: the retained rounding row uses `NGB` with precision `2`, while the normalized SWIFT currency is `NGN`.