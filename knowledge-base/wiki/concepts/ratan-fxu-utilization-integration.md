---
type: concept
title: RATAN-FXU Utilization Integration
tags: [ratan, fxu, mx-fxcash, utilization, accounting, solace, integration]
related: [fxu, mx-fxcash, ratan, ratanone-message-bridge, solace, ratan-interface-architecture, 5-ratan--17-ratan-interfaces--28-ratan-and-fxumx-fxcash-40630--hwa4i8]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and FXU(MX-FXCASH) 40630.md"]
---

# RATAN-FXU Utilization Integration

The RATAN-FXU utilization integration is the documented interaction in interface `40630` through which `FXU`, using `MX-FXCASH`, queries cashflow status from RATAN and sends a `FullUtilize` accounting request through `Solace`.

## Two Interaction Patterns

### Cashflow-status API query

`FXU` calls a RATAN API to query cashflow status. The source confirms the participating systems but does not provide enough information to treat the interaction as an authoritative API contract.

### Utilization request and response

The source documents the following route:

```text
FXU -> Solace Topic1 -> Solace Queue1 -> RATANONE
    -> Solace Topic2 -> Solace Queue2 -> FXU
```

This indicates a request path from `FXU` through `Solace` to `RATANONE`, followed by a response path through a second `Solace` topic and queue back to `FXU`. The names are placeholders, and the source does not establish whether `RATANONE` is a business-processing service, a message bridge, or both.

## Business Scope

The interface is associated with:

- `FullUtilize` as the named utilization request.
- Accounting as the request purpose.
- `SPOT`, `Forward`, and `SWAP` as supported product categories.
- `JSON` as the message format.

No product-specific message or accounting differences are documented.

## Unresolved Contract Details

The following require confirmation from the FXU technical design:

- Whether the API query and Solace utilization flow are both part of interface `40630`.
- The actual API endpoint, method, schemas, authentication, and error handling.
- Whether `FullUtilize` is a message type, business event, API operation, or field value.
- Actual topic and queue names.
- Ownership of processing, persistence, acknowledgement, retries, duplicates, timeouts, and dead-letter handling.
- The precise role of `RATANONE`.