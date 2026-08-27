---
type: source
title: "Ratan Action and LMS Event Matrix — 19 September 2023"
authors: []
year: 2023
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ratan, lms, event-matrix, integration-requirements]
related: [ratan, cash-settlement-home-page, lms, ratan-lms-action-event-mapping, surrounding-system-integration, lms-event-contract, what-is-the-authoritative-ratan-to-lms-action-and-event-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Ratan Action and LMS Event Matrix.md"]
---
# Ratan Action and LMS Event Matrix — 19 September 2023

## Scope

This source reference identifies an Excel attachment named `Ratan Action and LMS Event Matrix 20230919.xlsx`. It is located under the Cash Settlement Home Page functional requirements for surrounding-system integration and appears intended to map actions performed by or routed through [[entities/ratan|Ratan]] to events in [[entities/lms|LMS]].

The accessible Markdown source contains only the attachment reference. The workbook sheets and matrix rows are not available in the supplied source extract.

## Evidence and limitations

The filename provides moderate evidence that the workbook concerns Ratan actions and LMS events. The `20230919` suffix likely indicates 19 September 2023, but this is a filename inference rather than verified document metadata.

No event-level requirements can be confirmed, including:

- Ratan action names or workflow states;
- LMS event names, identifiers, or directions;
- triggering conditions;
- payload or schema definitions;
- synchronous or asynchronous processing;
- delivery, retry, ordering, deduplication, or reconciliation behavior;
- error handling and ownership;
- effective dates, approval status, or version history.

No SQL DDL, API signatures, configuration, event schemas, or structured tables are present in the accessible source text.

## Required workbook review

A validated review requires the workbook or an export of every sheet. The extraction should preserve sheet names, row identifiers, action names, LMS event names, actor or system columns, statuses, notes, dates, and any color or status encoding.

Particular attention should be paid to whether the matrix defines outbound Ratan notifications, inbound LMS commands or acknowledgements, lifecycle transitions, exception and reversal flows, manual versus automated actions, correlation identifiers, and idempotency controls.

The matrix should be compared with current Ratan service boundaries before any implementation responsibility is assigned to a particular service.

## Relationship to the wiki

This source is directly relevant to [[entities/cash-settlement-home-page|Cash Settlement Home Page]] integration requirements and may extend [[entities/ratan|Ratan]] coverage. The available evidence does not establish that any specific Ratan microservice owns or emits LMS events.

The unresolved contract is tracked in [[queries/what-is-the-authoritative-ratan-to-lms-action-and-event-contract|What Is the Authoritative Ratan-to-LMS Action and Event Contract?]].