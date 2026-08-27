---
type: entity
title: ratan-cashflow-lifecycle-service
created: 2026-08-22
updated: 2026-08-24
tags: [ratan, cashflow, lifecycle, write-model, status-machine, service, api, cashflow-splitting, cashflow-lifecycle, concurrency-review, domain-events, nostro, SCBML, Stella, data-migration, messaging, microservice, cash-settlement, Camunda, redis, redisson]
related: [ratan, ratan-cash-settlement-query-service, ratan-cqrs-cashflow-read-model, murex-cashflow-status-lifecycle, murex-ratan-reversal-and-replacement-lifecycle, ado, stella, murex, cashflow-query-api-performance-optimization, cashflow-splitting, split-cashflow-api-contract, cashflow-auto-split-failure, ratan-cash-settlement-netting-service, message-holding-service-impl, cashflow-processing-concurrency, held-cashflow-reinstatement, rfi-nostro-stamping-based-on-portfolio, nostro-notification-and-refresh, ratan-indonesia-entity-scoped-data-migration, cashflow-lineage-and-operational-visibility, ratan-cashflow-group-management-service, ratanone-stella-ambassador, strategic-cashflow, stella-cashflow-status-synchronization, stella-batch-and-single-status-updates, uber, camunda, cashflow-lifecycle-state-machine-restructuring, cashflow-action-time-format, process-in-topic, process-in-publication-contract, kafka-persistent-retry-and-dlt-recovery, redis, redisson, redis-client-outage-recovery, ratan-distributed-lock-ownership, cross-service-lock-validation, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--25-redisson-timeout-analysis--112c01x]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Cashflow query api optimization.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Tech Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Code Concurrent Issues.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Change List and API.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Data Migration - Indonesia.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Strategic Cashflow Stella Ambassandor.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/Uber Dev Testing Question.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Redisson timeout analysis.md"]
---
# ratan-cashflow-lifecycle-service

`ratan-cashflow-lifecycle-service` is described differently across the source documents. The Indonesia data-migration source refers to the corresponding database schema as `ratan_cashflow_lifecycle_service`.

- The RATANONE Cash Settlement Technical Design describes the service as RATAN's main business interface and write-side cashflow persistence service.
- The Cashflow Query API Optimization functional-requirement source describes `RATAN-CASHFLOW-LIFECYCLE-SERVICE` as a [[ratan]] service providing cashflow-detail query APIs to accounting, batch, group-management, LMS, rule, query, SSI-stamping, and netting services.
- The Splitting Tech Design describes it as performing cashflow status updates used by both manual and automatic splitting.
- The Strategic Cashflow Stella Ambassador source describes it as producing strategic-cashflow status-update commands and consuming Stella result messages.
- The Uber development-testing notes describe it as the lifecycle service used for a Camunda holding check and as expected to publish lifecycle-related events to `process-in` for at least some actions.
- The Redisson timeout-analysis source describes it as a Cash Settlement service that processes lifecycle-status movements and cashflow `preCheck` requests.
- The Code Concurrent Issues source identifies it as the service grouping for three `MessageHoldingServiceImpl` issue-inventory entries. That source does not define the service's deployment topology or its relationships with other Ratan services.
- The RFI Nostro stamping based on Portfolio source requires it to publish `nostroType` in cashflow domain events and include it in the response from `/v2/ratan/cashflow/move/status`.
- The Indonesia data-migration source describes the `ratan_cashflow_lifecycle_service` schema as containing cashflow affirmation status, holding messages, SCBML history and messages, and Stella message event sources.

## Write-side and lifecycle responsibilities

According to the RATANONE Cash Settlement Technical Design, the service is responsible for:

- Cashflow persistence from STELLA and Murex messages
- Request-based cashflow creation
- Reversal and rebook tagging for NSTP processing
- A status machine for individual or transactional batch changes

The UI can invoke the following direct lifecycle actions without service orchestration:

