---
type: query
title: What Are the RDM Feed Schedules, Schemas, and Failure Handling?
created: 2026-08-25
updated: 2026-08-25
tags: [rdm, ratan, feeds, schemas, schedules, failure-handling, open-question]
related: [rdm, ratan-rdm-reference-data-integration, fileit, solace, konggateway, rat-pct2-refresh]
sources: ["RATAN/RATAN -Interfaces/Ratan and RDM 38430.md"]
---
# What Are the RDM Feed Schedules, Schemas, and Failure Handling?

## Question

What are the technical and operational contracts for the seven RDM feeds received by RATANONE - 51358?

## Missing information

The source does not specify:

- File names, locations, formats, schemas, encryption, acknowledgements, retention, or replay rules for FileIT feeds.
- Enterprise Solace topics, payloads, notification semantics, delivery guarantees, or retry behaviour.
- The `RAT_PCT2_REFRESH` schedule, API endpoint, authentication, response schema, timeout, retry, or reconciliation behaviour.
- Data-quality validation, rejection handling, monitoring, alerting, or incident escalation.
- The consuming RATAN component for each feed.

## Priority

The Rules Engine Configuration Table and PCT2 portfolio-data refresh require particular clarification because their downstream consumers and business processing effects are not identified. The `Enterprise solace notification/FileIt` wording for the currency holiday and weekend feed also requires clarification.