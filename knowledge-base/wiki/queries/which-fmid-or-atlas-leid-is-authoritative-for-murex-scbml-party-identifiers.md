---
type: query
title: Which FMID or Atlas LEID Is Authoritative for Murex SCBML Party Identifiers?
created: 2026-08-24
updated: 2026-08-24
tags: [fmid, atlas, sci, murex-211, scbml, open-question]
related: [murex-party-fmid-enrichment, murex-payment-mxml-to-scbml-transformation, murex-211, sci]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - MxML mapping to SCBML.md"]
---
# Which FMID or Atlas LEID Is Authoritative for Murex SCBML Party Identifiers?

## Question

Which identifier must populate the SCBML `partyId` element using the `FMID` party-identifier scheme?

## Evidence

The primary mapping gives:

- Booking entity: `10075222`.
- Counterparty: `400899993`.

The enrichment examples give:

- `SHANGHAI` `M_ATLAS_LEID`: `10036642`.
- `LOUDRECOMSH/BJG` `M_ATLAS_LEID`: `400796812`.

The source also exposes both `M_SCI_ID` and `M_ATLAS_LEID` in SQL results and refers to MxML extra-info fields as SCI FMID values.

## Required resolution

Confirm:

1. Whether SCBML expects `M_SCI_ID`, `M_ATLAS_LEID`, or another FMID.
2. Which source takes precedence when MxML extra-info and database lookup differ.
3. Whether the examples represent different environments or different identifier versions.
4. What validation and failure behavior applies when no identifier is available.