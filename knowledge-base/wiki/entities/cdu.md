---
type: entity
title: CDU
created: 2026-08-23
updated: 2026-08-23
tags: [CDU, trade-confirmation, notification, upstream-system, trade-data, ssi-stamping, system, downstream-system, uber, cash-settlement, confirmation, bcs, "trade confirmation", Kafka, testing, confirmation-status, trade-version, cashflow-stp, stella, trade-validation, auto-validation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/CDU Trade Confirmation Notification & Cashflow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade Strategic SSI Stamping Tech Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Trade Cashflow SSI Stamping on Uber Message.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Migrating BCS to Strategic Workflow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Mock testing data userguide.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Ratan Non Economic Cashflow Handling.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Confirmation & Cashflow STP.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/RATAN Settlement Control on Trade Validation.md"]
related: ["ratan", "scbml", "trade-confirmation-driven-cashflow-stp", "trade-cashflow-reference-linkage", "graphql-trade-snapshot-retrieval", "ratan-ssi-stamping", "does-cdu-and-graphql-snapshot-identity-hold-for-trade-id-and-major-version", "cdups", "uber", "ssi-stamping-service", "sabre", "bcs", "tds3", "bcs-cdu-match-status-confirmation", "bcs-strategic-workflow-migration", "kafka", "kafka-settlement-test-topics", "mock-settlement-test-data-generation", "stella", "cashflow-version-concurrency-control", "non-economic-cashflow-suppression", "what-is-the-authoritative-cdu-confirmation-status-contract", "trade-validation-cashflow-gating"]
---

# CDU

## Roles and source-system relationships

The deprecated *CDU Trade Confirmation Notification & Cashflow* functional requirement identifies CDU as the upstream notification source that sends trade affirmation or confirmation-status notifications consumed by [[ratan]].

The *Trade Confirmation & Cashflow STP* requirement names CDU as the provider of trade-confirmation status in the Stella trade-to-cashflow control described by [[trade-confirmation-driven-cashflow-stp]].

The *Mock testing data userguide* identifies CDU as the source system for the trade-confirmation status-message procedure used in testing.

The *Migrating BCS to Strategic Workflow* requirement identifies CDU as the current source of match status consumed by [[bcs]] cashflow processing. That source contrasts CDU match status with [[tds3]] trade information.

Separately, the SSI stamping technical design identifies CDU as the provider of the latest trade snapshot used for SSI stamping.

In the *Trade Cashflow SSI Stamping on Uber Message* requirement, CDU is named as a downstream consumer of SABRE's `uber` trade format. That requirement states that the SSI Stamping Service should return a post-stamped `uber` message to CDU.

## Trade confirmation notification processing

The CDU notification is expected to include sufficient identifiers for Ratan to locate the underlying cashflow or cashflows. The proposed linkage data includes:

- Trade ID
- Tracking Version
- Event ID
- A new Reference ID

The intended flow described by the deprecated functional requirement is:

```text
CDU trade confirmation notification
    -> Ratan identifies the related cashflow
    -> Ratan validates linkage and freshness
    -> Ratan releases the cashflow to STP or raises an exception
```

## Confirmation status and trade-version handling

The *Ratan Non Economic Cashflow Handling* requirement identifies CDU as the confirmation-status notification component. That requirement states that CDU uses the latest trade ID and trade version when producing confirmation-status notifications.

It further states that CDU uses the latest trade version regardless of whether a trade amendment is economic or non-economic. Its illustrative scenario is:

- New trade booking: `T1 + V1`
- Non-economic amendment: `T1 + V2`
- Economic amendment: `T1 + V3`

This latest-trade-version principle is distinct from cashflow settlement eligibility. A cashflow may be suppressed from Ratan settlement visibility while CDU still references the latest trade version for confirmation status.

The same requirement expects Ratan to follow CDU's latest-version principle when driving cashflow STP. It does not define how CDU handles out-of-order, duplicated, or late confirmation messages, nor does it specify the authoritative version-comparison mechanism.

The *Trade Confirmation & Cashflow STP* requirement separately states that, for selected update-like Stella events, CDU is expected to confirm the latest trade major version. That source associates CDU confirmation with `Y` outcomes in its business-case matrix.

See [[cashflow-version-concurrency-control]] and [[non-economic-cashflow-suppression]].

## Stella trade-to-cashflow control

In the Stella trade-to-cashflow control described by [[trade-confirmation-driven-cashflow-stp]], the *Trade Confirmation & Cashflow STP* requirement identifies CDU as the provider of trade-confirmation status.

That source does not define CDU's expansion, ownership, authoritative upstream data source, interface, message contract, or the semantics of its confirmation states. These gaps are tracked in [[what-is-the-authoritative-cdu-confirmation-status-contract]].

## Proposed trade-validation role

The *RATAN Settlement Control on Trade Validation* requirement names CDU as part of a proposed Stella enhancement for auto-validation of SCF and LoanDepo trades.

That source does not define CDU's full name, ownership, implementation role, validation logic, effective date, or production status. The September 2024 enhancement is explicitly marked TBC and should not be treated as an approved capability. See [[trade-validation-cashflow-gating]].

## Testing role

The *Mock testing data userguide* instructs a tester to obtain a CDU message sample, replace identifiers with values from the target cashflow, and produce the result to:

```text
CDU_Trade_Confirmation_Process_In
```

The fields explicitly identified for replacement are:

```text
legalEntityFmId
counterpartFmId
tradeId
tradeVersion
```

That source does not specify the complete CDU message schema, required headers, confirmation-status values, or the evidence required to verify successful downstream event publication.

## BCS strategic-workflow migration

The *Migrating BCS to Strategic Workflow* requirement states that the Strategic Workflow migration must determine whether CDU remains the authoritative confirmation source or whether the target flow should use [[tds3]] or another source.

That source does not provide an interface contract, status mapping, or reconciliation evidence. It therefore does not establish whether CDU should remain authoritative in the target workflow.

## SSI stamping and trade snapshots

The SSI stamping design expects that a CDU snapshot can also be found through GraphQL using the same `Trade_Id` and `Trade_Lake_Trade_Major_Version`.

That design does not establish CDU as a system of record or define a synchronization, reconciliation, or minor-version selection contract with GraphQL. This assumption is tracked in [[does-cdu-and-graphql-snapshot-identity-hold-for-trade-id-and-major-version]].

## `uber` message delivery

The *Trade Cashflow SSI Stamping on Uber Message* requirement describes the SSI Stamping Service returning a post-stamped SABRE `uber` message to CDU.

That source also describes delivery to [[cdups]], including a possible Solace channel. The relationship between CDU and CDUPS is unresolved: CDU and CDUPS should not be treated as the same system until their ownership and message-consumption roles are confirmed.

## Scope and implementation status

The deprecated functional requirement does not establish that the CDU notification interface or the proposed Reference ID control was implemented in production. The document is explicitly deprecated.