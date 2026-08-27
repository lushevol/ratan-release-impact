---
type: entity
title: FXU
tags: [fxu, cash-settlement, utilization-pilot, integration, fx-utilization, transaction-banking, interface, settlement, utilization, market-expansion, ratan, acronym, unverified, utilization-orchestration, foreign-exchange, settlement-method, system, release, go-live, RATANONE, cashflow, accounting]
related: [fmrp, utilization-pilot, cash-settlement-delivery-dependencies, ratan, scpay, blade, fx-utilization, utilization-request-idempotency, utilization-remaining-amount, razor, ebbs, fxu-settlement-method-amendment, forward-trade-util-stamping, trade-remaining-amount-visibility, fxu-razor-fmrp-routing, utilization-functions, cross-market-expansion-dependencies, tds3, stella, fx-utilization-data-for-blade-controls, fxu-message-driven-integration, fxu-utilization-validation, cash-settlement-platform, cash-settlement-query-service-graphql-read-model, utilization-service, gross-util-settlement-method-transition, fxu-utilization-response-contract, cashflow-blotter, fxu-test-case, fxu-cashflow-utilization, ratanone, uber, uber-fxu-technical-live-and-business-go-live-2026, technical-live-versus-business-live, accounting-update-production-volume-baseline, mx-fxcash, ratanone-message-bridge, solace, ratan-fxu-utilization-integration, 5-ratan--17-ratan-interfaces--28-ratan-and-fxumx-fxcash-40630--hwa4i8]
created: 2026-08-22
updated: 2026-08-25
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Dependencies for expansion to other Markets.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Dependencies for expansion to other Markets/Utilization Functions.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/FX Utilization Process  Data Integration for Blade Controls & Visibility.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/Draft Design For Phase2.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber & FXU Technical Live Plan.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber & FXU Technical Live Plan/Production Existing Data Testing Cases.md", "RATAN/RATAN -Interfaces/Ratan and FXU(MX-FXCASH) 40630.md"]
---

# FXU

## Identification and role

FXU (FX Util) is described by the functional and technical-design sources as the Transaction Banking utilization application through which operations retrieve eligible FX deals, view utilization state, and submit utilization instructions.

The FX Utilization Process source identifies FXU as the system that orchestrates FX utilization requests. The technical design identifies FXU as the central subject of the [[fxu-technical-design]] for foreign-exchange utilization in the Cash Settlement domain. It describes FXU as participating in:

- Cashflow and trade selection
- Utilization processing
- Acknowledgement
- Exception management
- Synchronization with [[ratan]] and [[tds3]]

The [[fxu-test-case]] source identifies FXU as the system or product area addressed by its test case. It associates FXU with a `ForeignExchange:Swap` trade scenario and cashflow-utilization behavior in the [[cash-settlement-platform]].

The Phase 2 draft design uses FXU as a cash-settlement domain scope. It associates the `UTIL` settlement-method value with cashflows belonging to FXU scope and distinguishes that scope from `GROSS`.

The RatanOne Cash Settlement UBER and FXU release-plan source describes FXU as the FX-utilization capability tracked in that release plan.

The *Utilization Functions* source names FXU in its folder context alongside [[ratan]], but does not define the acronym or establish whether FXU is a system, service, team, functional domain, or ownership boundary. Its precise role must therefore be confirmed from the source body or other authoritative documentation. The application and orchestration descriptions above are supported by the other listed sources.

The FXU test-case source does not identify FXU's owning team, service boundaries, interfaces, persistence model, or deployment topology.

## Interface 40630 and MX-FXCASH context

A separate RATAN interface source identifies `FXU` as the upstream application in interface `40630`. According to that source:

- FXU uses its `MX-FXCASH` function or interface.
- FXU calls a [[ratan]] API to query cashflow status.
- FXU sends a `FullUtilize` request for accounting through [[solace|Solace]].
- FXU participates in a Solace request-and-response route involving [[ratanone-message-bridge]] or another `RATANONE` component.
- Interface `40630` documents the `SPOT`, `Forward`, and `SWAP` product categories.

That interface source describes the payload format as `JSON`, but does not define the API contract, message schema beyond `JSON`, actual Solace destinations, or operational handling of retries, acknowledgements, and failures. It also states that the relationship between FXU and [[mx-fxcash]] should be confirmed in the linked FXU technical design.

