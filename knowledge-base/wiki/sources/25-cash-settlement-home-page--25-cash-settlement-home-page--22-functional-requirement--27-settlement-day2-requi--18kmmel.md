---
type: source
title: SSI Selection Not Treated as Ad Hoc SSI — SSI Refresh Logic
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, ssi, refresh, exceptions, functional-requirement]
related: [ssi-refresh-exception-lifecycle, pre-adhoc-error-and-adhoc-ssi-exception-lifecycle, what-are-the-ssi-refresh-outcomes-for-each-exception-and-static-data-mutation, does-manual-touch-prevent-ssi-id-refresh-or-only-adhoc-ssi-classification]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI/ssi refresh logic.md"]
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page Functional Requirement"
---
# SSI Selection Not Treated as Ad Hoc SSI — SSI Refresh Logic

This functional-requirement document concerns SSI selection and refresh behavior. Its title indicates that the described SSI-selection flow must **not** be treated as ad hoc SSI handling.

Most detailed operational behavior is embedded in screenshots and is not available as transcribed text. Therefore, this source establishes scenario scope and exception-code mappings, but does not establish the expected transition or refresh outcome for individual cases.

## Explicit Exception Mappings

| Scenario | Exception identifier |
| --- | --- |
| Mismatch Exception | `SETTLEMENT_ACCOUNT_OR_MEANS_MISMATCH_EXCEPTION` |
| Missing Nostro Exception | `MISSING_NOSTRO_ERROR` |
| Missing Vostro Exception | `MISSING_VOSTRO_ERROR` |
| Multi Vostro Exception | `MULTI_VOSTRO_ERROR` |

## Mutation Events in Scope

The source organizes screenshot-based behavior by the following events:

| Scenario | Event labels present in the source |
| --- | --- |
| `SETTLEMENT_ACCOUNT_OR_MEANS_MISMATCH_EXCEPTION` | Insert; Update |
| `MISSING_NOSTRO_ERROR` | Insert; Update/Delete |
| `MISSING_VOSTRO_ERROR` | Insert/Update/Delete |
| `MULTI_VOSTRO_ERROR` | Insert; Update/Delete |
| No Exception | Insert; Update/Delete |

The named “No Exception” case confirms that the document addresses normal SSI-refresh scenarios as well as error scenarios.

## Manual-Touch Note

The document includes the note:

> 只要是manual touch ->ssi id (no)

This appears to suggest that a manually touched cashflow should not have its SSI ID changed or refreshed. The wording is too terse to determine whether “SSI ID (no)” means no update, a null SSI ID, or exclusion from a process. Treat this as unverified pending transcription of the screenshots and business confirmation.

## Evidence Limits

The supplied text does not reveal:

- the trigger predicates for any exception;
- whether an exception is created, retained, resolved, or replaced after a mutation;
- whether SSI ID is restamped, retained, cleared, or manually selected;
- the definition of “manual touch”;
- service ownership, downstream messages, audit effects, or production behavior.

The trailing `Prod->` marker is followed only by an inaccessible screenshot and is not evidence of current production behavior.

## Related Documentation

The source is relevant to [[pre-adhoc-error-and-adhoc-ssi-exception-lifecycle]], but does not define how this non-ad-hoc selection flow maps to that lifecycle. It also provides event-scope evidence for [[ssi-refresh-exception-lifecycle]] and potentially relates to [[nostro-notification-and-refresh]] and [[scb-receive-vostro-validation]] without proving their specific selection rules.