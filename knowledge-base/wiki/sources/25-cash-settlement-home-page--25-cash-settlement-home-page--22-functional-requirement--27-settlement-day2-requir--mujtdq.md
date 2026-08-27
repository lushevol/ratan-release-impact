---
type: source
title: RFI Nostro Stamping Based on Portfolio — UAT
created: 2026-08-23
updated: 2026-08-23
tags: [uat, ratan, nostro, rfi, portfolio, krw, swift, ebbs]
related: [portfolio-based-nostro-stamping, notice-to-receive-mt210-control, does-portfolio-based-nostro-stamping-apply-to-fixing-spot-forward-irs-and-swap, does-ad-hoc-ssi-override-portfolio-based-nostro-stamping, which-nostro-is-selected-for-non-rfi-receive-cashflows-with-kro-main, nostro-stamping, mt210-message-generation, amendment-driven-cashflow-correlation, receive-only-swift-suppressed-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/RFI Nostro stamping based on Portfolio - UAT.md"]
authors: []
year: 2026
url: ""
venue: UAT test evidence
---
# RFI Nostro Stamping Based on Portfolio — UAT

This UAT document records RATAN validation for portfolio-driven nostro selection in KRW/KRO scenarios. It tests RFI and non-RFI portfolios, pay and receive cashflows, SI mismatch exceptions, `Notice to Receive` behavior, portfolio amendments, manual SSI selection, and `swift_suppression` accounting.

## Findings

- Tests 1–5 passed: RFI portfolio cashflows used the RFI nostro, `KRO OTH 1`; the tested non-RFI pay cashflow used the primary/non-RFI nostro, `KRO MAIN`.
- Tests 3–5 passed: a manually changed vostro settlement means/account may create an SI mismatch exception without preventing the portfolio-driven nostro result or expected SWIFT generation.
- Tests 6 and 6.1 support a configuration dependency: receive-side MT210/tag `:25:` generation is tied to the selected nostro static data's `Notice to Receive` setting.
- Tests 8 and 9 passed: changes across the RFI/non-RFI portfolio boundary are economic amendments, producing withdrawal and replacement cashflows in `WAITING`.
- Test 10 passed: a non-RFI-to-non-RFI portfolio change is not an economic amendment; the resulting events are offset in the group blotter.
- Tests 11 and 12 passed: `swift_suppressed` cashflows retain portfolio-specific EBBS accounting selection.
- Test 7 passed: ad hoc SSI exposes nostro type in list and form views and permits selecting an RFI nostro for a non-RFI portfolio.
- Test 13 remains outstanding: CDU regression testing is required for fixing, spot, forward, IRS, and swap trades that are expected to retain the existing SI-matched nostro process.

The evidence is limited to the tested KRW/KRO configuration. It does not establish a universal portfolio-stamping rule for all products, currencies, or message flows.

## UAT Cases

| Test case | Scenario | Test data | Status |
| --- | --- | --- | --- |
| 1 | RFI portfolio, KR currency, SCB pay; vostro `KRO OTH 1`; RFI nostro `KRO OTH 1`; expected SWIFT generation | `M00135898503` | Pass |
| 2 | RFI portfolio, KR currency, SCB receive; RFI nostro `KRO OTH 1`; expected MT210 with tag `:25:` | `M00135980062` | Pass |
| 3 | RFI portfolio, KR currency, SCB pay; vostro changed to `KRO MAIN`; RFI nostro `KRO OTH 1`; expected SI mismatch and SWIFT | `M00195898503` | Pass |
| 4 | RFI portfolio, KR currency, SCB receive; vostro changed to `KRO MAIN`; RFI nostro `KRO OTH 1`; expected SI mismatch and MT210 tag `:25:` | `M00145980062` | Pass |
| 5 | Non-RFI portfolio, KR currency, SCB pay; vostro `KRO OTH 1`; primary/non-RFI nostro `KRO MAIN`; expected SI mismatch and SWIFT | `M00205898503` | Pass |
| 6 | Non-RFI portfolio, KR currency, SCB receive; `KRO MAIN` static data with `Notice to Receive = N`; tag `:25:` not generated | `M00155980062` | Configuration-dependent outcome |
| 6.1 | Non-RFI portfolio, KR currency, SCB receive; `KRO MAIN` static data with `Notice to Receive = Y`; expected MT210 with tag `:25:` | `M00156980062` | Pass |
| 7 | Ad hoc SSI displays nostro type and permits RFI-nostro selection for a non-RFI portfolio | `M00215898503` | Pass |
| 8 | Non-RFI-to-RFI portfolio change treated as an economic amendment | Trade `208099012`; `M00245898503`; `M00255898503` | Pass |
| 9 | RFI-to-non-RFI portfolio change treated as an economic amendment | Trade `308099012`; `M00265898503`; `M00275898503` | Pass |
| 10 | Non-RFI-to-non-RFI portfolio change not treated as an economic amendment; offset events in group blotter | Trade `508099012`; `M00285898513`; `M00295898513` | Pass |
| 11 | RFI cashflow enters `swift_suppressed`; accounting uses the RFI nostro EBBS account | `M00286898513` | Pass |
| 12 | Non-RFI cashflow enters `swift_suppressed`; accounting uses the non-RFI nostro EBBS account | `M00156980063` | Pass |
| 13 | Fixing, spot, forward, IRS, and swap trades continue to stamp the nostro matched with vostro SI | — | CDU regression test required |

## MT210 Evidence

The outbound message captured for test 4 identifies RATAN as sender, `FMSwiftGateway` as capture system, and MUREX as trade source.

```text
{1:F01SCBLGB2LATSY0000000000}{2:I210SCBLKRSEXXXXN}{4: :20:DV02M00145980062 :25:03910010005 :30:260324 :21:DV02M00145980062 :32B:KRW29900000000, :52A:BOFAKR2XXXX -}
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<scb:SCBML scbmlVersion="4-0" xmlns:scb="http://www.sc.com/SCBML-1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.sc.com/scbml/communication/external-1" xmlns:fpmlrep="http://www.fpml.org/FpML-5/reporting" xsi:schemaLocation="http://www.sc.com/SCBML-1 ../../../core/4-0/scbml-4-0.xsd http://www.sc.com/scbml/communication/external-1 ../../../payloadType/externalCommunicationPayload/4-0/scbml-externalCommunicationPayload-4-0.xsd">
  <scb:header>
    <scb:messageDetails>
      <scb:messageVersion>1.0</scb:messageVersion>
      <scb:messageType>
        <scb:typeName>ExternalCommunication</scb:typeName>
        <scb:subType>
          <scb:subTypeName>SWIFTMessage</scb:subTypeName>
        </scb:subType>
      </scb:messageType>
    </scb:messageDetails>
    <scb:originationDetails>
      <scb:messageSender>
        <scb:messageSender systemScheme="http://www.sc.com/coding-scheme/system">RATAN</scb:messageSender>
        <scb:senderDomain>
          <scb:domainName domainNameScheme="http://www.sc.com/coding-scheme/domain-name">FM</scb:domainName>
          <scb:subDomainName subdomainNameScheme="http://www.sc.com/coding-scheme/subdomain-name">
            <scb:subDomainType>PaymentData</scb:subDomainType>
          </scb:subDomainName>
        </scb:senderDomain>
        <scb:countryCode>ALL</scb:countryCode>
      </scb:messageSender>
      <scb:messageTimestamp>2026-05-06T03:23:49Z</scb:messageTimestamp>
      <scb:initiatedTimestamp>2026-05-06T03:23:49Z</scb:initiatedTimestamp>
      <scb:trackingId>6fb1a6ee-d4d5-46d0-9642-34f57b16761d_MT210</scb:trackingId>
    </scb:originationDetails>
    <scb:captureSystem>FMSwiftGateway</scb:captureSystem>
    <scb:process>
      <scb:processName>ExternalCommunicationNotification</scb:processName>
      <scb:eventType>Report</scb:eventType>
      <scb:workflowState></scb:workflowState>
      <scb:trackingVersion></scb:trackingVersion>
      <scb:tradeId tradeIdScheme="http://www.sc.com/coding-scheme/tradeId">M00145980062</scb:tradeId>
    </scb:process>
  </scb:header>
  <scb:payload>
    <scb:payloadFormat>XML</scb:payloadFormat>
    <scb:payloadVersion>ExternalCommunication-4-0</scb:payloadVersion>
    <externalCommunicationNotification fpmlVersion="5-9">
      <tradeSource tradeSourceScheme="http://www.sc.com/coding-scheme/tradeSource/originalSourceSystem">
        <name>MUREX</name>
      </tradeSource>
      <externalSnapshotReport>
        <communicationDomain>SWIFTGateway</communicationDomain>
        <communicationFormat>MT</communicationFormat>
        <communicationName>SWIFTMessage</communicationName>
        <confirmationOrPaymentReport>
          <confirmationMethod>SWIFT</confirmationMethod>
          <linkId linkIdScheme="http://www.sc.com/coding-scheme/linkId/confirmationDocumentLinkId"></linkId>
          <reportRawData>
            <tradeID>M00145980062</tradeID>
            <tradeVersion></tradeVersion>
            <legIndicator></legIndicator>
          </reportRawData>
          <resources>
            <resourceId resourceIdScheme="http://www.sc.com/coding-scheme/resourceId">Payment</resourceId>
            <resourceType resourceTypeScheme="http://www.sc.com/coding-scheme/resourceType">Embedded</resourceType>
            <message>{1:F01SCBLGB2LATSY0000000000}{2:I210SCBLKRSEXXXXN}{4: :20:DV02M00145980062 :25:03910010005 :30:260324 :21:DV02M00145980062 :32B:KRW29900000000, :52A:BOFAKR2XXXX -}</message>
          </resources>
        </confirmationOrPaymentReport>
      </externalSnapshotReport>
      <party id="Party1">
        <fpmlrep:businessUnit>
          <fpmlrep:businessUnitId>02</fpmlrep:businessUnitId>
          <fpmlrep:country>GB</fpmlrep:country>
        </fpmlrep:businessUnit>
      </party>
    </externalCommunicationNotification>
  </scb:payload>
</scb:SCBML>
```

## Evidence Limitations

Tests 6 and 6.1 describe non-RFI receive cashflows and `KRO MAIN` static data, but their expected-result wording says the cashflow is stamped to the RFI nostro. This conflicts with test 5 and appears to be a copy/paste defect. See [[which-nostro-is-selected-for-non-rfi-receive-cashflows-with-kro-main]].

Test 12 is labelled as a non-RFI scenario and expects non-RFI EBBS accounting, but its test step says “RFI portfolilo.” The scenario and expected result identify the intended interpretation, but the source should be corrected.

The unexecuted test 13 may limit the scope of [[portfolio-based-nostro-stamping]] for standard trade types.