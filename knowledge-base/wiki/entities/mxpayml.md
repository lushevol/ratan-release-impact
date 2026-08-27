---
type: entity
title: MxPayML
created: 2026-08-22
updated: 2026-08-23
tags: [murex, xml, payment-messaging, ratan, integration, mxpayml, payment-mxml, murex-211]
related: [murex, ratan, murex-payment-trade-lineage-identifiers, murex-211, murex-payment-mxml-to-scbml-transformation, scbml-cashflow-payload]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Analyse murex event impacting payment to Ratan.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - MxML mapping to SCBML.md"]
---
# MxPayML

## Role

According to the Murex-event analysis source, MxPayML is the Murex XML payment payload used to transmit cashflow and trade-lineage information to [[ratan]] in the CN settlement integration.

According to the MxML-to-SCBML mapping source, MxPayML—also called Payment MxML or Payment MXML—is the proposed inbound Murex 2.11 payment-message format for China settlement cashflows. It supplies direct payment fields and identifies enrichment points for data unavailable in the base message.

## Fields identified in the Murex-event analysis

The Murex-event analysis source identifies the following fields as relevant:

- `flowID`
- `Action`
- `tradeLastMKT`
- `TrnRef`
- `TrnID`
- `TrnParentID`
- `TrnOriginalID`
- `comment`
- `CpuDate`
- `CpuTime`
- Payment snapshots

According to that source, these fields support interpretation of reverse, replacement, fixing, and market-operation effects.

## Fields referenced by the MxML-to-SCBML mapping

The MxML-to-SCBML mapping source references:

- `event`
- `flowStatus`
- `transactionID`
- `flowID`
- `flowAmount`
- `currency`
- `systemDate`
- `releaseDate`
- `type`
- `portfolio`
- `user`
- `entity`
- `counterparty`
- `isCredit`
- `transactionFamily`
- `transactionGroup`
- `transactionType`
- `scbExtraInfoBlock/entityFMID`
- `scbExtraInfoBlock/counterpartyFMID`
- `scbExtraInfoBlock/action`
- `scbExtraInfoBlock/TrnParentID`
- `scbExtraInfoBlock/TrnOrginalID`
- `scbExtraInfoBlock/Flows/flow`

## Contract status and interface cautions

The MxML-to-SCBML mapping source treats the MxPayML mapping as a draft. It states that trade-confirmation status, party FMIDs, trader data, and some product data require MxML enhancement or external enrichment. No sample MxPayML document is included for validation.

> [!CAUTION]
> In the Murex-event analysis source, the cited XPath for `tradeLastMKT` begins with `k/`, and the XPath for `TrnOriginalID` is written as `TrnOrginalID`. These are source-recorded values, not validated interface-contract definitions. Validate them against representative production messages before implementation.

See [[murex-payment-trade-lineage-identifiers]] and [[what-is-the-approved-ratan-correlation-key-for-murex-reversal-and-new-payments]].