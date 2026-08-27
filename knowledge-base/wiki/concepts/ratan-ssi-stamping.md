---
type: concept
title: RATAN SSI Stamping
created: 2026-08-23
updated: 2026-08-24
tags: [ratan, ssi, cashflow, stamping, settlement, enrichment, unverified]
related: [ratan, ssi-plus, vostro-nostro-ssi-selection, ssi-maker-checker-remediation, ssi-effective-date-selection, scbml-ssi-field-mapping, ratan-settlement, 5-ratan--25-ratan-core-function-copy--31-ratan-settlement-50ssi-stamping--ea95v1]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow.md", "RATAN/RATAN -Core Function copy/RATAN-Settlement  5.0_SSI Stamping.md"]
---
# RATAN SSI Stamping

RATAN SSI stamping is described by the *FMRP - SSI Stamping Flow* source as the process of selecting settlement instructions for a cashflow, applying selected Vostro and Nostro data, enriching confirmation and SCBML outputs, and creating remediation exceptions where selection is incomplete or ambiguous.

That source states that the requirement applies effective-date filtering before selection, uses separate UK and non-UK matching priorities, and requires re-stamping of impacted cashflows after SSI updates. It describes functional behavior rather than a complete API or event-processing contract.

## Functional behavior described by the FMRP SSI Stamping Flow source

According to *FMRP - SSI Stamping Flow*:

- SSI selection is performed for a cashflow.
- Selected Vostro and Nostro settlement-instruction data is applied.
- Confirmation and SCBML outputs are enriched.
- Incomplete or ambiguous selection creates remediation exceptions.
- Effective-date filtering is applied before selection.
- UK and non-UK matching use separate priorities.
- Cashflows impacted by SSI updates must be re-stamped.

## Scope and unverified areas in the RATAN-Settlement 5.0 source

The *RATAN-Settlement 5.0 SSI Stamping* source identifies an apparent settlement-related capability solely from its filename. That source does not define SSI, its lifecycle role, or the mechanism by which a value would be assigned or recorded.

For that source, the following matters remain unverified and require source evidence:

- the authoritative SSI source and lookup keys;
- the owning service or component;
- when stamping occurs in the settlement lifecycle;
- selection, precedence, fallback, and override rules;
- whether values are persisted, versioned, auditable, immutable, or restamped;
- failure and exception behavior; and
- any relationship to payment generation, SWIFT generation, or payment identification.

This unverified scope applies only to the apparent [[ratan-settlement]] subject identified by the *RATAN-Settlement 5.0 SSI Stamping* source. It does not establish a shared RATAN or RatanOne-wide mechanism.