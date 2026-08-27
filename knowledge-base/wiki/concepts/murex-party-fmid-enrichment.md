---
type: concept
title: Murex Party FMID Enrichment
created: 2026-08-24
updated: 2026-08-24
tags: [fmid, atlas, sci, entity-enrichment, counterparty, murex-211]
related: [murex-211, sci, murex-payment-mxml-to-scbml-transformation, mxpayml, scbml-cashflow-payload, which-fmid-or-atlas-leid-is-authoritative-for-murex-scbml-party-identifiers]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - MxML mapping to SCBML.md"]
---
# Murex Party FMID Enrichment

## Purpose

Party FMID enrichment translates Murex booking-entity and counterparty labels into the party identifiers required by the SCBML cashflow payload.

The target uses SCBML `partyId` elements with the scheme:

- `http://www.sc.com/coding-scheme/partyId/FMID`

## Booking entity

For a booking entity such as `SHANGHAI`, the source proposes either:

- MxML enhancement through `scbExtraInfoBlock/entityFMID`; or
- Lookup through `ENTITY_DBF` joined to `COUNTERP_DBF`.

The documented SQL is:

```sql
SELECT EN.M_LABEL,EN.M_CTP_COD,CP.M_SCI_ID,CP.M_ATLAS_LEID
FROM TABLE#DATA#ENTITY_DBF EN, TABLE#DATA#COUNTERP_DBF CP
WHERE EN.M_CTP_COD=CP.M_LABEL AND EN.M_LABEL='SHANGHAI'
```

## Counterparty

For `LOUDRECOMSH/BJG`, the source proposes MxML enhancement through `scbExtraInfoBlock/counterpartyFMID` or lookup in `COUNTERP_DBF`:

```sql
SELECT M_LABEL,M_SCI_ID,M_ATLAS_LEID
FROM TABLE#DATA#COUNTERP_DBF
WHERE M_LABEL='LOUDRECOMSH/BJG'
```

## Identifier ambiguity

The primary mapping examples are `10075222` for the booking entity and `400899993` for the counterparty. The enhancement examples provide `M_ATLAS_LEID` values `10036642` and `400796812`.

The source labels these values as SCI FMID / Atlas IDs but does not explain the discrepancy or establish whether `M_SCI_ID`, `M_ATLAS_LEID`, or the MxML extra-info values are authoritative. This is tracked in [[which-fmid-or-atlas-leid-is-authoritative-for-murex-scbml-party-identifiers]].

## Operational importance

An incorrect party identifier can route a cashflow to the wrong booking entity or counterparty. Identifier domain, environment, source precedence, and validation behavior must therefore be confirmed before implementation.