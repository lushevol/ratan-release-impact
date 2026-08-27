---
type: entity
title: Cash Settlement Platform
created: 2026-08-23
tags: [cash-settlement, payment-processing, integration, deprecated, platform, indonesia, architecture, ratanone, microservices]
related: [stella, fmsre, amh, murex-2-11, cashflow-blotter, payment-date-override, cashflow-status-lifecycle, cash-settlement-dc-failover-strategy, deployment-profile, cluster, virtual-ip, cash-settlement-service-landscape, cash-settlement-capacity-planning-baseline, ratan, cashflow-lifecycle-service, ratan-cash-settlement-group-management-service, camunda-7, kafka, postgresql, redis]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/SFMRP - Cash Settlement Platform Integration（Deprecated）.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Active-Active to Active-Passive.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design.md"]
updated: 2026-08-23
---

# Cash Settlement Platform

The Cash Settlement Platform is described differently across the source documents:

- The deprecated SFMRP integration requirement describes it as a historical payment-processing component that receives cashflow events from [[stella]], persists enriched records to a payment lake, and owns lifecycle transitions after ingestion.
- The Cash Settlement System Design represents it as a RatanOne service landscape containing frontends, common services, BAU services, and CN-specific Cash Settlement services.
- The Indonesia 2026 Active-Active to Active-Passive architecture note identifies it as the deployment target for services operated across a primary and backup data centre.

These descriptions should not be treated as a single verified runtime architecture. The Cash Settlement System Design is a design inventory rather than a verified runtime architecture, while the SFMRP integration requirement is deprecated. Current component boundaries, data-store identity, API contracts, status semantics, deployment environments, data ownership, and operational ownership require validation against authoritative non-deprecated material.

## Historical responsibilities

The deprecated SFMRP integration requirement assigns the platform responsibility for:

- Persisting inbound cashflows and lifecycle versions to the payment lake.
- Materializing `PROJECTED` cashflows into `QUEUED` within the VD-5 window.
- Running STP/NSTP processing and supporting Settlement Ops maker/checker actions.
- Generating payment messages for [[fmsre]].
- Processing routing acknowledgement from [[amh]].
- Creating netting resultants, reversing netting on amendment, and performing payment splitting.
- Maintaining platform-owned child payments that are described as transparent to Stella.

These responsibilities are historical design evidence only. They do not by themselves establish the current service boundaries, interfaces, data stores, or ownership model.

## RatanOne service landscape

The Cash Settlement System Design represents the platform as a RatanOne service landscape containing:

- Frontends.
- Common services.
- BAU services.
- CN-specific Cash Settlement services.

The inventory includes domain-oriented services for:

- Netting.
- Settlement orchestration.
- Query.
- SSI stamping.
- Cashflow lifecycle management.
- Exceptions.
- MXG cashflow adaptation.
- Rules.
- Group management.

It also declares dependencies on the following workflow, messaging, database, cache, discovery, and observability technologies:

- [[camunda-7]]
- [[kafka]]
- [[postgresql]]
- [[redis]]
- ELK technologies

The source does not identify component ownership, interfaces, request flows, event flows, deployment environments, or data ownership. Existing pages such as [[ratan]], [[cashflow-lifecycle-service]], [[query-service]], [[netting-service]], and [[rule-service]] may be related, but the Cash Settlement System Design does not prove exact service identity.

## Indonesia deployment options

The Indonesia 2026 Active-Active to Active-Passive architecture note compares the following operating models for the platform's services across primary and backup data centres:

- A single [[deployment-profile]] with [[virtual-ip]] switching, intended to provide Active-Passive operation.
- Two deployment profiles for two [[cluster]]s, with isolated data centres and a possible Active-Active operating risk.

That architecture note compares possible deployment approaches but does not provide a component-level platform architecture. It does not establish whether the platform includes [[ratan]], Murex, FMRP, Solace, or other systems documented elsewhere in the wiki. This is separate from the Cash Settlement System Design's representation of the platform as a RatanOne service landscape.

The approved strategy, recovery objectives, state-replication model, and message-processing ownership remain unspecified in the Indonesia architecture note.