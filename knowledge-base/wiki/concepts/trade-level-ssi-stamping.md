---
type: concept
title: Trade-Level SSI Stamping
created: 2026-08-24
updated: 2026-08-24
tags: [SSI-stamping, trade, cashflow, RATANONE, UBER]
related: [product-agnostic-ssi-stamping, trade-ssi-stamping-idempotency-and-versioning, ssi-stamping-reference-data, cashflow, nstp-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design.md"]
---
# Trade-Level SSI Stamping

Trade-level SSI stamping is the proposed practice of deriving SSI results from an inbound UBER trade, persisting those results against the trade, and reusing them for the cashflows produced by that trade.

## Intended behavior

1. Decode the UBER message into the RATAN Logic Model.
2. Extract and normalize settlement-relevant attributes.
3. Invoke the SSI stamping service once for the trade where possible.
4. Persist the result for the trade identity and version.
5. Match the stored result to each related cashflow.
6. Fall back to cashflow-level stamping or NSTP exception handling when no safe result is available.

The design seeks to reduce repeated stamping while keeping SSI information in the RATAN cashflow model for downstream processing and SCBML generation.

## Required correctness contract

Reuse must not rely on currency alone. The canonical matching key must define currency, debit/credit or pay/receive direction, product or settlement type, party and account role, legal entity, settlement method, and any other attribute that can change the applicable SSI.

The source proposes `tradeId + majorVersion` as the persistence identity, but this remains unresolved. See [[concepts/trade-ssi-stamping-idempotency-and-versioning]].

## Limitations

The proposal does not quantify stamping reduction, matching accuracy, latency, exception rates, or refresh cost. It also does not specify the behavior when a trade result is partial, stale, duplicated, or received after cashflow enrichment.