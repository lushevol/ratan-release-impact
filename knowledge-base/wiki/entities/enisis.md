---
type: entity
title: ENISIS
created: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Korea Cashflow Migration -Ratan to OLTP Accounting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Ratan One Processing Guide(DOI)-Korea.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Swift - Enisis.md", "RATAN/RATAN -Interfaces/Ratan and ENISIS 50157.md"]
tags: ["swift", "integration", "payment-messaging", "fmrp", "messaging", "korea", "payment-processing", "exception-management", "enisis", "external-system", "cash-settlement", "gateway", "settlement"]
related: ["ratan-swift-message-generation", "swift-status-lifecycle-and-reconciliation", "amh", "oltp-accounting-message-contract", "korea-ratan-oltp-accounting-integration", "ratan", "korea-accounting-and-swift-exception-monitoring", "korea-kro-non-kro-payment-routing", "korea-swift-enisis", "enisis-legacy-connection-retention", "incremental-enisis-flow-extension", "ratanone", "swift-service", "swift", "fm-solace", "ratan-enisis-swift-interface", "korea-fmo-payment-recovery"]
updated: 2026-08-24
---

# ENISIS

ENISIS is described across functional requirements, a Korea RATAN operating guide, a Korea SWIFT and settlement-accounting technical design, and the documented RATAN–ENISIS interface as a SWIFT-related external integration component with distinct roles.

The `RATAN/RATAN -Interfaces/Ratan and ENISIS 50157.md` source identifies ENISIS as the target-side SWIFT gateway in documented Korea PROD, with application identifier `50157-ENISIS`. According to that source:

- [[ratan]] transmits MX messages and MT210 through [[fm-solace]] to ENISIS.
- ENISIS processes those messages and forwards them to the [[swift]] network.
- ENISIS returns separate MX and MT ACK/NACK messages to RATAN through FM Solace.

The other sources describe additional or differently scoped ENISIS roles:

- The FMRP SWIFT-generation requirement identifies ENISIS as an alternative integration path for RATAN-generated MT/MX messages.
- The Korea Cashflow Migration requirement identifies ENISIS as a component in the Korea accounting flow that updates the Solace/JMS `imsTimestamp` to system time for the RATAN–OLTP exchange.
- The Korea Cashflow Migration requirement also identifies ENISIS as the SWIFT-processing destination for specified NOS payment flows. Its responsibilities beyond the timestamp update and named payment-routing references are not defined in that requirement.
- The Korea RATAN operating guide describes ENISIS as a downstream SWIFT-related system.
- The Korea SWIFT and settlement-accounting design identifies Enisis as an external integration target and directs implementation to add Enisis-specific logic to an existing flow while retaining the previous Enisis connection approach.

## RATAN–ENISIS message flow

According to the documented RATAN–ENISIS interface:

1. [[ratan]] sends MX messages and MT210 through [[fm-solace]].
2. ENISIS receives and processes those messages.
3. ENISIS forwards the messages to the [[swift]] network.
4. ENISIS sends separate MX and MT ACK/NACK messages back to RATAN through FM Solace.

The documented receiver queues at RATAN are:

| Message type | Receiver queue |
|---|---|
| MX acknowledgement | `q-51358-ratanone-enisis-mx-status-ack` |
| MT acknowledgement | `q-51358-ratanone-enisis-mt-status-ack` |

The RATAN–ENISIS interface source does not define ACK/NACK payloads, correlation identifiers, timing, retries, or behavior for lost or duplicated acknowledgements.

## FMRP SWIFT-generation status contract

According to the FMRP SWIFT-generation requirement, ENISIS receives generated messages and returns response statuses through `/AMHMessage/Payload/ResponseHeader/Status`.

| Status | Meaning | RATAN status and description |
|---|---|---|
| `2` | ENISIS technical ACK | `RELEASED` with `Pending ENISIS Disp` |
| `0` | Business ACK from SAA/AMH | `SETTLED` with `Released by AMH` |
| `1` | Business NACK from SAA/AMH | `RELEASED` with `AMH Error` |

The same requirement states that the tracking ID is available at `/AMHMessage/Header/UniqueID`.

This status contract is a requirement-level integration definition, not evidence that ENISIS behavior is deployed or operationally verified. It is distinct from the MX and MT acknowledgement queues documented in the RATAN–ENISIS interface source; the available sources do not establish whether these are two representations of the same acknowledgement flow.

## Korea accounting and payment-flow references

The Korea Cashflow Migration requirement states that ENISIS updates the Solace/JMS `imsTimestamp` to system time for the RATAN–OLTP exchange.

The same requirement names ENISIS as the SWIFT-processing destination for specified NOS payment flows. It does not define ENISIS responsibilities beyond the timestamp update and the named payment-routing references.

## Korea operating-guide exception handling

The Korea RATAN operating guide identifies `FinalCancelled` as an ENISIS NACK status.

For affected Korea SWIFT items, the guide states that users may process the item in the exception blotter or replay it in ENISIS. The guide does not define replay eligibility, retry limits, duplicate prevention, or post-replay confirmation behavior.

## Operational support and recovery

The RATAN–ENISIS interface source lists the following operational contacts:

- PSS contact: `ENISIS - SCBK.FX_Support <SCBK.FX_Support@sc.com>`
- PSS Manager: Park, Jung Hyeon

That source also states that Korea FMO may manually draft MX messages in ENISIS when technical recovery or replay cannot resolve a payment.

## Existing-connection and extension constraints

According to the Korea SWIFT and settlement-accounting technical design:

- New Enisis-specific processing logic should follow the existing flow.
- The established Enisis connection method should be retained.
- The source does not identify the protocol, endpoint, authentication model, certificates, network route, client library, or connection owner.

## Scope boundaries

The RATAN–ENISIS interface source describes ENISIS as a target-side SWIFT gateway and states that it forwards messages to the [[swift]] network. Separately, the Korea SWIFT and settlement-accounting technical design does not, by itself, establish whether Enisis is:

- a Swift network component;
- an accounting target;
- a RATANONE-owned service; or
- connected through [[swift-service]] or [[accounting-service]].

These relationships must not be inferred beyond the explicitly documented interface description without additional implementation documentation.

## Open questions

The Korea SWIFT and settlement-accounting technical design tracks the connection contract in [[what-is-the-existing-enisis-connection-contract]] and the required functional extension in [[what-new-enisis-logic-is-required-in-the-existing-flow]].