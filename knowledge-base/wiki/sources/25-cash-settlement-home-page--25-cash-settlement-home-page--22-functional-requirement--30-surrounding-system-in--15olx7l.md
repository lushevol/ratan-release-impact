---
type: source
title: LMS Feed Functional Requirement
authors: [Jill Du]
year: 2023
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/10917020"
venue: "Cash Settlement Home Page functional requirements"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, lms, ratan, fmrp, cashflow, scbml, integration]
related: [ratan, cash-settlement-home-page, lms, lms-cashflow-feed-eligibility, netting-resultant-allotment-default, lms-feed-entity-filter-before-and-after, what-is-the-authoritative-fmrp-field-20-prefix-mapping, is-the-lms-entity-filter-fully-removed-for-all-entities, what-is-the-authoritative-lms-settlement-means-and-beneficiary-bic-contract, what-are-the-authoritative-lms-scxml-xpath-mappings, razor, stella, nostro-stamping, vostro-data-sourcing-from-ssi-plus, netting-eligibility-static-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/LMS Feed.md"]
---

# LMS Feed Functional Requirement

## Scope and status

This requirement defines the cashflow feed from [[ratan]] and FMRP into [[lms]]. It covers feed eligibility, entity filtering, source-system identification, withdrawal behavior, settlement-instruction fields, and netting-resultant allotment.

The document was reviewed and agreed with business owners on July 21, 2023. A later entity-filter change is dated 2025-10-28. The document owner is Jill Du. Product owners are Dinesh and Arockia. Business owners are Kannan, Kamesh, Balasubramanian, and Nivethitha. Developers are Li, Daniel Zhaolei Huang, and Caroline Xinmiao. QA contacts are Ma and Shimeng.

## Settlement-data requirements

- SCB Pay cashflows require both Vostro and Nostro.
- SCB Receive cashflows require Nostro only.

These requirements complement, but are distinct from, the LMS delivery gates documented below.

## Effective LMS eligibility

The explicit status and settlement rules are:

| Condition | Feed result |
| --- | --- |
| Cashflow status `RELEASED` | Send to LMS |
| Cashflow status `SETTLED` | Send to LMS |
| Any other cashflow status | Do not send |
| Settlement means `Nos` | Eligible |
| Settlement means `Over Account` | Not eligible |
| Settlement means `FXBRREC` | Not eligible |
| Other settlement means | Not eligible |
| Beneficiary BIC `REJECTXXALL` | Not eligible |
| Any other beneficiary BIC | Eligible |

The logical model fields named by the source are:

```text
Settlement_Instruction.Account.SCB_Nostro_Account_Type
Settlement_Instruction.Account.Beneficiary_BIC_code
```

The effective rule can be represented as:

```text
SendToLMS =
    cashflowStatus IN {RELEASED, SETTLED}
    AND settlementMeans = Nos
    AND beneficiaryBIC != REJECTXXALL
    AND currentEntityPolicyAllowsDelivery
```

## Entity-filter change

The original design excluded a hard-coded list of booking entities. The later requirement states:

> Remove entity filter on Ratan side and send all entities to LMS.

The message template is stated to be unchanged. The affected entities changed from `No` to `Yes`, including:

- `SCB EGYPT*CAI`
- `SCB SAUDI*RYD`
- `NEPAL GRINDLAYS*KTM`
- `SCB KL*KUL?`
- `STANCHART SAADIQ*KUL`
- `SCB TAIPEI*TPE`
- `SCB TAIPOBU*TPE`
- `SCB BANGKOK*BKK`
- `SCB MAUR*PLO`
- `SCB JAKARTA*JKT`
- `SCB MANILA*MNL`
- `SCB TOKYO*TYO`
- `SCBL*JBG`
- `SC PVT BK JE BR*STH`
- `CAZENOVE*HKGJ@`
- `SCB MNL FCD*MNL`

`Other Manual Entities` remains eligible. `PHILIP FCU` appears in the later table as `No`, without an FMID or branch code. The user cases still refer to the former “16 entities” condition, so the current exception policy requires confirmation.

The change is associated with ADO Story `10917020`, “LMS - Remove the entity filter in LMS feed”.

## Withdrawal behavior

A withdrawal is not sent while it remains in `Waiting + Pending Exception`. After maker-checker completion, the withdrawal reaches `Released` and is sent to LMS. This makes maker-checker release a delivery gate rather than sending every withdrawal event immediately.

## Source-system and SWIFT field 20 mapping

The source states that LMS receives the raw source-system value from Ratan and that RAZOR generates the SWIFT field 20 prefix downstream.

| Booking System | Source System | Flow | Prefix of field 20 |
| --- | --- | --- | --- |
| SABRE EQ | `STELLA` | SABRE EQ -> BCS STELLA -> STELLA -> TDS3 -> RATAN ONE | `EQ` |
| LOANIQ | `LOANIQ` | LOANIQ -> STELLA -> TDS3 -> RATAN ONE | `LQ` |
| BLADE/S2BX/CFETS | `FMRP` | BLADE/S2BX/CFETS -> STELLA -> TDS3 -> RATAN ONE | `DV` |

The surrounding prose states `MX`, rather than `DV`, for the BLADE/S2BX/CFETS China go-live flow. This discrepancy is tracked in [[what-is-the-authoritative-fmrp-field-20-prefix-mapping]].

## Netting-resultant allotment

ADO Story `6969335`, “LMS Feed - Update value as NETTING RESULTANT where taxonomy is empty”, defines the following default:

```text
If the cashflow is a netting resultant,
the cashflow ID starts with N*,
and the original allotment is blank,
populate allotment with NETTING RESULTANT.
```

The rule is conditional. Existing product taxonomy is retained when present. Examples include `CURR|FXD|FXD`, `COM|SWAP`, and the default `NETTING RESULTANT`.

## SCBML message contract

The message is an XML `SCBML` payload with `scbmlVersion="4-0"`, `messageType` `CashflowData`, `payloadType` `cashflowPayload`, `payloadVersion` `4-0`, and an `Insert` event.

The source template is reproduced below:

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
     <conf:intermediaryInformation>
      <conf:routingIdsAndExplicitDetails>
       <conf:routingIds>
        <conf:routingId>${intermediaryInformationRoutingId!}</conf:routingId>
       </conf:routingIds>
      </conf:routingIdsAndExplicitDetails>
     </conf:intermediaryInformation>
     <conf:beneficiaryBank>
      <conf:routingIdsAndExplicitDetails>
       <conf:routingIds>
        <conf:routingId>${beneficiaryBankRoutingId!}</conf:routingId>
       </conf:routingIds>
      </conf:routingIdsAndExplicitDetails>
     </conf:beneficiaryBank>
     <conf:beneficiary>
      <conf:routingIdsAndExplicitDetails>
       <conf:routingIds>
        <conf:routingId>${beneficiaryRoutingId!}</conf:routingId>
       </conf:routingIds>
       <conf:routingName>${beneficiaryRoutingName!}</conf:routingName>
       <conf:routingAccountNumber>${beneficiaryRoutingAccountNumber!}</conf:routingAccountNumber>
      </conf:routingIdsAndExplicitDetails>
     </conf:beneficiary>
     <scb:orderingCustomer>
      <conf:routingIdsAndExplicitDetails>
       <conf:routingIds>
        <conf:routingId>${orderingCustomerRoutingId!}</conf:routingId>
       </conf:routingIds>
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
       <conf:routingIds>
        <conf:routingId>${correspondentInformationRoutingId!}</conf:routingId>
       </conf:routingIds>
      </conf:routingIdsAndExplicitDetails>
     </conf:correspondentInformation>
     <conf:beneficiary>
      <conf:routingIds>
       <conf:routingId>${beneficiaryBankParty1RoutingId!}</conf:routingId>
      </conf:routingIds>
     </conf:beneficiary>
     <scb:partyReference href="party1"/>
    </scb:settlementInstruction>
   </scb:cashflowSSI>
  </scb:cashflowPayload>
 </scb:payload>
</scb:SCBML>
```

## Active field mapping

| Field Name in Message Template | XPath | Mandatory | Sample |
| --- | --- | --- | --- |
| `stackFlow` | `/scb:SCBML/scb:header/scb:originationDetails/scb:messageSender/scb:messageSender[@systemScheme='http://www.sc.com/coding-scheme/stack-flow']` | N | `FMRPMUREX` |
| `messageTimestamp` | `/scb:SCBML/scb:header/scb:originationDetails/scb:messageTimestamp` | Y | `2025-10-25T01:50:11.502170181` |
| `trackingId` | `/scb:SCBML/scb:header/scb:originationDetails/scb:trackingId` | Y | `e4629d3f-2b13-45f8-b042-8f4d90eca680` |
| `businessEvent` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:event` | Y | `New/Withdrawal` |
| `nettingId` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:linkId` | Y for netting | `c65e315b-afd2-11f0-8792-005056ac01ca` |
| `cashflowId` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:header/scb:cashflowIdentifier/scb:cashflowId` | Y | `M00202510132` |
| `receiverPartyReference` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:receiverPartyReference` | Y | `Debit` |
| `isoCurrency` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:paymentAmount/conf:currency` | Y | `USD` |
| `paymentAmount` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:paymentAmount/conf:amount` | Y | `1870.00` |
| `unadjustedDate` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:paymentDate/conf:unadjustedDate` | Y | `2025-07-29` |
| `tradeId` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:partyTradeIdentifier/conf:tradeId` | Y | `103991599` |
| `tradeBookingTimestamp` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:partyTradeInformation/conf:executionDateTime` | N | `2025-06-27T14:27:44Z` |
| `sourceSystem` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:partyTradeInformation/scbextn:tradeSource/scbextn:name` | N | `Murex` |
| `productType` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:productType` | Y | `IFXXXX` |
| `allotment` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:productId` | Y | `CURR|FXD|FXD` |
| `portfolioName` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:tradePortfolio/conf:partyPortfolioName/conf:portfolioName[1]` | Y | `FXI_OP_LDN` |
| `tradeWorkflowStatus` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:state` | N | `VALD` |
| `legalEntityId` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id='party1']/conf:partyId[@partyIdScheme='http://www.sc.com/coding-scheme/partyId/LEID']` | N | `11090155` |
| `party1FmId` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id='party1']/conf:partyId[@partyIdScheme='http://www.sc.com/coding-scheme/partyId/FMID']` | Y | `10075222` |
| `dealerPersonId` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id='party1']/conf:person/conf:personId` | N | `1474102` |
| `party2FmId` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id='party2']/conf:partyId[@partyIdScheme='http://www.sc.com/coding-scheme/partyId/FMID']` | Y | `400617196` |
| `party2FmCode` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id='party2']/conf:partyId[@partyIdScheme='http://www.sc.com/coding-scheme/partyId/FMCODE']` | N | `EDELWEISS I S P*SIN` |
| `ssiId` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:SSIId` | N | `47349561` |
| `settlementAccountNo` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction/scb:settlementMeans/scb:settlementAccountNo` | N | `USD MAIN` |
| `beneficiaryBankRoutingId` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction/conf:beneficiaryBank/conf:routingIdsAndExplicitDetails/conf:routingIds/conf:routingId` | N | `SCBLSG22XXX` |
| `beneficiaryRoutingName` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction/conf:beneficiary/conf:routingIdsAndExplicitDetails/conf:routingName` | N | `EDELWEISS INTERNATIONAL SINGAPORE` |
| `beneficiaryRoutingAccountNumber` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction/conf:beneficiary/conf:routingIdsAndExplicitDetails/conf:routingAccountNumber` | N | `0106533495` |
| `correspondentInformationRoutingId` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction/conf:correspondentInformation/conf:routingIdsAndExplicitDetails/conf:routingIds/conf:routingId` | N | `SCBLUS33XXX` |

