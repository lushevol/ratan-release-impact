---
type: entity
title: RAZOR
created: 2026-08-22
updated: 2026-08-25
tags: ["system", "trade-lookup", "integration", "settlement-platform", "downstream-system", "cashflow-processing", "settlement-accounting", "reporting", "fmrp", "china", "RAZOR", "UAT", "Prime", "Islamic-settlement", "settlement-methods", "settlement", "accounting", "swift", "payment-splitting", "reference-implementation", "settlement-integration", "payment-messaging", "cash-settlement", "cashflow", "release", "fx", "dvp", "reference-system", "automation", "cutoff", "configuration", "qatar", "settlement-system", "nostro-static-data", "fmo", "account-normalization", "payments", "correction-and-reversal", "upstream-system", "acknowledgement", "source-system", "scbml", "fxu", "ratan", "fx-replication"]
related: ["cash-settlement-2025-roadmap", "ratan", "ratan-settlement", "cash-settlement", "straight-through-processing", "cashflow-exception-handling", "murex-to-ratan-cashflow-integration", "murex-cashflow-migration-to-ratan", "ebbs-settlement-accounting", "murex", "settlements-brp-prioritization", "prime-trade-migration", "fmsgw", "stella", "ebbs", "loaniq", "settlement-integration-static-data-readiness", "fmrp", "murex-2-11", "murex-2-11-cn-derivative-settlement", "is-auto-split-in-scope-for-fmrp-cn-settlement", "cn-trade-migration", "early-settled-cashflow-migration-handling", "netting-api-contract", "what-is-the-authoritative-razor-release-validation-for-netting", "suspended-versus-projected-cashflow-status", "fx-replication-to-razor", "stella-ratan-cashflow-filtering", "tds3", "auto-dvp", "ebbs-rta-notification", "rta-cashflow-validation", "release-cutoff-configuration", "manual-entity-go-live-static-data-controls", "what-are-the-authoritative-razor-release-cutoff-values-for-qatar-tanzania-and-bangladesh", "what-are-the-final-qatar-release-cutoff-and-ebbs-configurations", "nostro-static-golden-source", "nostro-account-normalization", "nostro-account-taxonomy", "ratan-versus-razor-nostro-representation", "rdm", "fmrp-stella", "released-settled-amendment-control", "cashflow-version-concurrency-control", "cashflow-status-write-back", "backward-workflow-design", "cash-settlement-platform", "cash-settlement-exception-handling", "cashflow-reinstatement-and-replay", "cash-settlement-ola-break-monitoring", "oscar", "scbml", "cashflow-status-change-event-contract", "fx-cashflow-status-write-back", "fxu", "ratan-tds3-trade-lake-integration", "ratan-fx-replication", "ratan-fmsgw-settlement-messaging"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/2025 Target.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/Cashflow Logical Model Fields & Data Store.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration.md", "Cash Settlement Home Page/Cash Settlement Home Page/Strategic Cash Settlements Features/Settlements BRP/Settlements BRP Prioritization.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Ops weekly session/2022-11-16.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Trade Migration - Settlement Process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Service - GUI & API intergration.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SUSPENDED vs PROJECTED cashflow status in Ratan.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall/Tranche2.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Nostro SSI/Nostro Static Golden Source.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Ratan & Stella cashflow integration.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Backward Workflow Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FX Replication Status Write Back.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design.md", "RATAN/RATAN -Interfaces/Ratan and SABRE (TDS3)-29126.md"]
---

# RAZOR

RAZOR is referenced across the available requirements as a settlement destination, downstream settlement platform, payment and Swift-processing system, integration or messaging dependency, DVP automation reference system, release-cutoff configuration source, settlement-accounting component, and—separately—as a team, system, or workstream in delivery records.

The **Backward Workflow Design** source identifies Razor as an upstream settlement platform that writes settlement outcomes back to [[ratan]]. Conversely, the **Exception Handling** source describes Razor as a downstream processing system in the Cash Settlement flow: Ratan sends cashflows to Razor and receives acknowledgements, negative acknowledgements, and status events. The **FX Replication Status Write Back** source separately identifies Razor as the sender of an SCBML `CashflowStatusChange` message.

The **Ratan and SABRE (TDS3)** interface overview also identifies RAZOR as a downstream recipient of selected RATAN outputs. These contexts are not necessarily evidence of one unified technical or organizational role.

## Documented RATAN, TDS3, and settlement routes

According to the **Ratan and SABRE (TDS3)** interface overview:

- The FX-replication route is `TDS3 → RATAN → RAZOR`; [[ratan]] applies filtering before forwarding intended trades to RAZOR.
- In the documented settlement lineage, RATAN sends onward to `RAZOR/FMSGW` after data has passed through `BCS Stella/Blade → FMRP Stella → TDS3 → Solace → RATAN`.

The interface overview does not define RAZOR's business function, ownership, transport protocol, message contract, acceptance rules, or whether it receives every applicable RATAN settlement flow.

## FXU accounting and Swift role

According to the **FXU Technical Design** source, RAZOR is the accounting system in Options 1 and 2 of the FXU integration design, and the Swift system in all three listed options.

| Option | Accounting | Swift |
| --- | --- | --- |
| 1 | RAZOR | RAZOR |
| 2 | RAZOR | RAZOR |
| 3 | RATAN | RAZOR |

This FXU option-specific allocation is distinct from the proposed China target-state accounting role described below. The FXU source does not describe RAZOR APIs, message contracts, or failure semantics.

## Settlement destination and relationship to Ratan

According to the **SUSPENDED vs PROJECTED cashflow status in Ratan** source, Razor is a settlement destination for cashflows excluded from Ratan processing. That source discusses replication from [[ratan]] and [[tds3]] into Razor, including:

- FX spot
- FX forward
- FX swap
- Selected PCD/DCD routing scenarios

Cashflows expected to settle in Razor are generally intended to be suppressed before or outside Ratan. In the amendment scenario described by that source, original Razor cashflows may be withdrawn while replacement `FX_DCD` cashflows are expected to settle in Ratan.

That source does not establish Razor as the authoritative owner of suppression status, or define reconciliation behavior when [[stella]], Ratan, and Murex rule versions differ.

This exclusion-and-replication context is distinct from the proposed target-state role for RATAN-eligible, non-precious-metal China cashflows, the FXU option allocations, and the route statements in the Ratan–TDS3 interface overview.

## Payment, status, acknowledgement, and backward workflow

The **Ratan & Stella cashflow integration** source describes Razor as the payment and Swift-processing system in the proposed FMRP flow. According to that source:

- [[ratan]] sends validated cashflows to downstream processing.
- Razor generates or returns `Released` and `Settled` status information.
- Ratan applies those statuses to the operational cashflow.
- Ratan may replicate the status information to [[stella]].

For amendments concurrent with release, the same source describes a correction-and-reversal flow in which Razor sends:

- `MT292/MT192` reversal messages
- `MT202/MT103` original or replacement payment messages

Separately, the **Backward Workflow Design** source identifies Razor as the named upstream settlement platform in the backward workflow. It states that Razor writes settlement outcomes back to Ratan and lists the following Razor-to-Ratan messages or statuses:

- `ACK/NACK`
- `RELEASED`
- `SETTLED`

That source identifies Razor as the origin of settlement outcomes, while Ratan is responsible for updating cashflow state and synchronizing downstream. Ratan’s documented update payload supports `RELEASED` and `SETTLED`; no payload for `ACK` or `NACK` is provided.

The **Exception Handling** source provides a more specific exception-handling assertion: a Razor NACK moves a cashflow to `FAILED`. OPS can reinstate the cashflow for another processing attempt or manually book it in [[oscar]].

The **Backward Workflow Design** source does not define the precise semantics of `ACK` or `NACK`, including whether they are transport acknowledgements, business responses, or cashflow states. This remains distinct from the **Exception Handling** source’s stated NACK-to-`FAILED` behavior. The backward-workflow source also does not specify Razor’s transport protocol, endpoint, retry behavior, or message contract beyond the listed status names.

Likewise, the **Ratan & Stella cashflow integration** source does not define a complete Razor interface, message schema, retry policy, or status-authority contract. Its status-flow and amendment behavior does not resolve the separate suppression, replication, or settlement-destination questions described in [[suspended-versus-projected-cashflow-status]].

## SCBML status-change message evidence

According to the **FX Replication Status Write Back** source, Razor is the sender of an SCBML `CashflowStatusChange` message. The sample in that source assigns the following values:

| Message element | Sample value |
|---|---|
| Cashflow ID | `373670953` |
| Linked trade ID | `330134747` |
| Version-like `id` | `1` |
| `messageSender` | Razor |
| Sender domain | `FM` |

This is message-level evidence of Razor acting as a source or sender for a cashflow-status change. It does not establish Razor’s broader architecture, ownership, delivery channel, relationship to a specific Cash Settlement consumer, complete SCBML schema, transport contract, retry behavior, or status-authority model.

## OLA-break handling

According to the **Exception Handling** source, a Ratan-to-Razor OLA break leaves a cashflow in `READY+Pending Ack`. The source proposes:

- IMS-based alerting
- Potential manual replay from the cashflow blotter

These are proposed handling measures; the source does not establish a final alerting implementation, replay mechanism, or operational runbook.

## Settlement accounting and reporting role

According to the **Settlement - Murex 2.11 Cashflow Integration** source, Razor is the proposed target-state component for settlement accounting and related downstream reporting for RATAN-eligible, non-precious-metal China cashflows.

That source assigns non-precious-metal NET/GROSS, SWIFT, and settlement-accounting processing to [[ratan]] and Razor. It distinguishes this from Murex, which retains:

- Trade-accounting output to Aspire
- Precious-metal BAU settlement accounting

For flows routed to RATAN, Murex is expected to suppress FMSRE, Aspire, and EBBS settlement-accounting output.

The final accounting model and complete reporting ownership require confirmation. See [[ebbs-settlement-accounting]] and [[which-murex-payment-reports-move-to-razor-ratan-or-remain-for-precious-metals]].

## Nostro static-data role

According to the **Nostro Static Golden Source** source, RAZOR currently maintains:

- Nostro static data
- Over-account static data
- Suspense-account static data
- Suspense settlement means
- EBBS account information in `TABLE#DATA#SITRN_DBF`
- A Bridge Account Number through a lookup table

The source demonstrates that RAZOR account-number representations differ from NAMS values. The proposed centralized Nostro model must preserve RAZOR-specific representation and lookup requirements and must not treat RAZOR values as interchangeable with NAMS source values.

The source’s proposed model makes RAZOR a downstream consumer of the Nostro model distributed by [[rdm]]; it does not establish that RAZOR’s existing account representation is the golden-source representation.

## Role in the cashflow logical model

According to the **Cashflow Logical Model Fields & Data Store** source, Razor is the downstream settlement platform referenced by the Ratan cashflow logical model.

Ratan retains Razor-related operational information, including:

- Cashflow sub-state
- Sub-state updater
- Cashflow type

For a Negative Acknowledgement event, Razor is stated to send the Murex error message, which is mapped to `Cashflow.Exception_Reason`.

The cashflow logical-model source also links settlement-routing data held by Ratan to Razor processing, including:

- The Ratan STP indicator
- STP cutoff handling
- Value-date enrichment used for settlement instructions

## Release-cutoff configuration

The **Go live checklist for Manual Entities—Overall** source identifies Razor as the source of the Currency, Shifter, Time, and Timezone values used for release-cutoff configuration for Qatar, Tanzania, and Bangladesh.

The checklist does not contain the actual Razor values, configuration keys, effective dates, or deployment evidence.

The separately generated **Tranche2** checklist specifically identifies Razor as the source of Qatar’s currency, shifter, time, and timezone values. That source does not record the effective values drawn from Razor or confirm their deployment in Ratan. The Qatar dependency remains open in [[what-are-the-final-qatar-release-cutoff-and-ebbs-configurations]].

See also [[what-are-the-authoritative-razor-release-cutoff-values-for-qatar-tanzania-and-bangladesh]].

## Auto DVP reference behavior

According to the **Auto DVP (eBBS)** source, Razor is an existing DVP automation system used as a behavioral reference for RATAN Auto DVP.

The source describes Razor as:

- Validating EBBS references across Narration fields
- Validating receipt information
- Using a contract identifier to locate the linked pay cashflow
- Filtering duplicate RTAs by narration

The source also reports that Razor:

- Excludes the high-volume India `CorporateFinancial` topic
- Does not use value date as a matching condition for some African cases

These observations are comparator evidence only. They are not automatically requirements for RATAN Auto DVP or any other system.

## Netting release controls

According to the **Netting Service - GUI & API intergration** source, Razor is the downstream system relevant to RATAN netting release controls.

The netting requirement states, as **TBC**, that neither the current nor a previous component cashflow version should have been sent to Razor before netting proceeds. It does not define:

- Whether this is a mandatory backend block
- How send history is established
- Which Razor acknowledgement or status is authoritative

The requirement also distinguishes resultants retained in RATAN from resultants released or settled downstream. A released or settled resultant is reversed through a newly generated Withdrawal event rather than simply being marked `Dead`.

See [[what-is-the-authoritative-razor-release-validation-for-netting]].

## CN trade migration settlement process

According to the **CN Trade Migration - Settlement Process** source, Razor is the settlement integration or messaging dependency referenced by the CN migration requirement.

The proposed batch operation that moves selected [[stella]] cashflows from `PROJECTED` to `SETTLED` must be status-only. It must not:

- Initiate settlement through Razor
- Send Razor messages

This batch-operation constraint is specific to the CN trade migration requirement. It does not replace or generalize the proposed target-state settlement-accounting role for RATAN-eligible, non-precious-metal China cashflows.

## Q4 2023 integration and accounting delivery involvement

According to the **2023-Q4 Analysis** source, RAZOR was a major integration and accounting dependency in the Q4 2023 Cash Settlement delivery plan.

The source records RAZOR involvement in:

- Receiving FX trades from [[ratan]]
- Cashflow-status writeback to [[stella]] for hard-block scenarios
- EBBS and non-EBBS feed design
- EBBS account mapping
- Lifecycle testing and investigation of missing cashflow-status updates
- [[loaniq]] and LMS integration testing

The FX-trade-feed requirement was reported as finalized on 2023-11-20. Earlier updates in that source identified expiry-event synchronization between STELLA and RAZOR as an open question.

The source does not establish final ownership or production status for RAZOR–STELLA lifecycle and expiry-event handling.

## CN Settlement Ops reference behavior

The CN Settlement Ops session dated 2022-11-16 references Razor as an existing BAU example for payment splitting and Field 20 prefix configuration.

According to that session:

- Payments exceeding predefined thresholds may be automatically split.
- Applicability is limited to particular countries and currencies.
- Threshold static data is defined at currency level.
- Post-split payments carry a parent-payment linkage in SWIFT Field 72.
- The session referred to an `FX` prefix in Razor as an analogy for a potential FMRP Field 20 prefix.

This reference behavior is not a requirement for [[murex-2-11]] derivative settlement. The meeting stated that no Murex 2.11 derivative auto-split requirement had been identified.

## Prime, CPN, and settlement-method work

According to the **Settlements BRP Prioritization** source, RAZOR is identified as a team, system, or workstream supporting:

- Prime UAT
- Prime new-event analysis
- CPN analysis and design
- Settlement-method analysis
- Islamic UAT support

That source does not distinguish whether RAZOR is an application, delivery team, or programme name. This characterization is separate from the settlement-platform role described in the cashflow and Murex integration sources, and its exact organizational and technical role requires confirmation.

## Recorded trade-lookup issue

The **2025 Target** source mentions RAZOR as a trade-lookup source in a Sprint 2 issue within the [[cash-settlement-2025-roadmap]].

The source labels the following item as released:

> ND IRS issue - Trade ID looked up RAZOR trade

This indicates that a Trade ID lookup incorrectly or unexpectedly resolved to a RAZOR trade. The source does not provide the defect mechanism, expected matching behavior, remediation, test evidence, affected environment, or further release details.

## Evidence boundary

The available sources do not provide a broader unified description of Razor’s purpose, architecture, ownership, or supported products beyond the distinct contexts documented above.

In particular:

- The Ratan–TDS3 interface overview documents selected routes and Ratan filtering but does not define RAZOR’s business function, ownership, protocol, contract, acceptance rules, or full settlement-flow coverage.
- The settlement-destination and replication source does not establish authoritative suppression ownership or reconciliation behavior among Stella, Ratan, and Murex.
- The FMRP and backward-workflow sources do not define a complete Razor interface, message schema, transport protocol, endpoint, retry policy, or status-authority contract.
- The backward-workflow source does not define `ACK` and `NACK` semantics or a payload for them.
- The FXU design identifies accounting and Swift-system allocations by option, but does not define RAZOR APIs, message contracts, or failure semantics.
- The Exception Handling source establishes NACK-to-`FAILED` behavior and proposes IMS alerting and potential blotter replay for OLA breaks, but does not establish final implementation details or operational procedures.
- The Murex 2.11 cashflow-integration source limits Razor’s proposed target-state accounting and reporting role to RATAN-eligible, non-precious-metal China cashflows; final accounting and reporting ownership remains to be confirmed.
- The Nostro static-data source describes a proposed downstream-consumer role for RAZOR and requires preservation of RAZOR-specific representations and lookups; it does not make those representations interchangeable with NAMS values or establish RAZOR as the centralized golden source.
- The release-cutoff checklists identify Razor as a configuration-value source but do not provide effective values, configuration keys, effective dates, or deployment evidence.
- The Auto DVP and CN Settlement Ops observations are comparator or BAU-reference evidence only, not automatically requirements for RATAN Auto DVP or Murex 2.11 derivative settlement.
- The netting send-to-Razor control is explicitly **TBC** and does not define its mandatory nature, send-history determination, or authoritative acknowledgement or status.
- The Q4 2023 delivery records do not establish final ownership or production status for RAZOR–STELLA lifecycle and expiry-event handling.
- The BRP-prioritization source does not establish whether RAZOR in its Prime, CPN, settlement-method, and Islamic-UAT references is the same technical component, a team, or a workstream.
- The recorded released trade-lookup issue does not describe its defect mechanism or remediation.