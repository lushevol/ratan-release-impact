---
type: concept
title: FXU Utilization Response Contract
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, utilization, api-contract, ack, nack]
related: [fxu, utilization-service, utilization-dlq-retry-and-failure-semantics]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/Draft Design For Phase2.md"]
---
# FXU Utilization Response Contract

The draft defines an FXU utilization response contract that combines outcome status with request context.

For a parsed utilization request, the response contains:

- `Utilization.Utilization_Id`
- `Utilization.Response`, illustrated as `ACK` or `NACK`
- `Utilization.Error_Reason`
- `Request_Info.Utilization`, which echoes utilization and trade information from the request

The echoed trade context includes trade ID, trade major version, swap-leg ID, exchanged-currency codes, and utilization amounts. This enables response consumers to correlate the outcome with the submitted request without separately recovering request data.

An automatic-utilization response differs from the enriched outcome response: it contains `Utilization_Id`, trade context, utilization amounts, and remaining amounts, but does not show `ACK`, `NACK`, or `Error_Reason`.

The draft uses both JSON strings and JSON numbers for amount fields. It does not define a canonical numeric representation, precision, rounding policy, or the semantic rules for remaining amounts.