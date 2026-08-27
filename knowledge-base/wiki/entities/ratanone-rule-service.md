---
type: entity
title: ratanone-rule-service
created: 2026-08-22
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker Tech Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Investigate SCI Response Data - eueNotice.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker go-live checklist.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker go live checklist.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/[Deprecated", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Global Rule Sync From Ratan GDC to Ratan ID.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan-rule-service reconstruction for rule-engine.md"]/Rule Service Migration.md"]
tags:
  - microservice
  - rule-engine
  - nstp
  - hard-blocker
  - ratan
  - trade-validation
  - regulatory-controls
  - rule-service
  - backend-service
  - cash-settlement
  - rules
  - solace
  - synchronization
  - service
  - migration
  - RatanOne
related:
  - ratan-one
  - rule-service
  - resultant-hard-blocker-stamping
  - swap-agent-coupon-interim-mtm-hard-blocker
  - ratan
  - ratanone-trade-service
  - ratanone-data-ambassador
  - eue-notice-trade-validation-rule-dependency
  - what-is-the-rule-engine-behavior-when-lds-eue-notice-is-absent
  - hard-blocker-exception
  - hard-blocker-go-live-checklist
  - swap-agent-hard-blocker
  - resultant-cashflow-hard-blocker-propagation
  - ratan-cash-settlement-netting-service
  - ratan-gdc
  - ratan-indonesia
  - solace
  - ratan-global-rule-synchronization
  - rule-sync-idempotency-and-version-ordering
  - deployment-profile
  - ratan-rule-service
  - ratan-suppression-service
  - rule-service-consolidation
  - database-backed-rule-loading
  - rule-service-domain-boundaries
  - ratanone
  - ratan-rule-engine
  - rule-maintenance-and-validation-pipeline
  - special-rule-processing
  - scbml
  - netting-service
---

# ratanone-rule-service

`ratanone-rule-service` is a Ratan back-end service and rule-management microservice.

The existing hard-blocker documentation describes it as constructing rule-engine requests for Ratan cashflows and evaluating RATAN validation rules. The deprecated Swap Agent analysis describes it as supporting the creation, approval, enabling, disabling, updating, and rejection of settlement rules.

A separate reconstructed technical design assigns the service responsibility for direct rule maintenance and rule evaluation or filtering for cash-settlement rule categories. That design covers `NSTP`, netting, suppression, and Swift Suppression rules. These responsibilities are presented by that source as a proposed or reconstructed design rather than as a complete normative specification.

Separately, the Global Rule Sync from Ratan GDC to Ratan ID design identifies `ratanone-rule-service` as the implementation scope for Proposal A Global-rule synchronization.

The archived Rule Service Migration design describes `ratanone-rule-service` differently: as the **proposed** consolidated destination for CN and BAU rule maintenance and validation. That archived proposal does not prove migration completion, current deployment status, target API compatibility, or production adoption.

It is listed as a required deployment dependency for the hard-blocker rule.

## Responsibilities in the reconstructed cash-settlement design

According to the reconstructed technical design, `ratanone-rule-service` is assigned responsibility for:

- Creating rules.
- Deleting rules.
- Changing rule status.
- Updating rule content.
- Evaluating or filtering validation results.

The covered rule areas are:

- `NSTP`
- Netting
- Suppression
- Swift Suppression

For `NSTP`, the UI supplies exception information in `metaData`.

The same source describes the service as returning either a filtered result or a success response after processing the relevant rules.

## Service boundary and processing flow

According to the reconstructed technical design:

1. A domain service converts [[scbml]] data into JSON.
2. The JSON is passed to `ratanone-rule-service`.
3. `ratanone-rule-service` returns a filtered result or a success response.
4. Special rules receive additional preprocessing before evaluation.

That source does not establish that `ratanone-rule-service` owns general cashflow lifecycle transitions. It also does not establish that [[netting-service]] owns rule maintenance.

## Archived rule-service migration proposal

According to the archived Rule Service Migration design, the proposed consolidated target would:

- Store rules in `ratanone_rule_service.ratan_rule`.
- Select rules using `business_flow` and `rule_type`.
- Receive BAU Suppression and Netting Rules from legacy services.

