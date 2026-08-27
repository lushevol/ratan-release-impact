---
type: source
title: RATANONE Cash Settlement Technical Design
authors: []
year: 2026
url: ""
venue: Internal technical design
created: 2026-08-22
updated: 2026-08-22
tags: [ratanone, cash-settlement, technical-design, architecture, murex, netting]
related: [ratan, ratan-one, strategic-settlements-platform, cashflow-group-completeness-gating, ratan-cqrs-cashflow-read-model, strategic-cash-settlement-entitlement-model, ratan-cashflow-lifecycle-service, ratan-cash-settlement-query-service, ratan-cash-settlement-group-management-service, ratan-cash-settlement-netting-service, murex-to-ratan-cashflow-interface]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design.md"]
---
# RATANONE Cash Settlement Technical Design

This technical design inventories the intended Strategic Cash Settlement architecture for RATANONE. It assigns RATAN the intended golden-source, lifecycle, materialization, CPN netting, and fail/reinstate responsibilities, contrasting these with the BCS/EG model based on TDS3 and FMRP STELLA.

The document is an architecture reference rather than evidence of deployed operation. Its “Overall Design” and “Workflow” sections contain no substantive content, and several service-table rows are structurally ambiguous.

## Strategic versus legacy cash settlement

| Functionalities | BCS/EG cash settlement | Strategic cash settlement |
| --- | --- | --- |
| Cashflow Golden Source | TDS3 | RATAN (Postgre SQL) |
| Cashflow Creation | FMRP STELLA | MUREX 2.11, FMRP STELLA, RATAN |
| Cashflow Lifecycle | FMRP STELLA | RATAN |
| Cashflow Materialization | FMRP STELLA | RATAN |
| Netting (CPN) | FMRP STELLA | RATAN |
| Fail/Reinstate | FMRP STELLA | RATAN |
| Products scope | BCS products + EG FX | CN IRS, CCS, Loan&Deposit, NDF |
| Exception handling | One by one on Exception blotter | All in one go on cashflow detail page |
| Function entitlement | Different tiles via different EMS2 entities, transition in progress to CN | Only 1 EMS2 entity (X_RATANONE), different tiles control via different subjects |

## Service architecture

The source describes a domain-service architecture:

- The Murex adaptor transforms MxML to SCBML, aligns messages to group management, and maintains CFI mappings.
- [[ratan-cash-settlement-group-management-service]] gates workflow publication until a complete trade-ID and major-version group has arrived. It supports exceptional manual force-STP, upstream status writeback, trade-event consumption, and message standardization.
- Camunda coordinates upstream STP, exception closure, maker/checker activity, and technical-failure routing.
- [[ratan-cashflow-lifecycle-service]] is the stated write-side persistence and status-machine service.
- [[ratan-cash-settlement-query-service]] maintains an event-driven read model and GraphQL query interface.
- [[ratan-cash-settlement-netting-service]] validates components, produces resultants, and supports un-netting. Split processing and auto-netting are explicitly future scope.
- SSI stamping handles Vostro/Nostro stamping, exceptions, and SSI updates.
- FX utilization persists UTIL cashflows, processes Razor FXU requests, and performs EOD auto-utilization and auto-past-due processing.

## Murex MQ interface

| Source system | Target System | Purpose | Publish end | Consume end | Dev config | Prod config |
| --- | --- | --- | --- | --- | --- | --- |
| Murex | Ratan | 1. Cashflow publishing 2. Ack on released status | CF.MXG.RATAN.RQST | CF.MXG.RATAN.RQSTIN | Host 10.198.198.93 Port 8212 Channel UKMXGCLNTS2 Queue manager UKFM02S1 User ukmxgmq | Host Port 8212 Channel Queue manager User ukmxgmq |
| Ratan | Murex | 1. Ack on cashflow consuming 2. Released status | CF.RATAN.MXG.RESP | CF.RATAN.MXG.RESPIN |  |  |

Solace connections are stated to reuse BAU connections; the source directs readers to ASRM for details.

## Persistence inventory

