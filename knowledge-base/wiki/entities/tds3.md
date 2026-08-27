---
type: entity
title: TDS3
created: 2026-08-22
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - Korea Cashflow Migration.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/NDS Auto Netting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis/SFX Supporting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Copy of Trade Confirmation & Cashflow STP - Deprecated.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CPN Tech Design - Draft for now.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Migrating BCS to Strategic Workflow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Mock testing data userguide.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - MxML mapping to SCBML.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/EG   NP   SAU UBER Roll Out & FXU Business Go-Live Runbook on 04 04.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Trade Information Tech Design.md", "RATAN/RATAN -Interfaces/Ratan and CDUPS 51512.md"]
tags: ["tds3", "trade-confirmation", "integration", "stp", "nstp", "data-source", "trade-enrichment", "cash-settlement", "upstream-system", "historical-data", "lifecycle-events", "sfx", "stella", "confirmation", "cashflow", "deprecated-evidence", "payment-lake", "trade-information", "bcs", "trade processing", "Kafka", "testing", "trade-data", "enrichment", "murex-211", "synchronization", "fxu", "scbml", "publisher", "release-operations", "trade-state", "message-routing", "trade-processing"]
related: ["korea", "cashflow-status-handling", "high-risk-nstp-rule", "nds-auto-netting", "ndirs", "murex-2-11", "ratan", "sfx", "cashflow-migration-readiness", "migration-weekend-lifecycle-event-control", "stella", "cdu-ps", "trade-confirmation-driven-cashflow-stp", "entities/stella", "payment-lake", "cpn-netting", "automatic-un-netting-on-trade-market-events", "bcs", "cdu", "bcs-cdu-match-status-confirmation", "bcs-strategic-workflow-migration", "kafka-settlement-test-topics", "mock-settlement-test-data-generation", "murex-211", "mxpayml", "murex-payment-mxml-to-scbml-transformation", "fxu", "razor", "transaction-synchronization", "tdsx", "sabre-pss", "upstream-cashflow-replay-for-group-completion", "trade-information-sourcing-for-cash-settlement", "data-ambassador", "lms", "cdups", "ratan-cdups-trade-confirmation-flow", "post-trade-orchestration"]
---

# TDS3

TDS3 is referenced as an upstream trade-data system and, in selected RATAN and CDUPS confirmation flows, as an intermediate trade-data and message-routing application. The documented role varies by source, trade type, and integration.

## Role in trade-information sourcing

The *Trade Information Tech Design* source identifies TDS3 as the central trade-data system referenced by both trade-information sourcing options in the [[trade-information-sourcing-for-cash-settlement]] analysis.

- **Option 1:** The Cashflow service would query TDS3 through [[data-ambassador]] for each cashflow event.
- **Option 2:** The existing trade service would continue consuming all trades from TDS3 and provide a locally replicated copy for downstream use.

The source identifies the following information as required for Cash Settlement use cases:

- Entity LEID and Trader ID for LMS feed generation.
- Instrument for a potential Cashflow Blotter Query, with BCS named as the context or source.

The canonical TDS3 lookup keys, response schema, ownership, access mechanism, and service-level requirements are not documented. The source does not establish a direct Cash Settlement integration, an approved access pattern, or a production contract.

## Integration and enrichment roles

### CN settlement mapping

The *CN Settlement - MxML mapping to SCBML* source identifies TDS3 as an enrichment source for the Murex 2.11 Payment MxML-to-SCBML transformation.

That source specifically assigns TDS3 responsibility for:

- Trade ID retrieval or confirmation for the SCB trade identifier.
- Trader information.
- Trader PSID.

The source does not define a TDS3 API, query, ownership model, availability guarantee, or failure behavior for this enrichment.

### Korea onboarding

In the Korea onboarding checklist source, TDS3 is identified as a required integration dependency for trade-confirmation status during Korea onboarding.

Confirmation status may influence settlement processing and STP/NSTP control. The Korea onboarding checklist source does not define the interface contract, message flow, ownership, or acceptance criteria.

### NDS Auto Netting data-source role

In the NDS Auto Netting source, TDS3 is the supporting data source used by RATAN to derive `Cashflow.ND_Parent_Typology` for NDS Fixing cashflows.

RATAN queries `Instrument_Common.Source_System_Instrument_Type` using the NID-derived `ND_Parent_Trade_Id` as `Source_System_Internal_Trade_Id`. When the source field contains separator-delimited data, RATAN uses the last value.

#### Timing risk

The NDS Auto Netting source identifies a timing risk: TDS3 may not have received the Murex data when RATAN performs enrichment, resulting in an empty parent typology.

Retry and failure handling are not defined in that source. See [[how-should-ratan-handle-empty-nd-parent-typology]].

