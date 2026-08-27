---
type: entity
title: Murex 2.11
created: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/2025 Target.md", "Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/FXO Mini Trade Migration - Ratan Cash Settlement - RunBook (2026-08-15 weekend).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/Cashflow Logical Model Fields & Data Store.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/LifeCycle/Cashflow & Payment cashflow id management.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Ops weekly session/2022-11-16.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Trade Migration - Settlement Process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SUSPENDED vs PROJECTED cashflow status in Ratan.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity STP.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Nostro SSI/Nostro Static Golden Source.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Rounding Rule - Tactical solution for H1 2024 Cashflow Migration.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Backward Workflow Design.md"]
tags: ["platform", "legacy-system", "cash-settlement", "Murex", "settlement", "cashflows", "FXO", "trading-platform", "cashflow-source", "upstream-system", "cashflow-id", "derivatives", "china", "cn", "trade-migration", "cashflow-suppression", "publishing", "version", "inter-entity", "trading-system", "settlement-system", "nostro-static-data", "fmo", "trade-booking", "cashflow-source-system", "vostro-ssi", "downstream-system", "settlement-status"]
related: ["cash-settlement-2025-roadmap", "cash-settlement-re-platforming", "cashflow-migration", "ratan", "auto-netting", "pre-rule-migration", "fxo-mini-trade-migration-ratan-cash-settlement", "ratan-settlement", "high-risk-nstp-rule", "trade-cashflow-reconciliation", "stella", "scbml", "tds3", "cashflow-logical-model", "ratan-cashflow-id-management", "murex-to-ratan-rule-replication", "murex-korea", "fmrp", "opics", "murex-2-11-cn-derivative-settlement", "murex-2-11-field-20-format", "agency-payment-identification", "pre-trade-settlement-accounting-exceptions", "cn-trade-migration", "murex-stella-cashflow-reconciliation", "murex-2-11-cashflow-suppression", "suspended-versus-projected-cashflow-status", "stella-ratan-cashflow-filtering", "razor", "murex", "inter-entity-cashflow-stp", "settlement-day-2", "nostro-static-golden-source", "nostro-centralization", "automated-cashflow-rounding", "ssi-plus", "vostro-ssi-redundancy-and-product-scoping", "cfi-code-mapping-for-murex-vostro-ssi", "cashflow-status-write-back", "backward-workflow-design", "adaptor", "cash-settlement-platform"]
updated: 2026-08-23
---
# Murex 2.11

Murex 2.11, also written as `MUREX2.11` in the Nostro static-data requirement and as `Murex2.11` in the backward-workflow design, is an upstream trading-platform and cashflow source system for [[ratan]] settlement processing. In the China derivative-product context recorded during the 16 November 2022 CN Settlement Ops session, it was discussed for trade booking and settlement processing.

In the proposed [[cn-trade-migration]], Murex 2.11 is described as the legacy CN trade and cashflow source.

The Inter Entity STP requirement explicitly identifies Murex 2.11 as the source platform and version for the proposed [[inter-entity-cashflow-stp]] requirement. That requirement is associated with Azure DevOps Story 6473009, **STP SCB counterparty cashflows**.

The backward-workflow design separately names Murex2.11 as a downstream target for cashflow-status synchronization from Ratan. These upstream and downstream roles apply to different documented flows and should not be generalized into a single system-direction claim.

## Source Scope and Boundaries

This page preserves distinct source scopes:

- The cashflow-ID requirement describes conversion of Murex 2.11 source cashflow IDs to [[ratan]] IDs.
- The 16 November 2022 CN Settlement Ops session describes China derivative settlement operations, including Field 20 references, payment processing, and exceptions.
- The CN trade-migration settlement-process source describes an assumed cutover design and migration-weekend cancellation handling.
- The suspended-versus-projected cashflow-status source describes publishing and suppression criteria for cashflows routed to Ratan, Razor, Razor FX, Razor ALM, or dedicated payment queues.
- The Inter Entity STP requirement is limited to inter-entity cashflows from Murex 2.11 classified as MX cashflows.
- The Nostro Static Golden Source requirement describes MUREX2.11 as one of the systems that currently maintains or requires Nostro, over-account, and suspense-account static data. It discusses a proposed golden-source model for reducing duplicated maintenance across such systems.
- The rounding-rule source describes Murex 2.11's BAU rounding behavior and the tactical rounding requirement for H1 2024 cashflow migration.
- The Vostro SSI source describes Murex 2.11 as the comparator platform for the BAU SSI product catalogue in the Vostro SSI analysis referenced by RATAN-10123.
- The backward-workflow design describes a separate Ratan-to-Murex2.11 cashflow-status synchronization path through an Adaptor.

The Inter Entity STP requirement does not imply that the same STP behavior applies to other Murex versions, non-MX flows, or Murex cashflows generally.

The CN derivative-session source does not establish behavior for [[murex-korea]], RATAN, or other Murex deployments. The cashflow publishing and suppression source does not establish whether Murex, [[stella]], or Ratan is authoritative when suppression rules overlap or are deployed with different versions.

The Nostro Static Golden Source requirement does not define a MUREX2.11 interface or confirm MUREX2.11's migration sequence to RDM-distributed data.

The rounding-rule source concerns the tactical H1 2024 cashflow-migration implementation and does not establish that Murex 2.11 is the strategic rounding owner.

