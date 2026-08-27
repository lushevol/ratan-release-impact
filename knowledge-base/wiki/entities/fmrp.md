---
type: entity
title: FMRP
created: 2026-08-22
updated: 2026-08-25
tags: ["program", "re-platforming", "business-initiative", "FMRP", "programme", "migration", "cash-settlement", "India", "settlement", "payment-processing", "amendments", "ratan", "FM-Re-Platforming", "settlements", "FX-rates", "API", "inter-entity-netting", "swift", "configuration", "cn-settlement", "SSI-stamping", "system", "process", "project-context", "trade-processing", "ssi", "product-taxonomy", "reference-data", "settlement-affirmation", "cashflow-flow", "high-value-payment", "architecture", "operating-model", "pre-trade", "post-trade", "Murex-2-11", "integration", "trade-validation", "major-version", "cashflow", "liquidity-management", "source-system"]
related: ["cash-settlement-2025-roadmap", "cash-settlement-re-platforming", "ratan", "murex-2-11", "fxo-mini-trade-migration-ratan-cash-settlement", "fxo", "ratan-settlement", "stella", "ccil-guaranteed-and-non-guaranteed-netting", "murex", "ratan-one", "murex-to-ratan-exception-mapping", "released-resultant-amendment-handling", "strategic-settlements-platform", "settlement-first-migration", "murex-cashflow-migration-to-ratan", "inter-entity-netting", "inter-entity-netting-spot-rate-retrieval", "chg0988640", "is-the-chg0988640-fmrp-spot-rate-endpoint-production-ready", "razor", "murex-2-11-field-20-format", "agency-payment-identification", "is-auto-split-in-scope-for-fmrp-cn-settlement", "ssi-stamping-service", "ssi-stamping", "scbml", "cdups", "trade-lake", "trade-ssi-stamping", "affirmation-email-scope-configuration", "settlement-email-template-and-contact-governance", "fmsgw", "loaniq", "ratan-high-value-payment-control", "stp-nstp-and-last-user-message-contract", "fmrp-stella", "fmrp-cashflow-responsibility-split", "murex-211", "ratan-10123", "fmrp-cashflow-publication-lifecycle", "fmrp-payment-eligibility-and-suppression", "murex-ratan-cashflow-message-contract", "tds3", "trade-validation-gating", "fmrp-major-version-backward-validation", "what-is-the-canonical-trade-validation-key-by-source-system", "lms", "ratan-lms-liquidity-cashflow-feed", "lms-country-and-entity-scope"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/2025 Target.md", "Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/FXO Mini Trade Migration - Ratan Cash Settlement - RunBook (2026-08-15 weekend).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CCIL Netting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 Payment Non-STP Exception.md", "Cash Settlement Home Page/Cash Settlement Home Page/Strategic Cash Settlements Features.md", "RATAN - 51358/RATAN/RATAN -Release/Ratan Release Plan 2026/Ratan New Onboarding Checklist 2026/2026_05_30_CHG0988640_Inter Entity Netting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Ops weekly session/2022-11-16.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Compatibility design for multiple entities.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Stamping Tech Design-Egypt.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade SSI Stamping - Product templates.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Derivative Settlement Affirmation - Email Automation.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/High Value Payment Control - RATAN.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Ratan & Stella cashflow integration.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Trade Validation Confirmation Process Tech Design.md", "RATAN/RATAN -Interfaces/Ratan and LMS 50686.md"]
---

# FMRP

## Context and role

FMRP is the programme or business-initiative context for the 2025 cash-settlement roadmap, the FXO mini trade migration and Ratan cash-settlement work, and the `CHG0988640` Inter-Entity Netting release.

The Strategic Cash Settlements Features source expands FMRP as **FM Re-Platforming** and describes it as the programme under which RATAN is being built as a [[strategic-settlements-platform]].

The 2025 roadmap source links to a Confluence page titled `2025 High Level Backlog - FM re-platforming` under the `FMRP` space. The FXO and Ratan runbook links the activity to `FMRP Trade Migration - Ratan Cash Settlement - PROD Approach` and the `FXO Tech Readiness - 8.0 - FM re-platforming - Confluence` reference.

Separately, the Murex 2.11 Payment Non-STP Exception source identifies FMRP as the target settlement-processing context in its Murex 2.11 Payment STP exception mapping.

The SSI Stamping compatibility-design source describes FMRP as the process area containing the SSI Stamping Flow for the strategic cash-settlement design. In that source, FMRP is the parent context for extending SSI stamping to additional legal entities.

The SSI Stamping Tech Design—Egypt source likewise identifies the flow as `FMRP - SSI Stamping Flow` and describes FMRP as the process context in which the SSI Stamping design is documented.

The Trade SSI Stamping—Product templates source describes FMRP as the project and processing context in which the trade SSI stamping requirement is specified.

The High Value Payment Control—RATAN source separately describes FMRP as a cashflow-processing flow in scope for RATAN high-value payment-control enhancements. This source-specific description does not by itself define the complete FMRP programme scope or operating boundary.

The Ratan & Stella cashflow integration proposal describes FMRP as the target operating model referenced by that proposal. This characterisation is specific to the proposal and should not be treated as a replacement for, or a complete definition of, FMRP as the FM Re-Platforming programme described by the Strategic Cash Settlements Features source.

The Trade Validation Confirmation Process Tech Design source separately describes FMRP as a trade source system covered by the proposed RatanOne trade-validation gate. This source-specific description does not replace the broader programme definition of FMRP or establish that the proposed gate is implemented.

## Strategic settlement role

According to the Strategic Cash Settlements Features source, FMRP provides the strategic trade stack whose cashflows are intended to share a central settlement and payment platform with legacy Murex cashflows.

During [[settlement-first-migration]], the source identifies two cashflow populations processed through RATAN:

1. FMRP strategic-trade cashflows.
2. Cashflows from Murex trade populations.

The Murex population is identified by that source as a separate population; this does not establish that Murex trade populations are part of FMRP itself.

The same source references FMRP rollout dependencies through the `RATAN Settlements FMRP Backlog`.

## Scope referenced by the sources

### 2025 roadmap and FXO/Ratan sources

The annual target associates FMRP with:

- CN LNBR
- UK Prime migration for PM and Rates
- CN CCS trade migration
- The broader [[cash-settlement-re-platforming]] effort

The separate FXO and Ratan source describes operational execution within the wider FMRP re-platforming context, specifically:

- FXO mini trade migration
- Ratan cash-settlement work

These references describe related FMRP contexts and source-specific activities; they do not establish that every listed activity belongs to a single complete FMRP scope.

### India and CCIL netting

The CCIL netting source describes FMRP as the migration and settlement-processing program under which India cashflow migration and mandatory CCIL netting were specified.

According to that source:

- India was an H1 2024 FMRP migration market.
- The strategic CCIL design was not expected to meet the release timeline.
- A tactical implementation was therefore used in [[ratan]], based on Murex 2.11 static data.

### FMRP 8.0 flow requirements

Later notes in the CCIL netting source attribute the following requirements to FMRP 8.0:

- IRS-netting resultants must be enriched with `Settlement Method = CCIL` before auto netting.
- Story `14473106` covers the `CCIL Guarantee` path.
- Story `15765034` covers flows initially booked as `GROSS` and converted by Ratan Settlement.

The documented examples end with `N3` in `WAITING + Pending Exception`; the CCIL netting source does not establish the complete post-netting settlement lifecycle.

## RATAN-to-LMS liquidity-management feed

The `Ratan and LMS 50686.md` source lists FMRP as a source system for the RATAN-to-LMS liquidity-management cashflow feed.

That source associates FMRP with these feed categories:

```text
CURR
FXD-FXD
CURR-XSW
CURR-OPT-SMP
CURR-OPT-ASN
COM-SWAP
CRD-RTRS
CRD-CDS
SCF-SCF
IRD-CF
IRD-IRS
IRD-CS
IRD-LN_BR
IRD-BOND
```

The original table formatting places pipe characters inside the data-feed cell, so the intended segmentation of these categories should be confirmed.

### LMS scope

The same source lists the following locations or entities as in scope:

```text
CN, IN, SG, UK, DE, HK, DUBAI, NEWYORK, DIFC
```

It states that the following should not flow to SAIL-LMS:

```text
Egypt, Malaysia, Nepal, Saudi, South Africa, Taipei, OBU-Taipei, Bangkok,
SCS HK, MAURITIUS, JAKARTA, MANILA, TOKYO, JOBURG, PHILIP FCU
```

This list mixes countries, locations, booking centres, and entity identifiers. It should not be interpreted as a normalized country taxonomy.

These LMS-feed statements come specifically from the `Ratan and LMS 50686.md` source. They establish FMRP's listing as a source system and the documented feed scope in that source, but do not by themselves establish the broader FMRP programme scope, the complete RATAN-to-LMS interface contract, or ownership of SAIL-LMS processing.

## Murex 2.11 cashflow-integration route

The CN Settlement—Murex 2.11 workflow-change source describes FMRP differently: as the cashflow-integration route between [[murex-211]] and RATAN. In that source, FMRP:

- Publishes eligible Murex payment flows.
- Records publication and response state.
- Processes RATAN acknowledgements and releases.

This route-specific description is documented configuration intent. It does not replace the Strategic Cash Settlements Features source's definition of FMRP as the FM Re-Platforming programme, nor does it establish that the workflow was deployed, tested, or enabled in production.

### Main implementation artifacts

According to the CN Settlement—Murex 2.11 workflow-change source:

- `SCB_FMRP_DBF` stores per-flow status, RATAN identifiers, and lifecycle timestamps.
- Murex formulas under the `client.scb.fmrp.*` namespace implement routing, filtering, enrichment, persistence, and retry behavior.
- `FmrpOutboundMQ` publishes outbound messages.
- `FmrpInboundMQ` receives RATAN responses.
- `FmrpInboundRouter` accepts acknowledged and released cashflow responses.
- `FlowEntrySpliter` fans out multi-flow responses into individual flow messages.

The same source states that FMRP shares the external-settlement entry point with the MLS/CPN route. It does not establish that `MLS` is equivalent to [[lms]].

### Documented eligibility checks

The CN Settlement—Murex 2.11 workflow-change source documents an insertion filter that checks:

- Entity membership in `FMRP_ENTITY_DBF`.
- Non-deliverable-currency status.
- Zero amount.
- Trade completeness.
- Precious-metal exposure.
- FXD suppression.
- CPT-related conditions.

That source records that the CPT formula's naming and result semantics require confirmation.

## Trade validation and RatanOne integration

The Trade Validation Confirmation Process Tech Design source describes FMRP as a trade source system covered by the proposed RatanOne trade-validation gate.

### Validation key and rule

According to that source, FMRP validation uses:

- Trade ID.
- Major version.
- Trade status.

A trade is considered validated when its status is one of:

- `SENT`
- `AFFIRMED`
- `CONFIRMED`
- `TOBESENT+Validate[action]`

The source states that validation of a higher major version applies backward to earlier major versions. For example, validation of major version 4 covers versions 1 through 3. This behavior is documented separately in [[fmrp-major-version-backward-validation]] and must not be applied to Murex without evidence.

### Confirmation and status sourcing

The design proposes sourcing FMRP confirmation and validation status from [[tds3]], while maintaining the trade key needed for cashflow processing within [[ratan-one]].

The source does not define:

- The detailed TDS3 API.
- The status-history contract.
- Handling of corrections.
- Handling of validation-status regressions.

These trade-validation statements apply specifically to the proposed RatanOne trade-validation design. They do not establish that FMRP universally uses this validation rule, that the gate is in production, or that the rule applies to other source systems such as Murex.

## Architectural intent and cashflow responsibility split

The Ratan & Stella cashflow integration proposal separates pre-trade cashflow generation from post-trade cashflow processing:

- FMRP Stella generates cashflow events and business versions.
- Post-trade applications, principally [[ratan]], manage materialization, lifecycle, NSTP, netting, payment processing, and settlement outcomes.

The proposal associates this design with China entity onboarding and Murex decommissioning. It does not identify a formal approval record or implementation status for the target architecture.

This proposed responsibility split does not establish that FMRP itself performs the post-trade functions assigned by the proposal to post-trade applications, nor does it establish a complete FMRP operating model or implementation boundary.

## Payment, amendment, and settlement-processing requirements

### Murex 2.11 payment exceptions

The Murex 2.11 Payment Non-STP Exception source assigns FMRP existing amendment logic to the following scenarios:

- Scan&Modify (`S&M`)
- Market-operation (`MOP`)
- Reversal (`REV`)

This assignment does not establish that FMRP reproduces the corresponding Murex validation rules. The source describes RATAN reversal behavior in terms of amendments after payment release, while outright cancellation may proceed through STP.

See [[murex-to-ratan-exception-mapping]] and [[released-resultant-amendment-handling]].

### High-value payment control

The High Value Payment Control—RATAN source specifies the following requirements for FMRP cashflows:

- RATAN must expose their USD-equivalent values in the Cashflow Blotter.
- RATAN must support filtering by that amount through both custom filters and direct-blotter filtering.
- RATAN must provide [[fmsgw]] with STP/NSTP status and user attribution for routing.

The source proposes `stpFlag` and `lastUser` as Swift-header fields for FMRP, but records their precise semantics as pending confirmation.

FMRP cashflow-affirmation authorization is also unresolved in that source. The listed options are:

1. Remove update affirmation from the cashflow-list view.
2. Apply an authorization-limit check.

The same source treats [[loaniq]] as part of the FMRP flow and requires the solution to align with [[razor]]. These statements are requirements or proposals in the High Value Payment Control—RATAN source and do not establish finalized field semantics, authorization design, or broader ownership boundaries for FMRP, LoanIQ, Razor, or FMSGW.

### CN settlement configuration discussion

A CN Settlement Ops weekly session held on 2022-11-16 discussed FMRP as a **potential** implementation and configuration location for CN settlement requirements derived from Murex 2.11 behavior.

The session proposed that:

- A Field 20 prefix could be defined in FMRP, analogously to [[razor]] configuration.
- Whether the prefix has routing significance remained unresolved.
- Whether agency-booking Field 20 logic should be implemented remained unresolved.
- An explicit scope decision was needed for auto split.
- Razor auto-split behavior must not be assumed to apply to FMRP CN Settlement.

These points are proposals and unresolved scope questions from the CN Settlement Ops session. They do not establish that the Field 20 prefix, routing logic, agency-booking logic, or auto-split behavior was implemented in FMRP.

## SSI Stamping Flow designs

The SSI Stamping compatibility-design source concerns the compatibility of the FMRP SSI Stamping Flow with booking entities in Saudi Arabia, Nepal, and Egypt.

The proposed change adds `CCY Pair` information to support expected Nostro selection.

The SSI Stamping Tech Design—Egypt source states that [[ssi-stamping-service]] receives SCBML messages associated with the flow, resolves Vostro and Nostro settlement instructions, and returns enriched SCBML for downstream confirmation processing.

The service behavior is attributed to the SSI Stamping Tech Design—Egypt source; it does not establish that FMRP itself receives SCBML messages, resolves settlement instructions, or performs downstream confirmation processing.

### Trade SSI stamping product-template requirement

The Trade SSI Stamping—Product templates source documents a flow in which [[ratan]] is central to SSI lookup and enrichment. In that source:

- [[cdups]] acts as the confirmation client.
- [[stella]] supplies trade data through SCBML.
- [[trade-lake]] supplies identifiers and temporal values used to locate the relevant trade version.

The source emphasizes a central SSI stamping service while treating trade SSI stamping and cashflow SSI stamping as linked but independent.

These statements describe the documented trade SSI stamping flow and do not establish that the named systems, their interfaces, or all SSI-stamping functions are owned by FMRP.

These SSI-stamping design-specific sources do not establish FMRP ownership, interfaces, deployment details, implementation status, or a complete FMRP system definition, lifecycle, or operational boundary.

## FX-rate dependency for CHG0988640 Inter-Entity Netting

The Ratan release-plan and onboarding-checklist source describes FMRP as the stated FX-rate dependency for the `CHG0988640` Inter-Entity Netting release.

In that source, RATAN is described as calling an FMRP spot-rate endpoint to retrieve the official end-of-day USD rate. The endpoint provided by the source is:

```text
https://sabre-dev-cloud-global.uk.standardchartered.com/fmrp-fx-fxcs/uat/rate/{date}/OFFICIAL_EOD/USD
```

The source does not establish that this is a production endpoint. It also does not document:

- Authentication
- Certificates
- Timeouts
- Date semantics
- Fallback behavior
- The owning RATAN component

### Claimed failure handling

The questionnaire in the same source states that the interface retries automatically three times and writes an error log if the interface fails.

The exact retry interval, alerting path, and behavior after the final failed attempt remain unspecified.

These endpoint and failure-handling claims apply specifically to the `CHG0988640` Inter-Entity Netting source and should not be generalized to all FMRP integrations.

## Settlement affirmation and email automation

The Derivative Settlement Affirmation—Email Automation source identifies FMRP as a product-taxonomy source that must be supported by [[cdups]] for granular client-contact configuration.

That source also states that FMRP may provide the taxonomy needed to identify Islamic trades, whose portfolios may begin with `ISL`.

The feasibility of identifying Islamic trades through FMRP is marked as **to be confirmed**. This is a source-specific requirement and does not establish that FMRP currently owns or implements the CDUPS contact-configuration or trade-identification functions.

## Relationship to the project

The FXO and Ratan source provides operational execution steps within the wider FMRP re-platforming context. It does not define FMRP governance, programme-level milestones, or release acceptance criteria.

The `CHG0988640` release-plan source documents FMRP's role as an FX-rate provider or dependency for that release, but does not establish broader FMRP ownership of the inter-entity-netting implementation.

The settlement-affirmation source documents a separate product-taxonomy and CDUPS configuration dependency; it does not establish that all settlement-affirmation email automation is part of FMRP's implementation boundary.

The High Value Payment Control—RATAN source documents requirements and unresolved design points for FMRP cashflows within RATAN. It does not establish that all RATAN high-value-payment controls, FMSGW routing functions, Swift-header behavior, or cashflow-affirmation controls are within FMRP's implementation boundary.

The Ratan & Stella cashflow integration proposal describes an intended pre-trade and post-trade division of responsibility. It does not establish programme governance, a formal architecture approval, delivery status, or a complete operational boundary for FMRP.

The Trade Validation Confirmation Process Tech Design source documents a proposed RatanOne validation gate for FMRP trades. It does not establish that the validation gate, TDS3 integration, backward-major-version behavior, or associated status contract is implemented, approved, or applicable outside that design.

The `Ratan and LMS 50686.md` source documents FMRP as a source system for a RATAN-to-LMS liquidity-management feed and gives a particular location/entity inclusion and exclusion list. It does not establish that the LMS feed is part of the complete FMRP programme scope, nor that the mixed location/entity list is a normalized country or entity taxonomy.

Further FMRP-specific requirements should be added when authoritative documentation becomes available.

## Limitations and source boundaries

Except for the Strategic Cash Settlements Features source's expansion of FMRP as FM Re-Platforming, the sources do not define programme governance, ownership, funding, or complete scope.

The CN Settlement—Murex 2.11 workflow-change source records route-specific configuration intent and implementation artifacts. It does not establish production deployment, testing, enablement, or that this route is the complete definition of FMRP.

The Ratan & Stella cashflow integration proposal identifies FMRP as a target operating model and proposes a responsibility split between FMRP Stella and post-trade applications. It does not identify a formal approval record or implementation status for that target architecture.

The CN Settlement Ops weekly session records potential configurations and unresolved decisions; it does not establish their implementation or final scope.

The SSI Stamping compatibility-design, SSI Stamping Tech Design—Egypt, and Trade SSI Stamping—Product templates sources do not define FMRP ownership, interfaces, deployment details, or implementation status. They also do not provide a complete FMRP system definition, lifecycle, or operational boundary.

The `CHG0988640` source does not establish that the documented FMRP spot-rate endpoint is production-ready, nor does it provide the complete operational details for the interface.

The Derivative Settlement Affirmation—Email Automation source marks the feasibility of Islamic-trade identification through FMRP as unconfirmed and does not establish implementation status for the associated taxonomy or contact-configuration requirements.

The High Value Payment Control—RATAN source leaves the semantics of the proposed `stpFlag` and `lastUser` fields pending confirmation and leaves the FMRP cashflow-affirmation authorization approach unresolved.

The Trade Validation Confirmation Process Tech Design source is a separate proposed technical design. Its statements about FMRP as a trade source system, the validation statuses, backward application of major-version validation, and TDS3 sourcing are limited to that source and should not be generalized to all FMRP processing or to other source systems.

The `Ratan and LMS 50686.md` source is separately scoped to the RATAN-to-LMS liquidity-management feed. Its category and location/entity lists require confirmation where formatting or taxonomy is ambiguous, and should not be generalized to other FMRP integrations or operating boundaries.