### SFX migration-cycle-2 historical-data role

In the SFX migration-cycle-2 support notes, TDS3 is identified as the upstream provider of historical data to [[ratan]].

For the documented migration-cycle-2 test, TDS3 reportedly sent only the final version of historical data to RATAN. The notes state that this was not production-like and that only a rebook event was received and processed.

This is a test-data limitation for the named SFX scenario, not evidence of TDS3 behavior in all environments or integrations. It prevents the source from demonstrating complete lifecycle-event sequencing. See [[cashflow-migration-readiness]].

## Trade confirmation and cashflow flows

### Trade-specific RATAN and CDUPS confirmation routes

The *Ratan and CDUPS 51512* source describes trade-specific confirmation routes involving TDS3:

- **Murex trades:** CDUPS sends the trade-confirmation event to TDS3, and RATAN synchronizes trade state from TDS3, including the cashflow STP condition.
- **FMRP trades:** [[stella]] sends trade XML to RATAN through TDS3 after updating the trade status.
- **BCS trades:** TDS3 has no such confirmation data; CDUPS sends the information directly to RATAN.

This source therefore does not support treating TDS3 as the universal confirmation route for all trade types.

### BCS confirmation and trade-information context

The *Migrating BCS to Strategic Workflow* source identifies TDS3 as a trade-information source that BCS currently does not use for cashflow confirmation. According to that source, BCS instead consumes match status from [[cdu]].

For the target confirmation contract, that source states that match-status confirmation must be explicitly distinguished from trade-information consumption. It does not establish that TDS3 should replace CDU.

The *Ratan and CDUPS 51512* source separately states that, for BCS trades, TDS3 has no confirmation data and CDUPS sends the information directly to RATAN. The two sources describe distinct aspects of BCS confirmation and do not establish a replacement of CDU or CDUPS by TDS3.

### Deprecated Stella confirmation flow

In the deprecated *Copy of Trade Confirmation & Cashflow STP* source, TDS3 is an integration component in the Stella confirmation flow.

That source describes TDS3 as:

- Sending Stella trade messages to [[cdu-ps]] through Solace.
- Forwarding confirmation-status notifications from Stella to [[ratan]].

Because this evidence is from a deprecated document, it does not establish TDS3's current interface ownership, message schema, or operational role.

The deprecated source's described flows to [[cdu-ps]] and [[ratan]] are separate evidence from the *Ratan and CDUPS 51512* source's FMRP trade-XML route from [[stella]] to RATAN through TDS3. The sources do not establish that these descriptions use the same interface, message schema, or ownership model.

### CPN netting path

The draft *CPN Tech Design - Draft for now* describes TDS3 as the integration component used for Stella-originated cashflow updates before they are written to Payment Lake.

The draft describes the path as:

```text
Stella -> TDS3 -> Payment Lake
```

According to that draft, this path is used for Stella component updates during:

- Initial CPN eligibility and netting.
- Manual un-netting.
- Trade amendment processing.
- Trade cancellation processing.
- Re-entry of the latest component version into CPN eligibility.

The draft does not define the TDS3 message contract or whether TDS3 participates in version-conflict detection.

The draft's Payment Lake path is separate evidence from the deprecated source's flows to [[cdu-ps]] and [[ratan]], and from the *Ratan and CDUPS 51512* source's trade-specific confirmation routes. The sources do not establish whether these paths share an interface, ownership model, or message contract.

## FXU integration and synchronization

The *FXU Technical Design* source identifies TDS3 as a participating system in the FXU integration design. FXU details are described as persisted in TDS3 under Options 1 and 2.

The source assigns coordination responsibility as follows:

- **Option 1:** FXU coordinates the process.
- **Option 2:** RATAN coordinates the process.
- **Option 3:** TDS3 must participate if synchronization of the remaining amount requires transactional control.

The source does not define TDS3's API, persistence schema, or transaction protocol for this integration.

## Message publishing and release operations

The runbook *EG NP SAU UBER Roll Out & FXU Business Go-Live Runbook on 04 04* identifies TDS3 as the publisher of SCBML trade and cashflow messages.

In that runbook:

- The proposed TDS3 publisher stop and restart were struck through.
- The runbook states that stopping only the target countries was not possible.
- The runbook does not document whether a broader publisher control was used.
- The runbook does not document how publishing was normalized after the release.

These runbook statements describe the documented release-operation context and do not establish a general TDS3 publishing-control procedure.

## Kafka test integration

The mock testing data user guide identifies TDS3 through the Kafka topic `TDS3_Trade_Message_Process_In`.

```text
TDS3_Trade_Message_Process_In: Receive Trade
```

The guide does not provide additional information about TDS3 ownership, message schema, processing guarantees, or downstream validation.