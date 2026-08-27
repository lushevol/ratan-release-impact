---
type: source
title: CN Settlement MxML Mapping to SCBML
authors: []
year: 2023
url: ""
venue: "Cash Settlement Home Page functional requirement"
created: 2026-08-24
updated: 2026-08-24
tags: [cn-settlement, murex-211, mxml, scbml, cashflow-integration, mapping]
related: [murex-211, murex-2-11, ratan, mxpayml, scbml-cashflow-payload, murex-payment-mxml-to-scbml-transformation, murex-party-fmid-enrichment, cn-payments-reporting-field-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - MxML mapping to SCBML.md"]
---
# CN Settlement MxML Mapping to SCBML

## Scope

This requirements artifact proposes a field-level transformation from Murex 2.11 Payment MxML to SCBML cashflow payloads for China settlement. It also identifies fields requiring MxML enhancement or enrichment from Murex database tables and TDS3, and inventories fields for CN Payments reports.

The document is a draft mapping rather than an implementation specification. The referenced updated mapping attachment, Payment MXML sample, and SCBML sample are not included. XPath validity, namespaces, occurrence behavior, and runtime values therefore require confirmation.

## Systems and data dependencies

The proposed dependency chain is:

- Murex 2.11 produces Payment MxML.
- TDS3 supplies trade and trader enrichment.
- Murex `TRN_HDR_DBF`, `ENTITY_DBF`, and `COUNTERP_DBF` supply confirmation and party-identifier data.
- RATAN MLS performs payer/receiver and product transformations.
- SCBML is the target cashflow payload.
- CN Payments reports consume a report-oriented field contract.

## Principal mapping decisions

The mapping proposes:

- `transactionID` to SCBML trade ID.
- `flowID` to a 12-character SCBML cashflow ID by left-padding with zeroes.
- `flowAmount`, `currency`, `systemDate`, `releaseDate`, and `portfolio` to corresponding SCBML amount, currency, event date, payment date, and portfolio fields.
- `entityFMID` and `counterpartyFMID` from `scbExtraInfoBlock` to SCBML party FMID identifiers.
- `isCredit` and a reverse indicator to payer, receiver, and pay/receive values.
- Murex Family/Group/Type dimensions to CFI code, ISDA taxonomy, and source-system instrument subtype.

The mapping hard-codes both cashflow versions to `0` and proposes `New` as the CN Payments event type. This conflicts with field descriptions that allow lifecycle changes and event types including Withdrawal and Amendment.

## Enrichment requirements

| Field | Values | Derivation |
|---|---|---|
| Trade confirmation status | COMP/VALD | `select M_VAL_STATUS from TRN_HDR_DBF WHERE M_NB= Trade ID` |
| Booking entity SCI FMID / Atlas ID | Entity-dependent | Resolve through `ENTITY_DBF` and `COUNTERP_DBF` |
| Counterparty SCI FMID / Atlas ID | Counterparty-dependent | Resolve through `COUNTERP_DBF` |
| Trader PSID and trader metadata | TDS3-dependent | Retrieve from TDS3 |
| Product classification | CFI, ISDA taxonomy, subtype | Derive from Murex Family/Group/Type; crosswalk remains unresolved |

## Identifier inconsistency

The primary mapping gives booking-entity FMID `10075222` and counterparty FMID `400899993`. Enhancement examples give `M_ATLAS_LEID` values `10036642` for `SHANGHAI` and `400796812` for `LOUDRECOMSH/BJG`.

The source does not establish whether these are different environments, different identifier domains, or alternative records. The authoritative value for the SCBML `FMID` scheme remains open; see [[which-fmid-or-atlas-leid-is-authoritative-for-murex-scbml-party-identifiers]].

## Preserved mapping inventory

| Items | Json | Field Description | Is_Mutiple_Occurance | Repeat Reason | Mapping Type | MxML Xpath | MxML Value | Comments | SCBML Xpath | SCBML Value |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Cashflow.Cashflow_Event_Type | Type of event New/Withdrawal/Amendment | Yes | W&N | Event | /MxPayML/event | Validate | New | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:event` | New |
| 2 | Cashflow.Cashflow_State | Current cashflow or payment lifecycle state | Yes | W&N | FlowStatus | /MxPayML/flowStatus | CHCK | PROJECTED | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:state` | PROJECTED |
| 3 | Trade.Trade_Id | SCB trade unique identifier | No |  | tradeID | /MxPayML/transactionID | 81708120 | get from TDS3 | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:partyTradeIdentifier/conf:tradeId` | 81708120 |
| 4 | Cashflow.Cashflow_Id | Unique cashflow identifier | Yes | W&N | cashflowID | /MxPayML/flowID | 87755146 | Add zeroes before the cashflow ID; total is 12 characters | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:cashflowIdentifier/scb:cashflowId` | 000087755146 |
| 5 | Cashflow.Payment_Amount | Payment amount for one cashflow | Yes | XVA | amount | /MxPayML/flowAmount | 23220.63 |  | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:paymentAmount/conf:amount` | 23220.63 |
| 6 | Cashflow.Payment_Currency | Payment currency | Yes | XVA | currency | /MxPayML/currency | USD |  | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:paymentAmount/conf:currency` | USD |
| 7 | Cashflow.Cashflow_Version | Version increased when payment transaction changes | Yes | W&N |  |  |  | hard code as 0 | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:cashflowIdentifier/scb:cashflowVersion` | 0 |
| 8 | Cashflow.Cashflow_Business_Version | Business version increased when materialized | Yes | W&N |  |  |  | hard code as 0 | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:cashflowIdentifier/scb:businessVersion` | 0 |
| 9 | Cashflow.Event_Date | Time when the payment event is created | Yes | W&N | payment create date | /MxPayML/systemDate | 20220606 |  | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:eventDate` | 2022-06-06 |
| 10 | Cashflow.Payment_Date | Unadjusted payment date | Yes | XVA | ReleaseDate | /MxPayML/releaseDate | 20220808 |  | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:paymentDate/conf:unadjustedDate` | 2022-08-08 |
| 11 | Trade.Settlement_Method | Settlement mechanism | No |  | Settlement method | /MxPayML/type | cash |  | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:partyTradeInformation/scbextn:settlementMethod` | Cash |
| 12 | Portfolio.Booking_Entity_Trade_Portfolio_Name | Unique booking portfolio name | No |  | portfilio | /MxPayML/portfolio | COM_SHA_BTB |  | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:tradePortfolio/conf:partyPortfolioName/conf:portfolioName` | COM_SHA_BTB |
| 13 | Instrument_Common.ISDA_Taxonomy | ISDA OTC derivatives product classification | No |  |  |  |  |  | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:productId` | Commodity:Swap |
| 14 |  | Payment action user |  |  | user name | /MxPayML/user | SPWONG（Payment action user） | trader get from TDS3 |  |  |
| 15 | Entity.Person.Trader_PSID | PeopleSoft ID of trader | No |  | Trader PSID |  |  | trader PSID get from TDS3 | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party/conf:person/conf:personId` | 1490619 |
| 16 |  | Trade confirmation status |  |  | trade confirmation status |  | COMP/VALD | MXML ENHANCE |  |  |
| 17 |  | Booking entity SCI FMID / Atlas ID | No |  | entity | /MxPayML/entity | SHANGHAI | MXML ENHANCE | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id="party1"]/conf:partyId` |  |
| 18 | Entity.Booking_Entity_SCI_FMID | Booking entity FMID |  |  |  | /MxPayML/scbExtraInfoBlock/entityFMID |  | In MXML get the SCB FMID via SCB entity info | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id="party1"]/conf:partyId` | 10075222 |
| 19 |  | Counterparty SCI FMID / Atlas ID | No |  | CP | /MxPayML/counterparty | LOUDRECOMSH/BJG | MXML ENHANCE | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id="party2"]/conf:partyId` |  |
| 20 | Entity.Counterparty_SCI_FMID | Counterparty FMID |  |  |  | /MxPayML/scbExtraInfoBlock/counterpartyFMID |  | In MXML get the CTP FMID via CP info | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id="party2"]/conf:partyId` | 400899993 |
| 21 | Cashflow.Payment_Payer_Party_Reference | Party responsible for making payment | Yes | XVA | payer | /MxPayML/isCredit | N | Do the transformation in Ratan MLS | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:payerPartyReference` | Party1 |
| 22 | Cashflow.Payment_Receiver_Party_Reference | Party receiving payment | Yes | XVA | receiver | /MxPayML/isCredit | Y |  | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:receiverPartyReference` | Party2 |
| 23 | Instrument_Common.Source_System_Instrument_Sub_Type | Murex source-system instrument subclassification | No |  | instrument_sub_type | fam/group/type/typology/strategy |  |  | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:productType` | {MocksubType} |
| 24 |  | Family |  |  | family | /MxPayML/transactionFamily | COM | MLS maps to CFI code; check with Dinesh |  |  |
| 25 |  | Group |  |  | group | /MxPayML/transactionGroup | SWAP |  |  |  |
| 26 |  | Type |  |  | type | /MxPayML/transactionType | FXD |  |  |  |
| 27 |  | Action |  |  | action | /MxPayML/scbExtraInfoBlock/action | INS |  |  |  |
| 28 |  | Last market |  |  | tradeLastMKT | /MxPayML/scbExtraInfoBlock/tradeLastMKT |  |  |  |  |
| 29 |  | Parent transaction ID |  |  | TrnParentID | /MxPayML/scbExtraInfoBlock/TrnParentID | 0 |  |  |  |
| 30 |  | Original transaction ID |  |  | TrnOrginalID | /MxPayML/scbExtraInfoBlock/TrnOrginalID | 81708120 |  |  |  |
| 31 |  | Flow detail |  |  | flow | /MxPayML/scbExtraInfoBlock/Flows/flow | Flowid:91145574, status:SNTR, value_date:20230110 |  |  |  |

## Enrichment SQL

```sql
select M_VAL_STATUS from TRN_HDR_DBF WHERE M_NB= Trade ID
```

```sql
SELECT EN.M_LABEL,EN.M_CTP_COD,CP.M_SCI_ID,CP.M_ATLAS_LEID
FROM TABLE#DATA#ENTITY_DBF EN, TABLE#DATA#COUNTERP_DBF CP
WHERE EN.M_CTP_COD=CP.M_LABEL AND EN.M_LABEL='SHANGHAI'
```

```sql
SELECT M_LABEL,M_SCI_ID,M_ATLAS_LEID
FROM TABLE#DATA#COUNTERP_DBF
WHERE M_LABEL='LOUDRECOMSH/BJG'
```

## CN Payments report inventory

The report proposal includes publication metadata, cashflow identifiers and state, payment details, product classification, trade identifiers and state, party identifiers, settlement and delivery methods, portfolio data, reversal references, business-unit fields, trader PSID, and action type.

Many fields are marked as requiring derivation logic. Payment type, publication ID, execution timestamp, business-unit mappings, and reversal behavior are not defined by the source.

## Limitations and open issues

- The source samples and updated attachment are absent.
- Several XPath expressions contain malformed or HTML-rendered URI quoting.
- FMID and Atlas identifier examples conflict.
- `CHCK` to `PROJECTED` is shown without a complete state conversion matrix.
- `Reverse=Y` behavior is unspecified.
- Event and version semantics are inconsistent with hard-coded output values.
- Product classification and CFI crosswalks remain provisional.
- `releaseDate` versus report `Value` payment-date sourcing requires reconciliation.

These limitations should be resolved before treating the mapping as an authoritative interface contract.