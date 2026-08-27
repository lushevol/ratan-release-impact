---
type: source
title: Static Configuration Design
authors: []
year: 2025
url: ""
venue: "RATANONE Cash Settlement Technical Design"
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, cash-settlement, static-configuration, maker-checker, technical-design]
related: [ratanone, static-configuration-management, shared-static-configuration-maker-checker-engine, pending-configuration-change-isolation, static-configuration-auditability, ratan-static-config-maker-request, ratan-static-config-audit-log, nostro-configuration, bicnetting-configuration, ratan-fxu-config, fxu, schema-evolution-for-cash-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Static configuration design.md"]
---
# Static Configuration Design

## Summary

This technical design proposes a reusable static-configuration management pattern for RATANONE Cash Settlement. Static configurations are hosted by the Static data service and consumed by other services. Users manage them through Blotter using maker/checker workflows.

The design addresses configuration retrieval, UI-based create/update/delete operations, approval and rejection, audit history, API reuse, and consistency across configuration domains such as Nostro, BicNetting, and FXU.

The document is a proposal and does not record an approved architectural decision. It compares three broad approaches:

1. Copying existing Nostro or BicNetting implementations.
2. Maintaining typed configuration tables while centralizing maker/checker requests and audit logs.
3. Using a unified JSON or metadata-driven configuration model.

The separated-table approach is presented as the most balanced option because it preserves domain-specific database constraints and customized validation while reducing duplicated workflow implementation.

## Current-State Problems

Existing Nostro and BicNetting implementations use different maker/checker semantics. Nostro changes the status of the main record and writes to an audit table. BicNetting creates a separate pending record for an update, later copies the approved data back to the original record, and discards the temporary record.

The source reports several consequences:

- Each new configuration domain requires duplicated CRUD, workflow, validation, audit, gateway, entitlement, and frontend work.
- Effective-data reads require status filtering.
- Pending updates do not have a clear version-control model.
- BicNetting audit history can span multiple record IDs.
- BicNetting lists may not refresh after operations.
- An original record may be deleted while an update request is pending.
- Direct SQL import and export require awareness of workflow state and maker/checker fields.
- Pending requests and effective records are currently mixed in some UI lists, complicating pagination and user understanding.

The source's descriptions of Nostro and BicNetting behavior are implementation findings rather than independently validated production metrics.

## Current Implementation State Matrix

| | Nostro main table | Nostro audit table | BicNetting main table | BicNetting audit table |
| --- | --- | --- | --- | --- |
| Maker create | Insert, status=ADD_PENDING | Insert ADD_PENDING | Insert, status=ADD_PENDING checker=System, id=784 | Insert ADD_PENDING |
| Maker update | set status=UPDATE_PENDING | Insert UPDATE_PENDING | Insert, status=UPDATE_PENDING id=785, updateRecordId=784 | Insert UPDATE_PENDING id=785 |
| Maker delete | set status=DELETE_PENDING | Insert DELETE_PENDING | | |
| Checker reject creation | set status=DISCARDED | Insert DISCARDED | | |
| Checker confirm creation | set status=SAVE_CONFIRMED | Insert SAVE_CONFIRMED | set status=SAVE_CONFIRMED | Insert SAVE_CONFIRMED |
| Checker reject update | set status=SAVE_CONFIRMED | Insert SAVE_CONFIRMED | set 785=DISCARDED | Insert DISCARDED id=785 |
| Checker confirm update | set status=SAVE_CONFIRMED, update data | Insert SAVE_CONFIRMED | set 784=SAVE_CONFIRMED, update data, set 785=DISCARDED | Insert SAVE_CONFIRMED id=784 |
| Checker reject deletion | set status=SAVE_CONFIRMED | Insert SAVE_CONFIRMED | | |
| Checker confirm deletion | set status=DELETE_CONFIRMED | Insert DELETE_CONFIRMED | | |

## Proposed Option 1

Option 1, described as separated configuration tables with shared audits, retains a typed table for each configuration domain. A shared engine manages maker requests, checker actions, and audit history.

Its intended properties are:

- Shared UI management APIs.
- One domain-specific fetch API for each configuration type.
- Effective approved data remains in the domain table.
- Pending requests remain in a separate request table.
- Database uniqueness constraints remain available.
- Domain-specific and customized validation remain possible.
- Audit history is centralized and attributable to a target table and target ID.
- Manual SQL import and export remain comparatively practical.

The proposed design does not define all transaction boundaries, authorization rules, identifier semantics, indexes, payload validation, or state transitions. These are implementation gaps rather than resolved behavior.

## Proposed Option 1 DDL

The following DDL is reproduced from the source:

```sql
CREATE TABLE ratan_static_config_maker_request (
    id bigserial NOT NULL PRIMARY KEY,
    maker_id TEXT NOT NULL,
    checker_id TEXT NULL,
    target_table TEXT NOT NULL,   -- target configuration table, eg. ratan_fxu_config
    target_id BIGINT,             -- id for update/delete
    operation_type TEXT NOT NULL, -- insert, update, delete
    data_status TEXT NOT NULL,    -- pending, confirmed, rejected, cancelled
    payload TEXT NOT NULL,        -- configuration json, differs accroding target table
    created_at timestamp NOT NULL DEFAULT now(),
	updated_at timestamp NOT NULL DEFAULT now()
);

CREATE TABLE ratan_static_config_audit_log  (
    id SERIAL PRIMARY KEY,
    operator TEXT NOT NULL,
    role TEXT NOT NULL,           -- maker/checker
    operation_type TEXT NOT NULL,
    target_table TEXT NOT NULL,
    target_id BIGINT,
    target_snapshot TEXT NOT NULL, 
    created_at timestamp NOT NULL DEFAULT now(),
);

CREATE TABLE IF NOT EXISTS ratan_fxu_config (
	id SERIAL PRIMARY KEY,
	booking_entity_fmid TEXT NOT NULL,
	counterparty_fmid TEXT NOT NULL,
	booking_entity_fmcode TEXT NOT NULL,
	counterparty_fmcode TEXT NOT NULL,
	is_auto_utilize BOOLEAN NOT NULL,
	settlement_means TEXT NOT NULL,
	settlement_account TEXT NOT NULL,
	created_at timestamp NOT NULL DEFAULT now(),
	updated_at timestamp NOT NULL DEFAULT now()
);
```

The audit-log DDL contains a trailing comma after `created_at`, which makes the statement syntactically invalid in PostgreSQL as written. The design also uses polymorphic `target_table` references and opaque `TEXT` payloads without database foreign keys, enumerated values, schema versions, or operational indexes.

## Alternative Designs

### Unified JSON configuration

A single table stores a configuration `type` and JSON `data` payload. This can reduce generic API and frontend effort, but makes ordinary relational uniqueness constraints, direct SQL operations, domain-specific validation, and adding new configuration fields more difficult.

### Metadata-driven configuration

A metadata table defines configuration fields and validation properties, while a separate value table stores field values. This supports generated UI and basic validation, but makes specialized controls and customized validation more difficult and may require multiple SQL inserts for manual data operations.

The comparison table in the source contains ambiguous effort markers and mixed consistency symbols. Its narrative supports the interpretation that typed tables preserve stronger database constraints than unified models; this should be confirmed before using the comparison as an authoritative decision record.

## Shared UI API Design

```py
GET /v1/static/config/{target_table}
```

```py
POST /v1/static/config/{target_table}
{
    (payload...)
}
```

```py
POST /v1/static/config/{target_table}/{target_id}/update
{
    (payload...)
}
```

```py
POST /v1/static/config/{target_table}/{target_id}/delete
```

```py
POST /v1/static/config/{target_table}/{target_id}/cancel
```

```py
POST /v1/static/config/{target_table}/{target_id}/approve
```

```py
POST /v1/static/config/{target_table}/{target_id}/reject
```

```py
GET /v1/static/config-audit-logs/{target_table}?page=0&size=5
```

The shared APIs standardize the UI management flow. The service-facing fetch API remains independently implemented for each configuration domain.

The API proposal does not specify stable logical resource names, target-table allowlists, request and response schemas, status codes, idempotency behavior, optimistic locking, audit filters, or maker/checker authorization rules. It is also unclear whether `{target_id}` identifies a domain record or a maker request.

## Open Questions

- Which architecture option is approved, and who owns the decision?
- What is the canonical identity relationship between a domain record and a maker request?
- What are the valid maker/checker state transitions?
- Must maker and checker identities differ?
- Can there be multiple pending requests for one target?
- How are approval operations made atomic across the request, domain record, and audit log?
- Does `ratan_static_config_audit_log` replace or coexist with `ratan_fxu_config_audit`?
- How are target tables allowlisted, authorized, and validated?
- What serialization, schema versioning, and validation rules apply to `payload` and `target_snapshot`?
- What indexes, retention rules, immutability controls, and entitlements are required?
- How will existing Nostro and BicNetting data and audit history be migrated?

## Related Wiki Context

This design extends [[concepts/schema-evolution-for-cash-settlement]] by proposing typed domain tables with centralized workflow mechanics. FXU is used as the illustrative domain through [[entities/ratan-fxu-config]] and [[entities/fxu]]. The audit ownership question remains connected to [[queries/what-is-the-authoritative-fxu-configuration-and-audit-integrity-contract]].

No existing decision is superseded by this proposal.