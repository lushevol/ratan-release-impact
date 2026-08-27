---
type: concept
title: Murex–RATAN Cashflow Message Contract
created: 2026-08-24
updated: 2026-08-24
tags: [Murex-2-11, RATAN, FMRP, XML, IBM-MQ, message-contract]
related: [fmrp, fmrp-cashflow-publication-lifecycle, ratan-10123]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change.md"]
---
# Murex–RATAN Cashflow Message Contract

The FMRP integration uses `MxPayML` for outbound messages and `MxPayMLResponse` for inbound RATAN responses.

## Inbound acceptance contract

`FmrpInboundRouter` accepts a response only when:

- `sourceSystem` is `RATAN`.
- `objectNature` is `cashflow`.
- `MXG2000/flowID` is greater than zero.
- `message` is exactly `RATAN Acknowledged` or `RATAN Released`.

All other responses are discarded.

## Per-flow fan-out

A response can contain multiple `MXG2000/flowID` elements. `FlowEntrySpliter` creates one output marker per `flowID/@id`; the transformation then retains the matching flow element. This ensures that acknowledgement and release processing operate on one Murex flow at a time.

## Acknowledgement and release

Acknowledgements use `sourceID` as the RATAN identifier and persist it in `M_RATAN_ID`. Releases treat a `sourceID` beginning with `N` as the RATAN network identifier and persist it in `M_RATAN_NET_ID`; other values become `0`.

The release response is enriched with:

```xml
<sourceSystem>MX2.11</sourceSystem>
<message>MX2.11 Acknowledged</message>
<event>Released</event>
```

The source does not define the receiving system’s expected semantics for this rewritten event.

## Transport

The documented inbound queue is `GMPCI.MLS.MXG.RQSTIN`, and the outbound queue is `GM.MXG.MLS.FEDS.UAT`. The outbound queue name indicates UAT configuration. The source does not specify production security or resilience settings.