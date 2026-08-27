---
type: project
title: Korea RATAN Settlement Migration
status: active
owner: ""
start_date: 2026-08-23
target_date: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, korea, migration, ratan, release-readiness]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--12-2026-changes--34-cash--vqrehe, korea-murex-ratan-interface-readiness, operational-level-agreement-for-settlement-interfaces, ratan, murex-korea, fm-solace, tlm, tis, ratan-pss, korea-pss]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Korea OLA and other release related DOCs.md"]
---
# Korea RATAN Settlement Migration

## Scope

This project covers the Korea Murex payment and trade message migration into [[entities/ratan]], together with operational readiness for RATAN integrations with [[entities/fm-solace]], [[entities/tlm]], and [[entities/tis]].

The source does not establish whether the migration is approved, deployed, or complete. The project therefore remains active pending authoritative release and support evidence.

## Readiness Status

| Workstream | Current status |
| --- | --- |
| Korea Murex-to-RATAN MQ details | Pending channel and interface confirmation |
| COMP trade volume | Pending |
| COMP trade message format and sample | Pending |
| COMP trade acknowledgement behavior | No ACK explicitly marked complete |
| Monitoring | Pending |
| RATAN-to-FM Solace OLA | Awaiting RATAN PSS approval |
| RATAN-to-TLM OLA | Pending PSS review and sign-off |
| RATAN-to-TIS OLA | Pending PSS review and sign-off |
| ASRM updates | Listed updates marked complete |

## Dependencies

- Approved OLA artifacts and version identifiers.
- Confirmed MQ channels and payment/trade routing details.
- Validated COMP trade samples and volume assumptions.
- Monitoring, alerting, reconciliation, and escalation arrangements.
- PSS review and sign-off.
- Authoritative status of `CHG1016055`.

## Risks and Unknowns

The source has no named owners or due dates for open actions. It also leaves the before-go-live and new-version columns largely blank. The change-record title contains `2026_08_01`, but the source does not identify whether this is a planned date, an approved date, a historical date, or a superseded date.

## Completion Criteria

The project should not be treated as operationally ready until the open interface details are resolved, monitoring is documented, applicable OLAs are approved, and the change record provides authoritative release status.