These interface-specific statements apply to the `40630`/`MX-FXCASH` source and do not replace the broader responsibilities, ownership alternatives, or proposed flows described by the Cash Settlement functional and technical-design sources.

## Ownership and responsibility boundaries

The sources do not establish a single resolved ownership model for FXU's responsibilities:

- The FX Utilization Process source does not identify FXU as the golden source for settlement, utilization amounts, or detailed utilization statuses. It attributes those data domains to [[ratan]]. This is consistent with the proposed MVP in the FXU–RATAN analysis, in which FXU queries RATAN for the remaining amount and associated data.
- The technical design presents three ownership options:
  1. FXU-owned coordination
  2. RATAN-owned coordination
  3. A RATAN-centered model with no explicit exception-management owner
- No technical-design option is recorded as selected.
- The technical design lists FXU detail persistence in RATAN, TDS3, and FXU for Options 1 and 2, but only in RATAN for Option 3.

See [[which-system-owns-fxu-transaction-coordination]].

The Phase 2 draft design states that FXU utilization behavior and manual scope changes are implemented through [[utilization-service]]. This is a statement of the draft design and does not resolve the broader ownership alternatives above.

## Responsibilities described by the technical design

The FXU Technical Design describes FXU as responsible for or involved in:

- Querying cashflows and related trade information through the FXU Query API
- Accepting utilization requests on `Cash_Settlement_FXU_Request_In`
- Returning ACK or NACK outcomes on `Cash_Settlement_FXU_Ack`
- Validating utilization identifiers, trade versions, currencies, amounts, settlement accounts, cashflow states, and value dates
- Potentially coordinating synchronization transactions, depending on the selected integration option
- Potentially owning exception management under Option 1

These are responsibilities and alternatives described by the technical design; they do not resolve the ownership questions above.

## Proposed utilization flow

According to the FXU–RATAN analysis, the proposed MVP flow is:

1. FXU queries [[ratan]] for the remaining amount and associated data.
2. FXU submits a full-utilization request through Solace.
3. FXU consumes an asynchronous ACK/NACK.

The separate interface `40630` source likewise states that FXU sends a `FullUtilize` request for accounting through Solace, but it does not define the actual destinations, acknowledgement behavior, retry handling, or failure handling.

FXU is expected to show:

- Utilized trade information
- Unutilized trade information
- Remaining-amount information
- Auto-utilized trade information

The FX Utilization Process source separately states that the underlying settlement, utilization-amount, and detailed-utilization-status data domains are attributed to RATAN rather than FXU. It does not establish that FXU is the authoritative source for those domains.

## API, messaging, and validation requirements

The FXU–RATAN analysis identifies the following additional API needs:

- Utilization currency 2
- Utilization amount
- Enriched response fields
- IMS headers
- Decimal tolerance
- A [[blade]] trade ID in requests

These are requirements identified by the analysis rather than a supplied API contract.

The technical design additionally describes:

- An FXU Query API for cashflow and related trade-information queries
- The inbound message channel `Cash_Settlement_FXU_Request_In`
- The acknowledgement channel `Cash_Settlement_FXU_Ack`
- Validation of utilization identifiers, trade versions, currencies, amounts, settlement accounts, cashflow states, and value dates

See [[utilization-request-idempotency]] and [[what-is-the-fxu-ratan-utilization-api-and-idempotency-contract]].

The interface `40630` source describes the interface payload as `JSON`, but expressly does not define a complete message schema or API contract. This limitation applies to that source and is separate from the requirements and channels listed in the FXU technical design.

## Blade relationship and data visibility

[[blade]] requires utilization information for trade-level visibility and controls on `UTIL` trades.

The FX Utilization Process source leaves open whether Blade should access RATAN directly or whether FXU should remain involved as an orchestration layer. It does not specify:

- An interface contract
- An ownership boundary
- An authoritative correlation key between FXU requests and RATAN cashflows

The requirement for a Blade trade ID in utilization requests is identified separately by the FXU–RATAN analysis. That requirement does not, by itself, resolve the open question about the authoritative correlation key.

## Utilization pilot scope and delivery status

According to the 2024 changes source, the pilot includes:

- Product support
- Swift Generation
- Accounting Generation
- Drop2/Drop3 events

The dependency plan records the FX Utilization (FXU integration) item as `Not required` and `Closed` under Razor/FMSGW. The same source's main pilot scope still names FXU integration. This distinction should be preserved until the delivery-plan semantics are confirmed; it does not by itself resolve whether FXU integration is required for the overall pilot.