- Hold and unhold
- Fail and reinstate
- SWIFT suppression and undo
- Cashflow suppression and undo
- Early materialization

The technical-design source lists `lms_message` under this service, but subsequent lifecycle-looking tables are malformed in the source rendering. Their ownership remains unconfirmed; see [[which-lifecycle-tables-are-owned-by-ratan-cashflow-lifecycle-service]].

## Camunda, Uber, and precheck observations

According to the Uber development-testing notes, the service exposes the following Camunda holding-check endpoint:

```text
POST http://ratan-cashflow-lifecycle-service/v1/cashflow/camunda/holding-check
```

For cashflow `C06810140004`, the endpoint returned HTTP 500 because it could not parse `2025-09-19T18:00:00Z`. The associated replay topic was `Settlement_Orchestration_Adhoc_Ssi`.

The notes identify the following integration responsibilities under test:

- Holding-check processing invoked through [[camunda]]
- Lifecycle publication to `process-in` after Swift unsuppression approval
- Determining whether Materialize should publish to `process-in`
- Coordination of lifecycle state changes with domain events and downstream projections

The Uber development-testing source does not define the complete lifecycle state machine or the authoritative action-to-event matrix. Its expectation that the service publishes to `process-in` applies to at least some actions and does not establish publication requirements for all lifecycle actions.

The Redisson timeout-analysis source separately records an HTTP 500 response from:

```text
POST /v2/ratan/camunda/cashflow/preCheck
```

See [[process-in-topic]], [[process-in-publication-contract]], [[cashflow-action-time-format]], and [[kafka-persistent-retry-and-dlt-recovery]].

## Redis and Redisson dependency

The Redisson timeout-analysis source documents a January 2026 incident in which the service emitted `Unable to write command into connection!` while connected to:

```text
redis://10.198.24.59:6379
```

The failure occurred while issuing a cached Lua `EVALSHA` command containing a `hexists` ownership check. The source associates the failure with Redis AOF disk exhaustion and finite Redisson send retries.

The source does not establish whether the service must fail requests, queue retries, or provide degraded behavior while lock operations are unavailable.

### Recovery expectation

The incident verification reports that lock operations resumed after Redis recovery without restarting the service. This is a desired resilience outcome, rather than evidence of uninterrupted availability during a Redis outage.

See [[redis-client-outage-recovery]] for the distinction between bounded outage failure and autonomous reconnection after service restoration. The precise Redisson configuration and caller behavior remain open in [[what-is-the-approved-redisson-outage-recovery-configuration]].

## Strategic-cashflow and Stella messaging

According to the Strategic Cashflow Stella Ambassador source, the service produces strategic-cashflow status-update commands and consumes Stella result messages.

The documented command routes are:

| Update type | Command route |
|---|---|
| Scheduled jobs | `Cashflow_Status_Batch_Command_In` |
| Individual status-update triggers | `Cashflow_Status_Command_In` |

The service consumes results from the corresponding batch and single response topics.

The Strategic Cashflow Stella Ambassador source does not define:

- Whether the service must prevalidate transitions that Stella rejects
- The service's recovery actions for `TL_RETRY_ERROR`

See [[ratanone-stella-ambassador]], [[strategic-cashflow]], [[stella-cashflow-status-synchronization]], and [[stella-batch-and-single-status-updates]].

## Splitting status updates

According to the Splitting Tech Design, the service version is `3.4.0` on branch `feature/settlement-day2-split-common`.

UAT injected a `6min40s` delay into the service's status-update API:

- For manual splitting, processing later completed and a parent domain event compensated child processing.
- For automatic splitting, a timeout could leave the parent in `TechFail` with no children, queued children, or successfully processed children.

The Splitting Tech Design also documents the rounding-configuration endpoint:

```text
GET /v1/cashflow/lifecycle/getRoundingConfig/{currency}
```

