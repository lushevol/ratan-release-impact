---
type: entity
title: DQSL
created: 2026-08-22
updated: 2026-08-24
tags: [dqsl, query-system, cashflow-splitting, integration, notification, ssi, static-data, cash-settlement, dependency, api, graphql, ratan, counterparty-data]
related: [cashflow-splitting, split-cashflow-downstream-integration, ssdr, cashflow-logical-model, ssi-plus, ratan, ssi-effective-date-selection, bpsi, cash-settlement-dependent-service-failure, query-service, sci, ratan-counterparty-data-integration, fm-data-platform-dqsl-rt]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md", "RATAN/RATAN -Interfaces/Ratan and BPSI-51437 & SCI-14768 (via DQSL 51129).md"]
---

# DQSL

## Overview

DQSL is described in the documented RATAN counterparty-information retrieval flow as an intermediary API layer. In that flow, RATAN sends DQSL a GraphQL request when trade details require counterparty information.

The source describing this flow does not provide a DQSL endpoint, GraphQL schema, operation name, request payload, response mapping, or failure contract.

## Cashflow-splitting integration

According to the Cashflow Splitting UAT, DQSL is a query and integration system expected to return split information to surrounding systems.

The UAT records this capability as `Done` and names Zugang as the tester, but the result field is blank. The record therefore documents the intended capability without providing explicit formal acceptance evidence.

## SSI-stamping notification

According to the SSI Stamping Flow requirement, DQSL is the notification channel through which [[ssi-plus]] communicates new and updated SSI records to the Elastic Search layer consumed by [[ratan]].

The requirement states that an SSI update notification causes RATAN to identify impacted cashflows and re-trigger SSI stamping using current Elastic Search records. It does not define event correlation, delivery guarantees, retries, idempotency, or the exact population of impacted cashflows.

## RATAN counterparty-information flow

According to the RATAN/BPSI/SCI source, the described flow is:

1. RATAN sends DQSL a GraphQL request when trade details require counterparty information.
2. DQSL invokes [[bpsi]] to obtain authentication required for access to [[sci]].
3. SCI data is returned to RATAN.
4. RATAN caches the SCI data and uses it in the trade-blotter view.

This flow is specific to the counterparty-information retrieval integration and is separate from the cashflow-splitting and SSI-stamping roles described above.

[[fm-data-platform-dqsl-rt]] may be related to the DQSL named in this flow, but the source does not establish that they are the same component. That relationship remains unverified.

See [[ratan-counterparty-data-integration]] and [[what-is-the-authoritative-ratan-dqsl-bpsi-sci-counterparty-api-contract]].

## Dependency and exception handling

According to the Exception Handling technical design, DQSL is a dependency route through which Ratan calls [[bpsi]] for FMCODE-related data.

The same source assigns DQSL PSS shared responsibility with RATAN PSS and BPSI PSS for restoring the BPSI API path.

For Query Service incidents involving an I/O error while fetching `/counterPartyDetails` data, the technical design directs investigation of service functionality to DQSL PSS.