The Vostro SSI source does not establish that alignment of product catalogues implies identical Vostro SSI-selection semantics across product classifications such as `MXG IRD`, `MXG IRD IRS`, `MXG IRD CS`, and `MXG SCF`.

The backward-workflow design does not establish that the Ratan-to-Murex2.11 status-synchronization path is the same as the Murex-to-Ratan cashflow-source flow. It also does not establish the detailed technical contract for the Adaptor-to-Murex integration.

## Cashflow and Rounding Flow

The rounding-rule source describes the current BAU flow as Ratan taking a rounded Murex amount and sending it to Razor. For the H1 release, Ratan is instead required to receive the original Murex amount and apply the agreed currency-specific rounding rule.

The Murex 2.11 input is supplied in MxML from:

```text
/MxPayML/flowAmount
```

Murex 2.11 BAU rounding behavior is the reference for the tactical Ratan implementation for [[stella]] cashflows; it is not identified as the new strategic rounding owner.

## Cashflow ID Conversion

In the cashflow-ID requirement, Murex 2.11 source cashflow IDs have a maximum length of 10.

[[ratan]] converts a Murex 2.11 ID to a 12-character Ratan ID by prepending `M` and zero-padding between the prefix and source value.

```text
1234567    -> M00001234567
1234567890 -> M01234567890
```

This rule is specifically scoped to Murex 2.11. The source does not define treatment of non-numeric, empty, already-prefixed, or overlength source values.

## Cashflow Publishing and Suppression

According to the suspended-versus-projected cashflow-status source, Murex 2.11 supplies publishing and suppression criteria for cashflows routed to:

- [[ratan]]
- Razor
- Razor FX
- Razor ALM
- Dedicated payment queues

The criteria cover:

- Internal funding
- Dummy portfolios
- Non-deliverable currencies
- FXD exceptions
- Auto-suppression
- CPN eligibility
- Trade status
- Entity scope
- Amounts
- Dates
- Dedicated queues

That source identifies gaps between these criteria and Ratan, including the absence of Ratan-side CPN eligibility logic.

## China Derivative Settlement Operations

For the scope recorded in the 16 November 2022 CN Settlement Ops session, Murex 2.11 behavior includes:

- Field 20 reference population.
- Payment and SWIFT generation.
- Manual client-requested payment splitting through [[opics]].
- Exception handling for missing SSI and upstream accounting failures.

### Known Issues and Open Scope

According to the CN Settlement Ops session:

- Agency-profile bookings may not generate payments in the China agent queue or SWIFT messages.
- Payment identification was described as portfolio-based, while Field 72 may identify agency payments.
- Auto split was not identified as a requirement for derivative products.
- Some `P2P` portfolios reportedly fail before payment-queue visibility because trade or settlement accounting is not generated.

See [[murex-2-11-cn-derivative-settlement]].

## CN Trade Migration and Cutover

According to the CN trade-migration settlement-process source's assumed cutover design, Murex 2.11 remains responsible for cashflows with VD on or before 10 May.

The same source states that Murex 2.11 may settle selected VD 13 May cashflows early on 10 May. This creates the overlap addressed by [[early-settled-cashflow-migration-handling]].

### Migration-Weekend Cancellations

According to the CN trade-migration settlement-process source, migration-weekend cancellation of Murex 2.11 trades produces reversal cashflows.

That source inconsistently calls for those reversal cashflows to be suppressed or held as NSTP; their authoritative Ratan handling is therefore open.

## Backward Workflow and Status Synchronization

The backward-workflow design names Murex2.11 as a downstream target for cashflow-status synchronization from Ratan. The documented integration path is:

```text
Ratan → Adaptor → Murex2.11
```

### External Technical Design Dependency

The Adaptor-to-Murex behavior is delegated to Section 2 of the external Confluence document titled:

```text
CN Settlement - Murex2.11 Technical Design - Derivative Strategy Projects
```

The supplied backward-workflow source does not reproduce that contract. Consequently, it does not establish Murex2.11 field names, accepted statuses, message cardinality, transport, validation, response, retry, or idempotency semantics.

## Inter-Entity STP Scope

The Inter Entity STP requirement explicitly identifies Murex 2.11 as the source platform and version for inter-entity cashflows classified as MX cashflows. It is associated with Azure DevOps Story 6473009, **STP SCB counterparty cashflows**.

This requirement is limited to that inter-entity scope and does not establish equivalent STP behavior for other Murex versions, non-MX flows, or Murex cashflows generally.

## Nostro and Account Static Data

According to the Nostro Static Golden Source requirement, MUREX2.11 is one of the systems that currently maintains or requires:

- Nostro static data
- Over-account static data
- Suspense-account static data

The proposed golden-source model is intended to reduce duplicated maintenance across systems that maintain or require this data. The requirement does not define a MUREX2.11 interface or confirm its migration sequence to RDM-distributed data.

## Vostro SSI Product Catalogue

In the Vostro SSI analysis referenced by RATAN-10123, Murex 2.11 is the comparator platform for the BAU SSI product catalogue.

That source asserts that the Murex 2.11 product catalogue aligns with [[ssi-plus]] catalogues for China and Global `CURR` and `IRD` security classifications. This assertion is not independently verifiable from the supplied document because the supporting screenshots and attached **Murex 2.11 CN Vostro SSI** dataset are unavailable.

The Vostro SSI source does not establish that catalogue alignment implies identical Vostro SSI-selection semantics across product classifications such as `MXG IRD`, `MXG IRD IRS`, `MXG IRD CS`, and `MXG SCF`.