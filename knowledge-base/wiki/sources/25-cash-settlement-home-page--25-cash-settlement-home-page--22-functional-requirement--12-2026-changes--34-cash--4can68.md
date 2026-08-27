---
type: source
title: RATAN to ENISIS
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, korea-migration, ratan, enisis, fm-solace, swift]
related: [ratan, enisis, mxg-kr, fm-solace, korea-migration, ratan-enisis-fm-solace-integration, korea-settlement-message-eligibility, is-technical-ack-firstsentok-terminal-for-ratan-enisis-korea-messages, what-is-the-final-ratan-enisis-fm-solace-header-contract, what-is-the-korea-ratan-enisis-nak-retry-and-exception-handling-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/RATAN to ENISIS.md"]
---
# RATAN to ENISIS

## Purpose

This functional requirement describes the intended Korea cash-settlement integration route from [[ratan]] to [[enisis]]. It is a design requirement for the [[korea-migration]] initiative, not evidence of deployment, end-to-end testing, or production readiness.

The current route is described as:

`MXG KR → RATAN → MX transformation → ENISIS via SFTP`

The target route requires RATAN to receive payment-initiation messages from [[mxg-kr]] and send qualifying MT and MX payment messages to ENISIS through [[fm-solace]]. MT scope is explicitly limited to MT210. The source does not define the target inbound payment-initiation contract or definitive ownership of MT/MX transformation.

## Outbound Eligibility

The Korea-route selection condition is:

```text
Cashflow Status in (RELEASED, SETTLED) and Settlement Mean='NOS'
```

The source attributes this condition to existing SWIFT logic. It is documented as Korea-migration-specific evidence in [[korea-settlement-message-eligibility]] and must not be generalized to other RATAN routes without confirmation.

## Message Scope

- MT messages sent to ENISIS are limited to **MT210**.
- The MX example uses ISO 20022 `pacs.009.001.08`, `swift.finplus`, and `swift.cbprplus.03`.
- The sample MX identifies `54949-FMSGW-MX` as `ApplicationID` and contains the topic `v1/settlement/51358-ratanone/fmsgw/-/scbml-4.0/cash/swift/mx`.
- `pacs.009.001.08` is an example message definition; this source does not establish it as the exclusive MX contract.

### Sample MT Message

```text
{1:F01SCBLGB2LATSY0000000000}{2:I210SCBLGB2LXTSYN}{4:
:20:DV02278728504469
:30:260403
:21:DV02278728504469
:32B:GBP1,
:52D:TMG MJ CEB DUCB NCCFMU
22E GIXYVXEV COXEISESV IHBSE SHA
CHINA
-}
```

### Sample MX Message

```xml
<?xml version="1.0"?>
<AMHMessage>
  <Header>
    <Direction>I</Direction>
    <UniqueID>DV02M01774601589</UniqueID>
    <TrafficType>REQ</TrafficType>
    <Country>GB</Country>
    <MsgType>pacs.009.001.08</MsgType>
    <Service>swift.finplus</Service>
    <Sender>ou=tsy,o=scblgb2l,o=swift</Sender>
    <Receiver>ou=tsy,o=scblgb2l,o=swift</Receiver>
    <ApplicationID>54949-FMSGW-MX</ApplicationID>
    <DataOwner>GBFMKT</DataOwner>
    <JMStopic>v1/settlement/51358-ratanone/fmsgw/-/scbml-4.0/cash/swift/mx</JMStopic>
    <RequestSubType>swift.cbprplus.03</RequestSubType>
  </Header>
  <Payload>
    <RequestOption>
      <NetworkPriority>Normal</NetworkPriority>
    </RequestOption>
    <RequestHeader>
      <Requestor>ou=tsy,o=scblgb2l,o=swift</Requestor>
      <Responder>ou=tsy,o=scblgb2l,o=swift</Responder>
      <Service>swift.finplus</Service>
      <RequestType>pacs.009.001.08</RequestType>
      <RequestRef>DV02M01774601589</RequestRef>
    </RequestHeader>
    <RequestPayload>
      <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02">
        <Fr>
          <FIId>
            <FinInstnId>
              <BICFI>SCBLGB2LTSY</BICFI>
            </FinInstnId>
          </FIId>
        </Fr>
        <To>
          <FIId>
            <FinInstnId>
              <BICFI>SCBLGB2LTSY</BICFI>
            </FinInstnId>
          </FIId>
        </To>
        <BizMsgIdr>DV02M01774601589</BizMsgIdr>
        <MsgDefIdr>pacs.009.001.08</MsgDefIdr>
        <BizSvc>swift.cbprplus.03</BizSvc>
        <CreDt>2026-03-27T08:53:23+00:00</CreDt>
      </AppHdr>
      <Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.009.001.08">
        <FICdtTrf>
          <GrpHdr>
            <MsgId>DV02M01774601589</MsgId>
            <CreDtTm>2026-03-27T08:53:23+00:00</CreDtTm>
            <NbOfTxs>1</NbOfTxs>
            <SttlmInf>
              <SttlmMtd>INDA</SttlmMtd>
              <SttlmAcct>
                <Id>
                  <IBAN>GB26SCBL60910491997874</IBAN>
                </Id>
              </SttlmAcct>
            </SttlmInf>
          </GrpHdr>
          <CdtTrfTxInf>
            <PmtId>
              <InstrId>DV02M01774601589</InstrId>
              <EndToEndId>DV02M01774601589</EndToEndId>
              <UETR>565f9648-4e58-41ee-8ad1-8f65414474cc</UETR>
            </PmtId>
            <IntrBkSttlmAmt Ccy="GBP">100</IntrBkSttlmAmt>
            <IntrBkSttlmDt>2026-03-27</IntrBkSttlmDt>
            <InstgAgt>
              <FinInstnId>
                <BICFI>SCBLGB2LTSY</BICFI>
              </FinInstnId>
            </InstgAgt>
            <InstdAgt>
              <FinInstnId>
                <BICFI>SCBLGB2LTSY</BICFI>
              </FinInstnId>
            </InstdAgt>
            <Dbtr>
              <FinInstnId>
                <BICFI>SCBLGB2LTSY</BICFI>
                <LEI>RILFO74KP1CM8P6PCT96</LEI>
              </FinInstnId>
            </Dbtr>
            <CdtrAgt>
              <FinInstnId>
                <BICFI>NBOKKWKWXXX</BICFI>
                <ClrSysMmbId>
                  <ClrSysId>
                    <Cd>GBDSC</Cd>
                  </ClrSysId>
                  <MmbId>AUTOTEST</MmbId>
                </ClrSysMmbId>
                <LEI>549300NB7FE83IH6BW96</LEI>
              </FinInstnId>
            </CdtrAgt>
            <Cdtr>
              <FinInstnId>
                <BICFI>SCBLGB2LTSY</BICFI>
                <LEI>RILFO74KP1CM8P6PCT96</LEI>
              </FinInstnId>
            </Cdtr>
            <CdtrAcct>
              <Id>
                <IBAN>KW43NBOK0000000000002023872477</IBAN>
              </Id>
            </CdtrAcct>
            <InstrForNxtAgt>
              <InstrInf>/FIN53/SCBLGB2LTSY</InstrInf>
            </InstrForNxtAgt>
            <Purp>
              <Cd>FREX</Cd>
            </Purp>
            <RmtInf>
              <Ustrd>/BNF/DERIVATIVES SETTLEMENTS</Ustrd>
            </RmtInf>
          </CdtTrfTxInf>
        </FICdtTrf>
      </Document>
    </RequestPayload>
  </Payload>
</AMHMessage>
```

The identifiers, BICs, IBANs, LEIs, dates, amounts, and topic values in the samples demonstrate message format only. This source does not designate them as production configuration.

## Acknowledgement Contract

RATAN consumes `UniqueID`, `Status`, `StatusText`, `StatusDate`, and `StatusMessage`. It does not consume `StatusSource`, optional `ResponsePayload/StatusAttributes`, or optional `XTSResponsePayload`.

| Field | M/O | Source | Values | Remarks | Used in Ratan | Comment From ENISIS |
| --- | --- | --- | --- | --- | --- | --- |
| /AMHMessage/Header/UniqueID | M | Ratan JMS Header | same with JMS Header | Tracking ID | Y | |
| /AMHMessage/Payload/ResponseHeader/Status | M | AMH Status | 0 = ACK, 1 = NAK, 2 = Technical Ack | | Y | Once ENISIS send the Technical Ack, Status will be presented '2'. |
| /AMHMessage/Payload/ResponseHeader/StatusText | M | AMH Status Text | FinalSentOK | FinalCancelled | FirstSentOK | | Y | Ack = FinalSentOK; Nak = FinalCancelled; Technical Ack = FirstSentOK |
| /AMHMessage/Payload/ResponseHeader/StatusDate | M | AMH Timestamp | 2021-01-07T15:35:51.443Z | | Y | |
| /AMHMessage/Payload/ResponseHeader/StatusSource | M | AMH Node Identifier | PN1 | | N | |
| /AMHMessage/Payload/ResponseHeader/StatusMessage | M | AMH Status Description | ACK received; T28027; postal-address validation text | | Y | Ack, Technical Ack = ACK received; Nak -MT=T28027 *(Finerrorcode); Nak -MX=Nak Text |
| /AMHMessage/Payload/ResponsePayload/StatusAttributes | C | As per SWIFTNet SwGbl StatusAttributes schema | `<StatusAttributes> <Severity>Fatal</Severity> <Code>Sw.Stds.D00001</Code> <Parameter>Level=1</Parameter> <Parameter>seev.047.001.01-ShareholdersIdentificationDisclosureResponseV01/ RequestPayload/BusAppHeader/head:BusinessApplicationHeaderV02_doc/ Fr/FIId/FinInstnId/BICFI</Parameter> <Text>Invalid BIC</Text> </StatusAttributes>` | Repeats for multiple SWIFTNet NAK errors | N | |
| /AMHMessage/Payload/XTSResponsePayload/ | C | For XtremeSec response | `<XTSResponsePayload> <versionTag>002</versionTag> <businessUnit>ROOT</businessUnit> <messageId>2345687</messageId> <status>001</status> <decision>UAM HIT</decision> <requestType>O</requestType> <comments>XYZ</comments> <owner> XYZ </owner> <checksum> XYZ </checksum> <systemIdentifier> XYZ </systemIdentifier> </XTSResponsePayload>` | Refer to "Sample XtremeSec Response" | N | |

The terminality of `Status=2` with `StatusText=FirstSentOK` is not defined. It must not be treated as final business success without resolution of [[is-technical-ack-firstsentok-terminal-for-ratan-enisis-korea-messages]].

## Header Contract

| | Field | Ratan MX/MT | Expected Response | Enisis logic | Comment |
| --- | --- | --- | --- | --- | --- |
| 1 | X-Outbound-Property-mxDocID | bf32797f-80d7-4f73-8173-b34644767dd9_MT103 | bf32797f-80d7-4f73-8173-b34644767dd9_MT103 | Same with Request | Can be used by ENISIS |
| 2 | X-Outbound-Property-messageType | Settlement | Settlement | Same with Request | Can be used by ENISIS |
| 3 | X-Outbound-Property-trackingId | bf32797f-80d7-4f73-8173-b34644767dd9_MT103 | bf32797f-80d7-4f73-8173-b34644767dd9_MT103 | Same with Request | Can be used by ENISIS |
| 4 | X-Outbound-Property-sender | RATAN | ENISIS | Can be empty | Can be used by ENISIS |
| 5 | X-Outbound-Property-targetSystem | ENISIS | RATAN | Can be empty | Can be used by ENISIS |
| 6 | X-Outbound-Property-OPICSBranch | 45 | 45 | Can be empty | Can be used by ENISIS |
| 7 | X-Outbound-Property-bookingSystem | RATAN | RATAN | Can be empty | Can be used by ENISIS |
| 8 | imsCorrelationId | M00AER010001 | M00AER010001 | Same with Request | Used by IMS |
| 9 | imsEvent | SENT | RECEIVED | Hardcode | Used by IMS |
| 10 | imsTimestamp | 1775113029668 | 1775113090000 | To be Updated by ENISIS as system time | Used by IMS |
| 11 | imsTraceId | 88e7b18e-6521-42c6-bd18-65929c7e6ba6 | 88e7b18e-6521-42c6-bd18-65929c7e6ba6 | Same with Request | Used by IMS |
| 12 | imsPreviousCorrelationId | M00AER010001 | M00AER010001 | Same with Request | Used by IMS |
| 13 | imsSpans | RATAN | RATAN,ENISIS | Hardcode | Used by IMS |
| 14 | trackingId | bf32797f-80d7-4f73-8173-b34644767dd9_MT103 | bf32797f-80d7-4f73-8173-b34644767dd9_MT103 | Not applicable for Ratan To be aligned between OLTP/KR EDMi/FM SOLACE | Mandatory for SOLACE |
| 15 | sender | RATAN | ENISIS | Not applicable for Ratan To be aligned between OLTP/KR EDMi/FM SOLACE | Mandatory for SOLACE |
| 16 | domainName | FM | FM | Not applicable for Ratan To be aligned between OLTP/KR EDMi/FM SOLACE | Mandatory for SOLACE |
| 17 | initiatedTimestamp | 1775113029668 | 1775113029668 | Not applicable for Ratan To be aligned between OLTP/KR EDMi/FM SOLACE | Mandatory for SOLACE |
| 18 | countryCode | KR | KR | Not applicable for Ratan To be aligned between OLTP/KR EDMi/FM SOLACE | Mandatory for SOLACE |

[[ratan-enisis-fm-solace-integration]] records the propagation and observability intent. The final mandatory-versus-optional header contract remains open because some fields are marked both “Can be empty” or “Not applicable for Ratan” and “Mandatory for SOLACE.”

## Stated Delivery Tasks

1. Compare RATAN MT messages with MT messages generated by [[murex]] KR.
2. Build a connection between RATAN and ENISIS through FM Solace.
3. Confirm request-message and ACK/NAK formats.
4. Define exception-scenario processing.

No timeout, retry, idempotency, duplicate-delivery, dead-letter, remediation-ownership, or settlement-status-update model is specified. See [[what-is-the-korea-ratan-enisis-nak-retry-and-exception-handling-model]].