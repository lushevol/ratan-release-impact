---
type: entity
title: LMS
created: 2026-08-23
updated: 2026-08-25
tags: ["downstream-system", "settlement", "integration", "lms", "settlement-accounting", "entity-filter", "korea", "cashflow-splitting", "routing", "tranche-3", "cash-settlement", "cashflow", "liquidity", "forecasting", "cashflow-feed", "downstream-platform", "reference-data", "surrounding-system", "feed-consumer", "ratanone", "liquidity-management", "receiving-system"]
related: ["vietnam-ifc-branch", "fmrp", "tag-20-logic", "should-the-vietnam-ifc-branch-feed-lms", "korea", "korea-settlement-accounting", "cashflow-splitting", "split-cashflow-downstream-integration", "clearing-swift-suppression", "jersey", "zhengzhou", "taeyuan", "entity-onboarding-static-data-controls", "what-is-the-authoritative-lms-routing-policy-for-jersey-zhengzhou-and-taeyuan", "ratan", "tranche-3-entity-onboarding", "loaniq", "stella", "settlement-integration-static-data-readiness", "cn-trade-migration", "early-settled-cashflow-migration-handling", "irs-cashflow-aggregation", "what-are-the-tlm-lms-and-cis-impacts-of-irs-cashflow-aggregation", "manual-entity-lms-reference-data-feed", "manual-entity-settlement-onboarding", "cross-border-debit-lms-feed-contract", "razor", "cash-settlement-home-page", "lms-cashflow-feed-eligibility", "scbml-cashflow-payload", "lms-event-contract", "ratan-lms-action-event-mapping", "what-is-the-authoritative-ratan-to-lms-action-and-event-contract", "lms-business-event-tracking", "what-is-the-lms-integration-contract", "ratanone", "lms-feed-source-identification", "what-is-the-authoritative-ratan-lms-message-sender-and-stack-flow-contract", "solace", "fm-bpms-lms", "ratan-lms-liquidity-cashflow-feed", "lms-country-and-entity-scope", "what-is-the-authoritative-ratan-to-lms-interface-contract"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Aggregation.md"]
---
# LMS

## Identity and documented scope

LMS is the named integration subject in the source document titled **LMS Integration**. It is also named as a surrounding system in the referenced `Ratan Action and LMS Event Matrix 20230919.xlsx`.

The available sources do not expand the acronym or identify LMS's owner. The **LMS Integration** source does not define LMS's system boundary, business responsibilities, or technical role. From that source alone, it is not known whether LMS publishes, consumes, transforms, or monitors events.

The newly generated **Ratan and LMS 50686** source identifies LMS as the receiving system in a documented RATAN liquidity-management cashflow flow:

```text
Ratan --(Solace)--> LMS
```

That source describes the surrounding application context as **FM-BPMS-LMS** and states that it extracts or receives cashflow data from RATAN for liquidity management. These claims apply to the RATAN liquidity-management flow and do not resolve the broader LMS role described by the **LMS Integration** source.

The relationship between LMS and the documented topic associations remains unresolved in what is the lms integration contract.

## RATAN relationship and downstream processing

The workbook title indicates that the `Ratan Action and LMS Event Matrix 20230919.xlsx` is intended to associate actions involving [[ratan|Ratan]] with events handled by LMS. Its accessible source does not establish whether LMS receives outbound events from Ratan, sends commands or acknowledgements to Ratan, or supports both directions.

The accessible workbook content does not make any individual action, event, payload, direction, or processing obligation verifiable.

The **LMS Feed** source separately documents LMS as the downstream consumer of eligible cashflow messages produced by [[ratan]] and FMRP. According to that source:

- [[ratan]] supplies raw source-system data.
- LMS generates the SWIFT field 20 prefix from that data.
- [[razor|RAZOR]] is involved in downstream payment-message generation.
- LMS receives an XML `SCBML` `CashflowData` message.

The **Ratan - LMS feed** technical-design source also identifies LMS as the downstream consumer of the Ratan feed. For that integration, LMS must align with Ratan's source-dependent `MessageSender` values and proposed `Stack Flow` values. That source does not establish the FMRP, RAZOR, or SCBML details listed by the **LMS Feed** source.

The **Ratan and LMS 50686** source describes a RATAN-to-LMS receiving flow over Solace, but does not provide a message schema, Solace subject, delivery guarantee, reconciliation process, or operational ownership.

## RATAN feed scope

The **Ratan and LMS 50686** source identifies feed coverage for:

- Stella
- FMRP
- LOANIQ

It explicitly excludes some source data from **SAIL-LMS**, including:

- Jersey data from Stella
- A list of FMRP locations or entities

That source does not establish whether LMS and SAIL-LMS are the same system, related deployments, or distinct destinations. The exclusions therefore apply specifically to the source's **SAIL-LMS** scope and must not be generalized into a complete LMS entity or country policy.

## Cashflow delivery eligibility

According to the **LMS Feed** source, LMS receives cashflows when the current delivery policy allows them, principally when:

- Cashflow status is `RELEASED` or `SETTLED`.
- Settlement means is `Nos`.
- Beneficiary BIC is not `REJECTXXALL`.
- Any current entity policy is satisfied.

The same source states that a later requirement removes the original hard-coded entity filter, while the treatment of `PHILIP FCU` remains unclear.

These eligibility claims come from the **LMS Feed** source and are separate from the RATAN and SAIL-LMS scope statements in **Ratan and LMS 50686**.

## Message format

According to the **LMS Feed** source, the integration uses:

```text
SCBML scbmlVersion="4-0"
messageType = CashflowData
payloadType = cashflowPayload
payloadVersion = 4-0
eventType = Insert
```

The payload includes:

- Cashflow identifiers
- Payment amount and currency
- Dates
- Trade references
- Source-system information
- Parties
- Product taxonomy
- Portfolio
- Workflow status
- Settlement instructions

The **Ratan - LMS feed** source does not specify an alternative message schema. It states only that the interface behavior, including source-dependent `MessageSender` values and proposed `Stack Flow` values, is documented in lms feed source identification.

The **Ratan and LMS 50686** source likewise does not provide a message schema.

## Manual-entity reference data

According to the **Feed Manual Entities to LMS** source, the 13 intended manual-entity records provide:

- FMID
- Country code
- FMCODE
- Branch code

That source does not identify the LMS owner, interface, target data model, feed publisher, schedule, validation rules, or acceptance response.

### Evidence boundary

The **Feed Manual Entities to LMS** source does not prove that any record was transmitted, accepted, reconciled, or kept synchronized in LMS. Its relationship to cross border debit lms feed contract must not be treated as evidence of a shared integration contract.

## Open integration questions

According to the **LMS Feed** source:

- The authoritative mapping for the FMRP source value and SWIFT field 20 prefix is unresolved: the source prose specifies `MX`, while its mapping table specifies `DV`.
- The relationship between the logical `SCB_Nostro_Account_Type` filter and the XML `settlementMeans` representation is unresolved.

The **LMS Integration** source leaves the following additional scope questions unresolved:

- Whether LMS publishes, consumes, transforms, or monitors events.
- What LMS's system boundary, business responsibilities, and technical role are.
- How the documented topic associations relate to the integration contract in what is the lms integration contract.

The **Ratan - LMS feed** technical-design source leaves the following implementation and operating details unspecified:

- LMS ownership.
- Interface schema.
- Acceptance criteria.
- Deployment procedure.
- Compatibility requirements.
- Support model.

The **Ratan and LMS 50686** source leaves the following details unspecified:

- LMS message schema.
- Solace subject.
- Delivery guarantee.
- Reconciliation process.
- Operational ownership.

These open questions apply to their respective source contexts and do not establish a single authoritative LMS contract. The authoritative technical contract for the RATAN-to-LMS interface remains an open question tracked in what is the authoritative ratan to lms interface contract.

## Open identification and event-contract questions

The accessible **Ratan Action and LMS Event Matrix** source leaves the following questions unanswered:

- What does LMS stand for?
- Which team or organisation owns LMS?
- Does LMS receive outbound events from Ratan, send commands or acknowledgements to Ratan, or support both directions?
- What interface and event-processing standards apply?
- Has the referenced 19 September 2023 workbook been superseded?
- Which individual Ratan actions, LMS events, payloads, directions, and processing obligations are defined by the workbook?

The **Ratan - LMS feed** source adds the unresolved relationship between its proposed `MessageSender` and `Stack Flow` behavior and any authoritative Ratan-to-LMS message-sender or stack-flow contract, as referenced by what is the authoritative ratan lms message sender and stack flow contract.

The **Ratan and LMS 50686** source does not resolve whether LMS and SAIL-LMS are the same system, related deployments, or distinct destinations.