The source also contains a struck-through historical “Detail Fields Mapping” section. Its paths include amendment fields such as `cancelledCashflowId`, `cancelledIsoCurrency`, `cancelledCashflowVersion`, `cancelledBusinessVersion`, `cancelledCashflowStatus`, `cancelledReceiverPartyReference`, and `cancelledUnadjustedDate`. These mappings should not be treated as the active executable contract without reconciliation.

## Known specification issues

- The China source-system mapping conflicts on `MX` versus `DV`.
- User cases retain the former 16-entity eligibility condition after the stated entity-filter removal.
- The “Vostro Beneficiary BIC” label does not clearly identify which settlement instruction owns `Beneficiary_BIC_code`.
- `SCB_Nostro_Account_Type` is used in the filtering logic but is not visibly serialized in the XML template.
- Several published XPath values contain malformed Markdown links or inconsistent element-versus-attribute syntax.
- The `legalEntityId` mapping is inconsistent in the source between `LEID` and `FMID`.

## Related systems

The integration flow references [[ratan]], RATAN ONE, [[stella]], TDS3, BCS STELLA, RAZOR, LMS, SABRE EQ, LOANIQ, BLADE, S2BX, CFETS, ADO, and Confluence. Existing SSI and Nostro pages provide related settlement context, but LMS delivery eligibility remains a separate concern.