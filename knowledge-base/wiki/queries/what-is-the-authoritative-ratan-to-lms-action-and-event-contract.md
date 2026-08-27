---
type: query
title: "What Is the Authoritative Ratan-to-LMS Action and Event Contract?"
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, ratan, lms, event-contract, integration]
related: [ratan, lms, ratan-lms-action-event-mapping, lms-event-contract, surrounding-system-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Ratan Action and LMS Event Matrix.md"]
---
# What Is the Authoritative Ratan-to-LMS Action and Event Contract?

## Question

What is the authoritative contract between Ratan actions and LMS events, including triggers, directions, payloads, delivery guarantees, retries, reconciliation, and ownership?

## Known evidence

The source references `Ratan Action and LMS Event Matrix 20230919.xlsx` under the Cash Settlement Home Page surrounding-system integration requirements. The accessible Markdown contains no workbook rows or event definitions.

The date-like suffix suggests a 19 September 2023 version or publication date, but this has not been verified and may not represent the current contract.

## Information needed

- The full workbook with every sheet and its formatting or status indicators;
- the meaning and ownership of LMS;
- the action-to-event rows and lifecycle states;
- payload and schema definitions;
- synchronous or asynchronous interaction semantics;
- correlation, idempotency, retry, ordering, and replay rules;
- exception, reconciliation, and audit requirements;
- evidence of later revisions or implementation changes.

## Resolution criteria

This query can be resolved when the workbook or an authoritative successor is available, its mappings are extracted without loss of structure, and each mapping is reconciled with current Ratan service ownership and operational behavior.