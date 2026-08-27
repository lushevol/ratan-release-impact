---
type: source
title: Ratan and ENISIS 50157
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, enisis, swift, korea, interface, fm-solace]
related: [ratan, enisis, murex-kr, fm-solace, ratan-enisis-swift-interface, korea-fmo-payment-recovery, what-is-the-authoritative-ratan-enisis-interface-contract, how-is-mt210-handled-between-ratan-and-enisis]
sources: ["RATAN/RATAN -Interfaces/Ratan and ENISIS 50157.md"]
authors: [Yunzhe Ta, Zhenzhen Liu, Daiqi Wang]
year: 2026
url: ""
venue: Internal interface documentation
---
# Ratan and ENISIS 50157

This source describes the Korea PROD integration in which [[murex-kr]] sends MxML through MQ to [[ratan]]. RATAN generates SWIFT MT messages, converts them to MX except for MT210, and transmits the converted MX messages and MT210 through [[fm-solace]] to [[enisis]]. ENISIS then processes the messages and forwards them to [[swift]].

The source records reviewed and updated dates of 2026-01-28, but its status field is blank despite stating that reviewed documents should be marked Published.

## End-to-end flow

```text
Murex KR → MQ → RATAN → FM Solace → ENISIS → SWIFT network
```

RATAN receives acknowledgement or rejection messages through the reverse path:

```text
ENISIS → FM Solace → RATAN
```

The documented acknowledgement channels are distinct for MX and MT.

## Korea PROD connection details

| Source | Target | Data type | Data format | Environment | Host/IP address | Sender Topic | Receiver Queue | Max Bind Count | Max-spool-usage (MB) | Reject-msg-to-sender-on-discard | Expected number of messages – Average / day | Expected number of messages – Peak / day | Largest Message Size | Average Message Size |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: | ---: | --- | --- |
| 51358-RATAN | 50157-ENISIS | MX-Swift | SCBML | PROD |  | `v1/settlement/51358-ratanone/ratanone/-/scbml-4.0/swift/mx/pub` |  | 6 | 300 | Y | 100 | 2000 | 15K | 10K |
| 50157-ENISIS | 51358-RATAN | MX-ACK/NACK | SCBML | PROD |  | `v1/settlement/50157-enisis/enisis/-/scbml-4.0/swift/mx/pub/ack` | `q-51358-ratanone-enisis-mx-status-ack` | 6 | 300 | Y | 100 | 2000 | 15K | 5K |
| 51358-RATAN | 50157-ENISIS | MT-Swift | JSON | PROD |  | `v1/settlement/51358-ratanone/ratanone/-/scbml-4.0/swift/mt/pub` |  | 6 | 300 | Y | 100 | 2000 | 15K | 10K |
| 50157-ENISIS | 51358-RATAN | MT-ACK/NACK | JSON | PROD |  | `v1/settlement/50157-enisis/enisis/-/scbml-4.0/swift/mt/pub/ack` | `q-51358-ratanone-enisis-mt-status-ack` | 6 | 300 | Y | 100 | 2000 | 15K | 5K |

The source leaves Host/IP address blank for every channel. The two outbound publication rows also have no receiver queue specified; it does not state whether topic subscriptions are intentionally used instead.

## Processing and recovery

Korea FMO monitors RATAN MX exceptions, replays messages after remediating static-data or temporary-service causes, and reconciles SSDR payment reports against ENISIS message extractions. If automated processing or replay cannot resolve a payment, operators manually draft an MX message in ENISIS or draft the payment in OSCAR.

For invalid Murex data, the source says RATAN does not return an ACK to Murex and Murex sends an exception email to Korea FMO. The Murex-to-RATAN acknowledgement contract itself is not specified.

## Contact and OLA reference

The ENISIS PSS contact is `ENISIS - SCBK.FX_Support <SCBK.FX_Support@sc.com>`. The listed PSS Manager is Park, Jung Hyeon (`JungHyeon.Park@sc.com`).

The source references the [RATAN OLA](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA), but does not reproduce service levels, ownership detail, or support commitments.

## Limitations

The document provides connection metadata but not payload schemas, message examples, validation rules, acknowledgement payload definitions, correlation identifiers, timeout rules, retry policy, or replay semantics. Its assertion that transmission is secure is not accompanied by security-control details.