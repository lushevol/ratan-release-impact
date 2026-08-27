---
type: query
title: What Are the SSI Refresh Outcomes for Each Exception and Static-Data Mutation?
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, refresh, exceptions, static-data, nostro, vostro]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--18kmmel, ssi-refresh-exception-lifecycle, nostro-notification-and-refresh, pre-adhoc-error-and-adhoc-ssi-exception-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI/ssi refresh logic.md"]
---
# What Are the SSI Refresh Outcomes for Each Exception and Static-Data Mutation?

The available requirement names SSI-refresh scenarios and mutation events, but places their expected outcomes in screenshots that have not been transcribed.

## Evidence Available

The source covers these exception identifiers:

- `SETTLEMENT_ACCOUNT_OR_MEANS_MISMATCH_EXCEPTION`
- `MISSING_NOSTRO_ERROR`
- `MISSING_VOSTRO_ERROR`
- `MULTI_VOSTRO_ERROR`

It also includes a no-exception case and considers Insert, Update, and/or Delete events depending on the scenario.

## Information Required

For every documented scenario and mutation event, obtain an authoritative textual specification of:

1. The data change that triggers reevaluation.
2. The eligible cashflow population.
3. The prior and resulting SSI ID.
4. Whether an exception is created, retained, deleted, resolved, or replaced.
5. Whether the cashflow is automatically restamped or requires manual action.
6. Whether manual touch changes the outcome.
7. Required notifications, downstream messages, audit records, retries, and observability.

## Why It Matters

Without these outcomes, [[ssi-refresh-exception-lifecycle]] cannot define a reliable state model and [[nostro-notification-and-refresh]] cannot claim an SSI refresh or notification contract.