---
type: source
title: Profile Limitation Maker Checker Design
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, rule-service, profile-limitation, maker-checker, static-configuration, api]
related: [profile-limitation, profile-limitation-maker-checker-workflow, profile-limitation-check-api, ratanone-rule-service, maker-checker-configuration-governance, pending-configuration-change-isolation, static-configuration-auditability, profile-limitation-lifecycle-and-api-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Rule Service Technical Design/Profile Limitation Maker Checker Design.md"]
authors: []
year: 0
url: ""
venue: ""
---
# Profile Limitation Maker Checker Design

This design describes a maker-checker workflow for profile limitations managed by Ratan Rule Service, together with a runtime API that checks a supplied profile, currency, and amount against a limitation.

The document refers to a table design but does not provide table fields, DDL, keys, constraints, indexes, or an old-value persistence model.

## Declared Statuses

The profile-limitation status machine declares these statuses:

- `ADD_PENDING`
- `EDIT_PENDING`
- `DELETE_PENDING`
- `CONFIRMED`
- `ADD_REJECTED`

## Lifecycle Behavior

| Current status | Action | Result | Required additional behavior |
|---|---|---|---|
| `ADD_PENDING` | Reject | `ADD_REJECTED` | Delete the record directly; record checker and time. |
| `EDIT_PENDING` | Reject | `CONFIRMED` | Restore the old profile-limitation value; record checker and time. |
| `DELETE_PENDING` | Reject | `CONFIRMED` | Restore the old profile-limitation value; record checker and time. |
| `ADD_PENDING` | Confirm | `CONFIRMED` | Record checker and time. |
| `EDIT_PENDING` | Confirm | `CONFIRMED` | Record checker and time. |
| `DELETE_PENDING` | Confirm | `CONFIRMED` | Set `is_delete` to `true`; record checker and time. |

The workflow is described in [[profile-limitation-maker-checker-workflow]]. Its intended separation between pending configuration and runtime reads relates to [[pending-configuration-change-isolation]] and [[maker-checker-configuration-governance]].

## Limitation Check API

```http
GET /v1/staticLimitation/checkLimitation/{profile}/{currency}/{amount}
```

Example response:

```json
{
  "reason": "",
  "success": true
}
```

The source specifies the route and response shape only. It does not define amount precision, comparison boundaries, currency format, not-found behavior, validation failures, HTTP error statuses, authentication, authorization, or the semantics of `reason`. See [[profile-limitation-check-api]].

## Ambiguities Requiring Resolution

- The visibility rule mentions `ADD_CONFIRMED`, but that status is absent from the declared status list. It may mean `ADD_PENDING`, or it may be an omitted state.
- A rejected addition is both assigned `ADD_REJECTED` and deleted directly. The source does not say whether an audit or history record retains the rejected state.
- The source says a limitation is disabled during certain pending states, but does not define a disabled status or activation field.
- Edit and delete rejection require restoration of an old value, but the persistence mechanism is unspecified.
- Delete confirmation combines `CONFIRMED` with `is_delete = true`; queryability and retention of such records are unspecified.

These unresolved points are tracked in [[profile-limitation-lifecycle-and-api-contract]].