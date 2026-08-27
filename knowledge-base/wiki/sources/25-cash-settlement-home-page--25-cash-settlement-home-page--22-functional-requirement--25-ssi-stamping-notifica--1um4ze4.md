---
type: source
title: Trade Strategic SSI Stamping Tech Design
authors: []
year: 2026
url: "https://confluence.global.standardchartered.com/pages/viewpageattachments.action?pageId=2599261958&metadataLink=true"
venue: Confluence
tags: [ssi-stamping, graphql, trade-data, technical-design, fmrp]
related: [cdu, graphql-trade-snapshot-retrieval, historical-trade-query-fallback, ratan-ssi-stamping, ssi-stamping-notification, does-cdu-and-graphql-snapshot-identity-hold-for-trade-id-and-major-version, what-triggers-historical-trade-query-fallback-for-ssi-stamping]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade Strategic SSI Stamping Tech Design.md"]
---
# Trade Strategic SSI Stamping Tech Design

This technical-design excerpt defines the intended trade-data retrieval path for SSI stamping. The normal path uses a GraphQL query constructed from the trade fields requested by the stamping flow. Consequently, only selected fields are populated in the normal response.

The design expects the latest trade snapshot used by [[cdu|CDU]] for SSI stamping to be discoverable through GraphQL using the same `Trade_Id` and `Trade_Lake_Trade_Major_Version`. This is an expectation rather than a stated consistency guarantee.

## Illustrative GraphQL request

```groovy
{
  trades(filter: [], searchFilter: "Trade_Id = '6648567050' and Trade_Lake_Trade_Major_Version=1", page: 0, size: 1) {
    results {
Entity {
  Booking_Entity_SCI_FMID
  Counterparty_SCI_FMID
}
Trade_Lake_Trade_Major_Version
Trade_Lake_Trade_Minor_Version
Swap_Instrument {
  IR_Leg {
    First_Leg {
      Notional_Amount_Currency
      Payer_Party_Reference
    }
  }
}
Instrument_Common {
  Financial_Instrument_Code
}
Trade_Id
Settlement_Method

    }
  }
}
```

## Selected trade attributes

The illustrated projection includes booking-entity and counterparty identifiers, trade major and minor version, first IRS-leg currency and payer reference, financial-instrument code, trade ID, and settlement method.

The sample values `Trade_Id = '6648567050'` and major version `1` are illustrative request values, not business constants.

## Historical fallback

If the flow falls back to a historical query, it retrieves all trade fields rather than the limited GraphQL projection. The source does not define the fallback trigger, historical data source, version-selection behavior, error handling, or how non-IRS trades are handled.

## Boundaries

This source describes retrieval of trade-side data for [[ratan-ssi-stamping|RATAN SSI Stamping]]. It does not define SSI matching or tie-breaking, SCBML field mapping, notification triggers, or maker/checker behavior.