The same archived design explicitly excludes the following from the proposed target scope:

- Data Entitlement Rule
- Fields
- Frontend Validation Rules

It states that Profile Limitation remains within the Rule domain boundary.

See [[rule-service-consolidation]], [[business-flow-and-rule-type-classification]], and [[rule-service-domain-boundaries]].

## Global-rule synchronization

According to the Global Rule Sync design, `ratanone-rule-service` is responsible for:

- Identifying Global rules from rule-expression attributes.
- Selecting producer or consumer behavior through global deployment configuration.
- Sending and consuming synchronization messages through FM Solace.
- Maintaining the producer-side latest-event synchronization ledger.
- Tracking per-DC statuses and responses.
- Retrying failed or timed-out outbound records through `SyncFailedRetryer`.
- Exposing rule-synchronization status and targeted resend behavior to the FE.

The Global Rule Sync design refers to a Rule Synchronizer and `SyncFailedRetryer` as components, but does not define their package interfaces, persistence transactions, or restart-recovery behavior.

## Rule-management API

The deprecated Swap Agent analysis records local endpoints under `/v2/rules/action/` for:

- `create`
- `confirm`
- `disable`
- `enable`
- `update`
- `reject`

That local test demonstrated the following rule lifecycle:

- `PROCESSING` transitioned to `LIVE`.
- A rule transitioned through `DISABLED` and back to `LIVE`.
- A rule update was recorded as `UPDATE_PENDING` before confirmation.

The local evidence supports API behavior only. It does not confirm that any tested rule ID, rule version, or operation level is deployed in production.

The reconstructed technical design contains a response example, but that example is evidence of a proposed or reconstructed contract rather than a complete normative API specification. The following contract details remain undocumented in that source:

- Request signatures
- Authentication
- Authorization
- Error behavior
- Idempotency
- Timeouts
- Concurrency behavior

The reconstructed design's statement that the service can delete rules is separate from the deprecated Swap Agent analysis, whose listed local endpoints do not include a `delete` operation.

## Hard-blocker processing

The existing hard-blocker design states that the service adds `Cashflow__Is_Hard_Blocker` to `EnhancedFact`. This makes the resultant hard-blocker marker available for NSTP rule evaluation and enables a hard-blocker rule to identify a resultant based on inherited component risk, rather than using a complex component-string expression.

Separately, the deprecated Swap Agent analysis states that the service was expected to evaluate `Cashflow__Component_Strategy_Payment_Hard_Blocker` through `EnhancedFact.java`.

These statements come from different source documents and describe documented hard-blocker behavior at different levels:

- The existing hard-blocker design describes stamping the resultant marker.
- The deprecated analysis identifies the expected hard-blocker field and implementation class.

The hard-blocker design cites a pull request and pipeline as implementation evidence, but does not demonstrate that the relevant version was deployed or active.

## Required deployment version

The hard-blocker go-live checklist lists the following required deployment version:

| Service | Version |
| --- | --- |
| `ratanone-rule-service` | `2.3.11` |

The checklist does not record whether version `2.3.11` was deployed or validated.

## Relationship to `ratan-rule-service`

The deprecated Swap Agent analysis distinguishes `ratanone-rule-service` from `ratan-rule-service`.

According to that analysis, `ratan-rule-service` implements:

- `HARD_BLOCKER` exception categorization.
- Submit validation.
- Approve validation.

These responsibilities are attributed to `ratan-rule-service` and should not be generalized as responsibilities of `ratanone-rule-service`.

## Trade-validation rules

A separate investigation identifies two `TRADE_VALIDATION` / `FO_SUPERVISION` rules that test:

```text
Custom__CounterParty__Legal_Entity_Main_Profile__LMP_Dodd_Stat__Lds_Eue_Notice != "Y"
```

The documented rules apply to qualifying [[murex]] and [[blade]] trades.

That investigation also states that `ratanone_rule_service.ratan_scbml_field_rest_config` is used when a counterparty field is absent, while separately noting “v3 validate/ no impact”.

The relationship between that fallback configuration, the versioned validation route, and the trade-validation invocation remains unconfirmed.