See [[why-does-auto-split-not-compensate-child-cashflows-after-lifecycle-timeout]].

## Query interfaces and data responsibilities

According to the Cashflow Query API Optimization source, the service exposes:

- `/v1/ratan/cashflow/query`
- `/v1/ratan/cashflow/query/cashflowIds`
- `com.scb.ratan.cashflow.lifecycle.lifecycle.entrypoint.CashflowLifecycleController#queryCashflowDataByCashflowIds`

The source identifies `feature/cashflowDetailOptimization-0912` in [[ado]] as the branch for a proposed optimization.

The same source states that the service retrieves caller-specific data from:

- `ratan_cashflow_scbml_history`
- `Ratan_Cashflow_Scbml_Message`
- `ratan_cashflow_cutoff_info`
- `ratan_cashflow_affirmation_status`
- `ratan_stella_message_event_source`

The event-source table exposes data associated with [[stella]]. In a [[murex]]-related workflow, accounting uses `murexStrategy`.

## Nostro classification and domain-event propagation

The RFI Nostro stamping based on Portfolio source requires the service to propagate `nostroType` through cashflow status movement and domain events:

- Cashflow domain events must publish `nostroType`.
- The response from the following endpoint must include `nostroType`:

  ```http
  /v2/ratan/cashflow/move/status
  ```

The requirement establishes propagation of the classification. It does not require historical cashflows to be refreshed when dedicated portfolio data changes. That distinction is relevant to [[nostro-notification-and-refresh]] and [[should-historical-cashflows-refresh-nostro-identifiers]].

## Indonesia data-migration role

According to the Indonesia data-migration source, the migration inventory scopes affirmation, holding, SCBML history, and Stella event-source records by `cashflow_id`.

For SCBML messages, the source proposes selecting `body_event_rowkey` values from SCBML-history records whose cashflows occur in the Indonesia-scoped group-message population. The source-supplied query is:

```sql
SELECT DISTINCT rcsh."body_event_rowkey"::text AS id
FROM "ratan_cashflow_lifecycle_service"."ratan_cashflow_scbml_history" rcsh
JOIN "ratan_cashflow_group_management_service"."ratan_cashflow_group_message" cd
  ON cd."cashflow_id"::text = rcsh."cashflow_id"::text
WHERE cd."booking_entity_id"::text = '8'
  AND rcsh."body_event_rowkey"::text != ''
```

The Indonesia data-migration source does not define:

- Whether all history rows are required
- Whether historical records need independent entity filtering
- Whether the group-message population is complete for lifecycle migration

See [[ratan-indonesia-entity-scoped-data-migration]] and [[cashflow-lineage-and-operational-visibility]].

## Concurrency-review inventory

According to the Code Concurrent Issues source, `ratan-cashflow-lifecycle-service` is associated with these `MessageHoldingServiceImpl` entries:

| Method or point | Concurrency-review status |
|---|---|
| `MessageHoldingServiceImpl.filterNettingResultantCashflowsV2` | Listed as a concurrency-review point |
| `MessageHoldingServiceImpl.filterRegularCashflowsV2` | Listed as a concurrency-review point |
| `MessageHoldingServiceImpl.releaseV2` — `successHoldingIds` point | Explicitly recorded as having “no concurrency point” |

The Code Concurrent Issues source provides no rationale, execution model, or test evidence for the distinction between the first two entries and the `releaseV2` `successHoldingIds` point.

## Operational considerations

The Cashflow Query API Optimization source reports large requests of up to 1,487 cashflows with a total duration of 9,624 ms. Its proposed design uses category-based retrieval, batching, and multithreaded processing.

Any implementation must remain compatible with lock-sensitive netting, unnetting, splitting, amount amendment, and lien processing.

See [[cashflow-query-api-performance-optimization]] for optimization constraints and [[what-is-the-authoritative-response-contract-and-field-projection-model-for-ratan-cashflow-query]] for the unresolved API-contract model.