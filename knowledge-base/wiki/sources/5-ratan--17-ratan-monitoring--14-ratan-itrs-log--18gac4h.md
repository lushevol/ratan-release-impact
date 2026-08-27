---
type: source
title: RATAN ITRS Log
authors: []
year: 2026
url: ""
venue: "RATAN monitoring record"
tags: [ratan, itrs, monitoring, incident-triage, operational-observability]
related: [itrs, ratanone, ratan-itrs-alert-triage, pv-check-bypass-risk, cashflow-business-version-monotonicity, ratan-transient-failure-recovery, what-is-the-impact-and-remediation-status-of-ca-pv-check-bypass, what-is-the-outcome-of-untriaged-ratan-monitoring-errors, is-sabre-timeout-caused-by-ratan-request-volume]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Monitoring/RATAN ITRS Log.md"]
---

# RATAN ITRS Log

## Scope

This operational monitoring record covers RATAN services and integrations from 2025-08-26 through 2026-03-25. It is a manually curated register of ITRS alerts, application log excerpts, developer confirmations, and brief dispositions.

The record distinguishes expected or non-business-impacting events from data-quality issues, recoverable technical failures, material functional defects, and incidents without a documented outcome. It should be read alongside [[concepts/ratan-operational-observability]] and [[concepts/ratan-itrs-alert-triage]].

## Principal findings

- Many alerts are expected operational outcomes, including browser websocket disconnects, missing data-entitlement roles, empty-token audit requests, stale-version STELLA actions with retry paths, and stale FMSGW updates rejected by RATAN's business-version checks.
- A material defect exists in `ratanone-ca-control-service`: `event_reason` is defined as `varchar(25)`, but `REMAINING_PARTY_FULL_NOVATION` is 29 characters. The source states that the affected trade major version will skip PV checking.
- Settlement orchestration can leave a Kafka offset uncommitted after `CannotCreateTransactionException` and retry until processing succeeds. Cashflow `006988767280` was reported as successfully processed, but the root cause remained open.
- The CA tracking-version null pointer, lifecycle JDBC connection failure, EBBS processor failure, and Kafka offset-commit timeout have no documented impact assessment or recovery evidence.
- The reported SABRE connection-timeout attribution to excessive RATAN request volume is not supported by rate, throttling, or SABRE-side evidence in this source.

## Alert classification

The source supports five operational categories:

1. **Expected or suppressible monitoring noise:** client websocket disconnects and selected state-machine rejections.
2. **User-visible access or validation failures:** missing entitlement roles, invalid GraphQL filter values, blank `cfiCode`, and empty MFA or audit-request tokens.
3. **Retry-recovered technical failures:** transaction setup failures and STELLA calls with automatic retry or settlement-exception-blotter fallback.
4. **Functional or control defects:** the CA schema constraint that causes PV-check bypass and the optimistic-locking defect planned for a future release.
5. **Untriaged failures:** events with no confirmation, owner, recovery outcome, or root-cause conclusion.

“No impact” is not uniformly equivalent to “no user impact.” Several rows prevent a user action while having no confirmed systemic settlement impact.

## Structured incident register

