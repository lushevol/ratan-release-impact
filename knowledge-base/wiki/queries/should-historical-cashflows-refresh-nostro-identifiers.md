---
type: query
title: Should Historical Cashflows Refresh Nostro Identifiers?
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, historical-data, migration, cashflow, open-question]
related: [nostro-static-data-migration, nostro-centralization, nostro-notification-and-refresh, ratan, ssi-plus]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Centralization.md"]
---
# Should Historical Cashflows Refresh Nostro Identifiers?

## Question

When Nostro static data is centralized, should historical cashflows linked to a Nostro ID be refreshed or remain associated with the original reference?

## Current evidence

The source raises this as an unresolved migration question. It does not specify whether refresh should apply to all historical cashflows, only active or unsettled cashflows, or none.

## Decision criteria

Resolution should consider:

- Audit preservation of historical settlement decisions.
- Continuity of Nostro identifiers across migration.
- Treatment of deleted or superseded records.
- Reconciliation between old TP-system data and `SSI+`.
- Impact on accounting and downstream reporting.
- Replay and recovery behavior for notification events.
- Whether historical records are immutable by policy.

## Candidate policies

1. Preserve historical references and maintain an identifier cross-reference.
2. Refresh only active or unsettled cashflows.
3. Refresh all historical cashflows to the centralized identifier.
4. Use a versioned reference model that preserves both original and current identifiers.

No option is approved by the source.
