---
type: source
title: Include Swift Suppressed Status in LMS Feed for Receipts
authors: []
year: 2025
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/10917030/"
venue: "Cash Settlement Functional Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, LMS, Swift, receipt-processing, functional-requirement]
related: [lms, murex, ratan, fmrp, scbml-cashflow-data-message, swift-suppressed-lms-feed-contract, cashflow-suppression-rule, manual-entity-lms-reference-data-feed, what-is-the-authoritative-lms-contract-for-swift-suppressed-receipts, does-lms-require-vostro-nostro-data-for-swift-suppressed-receipts, lms-feed-status-and-event-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/Include Swift Suppressed status in LMS feed (only for receipts).md"]
---

# Include Swift Suppressed Status in LMS Feed for Receipts

## Summary

This functional requirement changes the LMS feed eligibility rule for receipt-only cashflows. A cashflow in `Swift Suppressed` status must be sent to LMS when SCB receives funds from the client even though no corresponding nostro payment was generated in Ratan.

The initial eligibility change is clearly specified. The message contract for subsequent lifecycle transitions, the representation of the status in `CashflowData`, and the minimum settlement-instruction data remain subject to agreement with the LMS team.

## Work item and related documentation

- ADO Story 10917030: [Include Swift Suppressed status in LMS feed (only for receipts)](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/10917030/)
- Related document: [LMS Feed - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/LMS+Feed)
- Requirement status recorded in the source: pending agreement with LMS as of 2025-10-27.

## Eligibility rule

### Current behavior

| Cashflow status | Send to LMS |
|---|---|
| `RELEASED` | Yes |
| `SETTLED` | Yes |
| Others | No |

### Proposed behavior

| Cashflow status | Send to LMS |
|---|---|
| `RELEASED` | Yes |
| `SETTLED` | Yes |
| `Swift Suppressed (Receive only)` | Yes |
| `Undo Swift Suppression (Receive only)` | Pending LMS confirmation in the requirement table; later confirmed by Dinesh as requiring a message |
| `Swift Suppressed (Receive only)-Withdrawal` | Pending LMS confirmation in the requirement table; later confirmed by Dinesh as requiring a message |
| Others | No |

The rule is limited to receipt-only cashflows. It does not establish LMS eligibility for outbound Swift-suppressed cashflows or for all cashflows in a generic suppressed state.

## Business rationale

The source describes a case where:

1. Swift payment generation is suppressed.
2. No nostro payment occurs in Ratan.
3. SCB nevertheless receives payment from the client.
4. LMS must receive the cashflow so that downstream processing reflects the actual receipt.

This separates suppression of an outbound Swift payment from suppression of the underlying cashflow and its downstream representation. The distinction extends [[concepts/cashflow-suppression-rule]] and [[concepts/manual-entity-lms-reference-data-feed]].

## Scenario lifecycle

| Scenario | LMS action |
|---|---|
| `New -> Swift Suppressed (Receive Only)` | Send to LMS |
| `New -> Swift Suppressed (Receive Only) -> Undo Swift Suppression` | Another LMS message required; event and payload remain undefined |
| `New -> Swift Suppressed (Receive Only) -> Withdrawal (CANCELLED)` | Another LMS message required; event and payload remain undefined |
| `New -> Swift Suppressed (Receive Only) -> Manual Failed (FAILED)` | No decision recorded |

The source records the following existing withdrawal behavior:

- `Queued`, `Waiting`, and `Ready`: not sent to LMS.
- `Withdrawal-Cancelled`: not sent to LMS.
- `Released` and `Settled`: sent to LMS.
- `Withdrawal-Waiting` with a pending exception that reaches `Released` or `Settled`: sent to LMS.

## Message contract

The proposed message is an SCBML 4.0 XML `CashflowData` message. Its structure includes:

- SCBML header and message metadata.
- `Insert` processing event.
- A cashflow business event such as `New` or `Withdrawal`.
- Netting and cashflow identifiers.
- Payment amount, currency, and payment date.
- Trade, portfolio, product, and workflow information.
- Party and FM identifiers.
- Cashflow settlement instructions and SSI data.

The template does not contain an explicit dedicated cashflow-status field for `Swift Suppressed`. The status may therefore need to be represented through `businessEvent`, another existing field, or a change to the LMS contract.

The template remains a proposal and is not evidence of a finalized LMS interface.

## Message template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<scb:SCBML scbmlVersion="4-0" xmlns:scb="http://www.sc.com/SCBML-1" xmlns:conf="http://www.fpml.org/FpML-5/confirmation" xmlns:scbextn="http://www.sc.com/scbml/extension-2-0"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://www.sc.com/SCBML-1 ../../../../../core/4-0/scbml-4-0.xsd http://www.sc.com/SCBML-1 ../../../../../payloadType/cashflowPayload/4-0/scbml-cashFlow-4-0.xsd">
    <scb:header>
  <scb:messageDetails>
   <scb:messageVersion>1.0</scb:messageVersion>
   <scb:messageType>
    <scb:typeName>CashflowData</scb:typeName>
   </scb:messageType>
  </scb:messageDetails>
  <scb:originationDetails>
   <scb:messageSender>
    <scb:messageSender systemScheme="http://www.sc.com/coding-scheme/system-1-0">${stackFlow!}</scb:messageSender>
    <scb:senderDomain>
     <scb:domainName domainNameScheme="http://www.sc.com/coding-scheme/domainNamescheme-1-0">FM</scb:domainName>
     <scb:countryCode>ALL</scb:countryCode>
   </scb:messageSender>
   <scb:messageTimestamp>${messageTimestamp!}</scb:messageTimestamp>
   <scb:initiatedTimestamp>2016-08-06T05:20:04Z</scb:initiatedTimestamp>
   <scb:trackingId>${trackingId!}</scb:trackingId>
  </scb:originationDetails>
  <scb:captureSystem>Stella</scb:captureSystem>
  <scb:process>
   <scb:eventType>Insert</scb:eventType>
  </scb:process>
 </scb:header>
 <scb:payload>
  <scb:payloadFormat>XML</scb:payloadFormat>
  <scb:payloadType>cashflowPayload</scb:payloadType>
  <scb:payloadVersion>4-0</scb:payloadVersion>
  <scb:cashflowPayload>
   <scb:cashflow>
    <scb:header>
     <scb:event eventScheme="http://www.sc.com/coding-scheme/event/scbml-business-event">${businessEvent!}</scb:event>
     <scb:linkId linkIdScheme="http://www.sc.com/coding-scheme/linkId/cashflow/nettingId">${nettingId!}</scb:linkId>
     <scb:cashflowIdentifier>
      <scb:cashflowId cashflowIdScheme="http://www.sc.com/coding-scheme/cashflowId">${cashflowId!}</scb:cashflowId>
     </scb:cashflowIdentifier>
    </scb:header>
    <scb:payment>
     <conf:payerPartyReference href="party1"/>
     <conf:receiverPartyReference href="party2">${receiverPartyReference!}</conf:receiverPartyReference>
     <conf:paymentAmount>
      <conf:currency currencyScheme="http://www.fpml.org/coding-scheme/external/iso4217-2001-08-15">${isoCurrency!}</conf:currency>
      <conf:amount>${paymentAmount!}</conf:amount>
     </conf:paymentAmount>
     <conf:paymentDate>
      <conf:unadjustedDate>${unadjustedDate!}</conf:unadjustedDate>
      <conf:dateAdjustments>
       <conf:businessDayConvention>NONE</conf:businessDayConvention>
      </conf:dateAdjustments>
     </conf:paymentDate>
    </scb:payment>
   </scb:cashflow>
   <scb:tradeReferenceInformation>
    <conf:partyTradeIdentifier>
     <conf:issuer>party1</conf:issuer>
     <conf:tradeId tradeIdScheme="http://www.sc.com/coding-scheme/tradeId">${tradeId!}</conf:tradeId>
    </conf:partyTradeIdentifier>
    <scb:partyTradeInformation xsi:type="scbextn:PartyTradeInformation">
     <conf:partyReference href="party1"/>
     <conf:executionDateTime>${tradeBookingTimestamp!}</conf:executionDateTime>
     <scbextn:tradeSource tradeSourceScheme="http://www.sc.com/coding-scheme/tradeSource/originalSourceSystem">
      <scbextn:name>${sourceSystem!}</scbextn:name>
     </scbextn:tradeSource>
    </scb:partyTradeInformation>
    <scb:productType productTypeScheme="http://www.sc.com/coding-scheme/external/product-classification/financialInstrumentCode">${productType!}</scb:productType>
    <scb:productId productIdScheme="http://www.fpml.org/coding-scheme/product-taxonomy">${allotment!}</scb:productId>
    <scb:tradePortfolio>
     <conf:partyPortfolioName>
      <conf:partyReference href="party1"/>
      <conf:portfolioName>${portfolioName!}</conf:portfolioName>
     </conf:partyPortfolioName>
    </scb:tradePortfolio>
    <scb:state stateScheme="http://www.sc.com/coding-scheme/state/tradeWorkflowStatus">${tradeWorkflowStatus!}</scb:state>
   </scb:tradeReferenceInformation>
   <scb:party id="party1">
    <conf:partyId partyIdScheme="http://www.sc.com/coding-scheme/partyId/LEID">${legalEntityId!}</conf:partyId>
    <conf:partyId partyIdScheme="http://www.sc.com/coding-scheme/partyId/FMID">${party1FmId!}</conf:partyId>
    <conf:person id="trader">
     <conf:personId personIdScheme="http://www.sc.com/coding-scheme/personId/PSID">${dealerPersonId!}</conf:personId>
    </conf:person>
   </scb:party>
   <scb:party id="party2">
    <conf:partyId>Dummy</conf:partyId>
    <conf:partyId partyIdScheme="http://www.sc.com/coding-scheme/partyId/FMID">${party2FmId!}</conf:partyId>
    <conf:partyId partyIdScheme="http://www.sc.com/coding-scheme/partyId/FMCODE">${party2FmCode!}</conf:partyId>
   </scb:party>
   <scb:cashflowSSI>
    <scb:SSIId>${ssiId!}</scb:SSIId>
    <scb:settlementInstruction>
     <conf:intermediaryInformation>
      <conf:routingIdsAndExplicitDetails>
       <conf:routingIds><conf:routingId>${intermediaryInformationRoutingId!}</conf:routingId></conf:routingIds>
      </conf:routingIdsAndExplicitDetails>
     </conf:intermediaryInformation>
     <conf:beneficiaryBank>
      <conf:routingIdsAndExplicitDetails>
       <conf:routingIds><conf:routingId>${beneficiaryBankRoutingId!}</conf:routingId></conf:routingIds>
      </conf:routingIdsAndExplicitDetails>
     </conf:beneficiaryBank>
     <conf:beneficiary>
      <conf:routingIdsAndExplicitDetails>
       <conf:routingIds><conf:routingId>${beneficiaryRoutingId!}</conf:routingId></conf:routingIds>
       <conf:routingName>${beneficiaryRoutingName!}</conf:routingName>
       <conf:routingAccountNumber>${beneficiaryRoutingAccountNumber!}</conf:routingAccountNumber>
      </conf:routingIdsAndExplicitDetails>
     </conf:beneficiary>
     <scb:orderingCustomer>
      <conf:routingIdsAndExplicitDetails>
       <conf:routingIds><conf:routingId>${orderingCustomerRoutingId!}</conf:routingId></conf:routingIds>
      </conf:routingIdsAndExplicitDetails>
     </scb:orderingCustomer>
     <scb:settlementMeans>
      <scb:settlementAccountNo>${settlementAccountNo!}</scb:settlementAccountNo>
     </scb:settlementMeans>
     <scb:partyReference href="party2"/>
    </scb:settlementInstruction>
    <scb:settlementInstruction>
     <conf:correspondentInformation>
      <conf:routingIdsAndExplicitDetails>
       <conf:routingIds><conf:routingId>${correspondentInformationRoutingId!}</conf:routingId></conf:routingIds>
      </conf:routingIdsAndExplicitDetails>
     </conf:correspondentInformation>
     <conf:beneficiary>
      <conf:routingIds><conf:routingId>${beneficiaryBankParty1RoutingId!}</conf:routingId></conf:routingIds>
     </conf:beneficiary>
     <scb:partyReference href="party1"/>
    </scb:settlementInstruction>
   </scb:cashflowSSI>
  </scb:cashflowPayload>
 </scb:payload>
</scb:SCBML>
```

## Data mapping

| Field | Mandatory | Sample |
|---|---:|---|
| `stackFlow` | Not specified | `FMRPMUREX` |
| `messageTimestamp` | Not specified | `2025-10-25T01:50:11.502170181` |
| `trackingId` | Not specified | `e4629d3f-2b13-45f8-b042-8f4d90eca680` |
| `businessEvent` | Yes | `New/Withdrawal` |
| `nettingId` | Yes for netting | `c65e315b-afd2-11f0-8792-005056ac01ca` |
| `cashflowId` | Yes | `M00202510132` |
| `receiverPartyReference` | Yes | `Debit` |
| `isoCurrency` | Yes | `USD` |
| `paymentAmount` | Yes | `1870.00` |
| `unadjustedDate` | Yes | `2025-07-29` |
| `tradeId` | Yes | `103991599` |
| `tradeBookingTimestamp` | Not specified | `2025-06-27T14:27:44Z` |
| `sourceSystem` | Not specified | `Murex` |
| `productType` | Yes | `IFXXXX` |
| `allotment` | Yes | `CURR\|FXD\|FXD` |
| `portfolioName` | Yes | `FXI_OP_LDN` |
| `tradeWorkflowStatus` | No | `VALD` |
| `legalEntityId` | Not specified | `11090155` |
| `party1FmId` | Yes | `10075222` |
| `dealerPersonId` | Not specified | `1474102` |
| `party2FmId` | No | `400617196` |
| `party2FmCode` | No | `EDELWEISS I S P*SIN` |
| `ssiId` | No | `47349561` |
| `beneficiaryBankRoutingId` | No | `SCBLSG22XXX` |
| `beneficiaryRoutingName` | No | `EDELWEISS INTERNATIONAL SINGAPORE` |
| `beneficiaryRoutingAccountNumber` | No | `0106533495` |
| `settlementAccountNo` | No | `USD MAIN` |
| `correspondentInformationRoutingId` | No | `SCBLUS33XXX` |
| `beneficiaryBankParty1RoutingId` | No | `15199166301` |

Optional routing fields include `intermediaryInformationRoutingId`, `beneficiaryRoutingId`, and `orderingCustomerRoutingId`.

## Open questions

1. Which `businessEvent` values represent the initial Swift Suppressed receipt, Undo Swift Suppression, withdrawal, and Manual Failed?
2. Does LMS require an explicit cashflow-status field?
3. Should Undo and Withdrawal use the initial payload structure?
4. Does `Manual Failed` require a follow-up LMS message?
5. Which XML fields are mandatory when Vostro/Nostro stamping is unavailable?
6. Should additional stamping be performed before sending the message?
7. Is `receiverPartyReference = Debit` correct for a receive-only cashflow?
8. What are the retry, duplicate, ordering, and reconciliation rules for multiple messages for one `cashflowId`?

## Assessment

The requirement strongly establishes the initial feed-eligibility change but remains a partially specified integration contract. LMS confirmation is still required for lifecycle event mapping, payload semantics, missing settlement data, and operational handling.
