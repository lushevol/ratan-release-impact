---
type: concept
title: Murex COMP Confirmation Exception Resolution
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, comp, cashflow-exception, cashflow-stp, scbml, ratan]
related: [murex-211, ratan, tds3, trade-confirmation-driven-cashflow-stp, murex-ratan-cashflow-message-contract, what-is-the-murex-comp-status-and-idempotent-exception-closure-policy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Confirmation & Cashflow STP.md"]
---
# Murex COMP Confirmation Exception Resolution

Murex `COMP` confirmation exception resolution is the specified Ratan rule for resolving a Murex-derived cashflow's `Pending Confirmation/Affirmation` exception.

## Required Processing Rule

1. Extract `Source_System_Trade_Internal_Id` from a Murex trade SCBML message.
2. Match that value to cashflow `Trade_Id`.
3. When `Source_System_Validation_Status` is `COMP`, identify matching cashflows with `Pending Confirmation/Affirmation`.
4. Close that exception.
5. Move the cashflow to STP only when the closed exception was its only exception.

The STP condition is explicit and limited. This requirement does not authorize STP promotion when another cashflow exception remains.

## Trade-SCBML Extraction Paths

```text
Source_System_Trade_Internal_Id
(/scb:SCBML/scb:payload/scb:FPMLPayload/conf:trade|/scb:SCBML/scb:payload/scb:FPMLPayload/((*/(*:originalTrade|*:trade))|((*:novation|*:cancelReissue)/*:newTrade)))/conf:tradeHeader/conf:partyTradeIdentifier[conf:partyReference/@href="party1"]/conf:tradeId[@tradeIdScheme=http://www.sc.com/coding-scheme/tradeId/Murex/tradeInternalId]

Source_System_Validation_Status
/scb:SCBML/scb:payload/scb:FPMLPayload/scb:header/scb:process/scb:subState[@stateScheme=http://www.sc.com/coding-scheme/state/Murex]
```

## Unspecified Controls

The source does not define the meaning of `COMP`, event ordering, duplicate suppression, replay idempotency, status regression, matching cardinality, or recovery behavior. These controls are tracked in [[what-is-the-murex-comp-status-and-idempotent-exception-closure-policy]].