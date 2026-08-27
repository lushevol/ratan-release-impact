---
type: entity
title: FM-EDMi
created: 2026-08-24
updated: 2026-08-24
tags: [fm-edmi, messaging, jms-json, ratan, cdups]
related: [ratan, cdups, ratanone-message-bridge, ratan-interface-architecture, ratan-cdups-econaffirm-acknowledgement]
sources: ["RATAN/RATAN -Interfaces/Ratan and CDUPS 51512.md"]
---
# FM-EDMi

FM-EDMi is the formal messaging integration layer named by the source for RATANONE-CDUPS JMS-JSON exchanges.

## Defined flows

RATANONE publishes `EconAffirm` information to CDUPS:

```text
v1/post-trade/51358-ratanone/cdups/json-1.0/ecoaffirm/pub
```

CDUPS returns an ACK message to RATANONE through the following queue and publication identifier:

```text
q-51358-cdups-ratanone-ack
[CDU PS] v1/post-trade/51512-cdups/ratanone/json-1.0/ack/pub
```

The source separately describes the end-to-end transport as Solace. It does not establish how Solace relates to FM-EDMi, so the two names should not be assumed to be interchangeable without confirmation.