| Service | Exact material error or state | Disposition | Evidence status |
|---|---|---|---|
| `ratanone-query-service` | `GraphQL Error (Code: 504)` with `504 Gateway Time-out` from `nginx` | No impact/ignore; attributed to a complex cashflow-blotter filter causing an API timeout | Developer explanation recorded; query and latency evidence absent |
| `ratanone-query-service` | `Websocket Error Path: /api/ratan/notification/subscriptions` | No impact; VPN or network changes can disconnect the browser; downgrade log level | Developer confirmation recorded |
| `ratanone-query-service` | `Entitlement role is missing, please apply for entitlement role and try again.` | No impact/ignore; backend log mirrors the frontend entitlement popup | Developer confirmation recorded |
| `log_ratanone-query-service` | `Error happened service is unavailable pls check with support team.` | Fixed to expose actual query-failure details to users | Version and validation evidence absent |
| `ratanone-ca-control-service` | `TradeValuation.getTrackingVersion()` is `null`, causing `NullPointerException` in `PvServiceImpl.isTradeVersionEqual(PvServiceImpl.java:163)` | No confirmation recorded | Failure is evidenced; business impact unknown |
| `single-ui-bff` | `jwtToken is empty, validation failed`; `AsyncRequestNotUsableException` on `POST /v1/fmo/print` | No impact; UI audit request failed after empty-token validation | Developer confirmation recorded |
| `single-ui-bff` | `Error while getting response from MFA` | Check GUI volume and possible MFA outage; otherwise accept | Operational instruction only |
| `ratan-cash-settlement-orchestration` | `CannotCreateTransactionException: Could not open JPA EntityManager for transaction`; offset not committed and processing retried | Cashflow `006988767280` reportedly processed successfully; root cause open | Recovery evidence recorded; systemic resolution absent |
| `ratanone-api-gateway` | `PrematureCloseException: Connection has been closed BEFORE response` | No business impact; request was from frontend | Outcome and cause not independently evidenced |
| `ratanone-ca-control-service` | PostgreSQL `ERROR: value too long for type character varying(25)` | To be fixed; `REMAINING_PARTY_FULL_NOVATION` exceeds `event_reason` capacity and the trade major version will skip PV check | Strong schema and functional-impact evidence |
| `ratan-rule-service` | `OptimisticLockingFailureException` during `POST /v1/nstpException/closeAffirm/...` | No business impact; fix planned for next release | Deployment verification absent |
| `CN_ratan-cashflow-lifecycle-service` | Rule-service `500`: `Could not open JDBC Connection for transaction` | No confirmation recorded | Failure evidenced; outcome unknown |
| `CN_ratan-cash-settlement-accounting-service` | `EBBSJobProcessor` task exception for task ID `7379139886589689856` | No confirmation recorded | Exception detail and outcome absent |
| `ratanone-stella-ambassador` | `INVALID_TX_PROCESS_ERROR`: `Settle` not performed on latest version | Known issue; user replay if automatic retry does not resolve it | Retry and fallback described |
| `log_ratanone-data-ambassador` | TDS3 fetch error: missing entitlement role | No impact/ignore; expected access-control outcome | Developer confirmation recorded |
| `ratanone-message-bridge` | Kafka commit failure: `Timeout of 5000ms expired` for `Cash_Settlement_EBBS_Process_Out_GB-0`, offset `402993` | No confirmation recorded | Technical failure evidenced; recovery unknown |
| `ratanone-stella-ambassador` | SABRE connection timeout to `sabre-prod-cloud-global...:443` | No impact/ignore; source attributes it to excessive RATAN requests | Attribution unverified |
| `ratanone-stella-ambassador` | `INVALID_TX_PROCESS_ERROR` for `ValidateDirect` on a queued `Cash Settlement` / `Materialize` workflow | RATAN retries; unresolved calls appear in the settlement exception blotter | Recovery path described |
| `ratanone-swift-service` | `CashflowUpdateFailedException: Business version downgrade not allowed, existing: [1], request is: [0]` after FMSGW SWIFT ACK | Expected state-machine behavior; older acknowledgement cannot overwrite newer withdrawal-driven state | Sequence and versions explicitly recorded |
| `CN_ratan-cash-settlement-ssi-stamping-service` | `cfiCode must not be blank` | No impact/ignore; classified as a data issue | Input defect evidenced |
| `log_ratanone-query-service` | `Between operator should have a value pair provided` with `BET` and `values: null` | No impact/ignore; invalid frontend cashflow-blotter filter | Full request evidence recorded |

## Exact GraphQL filter evidence

```json
{
  "field": "Cashflow.Payment_Date",
  "operator": "BET",
  "values": null
}
```

The application error is:

```text
Between operator should have a value pair provided
```

## Exact CA database constraint evidence

```text
ERROR: value too long for type character varying(25)
```

```text
event_reason at max of 25 characters
REMAINING_PARTY_FULL_NOVATION
```

The source states:

```text
The impact is this major version of trade will skip PV check.
```

## Operational follow-up

The highest-priority follow-up is to identify trades affected by the CA schema defect, determine whether PV checks were skipped, and confirm retrospective validation or remediation. Untriaged infrastructure and processing failures also require owners, recovery outcomes, and closure evidence. A planned fix should not be treated as deployed until its release, deployment date, and post-release alert behavior are recorded.
