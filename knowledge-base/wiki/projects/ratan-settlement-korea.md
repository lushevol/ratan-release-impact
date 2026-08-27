---
type: project
title: RATAN Settlement Korea
status: active
owner: "CN squad"
start_date: 2026-08-01
target_date: 2026-08-01
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, korea, cash-settlement, migration, go-live]
related: [chg1016055, ratan, fmrp-uber, cash-settlement, auto-netting, release-rollback-readiness, post-implementation-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md"]
---
# RATAN Settlement Korea

## Project Brief

RATAN Settlement Korea is the Korea cash-settlement migration and production go-live delivered under [[chg1016055]]. The recorded go-live milestone was 2026-08-01. The source identifies the `CN` squad in the release summary, although it does not explain the relationship between that squad designation and the Korea deployment.

The project is retained as active because the source links to an operational-readiness and post-go-live issue tracker, while the final status of several production checks remains insufficiently documented.

## Scope

The go-live introduced or validated:

- Korea branch and entity configuration.
- Currency cut-off records and Nostro data.
- EBBS bridge accounts and transaction codes for FMID `10036645`.
- SWIFT sender BIC data, Korea MT210 behavior, and KR MX configuration.
- Auto-netting configuration ID `9`.
- Ten rule-engine records.
- OLTP integration and tactical TLM reconciliation.
- TIS query integration.
- Murex Korea ACK handling.
- Frontend Korea entities, currencies, dashboard filters, and warnings.
- Cross-service [[fmrp-uber]] trade attributes, rules, and routing.

## Delivery Components

The active package set includes:

- `51358-ratanone-static-data-service`
- [[51358-ratan-cash-settlement-accounting-service]]
- [[51358-ratanone-swift-service]]
- [[51358-ratan-cash-settlement-query-service]]
- [[ratan-cash-settlement-netting]]
- [[ratan-rule-service]]
- [[51358-ratan-cash-settlement-group-management-service]]
- `51358-ratan-mxg-cashflow-adaptor`
- [[51358-ratanone-db-repository]]
- `51358-mfe-cashflow-blotter`
- `51358-mfe-rules`
- `ratan-service-properties`

## Milestone Status

The release summary marks the following as complete:

- System Test
- Integration Test
- Acceptance Test
- Regression Test
- Performance Test
- Delivery Manager Signoff
- QA Signoff
- User Signoff

This is a declared release status rather than a complete audit record. Several detailed result fields are empty, and many PIT checks rely on screenshots rather than textual actual values and pass/fail outcomes.

## Dependencies and Risks

### Mixed release trains

The package incorporates changes related to `CHG1015864`, `CHG1030738`, and `CHG1026932`. This creates rollback and compatibility dependencies that are not captured in a consolidated matrix.

### Operational sequence

The release instructs operators to stop “MB, group and batch service,” but does not define the exact services or complete restart sequence.

### Configuration ambiguity

The CPT pair is recorded as `USD^1|KRO^1`. The project record must preserve `KRO`, but its intended meaning requires confirmation through [[is-kro-the-intended-cpt-currency-code]].

### Verification quality

The TLM performance record supplies a response volume of 20,286 items without performance thresholds. See [[what-were-the-tlm-performance-acceptance-criteria]].

The PIT plan covers application, database, routing, and UI checks, but does not consistently record actual values or explicit pass/fail status. See [[did-all-chg1016055-pit-checks-pass]].

## Rollback Readiness

Most active services state that rollback exists. The database deployment has separate execute and rollback pipelines. The available record does not establish a complete timed rollback procedure, decision authority, dependency order, or post-rollback verification plan.

## Post-Go-Live Follow-Up

Required follow-up includes:

- Confirm every PIT check and record actual results.
- Confirm the intended meaning of `KRO`.
- Explain the lower-numbered query and netting release branches.
- Confirm whether struck-through OpenSearch, Ansible, MB, and IBMMQ scope was formally removed.
- Record the TLM API performance acceptance criteria and results.
- Document the full stop, deployment, restart, and validation sequence.
- Confirm that the netting service was restarted after configuration ID `9` was introduced.

## Retrospective

A complete retrospective is not available in the source. It should be added when post-go-live issues, PIT outcomes, rollback readiness, and operational follow-up have been closed.