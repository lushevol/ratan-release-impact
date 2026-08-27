---
type: entity
title: Uber
created: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/RATAN - Uber Integration - Proposals.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Trade Cashflow SSI Stamping on Uber Message.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/PT result for UBER.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber & FXU Technical Live Plan.md"]
tags: ["uber", "ratan", "cash-settlement", "integration", "json", "trade-message", "sabre", "ssi-stamping", "message-flow", "RATANONE", "upstream-integration", "message-processing"]
related: ["ratan", "ratan-one", "fmrp", "scbml", "uber-legacy-workflow-isolation", "ratan-strategic-json-data-model", "ratan-uber-migration-options", "sabre", "ssi-stamping-service", "uber-message-ssi-stamping", "trade-id-version-ssi-stamping-request", "uber-scbml-performance-regression-testing", "25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--19101up", "25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--1isntku", "tdsx-uber-message-listener", "ratan-uber-integration-technical-design", "cd ups", "product-agnostic-ssi-stamping", "trade-level-ssi-stamping", "ratanone", "fxu", "uber-fxu-technical-live-and-business-go-live-2026"]
updated: 2026-08-24
---

# UBER

## Role and definition

UBER is an upstream integration and message-processing domain in the RatanOne Cash Settlement release plan.

The **Strategic SSI Stamping Design** characterizes UBER as the proposed standard exchange format for trade-related SSI stamping between [[ratan]] and [[cd ups]]. Within that design:

1. RATAN decodes UBER into the RATAN Logic Model.
2. RATAN extracts product-specific settlement attributes.
3. RATAN normalizes those attributes.
4. RATAN submits the normalized attributes to the [[ssi-stamping-service]].

UBER also carries the trade and cashflow context needed to reuse trade-level SSI results.

Other source documents use the term in broader or less specific ways:

- The RATAN integration proposal identifies Uber with the strategic cashflow-processing path associated with a JSON-based RATAN settlement data model. It does not establish whether Uber is a product, business flow, message type, or internal project name.
- The SSI-stamping requirement describes `uber` as SABRE's strategic trade-message format and as the successor to [[scbml]] for the relevant downstream SSI-stamping integration. It does not define the complete `uber` schema or interface.
- The performance-test source describes Uber as an inbound integration and message flow in Cash Settlement.
- The technical live plan describes UBER as an upstream integration and message-processing domain.

These descriptions are retained separately because the source documents do not establish that all uses of “Uber” refer to exactly the same object.

## Scope and release planning

The initial workflow scope includes the entities or business identifiers `EG`, `NP`, and `SA`, with `FXO` listed as additional phase-one scope.

The Uber & FXU Technical Live Plan records planned onboarding for `EG`, `NP`, and `SA`. It also records planned readiness, branch synchronization, and service-pipeline activity, but does not prove that production onboarding was completed or that its processing results were operationally accepted.

The planned UBER onboarding is intended to occur without enabling [[fxu]] in the March technical-release scope. The concrete behavior permitted during that technical-live period remains an open question in [[what-exactly-separates-eg-np-sa-uber-technical-live-from-business-live]].

## UBER message and SSI-stamping flow

The upgraded [[ssi-stamping-service]] is expected to:

1. Locate an `uber` message using a trade ID and version from [[tl]].
2. Stamp Vostro and Nostro information.
3. Return the post-stamped message.

The Strategic SSI Stamping Design additionally describes a product-agnostic processing path in which RATAN converts UBER data into the RATAN Logic Model, extracts and normalizes product-specific settlement attributes, and submits them for SSI stamping. UBER provides the trade and cashflow context required to reuse trade-level SSI results.

The available strategic-design source does not specify a complete UBER SSI structure or authoritative mappings for:

- Product taxonomy.
- Trade identity.
- Currency extraction.
- Direction semantics.
- Party fields.

## Message flow and performance testing

The performance-test source describes a Round 1 workload of 100 Uber messages and 200 cashflows, executed without Message Bridge.

That source treats non-regression of the existing [[scbml]] flow as mandatory and comparative Uber performance as a nice-to-have objective. It supplies no control baseline or isolated comparative timings; therefore, it does not demonstrate either outcome.

See [[uber-scbml-performance-regression-testing]] for the required evidence design and [[tdsx-uber-message-listener]] for the inbound listener context.

## Relationship to legacy processing

Uber processing is intended to coexist with the existing Murex and [[scbml]] flow during migration. Uber entity scope does not necessarily imply JSON format: historical cashflows in Uber scope may still carry SCBML.

The SSI-stamping requirement separately characterizes `uber` as SABRE's strategic trade-message-format successor to [[scbml]] for its downstream integration.

The proposal favors an independent Uber workflow while retaining the legacy workflow for other payments. Routing remains unresolved for:

- Operations that do not originate from inbound flow.
- Batch operations spanning message types.
- SSI refresh.
- Historical data.

## Migration

The planned sequence is:

1. Build a new Uber workflow and API set from front to back.
2. Integrate historical SCBML and Murex SCBML data.
3. Build Open Search extraction and front-end integration.
4. Rehearse a clear production cutover to prevent event loss.

This strategy is described in [[uber-legacy-workflow-isolation]] and compared with alternatives in [[ratan-uber-migration-options]].