---
type: concept
title: SSI Refresh Exception Lifecycle
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, refresh, exception-lifecycle, nostro, vostro, cash-settlement]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--18kmmel, pre-adhoc-error-and-adhoc-ssi-exception-lifecycle, nostro-notification-and-refresh, scb-receive-vostro-validation, what-are-the-ssi-refresh-outcomes-for-each-exception-and-static-data-mutation, does-manual-touch-prevent-ssi-id-refresh-or-only-adhoc-ssi-classification]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI/ssi refresh logic.md"]
---
# SSI Refresh Exception Lifecycle

SSI refresh exception lifecycle is the expected handling of cashflow SSI selection after relevant settlement data is inserted, updated, or deleted, particularly when selection is blocked by validation exceptions.

The available source establishes the scenarios and mutation-event categories under consideration, but not the actual state transitions or SSI-ID outcomes.

## In-Scope Exceptions

The source explicitly associates four scenario labels with system identifiers:

- Mismatch Exception: `SETTLEMENT_ACCOUNT_OR_MEANS_MISMATCH_EXCEPTION`
- Missing Nostro Exception: `MISSING_NOSTRO_ERROR`
- Missing Vostro Exception: `MISSING_VOSTRO_ERROR`
- Multi Vostro Exception: `MULTI_VOSTRO_ERROR`

A separate “No Exception” scenario covers valid or uniquely resolvable conditions.

## Mutation Coverage

| Scenario | Included mutation events |
| --- | --- |
| Settlement-account-or-means mismatch | Insert; Update |
| Missing Nostro | Insert; Update/Delete |
| Missing Vostro | Insert/Update/Delete |
| Multi Vostro | Insert; Update/Delete |
| No Exception | Insert; Update/Delete |

These labels establish that refresh behavior is expected to be considered in response to static-data mutations. They do not specify whether a mutation resolves an exception, creates a new exception, triggers re-stamping, or preserves an existing SSI ID.

## Separation from Ad Hoc SSI

The source title indicates that this SSI-selection process must not be treated as ad hoc SSI. This is a scoped requirement, not proof that manual interaction and ad hoc SSI are equivalent or mutually exclusive.

See [[pre-adhoc-error-and-adhoc-ssi-exception-lifecycle]] for the existing ad hoc exception context.

## Manual-Touch Constraint

A terse source note appears to state that manual touch prevents SSI-ID change. Its meaning is unresolved:

- “manual touch” is not defined;
- the affected operation is not identified;
- “SSI ID (no)” may mean no refresh, no value, or no eligibility.

No implementation rule should be inferred until the screenshots are transcribed or an authoritative requirement is supplied. Track this in [[does-manual-touch-prevent-ssi-id-refresh-or-only-adhoc-ssi-classification]].

## Boundaries

This concept does not establish a Nostro strategy, Vostro matching predicate, RFI behavior, dedicated-Nostro behavior, service owner, or notification contract. Related pages such as [[nostro-notification-and-refresh]] and [[scb-receive-vostro-validation]] may govern narrower workflows.