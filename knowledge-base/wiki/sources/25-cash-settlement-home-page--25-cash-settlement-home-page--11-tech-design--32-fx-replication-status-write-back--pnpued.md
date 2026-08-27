---
type: source
title: FX Replication Status Write Back
authors: []
year: 2023
url: ""
venue: ""
tags: [cash-settlement, fx, razor, scbml, cashflow-status]
related: [razor, scbml, fx-cashflow-status-write-back, cashflow-status-change-event-contract, which-service-consumes-and-persists-razor-cashflow-status-change-events, how-are-razor-cashflow-status-change-events-deduplicated-ordered-and-applied]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FX Replication Status Write Back.md"]
---
# FX Replication Status Write Back

## Summary

This source consists solely of a sample SCBML XML message, despite being labelled “Sample Json.” The XML declares a `CashflowStatusChange` message sent by [[razor]] from the `FM` domain. It provides one example of a Razor-identified cashflow with state `Settled`.

The artifact establishes payload shape and sample values only. It does not identify a destination service, transport mechanism, persistence target, state-transition policy, or operational handling for this write-back.

## Observed Contract

| Field | Observed value |
|---|---|
| Message type | `CashflowStatusChange` |
| Message version | `1.0` |
| Sender | `Razor` |
| Sender domain | `FM` |
| Country code | `ALL` |
| Initiated timestamp | `2023-11-02T10:27:28Z` |
| Tracking ID | `MX_FXCASH_373670953_330134747_1698892048219` |
| Process event type | `Insert` |
| Payload format | `XML` |
| Payload type/version | `cashflowPayload` / `4-0` |
| Cashflow ID | `373670953` |
| Linked trade ID | `330134747` |
| Version-like ID | `1` |
| Workflow state | `Settled` |
| Payment reversal | `false` |
| Payment date | `20230707` |
| Settled cash currency | `CNH` |

## Source Artifact

```xml
<?xml version="1.0" encoding="UTF-8"?>
<scb:SCBML xmlns:scb="[http://www.sc.com/SCBML-1](http://www.sc.com/SCBML-1)"
    xmlns:xsi="[http://www.w3.org/2001/XMLSchema-instance](http://www.w3.org/2001/XMLSchema-instance)" scbmlVersion="4-0" xsi:schemaLocation="[http://www.sc.com/SCBML-1](http://www.sc.com/SCBML-1) ../../../../../core/4-0/scbml-4-0.xsd [http://www.sc.com/SCBML-1](http://www.sc.com/SCBML-1) ../../../../../payloadType/cashflowPayload/4-0/scbml-cashFlow-4-0.xsd">
    <scb:header>
        <scb:messageDetails>
            <scb:messageVersion>1.0</scb:messageVersion>
            <scb:messageType>
                <scb:typeName>CashflowStatusChange</scb:typeName>
            </scb:messageType>
        </scb:messageDetails>
        <scb:originationDetails>
            <scb:messageSender>
                <scb:messageSender systemScheme="http://www.sc.com/coding-scheme/system-1-0">Razor</scb:messageSender>
                <scb:senderDomain>
                    <scb:domainName domainNameScheme="http://www.sc.com/coding-scheme/domainNamescheme-1-0">FM</scb:domainName>
                </scb:senderDomain>
                <scb:countryCode>ALL</scb:countryCode>
            </scb:messageSender>
            <scb:initiatedTimestamp>2023-11-02T10:27:28Z</scb:initiatedTimestamp>
            <scb:trackingId>MX_FXCASH_373670953_330134747_1698892048219</scb:trackingId>
            <scb:uniqueIdentifierMessageId/>
        </scb:originationDetails>
        <scb:captureSystem/>
        <scb:process>
            <scb:eventType>Insert</scb:eventType>
        </scb:process>
    </scb:header>
    <scb:payload>
        <scb:payloadFormat>XML</scb:payloadFormat>
        <scb:payloadType>cashflowPayload</scb:payloadType>
        <scb:payloadVersion>4-0</scb:payloadVersion>
        <scb:cashflowPayload>
            <scb:cashflowStatus>
                <scb:cashflowIdentifier>
                    <scb:cashflowId cashflowIdScheme="http://www.sc.com/coding-scheme/cashflowId/Razor">373670953</scb:cashflowId>
                </scb:cashflowIdentifier>
                <scb:isPaymentReversal>false</scb:isPaymentReversal>
                <scb:linkId linkIdScheme="http://www.sc.com/coding-scheme/tradeId/Razor">330134747</scb:linkId>
                <scb:id IdScheme="http://www.sc.com/coding-scheme/tradeId/Razor/version">1</scb:id>
                <scb:state stateScheme="http://www.sc.com/coding-scheme/state/workflowStatus">Settled</scb:state>
                <scb:paymentDate>20230707</scb:paymentDate>
            </scb:cashflowStatus>
            <scb:cashbalance>
                <scb:cashbalanceInfo>
                    <scb:settledCashCurrency>CNH</scb:settledCashCurrency>
                </scb:cashbalanceInfo>
            </scb:cashbalance>
        </scb:cashflowPayload>
    </scb:payload>
</scb:SCBML>
```

## Limits and Open Design Items

The source does not establish:

- the recipient service, topic, queue, or endpoint;
- whether `Insert` directs event persistence, status-history insertion, or current-state mutation;
- the authoritative identity key among `cashflowId`, `linkId`, `trackingId`, and `id`;
- duplicate, replay, ordering, and stale-version behavior;
- valid workflow states or transition rules;
- error handling, retries, reconciliation, entitlement, or observability controls.

The `cashflowPayload` example is relevant to [[scbml-event-payload-storage-impact]], but this source does not demonstrate any SCBML storage implementation. Its scalar Razor version field also does not establish equivalence with [[cashflow-version-tuple-comparison]].