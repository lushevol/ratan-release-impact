---
type: source
title: Nostro Centralization
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, settlement-day-2, nostro, static-data, functional-requirement]
related: [nams, ssi-plus, nostro-centralization, nostro-stamping, nostro-notification-and-refresh, nostro-static-data-migration, ratan, razor, rfi-stamping, keystone]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Centralization.md"]
---
# Nostro Centralization

## Summary

This internal functional requirement describes the planned centralization of Nostro static data. The source states that Nostro static data is currently maintained independently in transaction-processing (TP) systems and represented in different formats. The target direction is to consolidate the data in `NAMS`, after which Data Ops will create, amend, and close static data in `SSI+`. TP systems are expected to integrate with and consume the data from `SSI+`.

The requirement is an early scope and estimation document. It does not define final interfaces, message schemas, mappings, acceptance criteria, migration rules, or non-functional targets.

## Functional scope

### Nostro stamping

TP systems require a new connection with `SSI+` to query Nostro data. The source identifies two impacted `Ratan` use cases:

1. Cashflow or trade stamping with a Nostro query.
2. Accounting Nostro lookup.

Message formats and mappings remain to be confirmed. The source does not specify whether the query is synchronous, whether TP systems retain a local cache, or what fallback and error-handling behavior applies.

### Nostro notification

TP systems are expected to consume Nostro static-data lifecycle events from `SSI+` and trigger a Nostro refresh. The explicitly named events are:

- `New`
- `Update`
- `Delete`

The requirement also asks whether events beyond these three must be supported. Event payloads, ordering, delivery guarantees, replay behavior, idempotency, and deletion semantics are not defined.

### Data-format changes

The source identifies a terminology difference between systems:

- `Ratan` uses `NOS` in settlement.
- `Razor` uses `Nostro`.

The document does not establish whether this is only a label difference or represents incompatible data models. The impacts on `Ratan` and `Razor` should therefore remain separate until a canonical representation is agreed.

### Migration and related scope

The requirement includes support for data migration and explicitly raises the unresolved question of whether historical cashflows linked to a Nostro ID should be refreshed.

It also identifies two related areas:

- `RFI stamping`, which requires portfolio-to-Nostro mapping.
- `Keystone`, which was planned to go live in February 2026.

The dependency or sequencing relationship with `RFI stamping` and `Keystone` is not specified.

## Rough estimation

The source records the following rough estimate:

```text
Rough Estimation: 170

Nostro Stamping: 30+15
Nostro Notification: 20+15
NFR: 20
Data migration support: 20
QA: function/regression/automation -50
```

The estimate is provisional. No assumptions about staffing, dependencies, implementation complexity, or test scope are provided.

## Open questions

- Is `NAMS` the authoritative system of record, or does `SSI+` become authoritative after migration?
- Does `SSI+` provide synchronous query APIs, event streams, or both?
- What are the canonical Nostro identifiers and backward-compatibility rules?
- What are the query and event message schemas and mappings?
- Are event deliveries ordered, durable, replayable, and idempotent?
- What should happen when a Nostro record is deleted but is referenced by active or historical cashflows?
- Must TP systems retain local copies, or should they query `SSI+` at runtime?
- What canonical value should normalize `NOS` and `Nostro`?
- How does `RFI stamping` affect portfolio-to-Nostro mapping?
- What is `Keystone`'s precise dependency or overlap?
- What NFR targets apply to latency, availability, recovery, event processing, and reconciliation?
- Which QA scenarios cover lifecycle events, duplicates, replay, stale data, and migration outcomes?

## Evidence limitations

The source provides a clear architectural direction and rough scope, but it does not provide a system inventory, data dictionary, identifier mapping, API contract, event contract, migration decision, or test evidence. Statements about the target operating model should be treated as requirement-level intent rather than an approved implementation design.

See [[concepts/nostro-centralization]], [[concepts/nostro-stamping]], and [[concepts/nostro-notification-and-refresh]] for derived topics. The unresolved historical-data question is tracked in [[queries/should-historical-cashflows-refresh-nostro-identifiers]].
