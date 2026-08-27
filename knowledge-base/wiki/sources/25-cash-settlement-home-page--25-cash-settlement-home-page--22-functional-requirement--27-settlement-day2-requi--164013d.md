---
type: source
title: LMS - Remove the Entity Filter in LMS Feed
authors: []
year: 2025
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/10917020"
venue: Azure DevOps
tags: [functional-requirement, lms, ratan, cashflow-feed, scbml, entity-filter]
related: [ratan, lms, ratan-lms-entity-filter-removal, manual-entity-lms-reference-data-feed, has-lms-confirmed-all-entity-ratan-feed-compatibility, what-is-the-approved-null-product-taxonomy-allotment-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/LMS - Remove the entity filter in LMS feed.md"]
created: 2026-08-23
updated: 2026-08-23
---
# LMS - Remove the Entity Filter in LMS Feed

ADO Story 10917020 records a functional requirement for the [[ratan]] cashflow feed to [[lms]]: remove RATAN-side booking-entity-list validation and send cashflow messages for all entities to LMS.

The stated scope is limited to sending eligibility. The SCBML `CashflowData` message template is explicitly stated to remain unchanged. The cited confirmation, dated 2025-10-27, attributes the downstream handling of all entities to LMS.

## Recorded requirement

- Remove the entity filter on RATAN and send all entities to LMS.
- Do not change the message template sent to LMS.
- LMS-side handling, including proposed `DV`, `LQ`, and `MX` prefix behaviour, requires confirmation from the LMS team.

This source does not contain implementation evidence, LMS sign-off, acceptance criteria, volume assessment, error-handling rules, or reconciliation results. The proposed all-entity feed is therefore a requirement rather than demonstrated production behaviour.

## Open points

1. LMS must confirm that it can consume all entity records emitted by RATAN, including previously excluded entities.
2. The stated prefix behaviour—`DV` or `LQ` for RATAN messages and `MX` for other sources—is unconfirmed and must not be treated as an approved RATAN requirement.
3. The source says a null upstream `product-taxonomy` is populated as `???????` in `allotment`, while the mapping identifies `allotment` as mandatory. The approved fallback rule is unresolved.
4. Several supplied XPath expressions appear internally inconsistent with the template. The table is preserved as source evidence, not validated as an executable interface specification.

See [[ratan-lms-entity-filter-removal]] and [[has-lms-confirmed-all-entity-ratan-feed-compatibility]].

## SCBML message template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- edited with XMLSpy v2013 (x64) (http://www.altova.com) by Amit Kumar Singh (STANDARD CHARTERED BANK) -->
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
    </scb:senderDomain>
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
     <conf:intermediaryInformation><conf:routingIdsAndExplicitDetails><conf:routingIds><conf:routingId>${intermediaryInformationRoutingId!}</conf:routingId></conf:routingIds></conf:routingIdsAndExplicitDetails></conf:intermediaryInformation>
     <conf:beneficiaryBank><conf:routingIdsAndExplicitDetails><conf:routingIds><conf:routingId>${beneficiaryBankRoutingId!}</conf:routingId></conf:routingIds></conf:routingIdsAndExplicitDetails></conf:beneficiaryBank>
     <conf:beneficiary><conf:routingIdsAndExplicitDetails><conf:routingIds><conf:routingId>${beneficiaryRoutingId!}</conf:routingId></conf:routingIds><conf:routingName>${beneficiaryRoutingName!}</conf:routingName><conf:routingAccountNumber>${beneficiaryRoutingAccountNumber!}</conf:routingAccountNumber></conf:routingIdsAndExplicitDetails></conf:beneficiary>
     <scb:orderingCustomer><conf:routingIdsAndExplicitDetails><conf:routingIds><conf:routingId>${orderingCustomerRoutingId!}</conf:routingId></conf:routingIds></conf:routingIdsAndExplicitDetails></scb:orderingCustomer>
     <scb:settlementMeans><scb:settlementAccountNo>${settlementAccountNo!}</scb:settlementAccountNo></scb:settlementMeans>
     <scb:partyReference href="party2"/>
    </scb:settlementInstruction>
    <scb:settlementInstruction>
     <conf:correspondentInformation><conf:routingIdsAndExplicitDetails><conf:routingIds><conf:routingId>${correspondentInformationRoutingId!}</conf:routingId></conf:routingIds></conf:routingIdsAndExplicitDetails></conf:correspondentInformation>
     <conf:beneficiary><conf:routingIds><conf:routingId>${beneficiaryBankParty1RoutingId!}</conf:routingId></conf:routingIds></conf:beneficiary>
     <scb:partyReference href="party1"/>
    </scb:settlementInstruction>
   </scb:cashflowSSI>
  </scb:cashflowPayload>
 </scb:payload>
</scb:SCBML>
```

## Data mapping

| Field Name in Message Template | xPath | Mandatory | Sample |
| --- | --- | --- | --- |
| stackFlow | `/scb:SCBML/scb:header/scb:originationDetails/scb:messageSender/scb:messageSender[@systemScheme='http://www.sc.com/coding-scheme/stack-flow']` | N | FMRPMUREX |
| messageTimestamp | `/scb:SCBML/scb:header/scb:originationDetails/scb:messageTimestamp` | Y | 2025-10-25T01:50:11.502170181 |
| trackingId | `/scb:SCBML/scb:header/scb:originationDetails/scb:trackingId` | Y | e4629d3f-2b13-45f8-b042-8f4d90eca680 |
| businessEvent | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:event` | Y | New/Withdrawal |
| nettingId | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:linkId` | Y for netting | c65e315b-afd2-11f0-8792-005056ac01ca |
| cashflowId | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:cashflowIdentifier/scb:cashflowId` | Y | M00202510132 |
| receiverPartyReference | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:receiverPartyReference[@href='party2']` | Y | Debit |
| isoCurrency | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:paymentAmount/conf:currency` | Y | USD |
| paymentAmount | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:paymentAmount/conf:amount` | Y | 1870.00 |
| unadjustedDate | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:paymentDate/conf:unadjustedDate` | Y | 2025-07-29 |
| tradeId | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:partyTradeIdentifier/conf:tradeId` | Y | 103991599 |
| tradeBookingTimestamp | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:partyTradeInformation[@xsi:type='scbextn:PartyTradeInformation']/conf:executionDateTime` | N | 2025-06-27T14:27:44Z |
| sourceSystem | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:partyTradeInformation/scbextn:tradeSource/scbextn:name` | N | Murex |
| productType | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:productType` | Y | IFXXXX |
| allotment | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:productId` | Y | CURR\|FXD\|FXD |
| portfolioName | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:tradePortfolio/conf:partyPortfolioName/conf:portfolioName[1]` | Y | FXI_OP_LDN |
| tradeWorkflowStatus | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:state` | N | VALD |
| legalEntityId | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id='party1']/conf:partyId[@partyIdScheme='http://www.sc.com/coding-scheme/partyId/LEID']` | N | 11090155 |
| party1FmId | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id='party1']/conf:partyId[@partyIdScheme='http://www.sc.com/coding-scheme/partyId/FMID']` | Y | 10075222 |
| dealerPersonId | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id='party1']/conf:person//conf:personId` | N | 1474102 |
| party2FmId | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id='party2']/conf:partyId[@partyIdScheme='http://www.sc.com/coding-scheme/partyId/FMID']` | Y | 400617196 |
| party2FmCode | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id='party2']/conf:partyId[@partyIdScheme='http://www.sc.com/coding-scheme/partyId/FMCODE']` | N | EDELWEISS I S P*SIN |
| ssiId | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:SSIId` | N | 47349561 |
| intermediaryInformationRoutingId | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction[scb:partyReference/@href='party2']/conf:intermediaryInformation/conf:routingIdsAndExplicitDetails/conf:routingIds/conf:routingId` | N | |
| beneficiaryBankRoutingId | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction[scb:partyReference/@href='party2']/conf:beneficiaryBank/conf:routingIdsAndExplicitDetails/conf:routingIds/conf:routingId` | N | SCBLSG22XXX |
| beneficiaryRoutingId | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction[scb:partyReference/@href='party2']/conf:beneficiary/conf:routingIdsAndExplicitDetails/conf:routingIds/conf:routingId` | N | |
| beneficiaryRoutingName | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction[scb:partyReference/@href='party2']/conf:beneficiary/conf:routingIdsAndExplicitDetails/conf:routingName` | N | EDELWEISS INTERNATIONAL SINGAPORE |
| beneficiaryRoutingAccountNumber | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction[scb:partyReference/@href='party2']/conf:beneficiary/conf:routingIdsAndExplicitDetails/conf:routingAccountNumber` | N | 0106533495 |
| orderingCustomerRoutingId | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction[scb:partyReference/@href='party2']/scb:orderingCustomer/conf:routingIdsAndExplicitDetails/conf:routingIds/conf:routingId` | N | |
| settlementAccountNo | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction/scb:settlementMeans/scb:settlementAccountNo` | N | USD MAIN |
| correspondentInformationRoutingId | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction[scb:partyReference/@href='party1']/conf:correspondentInformation/conf:routingIdsAndExplicitDetails/conf:routingIds/conf:routingId` | N | SCBLUS33XXX |
| beneficiaryBankParty1RoutingId | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction[scb:partyReference/@href='party1']/conf:beneficiary/conf:routingIds/conf:routingId[@routingIdCodeScheme='http://www.sc.com/coding-scheme/routingId/ebbsAccountId']` | N | 15199166301 |