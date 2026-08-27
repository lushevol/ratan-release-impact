---
type: source
title: FX Utilization Process Data Integration for Blade Controls and Visibility
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [fx-utilization, blade, ratan, tds3, stella, functional-requirement, architecture]
related: [blade, ratan, tds3, stella, fxu, fx-utilization-data-for-blade-controls, blade-fx-utilization-data-access-options, should-blade-source-fx-utilization-directly-from-ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/FX Utilization Process  Data Integration for Blade Controls & Visibility.md"]
---
# FX Utilization Process Data Integration for Blade Controls and Visibility

## Document context

This is a version 1.0 functional-requirement and architectural-options analysis. The document does not specify an author, status, decision owner, or approved architectural decision.

Its subject is how [[entities/blade]] should access FX utilization data mastered by [[entities/ratan]]. The data includes remaining unutilized amounts and detailed cashflow utilization statuses.

## Business requirement

Blade requires utilization data to:

- Display accurate unutilized amounts at trade level.
- Apply hard blocks and controls to `UTIL` trades using current utilization status.
- Validate amendments and withdrawals against the remaining utilizable amount.

The requirement is therefore both informational and transactional. A presentation-only integration does not satisfy the full requirement.

## FX utilization process

Non-FM clients book FX deals in FM systems while settlement is managed by non-FM systems such as SCPAY and TradeXpress. A client may utilize a forward FX deal fully or partially:

- On the value date.
- Before the maturity date through early utilization.
- After the value date through Past Due processing.

Utilized deals are settled in the FX Branch Suspense Account. Unutilized deals are settled in the Past Due Account and remain available for a country-specific period of approximately 3–7 days after the value date. After that period, remaining unutilized deals are reversed and rate-difference costs may be charged to the client.

Multiple FX deals may be consolidated into a single net payment.

## Current architecture and data gap

Blade primarily sources trade data from [[entities/tds3]]. RATAN updates TDS3 with cashflow settlement statuses.

The identified gap is that granular FX utilization data is not currently propagated from RATAN to TDS3 through [[entities/stella]]. The missing data includes per-cashflow remaining amounts and specific utilization statuses required for Blade controls.

This is a granularity and propagation gap rather than a complete absence of settlement information.

## Architectural options

| Option | Description | Advantages | Risks and disadvantages |
|---|---|---|---|
| Option 1: RATAN → TDS3 enhancement | RATAN sends detailed FX utilization updates to TDS3 through STELLA. Blade continues to source trade and utilization data exclusively from TDS3. RATAN remains the golden source, while TDS3 becomes an authoritative replicated source for consumers such as Blade. | Preserves Blade’s single integration point; provides a consolidated trade and utilization view for other consumers. | Introduces synchronization latency; requires TDS3 data-model changes; may affect TDS3 performance and scalability; expands TDS3 from a trade-event store toward a trade-state store; increases an already overloaded system; affects downstream TDS3 consumers; creates a denormalized silver source; requires reconciliation back to RATAN. |
| Option 2: Blade integration with RATAN | Blade makes direct API calls to RATAN for FX utilization data for `UTIL` trades, for example when a user performs an action. Blade continues to obtain core trade data from TDS3. | Provides potentially fresher data from the golden source; leaves TDS3’s role unchanged for granular utilization data; avoids a replicated utilization source; fits the stated FM architectural pattern. | Requires Blade to integrate with two systems; couples Blade to RATAN availability, API contract, and performance; requires backend merging of TDS3 and RATAN data; needs robust and performant RATAN APIs; requires performance assessment and inconsistency handling. |
| Option 3: Blade → RATAN UI integration through OpenFin | Blade exposes RATAN utilization information through a UI integration. | May provide a quick visual way for users to inspect utilization data. | Primarily solves the display requirement; does not make utilization data available to Blade backend processes; cannot independently support hard blocks or authoritative amendment and withdrawal validation. |

## Analysis-stage preference

The document’s framing favors Option 2 because RATAN is identified as the golden source, Option 1 is criticized as denormalization and as inconsistent with the FMRP strategy, and Option 2 is described as fitting the agreed FM architectural pattern.

This is not an approved decision. The source does not provide API contracts, latency targets, availability requirements, failure-mode behavior, caching policy, authorization rules, load estimates, or reconciliation design.

## Important open questions

- What RATAN endpoints, schemas, and correlation keys are required?
- What are the exact utilization statuses and remaining-amount semantics?
- What freshness target applies to display data versus hard-block decisions?
- Should Blade cache RATAN responses?
- What happens when RATAN is unavailable or disagrees with TDS3?
- Should controls fail closed for amendments, withdrawals, and `UTIL` trade booking?
- How are concurrent utilization requests prevented from exceeding available amounts?
- Does Blade call RATAN directly, or does [[entities/fxu]] remain the orchestration layer?
- How are country-specific Past Due windows and reversal rules represented?
- What security, entitlement, audit, and rate-limiting requirements apply?

## Evidence limitation

The source references `image-2025-5-27_13-23-55.png`, but the image is not included in the available source text. The detailed trade-booking and utilization flow cannot therefore be independently verified from the document.

## Related wiki topics

The source is relevant to [[concepts/cashflow-status-lifecycle]], [[concepts/cashflow-event-versioning]], [[concepts/cashflow-expiry-versioning]], [[concepts/cashflow-reference-consistency-validation]], and the broader distinction between authoritative and replicated settlement data.