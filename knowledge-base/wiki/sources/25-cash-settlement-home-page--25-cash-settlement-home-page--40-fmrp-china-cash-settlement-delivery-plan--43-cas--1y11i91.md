---
type: source
title: "CHG1016055: RATAN Settlement Korea and FMRP UBER Go-Live Plan"
authors: []
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14578329"
venue: "Azure DevOps and Confluence"
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, korea, cash-settlement, release-management, fmrp-uber, pit]
related: [chg1016055, ratan, ratan-settlement-korea, fmrp-uber, production-release-management, release-rollback-readiness, post-implementation-testing, cash-settlement, auto-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md"]
---
# CHG1016055: RATAN Settlement Korea and FMRP UBER Go-Live Plan

## Summary

This operational release plan governs [[chg1016055]], scheduled for production deployment on 2026-08-01. Its primary subject is the [[ratan-settlement-korea]] go-live, but the package also contains cross-service [[fmrp-uber]] changes, Korea static data, SWIFT MT/MX integration, reconciliation APIs, routing configuration, frontend changes, and vulnerability remediation.

The release record identifies CTASK2166493 as its ServiceNow task and Azure DevOps Release Work Item 14578329 as its central delivery record. The release summary marks System Test, Integration Test, Acceptance Test, Regression Test, Performance Test, Delivery Manager Signoff, QA Signoff, and User Signoff as complete. Several detailed evidence fields remain blank, so the document establishes claimed approval more clearly than complete machine-readable test results.

## Primary Records

- Change request: `CHG1016055`
- ServiceNow task: [CTASK2166493](https://scbnow01.service-now.com/change_task.do?sys_id=99ba74d33ba58b50f6935d0b16e45a43&sysparm_record_target=change_task&sysparm_record_row=1&sysparm_record_rows=1&sysparm_record_list=change_request%3D308afc5f3b658b50f6935d0b16e45aa0%5EORDERBYassignment_group)
- Azure DevOps work item: [Release 14578329 CHG1016055: RATAN Settlement Korea Golive](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14578329)
- Operational-readiness tracker: [Korea Cash Settlement Migration - Operational readiness & Post go live Issue Tracker](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3729099405)
- Release date: `2026-08-01`
- Release-summary squad: `CN`
- AIG: not populated in the source

## Confirmed Active Package Inventory

The following table preserves the active branch, artifact, deployment-step, and owner data recorded for the release. Struck-through entries from the source are excluded from this confirmed inventory.

| No. | Service | Step | Current branch | Current package/build | Owner |
|---:|---|---:|---|---|---|
| 1 | `51358-ratanone-static-data-service` | 4 | `release/v4.3.2` | `4.3.2-20260720.10` | Chongxuan Li |
| 2 | `51358-ratan-cash-settlement-accounting-service` | 5 | `release/v2.2.0` | `2.2.0-20260730.2` | Chongxuan Li |
| 3 | `51358-ratanone-swift-service` | 5 | `release/v4.3.0.1` | `4.3.0.1-20260723.3` | Fengke Wu |
| 4 | `51358-ratan-cash-settlement-query-service` | 5 | `release/v4.3.2` | `4.3.2-20260723.1` | Chen Yang |
| 5 | `ratan-cash-settlement-netting` | 5 | `release/v3.0.14` | `3.0.14-20260723.3` | Yonghua Li |
| 6 | `ratan-rule-service` | 5 | `release/v3.1.8` | `3.1.8-20260720.3` | Yonghua Li; Chen Yang |
| 7 | `51358-ratan-cash-settlement-group-management-service` | 5 | `release/v3.2.3.3` | `3.2.3.3-20260729.4` | Chen Yang; Junli Gao; Xinmiao Huang; Yonghua Li |
| 8 | `51358-ratan-mxg-cashflow-adaptor` | 5 | `release/v3.0.1` | `3.0.1-20260720.3` | Chen Yang |
| 9 | `51358-ratanone-db-repository` | 2 | `feature/korea develop CHG1016055_Korea/ CHG1016055_Korea_Rollback` | Execute: `20260722.6`; rollback: `20260722.7` | Chongxuan Li; Guiling Wang |
| 10 | `51358-mfe-cashflow-blotter` | 6 | `release/v1.45.0` | `1.45.0-v1.45.0-20260723.7` | Guiling Wang |
| 11 | `51358-mfe-rules` | 6 | `release/v1.11.2` | `1.11.2-v1.11.2-20260722.2` | Guiling Wang |
| 12 | `ratan-service-properties` | 1 | `master` | `20260724.4` | Chongxuan Li |

## Package Scope

The active package set implements the following changes:

- Korea branch configuration and currency-based bridge accounts.
- Accounting-service OLTP integration and a tactical TLM reconciliation API.
- ENISIS real-time MT/MX ingress and egress, Korea MT210 processing, and KR MX configuration.
- TIS API support and new FMRP fields in the query service.
- Ten new [[fmrp-uber]] fields available to netting and rule checks.
- Korea confirmation upload support in the rule service.
- Korea cashflow handling, Eco/Non eco amendment behavior, routing changes, and manual-STP soft warnings in group management.
- NID and parent-typology fields plus ACK processing for Murex Korea.
- Korea static data, Nostro records, currency cut-offs, EBBS configuration, SWIFT configuration, rules, auto-netting configuration, and message-flow filters.
- Frontend entity lists, dashboard behavior, `FinalCancelled` Swift Error filtering, SCBML upload, and rule-field hierarchy changes.
- Korea CPT controls in `ratan-service-properties`.

The release therefore extends beyond a Korea-only migration. It changes multiple layers of [[ratan]], including configuration, persistence, message integration, rule evaluation, netting, routing, APIs, and user interfaces.

## Removed or Unconfirmed Scope

The source strikes through the following package entries, so they are not confirmed as production deployments under CHG1016055:

- `ratanone-opensearch-agent`, originally associated with FMRP UBER new-field support.
- `51358-ratanone-ansible`, originally associated with topic removal, consumer-group offsets, and SCBML filtering.
- MB message-type conversion to JSON.
- A proposed two-way IBMMQ connection between RATAN and Murex KR.

The document does not state whether these items were removed, deferred, superseded, or delivered through another change.

## Release Summary

| Squad | Release Date | Test summary | Release status |
|---|---|---|---|
| CN | 2026-08-01 | System Test, Integration Test, Acceptance Test, Regression Test, and Performance Test are checked | Delivery Manager Signoff, QA Signoff, and User Signoff are checked |

The detailed row leaves the test-plan, detailed test-results link, release-phase, and test-progress fields largely blank. This documentation gap is tracked by [[did-all-chg1016055-pit-checks-pass]].

## Performance-Test Record

| Item | Test Plan | Test Results |
| --- | --- | --- |
| For Korea TLM recon API PT | PT_TLM_Recon [Grafana](https://10.198.22.29:3000/d/aeilk3vuyzri8a/core-business-metric?orgId=1&from=1785131956910&to=1785131972403) | response total item: 20286 [Apache JMeter Dashboard](https://uklvadrtn006a.pi.dev.net:8081/performance-test/1785131956910/report/index.html) |

This record shows that the TLM reconciliation API returned 20,286 items during a performance test. It does not transcribe latency percentiles, throughput, concurrency, duration, error rate, resource utilization, acceptance thresholds, or an explicit pass/fail result. See [[what-were-the-tlm-performance-acceptance-criteria]].

## Production CPT Configuration

The production validation record preserves the following configuration exactly:

```yaml
EG_TBFX_CPTY_FMID: 401039206
CPT_ENTITY_LIST: 10036645
CPT_PAIRS: USD^1|KRO^1
CPT_END_DATE: 2026-08-24
```

`KRO` is retained exactly as recorded. Its intended business meaning is unresolved and tracked by [[is-kro-the-intended-cpt-currency-code]].

## Post-Implementation Testing

The [[post-implementation-testing]] plan covers:

1. Production CPT properties.
2. Korea currency cut-offs, Nostro data, Nostro audit data, EBBS records, SWIFT sender BIC data, auto-netting configuration, rule records, and accounting schema changes.
3. UBER flow and filter configuration.
4. New trade attributes in filter, view, and rule builders.
5. Korea entities and currencies.
6. The `FinalCancelled` value in the frontend Swift Error dashboard filter.
7. Business Event, Business Version, and soft-warning behavior.
8. Rule-version verification.

Many result cells are blank and rely on screenshots as evidence. The source does not consistently record executor, timestamp, actual value, or explicit pass/fail status.

## PIT SQL

```sql
select count(1) from ratanone.ratan_static_cashflow_currency_cut_off rsccco where rsccco .id like 'KR-%';

select count(1) from ratanone.ratan_static__cashflow_nostro where id like 'kr-%';

select count(1) from ratanone.nostro_manipulation_audit nma where nma.nostro_id like 'kr-%';

select * from ratanone.ratan_static__cashflow_ebbs_bridge_account where fmid = '10036645';

select * from ratanone.ratan_static__cashflow_ebbs_txn_code where fmid = '10036645';

select * from RATANONE_SWIFT_SERVICE.SWIFT_STATIC_DATA_SENDER_BIC where k_fmid = '10036645';

select * from cash_netting_service.ratan_auto_netting_type_config rantc where rantc .id = 9;

select * from ratanone_rule_service.ratan_rule_engine rre where rre.id in (
  '7457997868871385088',
  '7457997381321293824',
  '7466305984159481856',
  '7482680514733842432',
  '7455188317088448512',
  '7457606136212160512',
  '7480462423639629824',
  '7455181677777846272',
  '7457602179788111872',
  '7457602978320678912'
);

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'ratan_cash_accounting_service'
  AND table_name = 'ratan_accounting_response_info';

SELECT schemaname, tablename, indexname, indexdef
FROM pg_indexes
WHERE schemaname = 'ratan_cash_accounting_service'
  AND tablename = 'ratan_accounting_request_task_history';

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'ratan_cash_accounting_service'
  AND table_name = 'ratan_accounting_request_task';
```

## Expected Static-Data Counts

| Query subject | Expected count |
|---|---:|
| Korea currency cut-off records | 219 |
| Korea Nostro records | 115 |
| Korea Nostro audit records | 115 |

## UBER and SCBML Routing Checks

```sql
select *
from ratanone.ratan_bridge_flow
where flow_name in('uber-flow')
order by flow_name desc, route_id asc;
```

```sql
select rbf.flow_name,
       rbf.route_id,
       rbf.route_name,
       rbf.route_type,
       rbf.route_topic,
       f.*
from ratanone.ratan_bridge_filter f,
     ratanone.ratan_bridge_flow rbf
where rbf.id = f.flow_id
  and rbf.flow_name in('uber-flow')
order by rbf.flow_name desc, rbf.route_id asc;
```

```sql
select *
from ratanone.ratan_bridge_filter
where id = '619397e4-4b46-4e3f-ad5a-2b86c3c9d8fd';
```

## Rollback and Release-Train Dependencies

Most active service entries state that rollback exists. The database repository identifies separate execution and rollback pipelines:

- Execute pipeline: `20260722.6`
- Rollback pipeline: `20260722.7`

The source does not provide a complete timed rollback runbook, decision thresholds, verification criteria, or a fully named owner for every rollback action.

Some packages also contain changes merged from the 2026-07-25 release trains:

- `CHG1015864` ISO
- `CHG1030738` BAU
- `CHG1026932` C&A

For the query, netting, and cashflow-blotter packages, the source explicitly notes handling or rollback of BAU changes. No consolidated dependency or compatibility matrix is provided.

## Operational Gaps

The deployment sequence includes step `0`, recorded as “stop MB, group and batch service.” It does not identify exact deployable units, commands, owner, timing, expected stopped state, restart sequence, or required evidence.

The database scope also says to restart the netting service after introducing auto-netting configuration ID `9`, but the source does not provide an explicit textual confirmation that this restart completed.

## Assessment

The package matrix provides strong traceability among services, branches, artifacts, pull requests, pipeline runs, scope, and owners. The source also provides concrete production validation queries and expected static-data counts.

Evidence quality is weaker for final verification. Numerous PIT results depend on screenshots, the performance record lacks acceptance criteria, and the detailed release-summary fields are incomplete. The document should therefore be treated as a strong release-scope and deployment-lineage record, but only a moderate-quality record of final production outcomes.