| Service name | Description | Tables | Table purpose |
| --- | --- | --- | --- |
| ratan-cash-settlement-lms-service |  | lms_message lms_outbox_events lms_raw_message lms_trade ratan_lms_scbml_history | this table used for storage message send status for downstream this table used for storage per event record in one cashflow this table used for storage lms service received message and sent out message this table used for storage trade information ratan_lms_scbml_history, this table won’t used any longer, will be removed |
| ratan-cash-settlement-netting-service |  | t_cashflow t_request | maintain all cashflows information with the latest maintain all casfhflow update audit history |
| ratan-cash-settlement-orchestration | STP workflow base on camunda framework | ratan_cashflow_multiple_exception ratan_cashflow_user_task | Record all technical exceptions in STP workflow Record user task in STP workflow, like maker task & checker task |
| ratan-cash-settlement-query-service |  | cashflow_data cashflow_data_history t_event | cashflow_data: record cashflow scbml cashflow_data_history : record cashflow_data_history t_event : record received event message from cashflow lifecycle service |
| ratan-cash-settlement-ssi-stamping-service |  | cashflow_stamping cashflow_stamping_exception cashflow_stamping_legacy_exception cashflow_status_snapshot maker_checker_request raw_message stamped_nostro_account stamped_vostro_account stamping_outbox_events trade_stamping_message | cashflow_stamping: record cashflow stamping info cashflow_stamping_exception: record cashflow stamping exception cashflow_stamping_legacy_exception: record stamping exception reason cashflow_status_snapshot : record cashflow status_snapshot maker_checker_request: record maker checker request data raw_message : record cashflow scbml stamped_nostro_account: record cashflow nostro_account stamped_vostro_account: record cashflow vostro_account stamping_outbox_events: record received event trade_stamping_message: record trade stamping info |
| ratan-cash-settlement-group-management-service |  | ratan_cashflow_group ratan_cashflow_group_history ratan_cashflow_group_message ratan_cashflow_group_message_history ratan_cashflow_mapping ratan_cashflow_mapping_history ratan_cashflow_rounding_config ratan_cashflow_status_sync_up_blocking_queue ratan_inbound_message ratan_trade ratan_trade_history | 1. All cashflow message with same trade id + major version should be treated as a cashflow group. 2. Cashflow group audit table. 3. Persist cashflow message after receive any cashflows from upstream, message can be delivered only after all message arrived in the same group. 4. Cashflow group message audit table |
| ratan-cashflow-lifecycle-service | The cashflow main service, provide the main business interface. Persist the cashflow information and status change. | lms_message |  |
| ratan-exception-platform |  | rep_exception rep_exception_history | 1. Persist all exceptions published by domain services. 2. Exception audit table for tracking the exception change history. |
| rantan_mxg_cashflow_adaptor |  | mxg_cashflow_inbound mxg_cashflow_history mxg_cashflow_message static_data_cfi_code mxg_cashflow_exception mxg_cashflow_group mxg_cashflow_group_message | Record PayMent Info from murex; Record PayMent Info history; Record PayMent history message; Maintain CFI Code static data; Discarded; Record Payment group; Record Payment group Histories |
| ratan-cash-settlement-fx-utilization-service |  | ratan_fx_cashflow_brief_info ratan_fx_cashflow_utilization_history ratan_fx_accounting_send_failed_info ratan_fx_utilization_response_failed_info | 1. fx cashflow main table 2. fx utilization audit table 3. fx publish accounting msg and fx utilization response failure table |

The following rows appear after the lifecycle-service row without a repeated service name. Their ownership is not confirmed by the source rendering:

```text
ratan_cashflow_affirmation_status
ratan_cashflow_cutoff_info
ratan_cashflow_holding_message
ratan_cashflow_razor_stella_status_blocking_queue
ratan_cashflow_scbml_history
ratan_cashflow_scbml_message
ratan_cashflow_scheduler_job_record
ratan_minor_version_history
ratan_stella_message_event_source
ratanone_cashflow_service__cqrs_cashflow_events
razor_acknack_event_source
razor_cashflow_status_event_source
```

## Limitations and follow-up

The document does not define group-completeness calculation, force-STP authorization, MQ resilience controls, production MQ settings, read-model recovery, or authoritative ownership boundaries across RATAN, Murex, STELLA, Razor, and the query database. See [[what-controls-govern-force-stp-for-incomplete-cashflow-groups]], [[what-is-the-authoritative-ratan-cashflow-data-ownership-model]], and [[which-lifecycle-tables-are-owned-by-ratan-cashflow-lifecycle-service]].