---
type: concept
title: FMRP Outbound Cashflow Enrichment
created: 2026-08-24
updated: 2026-08-24
tags: [fmrp, mxpayml, message-enrichment, murex-211, cashflow]
related: [fmrp, murex-211, fmrp-murex-cashflow-status-synchronization, what-is-the-authoritative-fmrp-entityfmid-and-entityleid-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0118.md"]
---
# FMRP Outbound Cashflow Enrichment

`client.scb.fmrp.fmrpEnrich` is an Murex 2.11 XML transformation that appends `scbExtraInfoBlock` to outbound `MxPayML` before MQ publication.

## Enriched fields

- `publicationDateTime`: server-local `GETDATE()` formatting.
- `validationLevel`: output of `client.scb.tds.getValStatus`.
- `entityFMID`: sourced from `M_ATLAS_LEID`.
- `entityLEID`: sourced from `M_SCI_ID`.
- `counterpartyFMID`: resolved through `client.scb.tds.common.getLEID`.
- `traderID`: resolved from trade buyer/seller data and `TRN_USRD_DBF`.
- `portBizUnit`: `M_BIZ_UNIT` from `PORTFOLI_DBF`.
- `amendmentFlag`: `Y` when same-day `MKT_OP_DBF` replacement records of type `RPL` or `RPL_M` exist for the trade reference; otherwise `N`.

## Constraints and uncertainty

The timestamp formatting is not ISO 8601. The trader and portfolio queries use `SELECT TOP 1` without an `ORDER BY`, so deterministic selection is not established by the source.

The `entityFMID` and `entityLEID` labels appear counterintuitive relative to their underlying fields. The mapping must be validated against the recipient contract before it is treated as authoritative; see [[what-is-the-authoritative-fmrp-entityfmid-and-entityleid-mapping]].