## Phase 2 utilization behavior

The FXU–RATAN analysis proposes FXU support for:

- Partial utilization
- PastDue utilization
- Reverse utilization
- Early utilization

FXU should also block utilization when a cashflow is in `ERROR` status after an amendment or withdrawal event.

These capabilities are proposed requirements and do not establish that they have been implemented.

## Settlement-method scope in the Phase 2 draft

The Phase 2 draft design describes `UTIL` and `GROSS` as settlement-method values. It does not establish whether they are:

- Mutually exclusive lifecycle states
- Accounting classifications
- Routing attributes only

The draft contains one occurrence of `UITL`; this requires confirmation before it is treated as a valid identifier.

The draft also states that the cashflow data implications relate to [[cashflow-data]]. This data relationship is stated by the draft and does not, by itself, establish ownership of the underlying cashflow data.

## Test-case scope

The [[fxu-test-case]] covers the following FXU-related requirements:

- Creating a `ForeignExchange:Swap` trade
- Generating four cashflows from that trade
- Applying the `Util` settlement method
- Restricting selected cashflow actions
- Exposing utilization and source-trade fields in view-builder and customer-filter surfaces
- Adding utilization-related cashflow statuses
- Adding `FXBRREC-M` as a Vostro settlement-means value

These are source-level test-case requirements, not verified implementation outcomes.

## Market-expansion requirements

According to *Dependencies for expansion to other Markets*, FXU is required to:

- Support a utilization window for forward trades
- Support UTIL stamping for forward trades whose future cashflows have not yet materialized
- Identify whether a trade belongs to [[razor|RAZOR]] or [[fmrp|FMRP]]
- Trigger the request to the correct destination system for a single entity
- Support Early Utilization, Cancellation Charges, Auto Cancellation, and Time Option workflows

The market-expansion requirements do not establish that these capabilities are implemented.

### Market-expansion integrations

According to the market-expansion source, [[ratan|RATAN]] is responsible for moving a trade to Utilized within the utilization window and triggering the settlement-method amendment event to [[stella|Stella]].

That source further states that:

- FXU must integrate with [[razor|RAZOR]] and [[fmrp|FMRP]] for system-specific routing.
- [[ebbs|EBBS]] receives the accounting entry on value date.

### Unresolved market-expansion design questions

The market-expansion source does not define:

- The routing key
- The system of record
- API or event contracts
- Error handling
- The relationship between FXU trade status and cashflow-level status

The FX Utilization Process source separately states that no authoritative correlation key between FXU requests and RATAN cashflows is specified. This is an additional unresolved interface question and is not necessarily identical to the market-expansion source's unresolved routing-key question.

## Release-plan status and production-data context

The RatanOne Cash Settlement UBER and FXU release-plan source explicitly excludes FXU enablement from the `2026-03-28` technical-release scope and records an intended business-live date of `2026-04-04`.

In that release matrix, `51358-ratan-cash-settlement-fx-utilization-service` is marked `DO NOT DEPLOY!!` despite a passing pipeline.

The same source contains later FXU Phase 2 UAT4 records but does not provide:

- An approved activation record
- A cutover sequence
- Evidence that business live was completed

See [[what-is-the-authoritative-2026-04-04-fxu-go-live-cutover-and-time-zone-sequence]].

The *Production Existing Data Testing Cases* source names FXU in the parent path of [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--1ijfplm]], which is part of the `Uber & FXU Technical Live Plan` for [[ratanone]] Cash Settlement.

That source contains no explicit `AccountingUpdate` allocation for FXU. It is therefore not possible to determine whether its listed production counts are FXU-specific, Uber-specific, or combined.

## Related platform context

The technical design places FXU within the broader [[cash-settlement-platform]] and describes interactions with:

- [[ratan]]
- [[razor]]
- [[tds3]]

The `/api/ratan/stmcn/v1/cashflows` path suggests a relationship with [[ratan-query-service]], but the technical design source does not prove implementation ownership.

FXU is also discussed alongside:

- [[fmrp]]
- [[stella]]
- [[cash-settlement-delivery-dependencies]]
- [[scpay]]
- [[blade]]
- [[fx-utilization]]
- [[utilization-remaining-amount]]
- [[fx-utilization-data-for-blade-controls]]
- [[utilization-service]]
- [[mx-fxcash]]
- [[ratanone-message-bridge]]
- [[solace]]
- [[ratan-fxu-utilization-integration]]

