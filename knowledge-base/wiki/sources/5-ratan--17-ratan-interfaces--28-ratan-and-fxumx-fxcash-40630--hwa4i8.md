---
type: source
title: Ratan and FXU (MX-FXCASH) 40630
authors: [Yunzhe Ta, Junying Jiang, Fengke Wu]
year: 2026
url: "https://confluence.global.standardchartered.com/display/DSP/FXU+Tech+Detail+Design"
venue: "RATAN interface documentation"
tags: [ratan, fxu, mx-fxcash, interface, cashflow, accounting, solace]
related: [fxu, mx-fxcash, ratan, ratanone-message-bridge, solace, ratan-fxu-utilization-integration, what-is-the-authoritative-ratan-fxu-mx-fxcash-40630-interface-contract]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and FXU(MX-FXCASH) 40630.md"]
---

# Ratan and FXU (MX-FXCASH) 40630

## Summary

This interface document describes interface `40630` between `FXU`, using `MX-FXCASH`, and `RATAN`. `FXU` queries cashflow status through a RATAN API and sends a `FullUtilize` utilization request for accounting through `Solace`.

The documented product scope is `SPOT`, `Forward`, and `SWAP`. The source identifies JSON as the message format.

## Interface Data

| Attribute | Value |
| --- | --- |
| Interface identifier | `40630` |
| Upstream application | `FXU` |
| FXU function/interface | `MX-FXCASH` |
| Target application | `RATAN` |
| Intermediate component | `RATANONE` |
| Messaging platform | `Solace` |
| Message format | `JSON` |
| Request type | `FullUtilize` |
| Business purpose | Accounting |
| Products | `SPOT`, `Forward`, `SWAP` |

## Documented Flow

The source records the API interaction as:

```text
API:
MX-FXCASH(FXU) -> Ratan API
```

The utilization request and response flow is recorded as:

```text
FXU -> Solace Topic1 -> Solace Queue1 -> RATANONE
    -> Solace Topic2 -> Solace Queue2 -> FXU
```

`Topic1`, `Queue1`, `Topic2`, and `Queue2` are placeholders in the source and should not be treated as deployable endpoint names.

## Interface Description

- `FXU` calls the RATAN API to query cashflow status.
- `FXU` sends a `FullUtilize` request to RATAN for accounting through `Solace`.
- `RATANONE` appears in the utilization request and response route.
- The interface covers `SPOT`, `Forward`, and `SWAP`.

The source does not establish whether `RATANONE` performs business processing, acts as a message bridge, or performs both roles.

## Evidence Limits

This document is an interface inventory entry rather than a complete technical contract. It does not specify:

- The API HTTP method, endpoint, authentication, request schema, or response schema.
- Cashflow-status values or state transitions.
- Actual Solace topic and queue names.
- `FullUtilize` semantics as a message type, event, operation, or field value.
- Acknowledgement, retry, timeout, duplicate-handling, or dead-letter behavior.
- Product-specific differences across `SPOT`, `Forward`, and `SWAP`.
- Interface ownership, support contacts, or troubleshooting procedures.

The linked `FXU Tech Detail Design` and `FXU Technical Design` documents are required for implementation-level details:

- [FXU Tech Detail Design](https://confluence.global.standardchartered.com/display/DSP/FXU+Tech+Detail+Design)
- [FXU Technical Design - FXU Request/Response](https://confluence.global.standardchartered.com/display/DSP/FXU+Technical+Design#FXUTechnicalDesign-FXURequest/Response)

The referenced OLA is [RATAN - OLA - FM Settlement - IS](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA).

## Review and Publication Status

The document records updates by `@Yunzhe Ta` and `@Junying Jiang` on `2026-01-21`, and review by `@Yunzhe Ta` and `@Fengke Wu` on `2026-01-21`. Its `Status` field is blank, although the document states that status should be updated to `Published` after review. Formal publication therefore remains unconfirmed.

## Related Wiki Context

This page extends the existing [[concepts/ratan-interface-inventory]] and [[concepts/ratan-interface-architecture]] material with the `40630` identifier, the `MX-FXCASH` association, the `FullUtilize` request, and the documented `Solace` route. The role of [[entities/ratanone-message-bridge]] should be verified against [[queries/what-is-the-relationship-between-ratan-and-ratanone]].