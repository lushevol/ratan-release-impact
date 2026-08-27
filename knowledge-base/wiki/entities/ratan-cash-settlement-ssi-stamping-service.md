---
type: entity
title: ratan-cash-settlement-ssi-stamping-service
created: 2026-08-22
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Code Concurrent Issues.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Cashflow Dedicated Nostro Stamping Design(like RFI STRATEGY etc.).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Change List and API.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Dedicated Nostro Stamping Design--deprecated.md"]
tags: ["ratan", "ssi", "nostro", "vostro", "stamping", "service", "ssi-stamping", "concurrency-review", "cash-settlement", "maker-checker", "settlement"]
related: ["ratan", "ssi-stamping-hierarchy", "ssi-dual-blind-input", "payment-release-exception-orchestration", "ssi-stamping-service", "nostro-refresh-command", "ssi-exception-command", "scroll-query-and-publish-processing", "dedicated-nostro-stamping", "portfolio-currency-nostro-selection", "001-implement-rfi-selection-in-ssi-stamping-service", "rfi-nostro-stamping-based-on-portfolio", "dedicated-nostro-selection", "nostro-stamping", "ssi-plus", "nostro-records", "dedicated-nostro-match-conditions", "ratanone-static-data-service"]
---

# ratan-cash-settlement-ssi-stamping-service

## Service scope

`ratan-cash-settlement-ssi-stamping-service` applies Vostro and Nostro SSI stamping in the RATAN architecture.

The technical-design source also assigns the service:

- SSI exception generation and handling
- SSI-update handling

Its persistence inventory includes:

- Stamping records
- Current and legacy exception records
- Status snapshots
- Maker/checker requests
- Raw messages
- Stamped account records
- Outbox events
- Trade-stamping messages

The technical-design source establishes the service boundary but does not define SSI selection precedence or maker/checker authorization rules.

## Nostro lookup and RFI dedicated-Nostro selection

The Change List and API source states that `ratan-cash-settlement-ssi-stamping-service` changes its Nostro lookup when a cashflow references SSI. It additionally requires trade-stamp compatibility to be considered while querying Nostro data.

The RFI dedicated-Nostro design source identifies this service as the intended implementation point for dedicated-Nostro eligibility and selection. Under that source's proposal, the service must:

- Use portfolio-plus-currency lookup for eligible RFI KOR cashflows.
- Preserve standard lookup for all other cashflows.

That source proposes implementing the behavior in this service instead of in rule-engine, to minimize invocation dependencies and avoid changing rule-engine default behavior.

For NSTPSSI ad hoc maker/checker handling, the Change List and API source states that the service supports `fitNostro.nostroType` and `fitNostro.dedicatedPortfolio` for RFI cases.

Neither the RFI dedicated-Nostro design source nor the Change List and API source establishes matching precedence, fallback behavior, or ambiguity handling. The technical-design source likewise does not define SSI selection precedence or maker/checker authorization rules. These matters require clarification unless established by a separate source.

See [[dedicated-nostro-stamping]], [[portfolio-currency-nostro-selection]], and [[dedicated-nostro-selection]].

## Historical deprecated dedicated-Nostro proposal

The deprecated Dedicated Nostro Stamping Design presents this service as the primary stamping component for default and dedicated Nostro selection in RATAN. Its proposed changes for the service were to:

- Perform dedicated Nostro stamping before default lookup.
- Retrieve a dedicated Nostro using RFI portfolio and currency.
- Retain default lookup using `entity + ccy + settlementMeans + settlementAccount` as fallback.
- Remove ad hoc checks of settlement account and settlement means for dedicated cases.
- Return dedicated-match data that group management can compare during amendments.

The deprecated source references PR 2307445 for these changes. Merge, deployment, and current behavior are not confirmed by that source.

That source presents the service as a possible owner of dedicated-condition evaluation, while also proposing rule-engine ownership. It therefore does not resolve the architectural boundary between this service and rule-engine and should not be read as authoritative for the current dedicated-Nostro stamping architecture. See [[dedicated-nostro-match-conditions]] and [[what-is-the-authoritative-dedicated-nostro-stamping-architecture]].

## Concurrency-review references

The functional-requirements issue inventory names `ratan-cash-settlement-ssi-stamping-service` for two scroll-query-and-publish review points:

- `NostroRefreshCommand.scrollQueryAndPublish` with `queryResult`
- `SsiExceptionCommand.scrollQueryAndPublish` with `queryResult`

That source does not establish whether this service is identical to, a component of, or separate from [[ssi-stamping-service]]. That relationship requires verification.

No concurrency failure, duplicate-publication behavior, retry contract, or idempotency guarantee is documented in the functional-requirements issue inventory.