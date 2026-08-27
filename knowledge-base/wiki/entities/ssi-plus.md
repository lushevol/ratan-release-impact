---
type: entity
title: SSI+
created: 2026-08-22
updated: 2026-08-25
tags: [settlement-instructions, static-data, swift, cash-settlement, rma, data-quality, ssi, elastic-search, "SSI+", settlement-means, Nostro, ssi-plus, integration, downstream-system, lifecycle-management, settlement, standard-settlement-instruction, interface-50509, vostro, fmo-portal, tenant-integration]
related: ["korea-ssi-onboarding", "nostro-static-management", "swift-message-difference-acceptance", "murex-korea", "ratan-settlement", "mx211-cash-settlement-decommission", "client-settlement-automation-eligibility", "payment-and-cashflow-suppression-governance", "ratan", "murex", "nostro-static-data", "static-data-readiness", "swift-message-reconciliation", "fmswg", "amh", "ssi-data-quality-for-swift-generation", "settlement-integration-static-data-readiness", "dqsl", "ssi-effective-date-selection", "vostro-nostro-ssi-selection", "ssi-stamping-service", "ccy-pair-based-nostro-selection", "nams", "nostro-centralization", "nostro-stamping", "nostro-notification-and-refresh", "nostro-static-data-migration", "dormant-ssi-processing", "ratanone-stamping-service", "bcs", "what-is-the-authoritative-ssi-plus-inactivation-and-reactivation-contract", "what-is-the-authoritative-ssi-plus-nostro-message-contract", "ratan-ssi-stamping", "ssi-best-matching", "ssi-change-notification", "solace", "fmrp", "what-is-the-authoritative-ratan-ssi-plus-50509-interface-contract", "ratan-fmo-portal-tenant-integration", "fmo-portal"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/End to End Testing for Korea Migration.md", "Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/Settlement Touchpoints.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Murex and Ratan Swift Difference Review.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Production Issue - Swift Message.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Compatibility design for multiple entities.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Centralization.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Dormant SSI processing.md", "RATAN/RATAN -Interfaces/Ratan and SSI+ 50509.md", "RATAN/RATAN -Interfaces/Ratan(FMO Portal) and STAMP FSS LOANIQ SSI+ SSDR CES.md"]
---

# SSI+

## Overview

SSI+ is a settlement-instruction static-data system and control point referenced in cash-settlement documentation. Available sources describe it as supplying account, Nostro, and settlement-instruction data used for SWIFT-message generation, stamping, accounting queries, and downstream processing. The sources also describe SSI+ as influencing RATAN and Murex SWIFT generation.

The SSI Stamping Flow source describes SSI+ as the settlement-instruction static-data source used by [[ratan]] for Vostro and Nostro SSI selection and cashflow stamping. It states that SSI+ provides SSI records through Elastic Search and publishes notifications of new or updated SSI records through [[dqsl]].

The Compatibility Design for Multiple Entities source identifies SSI+ as the source for settlement-instruction data, including `Settlement_Instruction. Account.SCB_Nostro_Account_Type`.

The Nostro Centralization requirement positions SSI+ as the operational platform through which Data Ops is **expected** to create, amend, and close centralized Nostro static data. That requirement expects TP systems to integrate with and consume data from SSI+, making SSI+ the intended integration point for Nostro queries and static-data notifications.

The Dormant SSI processing design separately identifies SSI+ as the downstream SSI management system and intended consumer of SSI-use information in a proposed dormant-SSI process.

These statements reflect different source contexts. The Nostro Centralization requirement describes an expected operating and integration model, while the Dormant SSI processing design describes a proposed lifecycle process. The SSI Stamping Flow and Compatibility Design sources do not establish the authoritative SSI+ data model, its ownership, or the complete static-data schema or authoritative query interface.

## FMO Portal tenant status

The *Ratan(FMO Portal) and STAMP FSS LOANIQ SSI+ SSDR CES* source lists SSI+ as a tenant in the FMO Portal integration overview. Its documented status is `Online`.

The source does not define the status criteria or establish whether `Online` means production-ready. It also does not provide tenant-specific interface, ownership, or operational details.

## RATAN interface 50509

The *Ratan and SSI+ 50509* source describes SSI+ as the centrally maintained source of Standard Settlement Instruction (SSI) information used by RATAN under interface **50509**.

According to that source, SSI+ supports RATAN through two channels:

- SSI+ receives real-time API lookups from RATAN's SSI+ ES-cluster integration to identify a matching SSI record for an incoming cashflow.
- SSI+ publishes real-time SSI-record change notifications to RATAN through [[solace]] when records are updated, added, or deleted.

RATAN uses SSI data returned by SSI+ to perform [[ratan-ssi-stamping]] on cashflows. The matching attributes stated in the source are:

- Booking-entity FMID
- Counterparty FM code
- Currency
- CFI code

The interface-50509 source assigns SSI+ PSS responsibility for:

- Monitoring notification processing, API availability, and agreed response time.
- Informing RATAN PSS about planned downtime outside the greenzone.
- Informing RATAN PSS about unexpected outages.

The exact API and messaging contracts remain undocumented in the available interface-50509 source. See [[what-is-the-authoritative-ratan-ssi-plus-50509-interface-contract]].

Other sources do not establish an approved SSI+ interface with [[ratan]]. This limitation should be kept separate from the interface-50509 source's description of the RATAN integration.

## Expected Nostro integration responsibilities

The Nostro Centralization requirement describes the following expected SSI+ responsibilities:

- Provide Nostro data for stamping and accounting queries.
- Emit or expose lifecycle events for `New`, `Update`, and `Delete`.
- Support downstream refresh of Nostro data in TP systems.
- Participate in migration and data-format standardization.

That requirement does not define:

- Query API signatures.
- Event payloads or transport.
- Identifier formats.
- Mapping rules.
- Delivery, replay, ordering, or idempotency guarantees.
- Delete behavior for active and historical cashflows.
- NFR targets.

These gaps are tracked in [[what-is-the-authoritative-ssi-plus-nostro-message-contract]].

## SSI data and effective-date handling

According to the SSI Stamping Flow source, SSI+ source fields support settlement-instruction enrichment, including:

- Branch
- Currency
- CFI code
- Account details
- Agent details
- Payment method
- Effective-date attributes

For future-dated changes, that source states that SSI+ makes both the old end-dated record and the new start-dated `_ED` record available until the old record is removed and the new record is renamed.

See [[ssi-effective-date-selection]] and [[vostro-nostro-ssi-selection]] for related selection context.

## Settlement-means design use

The Compatibility Design for Multiple Entities source uses settlement means `FXBRREC` as a condition for the single Vostro path:

```text
/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction[scb:partyReference/@href='party2']/scb:settlementMeans/scb:settlementAccountNo
```

## Role in SWIFT generation and reconciliation

The Murex and Ratan SWIFT difference review attributes differences in BICs, account numbers, agent fields, and field 72 content to SSI+ configuration or data quality in multiple samples.

SSI+ differences must be separated from RATAN application-logic defects during [[swift-message-reconciliation]]. The review does not provide evidence that every requested SSI+ correction was completed and replay-verified.

See [[ssi-data-quality-for-swift-generation]] for data-quality dimensions relevant to generated SWIFT validity.

### Production evidence

The Production Issue - Swift Message source identifies two SSI+-related failures:

- An account required for an MXN MT103 beneficiary field `59` was unavailable in SSI+.
- Data associated with `Has_Cash_Custodian_Account` caused malformed MT202 field `57D` content. SSI+ was asked to correct SSI ID `43262410` in ES for cashflow `N00000014342`.

The latter issue was marked **Open** in the source. The evidence does not determine whether its cause was incorrect SSI data, flawed serialization of the flag, or both.

### Tranche 2 investigation

The Murex and Ratan SWIFT difference review identifies a Tranche 2 investigation involving ten cashflows with field `58A` differences. It names SSI ID `74663620` and assigns Sumita and Pradeesh to check the SSI+ record.

### Korea migration testing

The Korea migration end-to-end testing source documents an accepted SWIFT comparison difference in which Vostro information in SSI+ differed from Murex Korea. It also records a case in which a `:58A:` account was absent from SSI+.

A user accepted the difference, but the source does not identify the approver, define the production scope, or assess payment and compliance risk.

See [[korea-ssi-onboarding]] and [[swift-message-difference-acceptance]] for the corresponding configuration and reconciliation context.

## Proposed settlement-touchpoint uses

The MX2.11 decommission settlement-touchpoints source describes proposed SSI+ uses, including:

- RMA-related setup
- Beneficiary-name character controls
- Mandatory currency-information capture
- TPP flagging
- Selection of an SSI from multiple candidates

These are proposed uses described by that source. They do not establish the authoritative SSI+ data model, ownership, or an approved interface with [[ratan]].

## Dormant SSI processing

The Dormant SSI processing design intends SSI+ to receive information about recently used SSIs so that SSIs unused for 24 months can be marked inactive. Within that proposed process, SSI+ is described as the downstream lifecycle owner or status-update target.

The design does not define:

- An SSI+ API, file, or message contract.
- Whether SSI+ consumes BCS data, FMRP data, or a consolidated cross-flow feed.
- The precise 24-month cutoff calculation.
- Idempotency, retries, audit records, reconciliation, or error handling.
- Reactivation behavior when an inactive SSI is used again.

These unresolved lifecycle controls are tracked in [[what-is-the-authoritative-ssi-plus-inactivation-and-reactivation-contract]].

### Inputs to the proposed process

The Dormant SSI processing source describes a daily BCS endpoint:

```text
GET /api/v1/cashflows/ssi/{paymentDate}
```

The endpoint returns cashflow-ID and SSI-ID pairs. Historical use evidence is also calculated from query-model data and BCS stamping tables as part of [[dormant-ssi-processing]].

The lifecycle role and inputs in this section are specific to the Dormant SSI processing design and do not, by themselves, establish a general SSI+ interface or authoritative ownership model.