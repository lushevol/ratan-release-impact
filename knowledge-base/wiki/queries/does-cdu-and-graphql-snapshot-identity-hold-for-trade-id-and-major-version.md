---
type: query
title: Does CDU and GraphQL Snapshot Identity Hold for Trade ID and Major Version?
tags: [cdu, graphql, trade-data, ssi-stamping, versioning]
related: [cdu, graphql-trade-snapshot-retrieval, ratan-ssi-stamping, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--25-ssi-stamping-notifica--1um4ze4]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade Strategic SSI Stamping Tech Design.md"]
---
# Does CDU and GraphQL Snapshot Identity Hold for Trade ID and Major Version?

Does the latest snapshot used by [[cdu|CDU]] for SSI stamping always resolve to the same GraphQL trade snapshot when queried by `Trade_Id` and `Trade_Lake_Trade_Major_Version`?

## Why this is open

The design states that the CDU snapshot should also be found in GraphQL under the same trade ID and major version. However, the GraphQL request retrieves one result without filtering on `Trade_Lake_Trade_Minor_Version`.

## Questions to resolve

- Can GraphQL lag CDU ingestion or publication?
- Can multiple minor versions satisfy the same trade ID and major-version predicate?
- What ordering applies when `size: 1` is used?
- What must SSI stamping do when the GraphQL result is absent, stale, ambiguous, or incomplete?
- Is there a reconciliation or retry contract between CDU and GraphQL?

## Evidence

[[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--25-ssi-stamping-notifica--1um4ze4]] states the expected alignment but does not provide a verified consistency contract.