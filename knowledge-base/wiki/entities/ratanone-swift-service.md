---
type: entity
title: ratanone-swift-service
created: 2026-08-23
updated: 2026-08-25
tags: [ratanone, swift, deployment, cash-settlement, ratan, mt210, krw, fmsgw, cashflow-status, business-version, monitoring]
related: [rfi-dedicated-nostro-stamping, rfi-nostro-stamping-based-on-portfolio, mt210-message-generation, swift, ratanone, fmsgw, ratan-fmsgw-settlement-messaging, cashflow-business-version-monotonicity, ratan-accounting-status-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Cashflow Dedicated Nostro Stamping Design(like RFI STRATEGY etc.).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Change List and API.md", "RATAN/RATAN -Monitoring/RATAN ITRS Log.md"]
---

# ratanone-swift-service

## Deployment context

The existing version identifies `ratanone-swift-service` as part of the proposed RFI dedicated-Nostro go-live deployment set.

The existing version's source does not define a direct change to the service's message contract or processing behavior.

## MT210 change

The newly generated version based on the change-list and API source states that `ratanone-swift-service` is responsible for a narrow MT210 change: generating tag 25 when the following condition holds:

```text
ccy=KRW and sendersCorrespondent53Account!=null
```

The requirement does not specify:

- Tag 25 content
- Blank-string behavior
- Whitespace normalization
- Replay or retry handling

See [[mt210-message-generation]].

These MT210 details are stated by the newly generated version and remain separate from the existing version's statement that its source does not define a direct message-contract or processing-behavior change.

## FMSGW acknowledgement and cashflow status handling

The newly generated version based on `RATAN/RATAN -Monitoring/RATAN ITRS Log.md` states that `ratanone-swift-service` processes SWIFT responses from [[fmsgw]] and applies cashflow status updates.

A FMSGW acknowledgement requested business version `0` while RATAN already held version `1`. The service raised:

```text
CashflowUpdateFailedException: Business version downgrade not allowed, existing: [1], request is: [0]
```

The monitoring-log source explains that a withdrawal event had already arrived upstream before the FMSGW acknowledgement. Rejecting the older update preserves business-version monotonicity and was classified as expected state-machine behavior.

See [[cashflow-business-version-monotonicity]].