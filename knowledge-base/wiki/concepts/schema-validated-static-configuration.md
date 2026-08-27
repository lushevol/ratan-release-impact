---
type: concept
title: Schema-Validated Static Configuration
created: 2026-08-24
updated: 2026-08-24
tags: [static-configuration, json-schema, validation, data-modeling]
related: [static-configuration-management, unified-json-configuration, settlement-booking-entity-configuration, what-is-the-static-configuration-lifecycle-and-versioning-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft).md"]
---
# Schema-Validated Static Configuration

Schema-validated static configuration combines generic configuration storage with a per-context schema that validates the shape of each configuration-content record.

The draft proposes a definition record containing a `context`, consumer `domain`, JSON Schema text, lifecycle state, and version. Individual content records then carry generic `key`, `value`, `type`, `sub_type`, and `metadata` fields. This supports distinct structures for contexts such as operator mappings and settlement booking entities while retaining a common persistence model.

## Proposed validation model

The draft identifies JSON Schema as the validation standard. For example, booking entities require an FMID-like key, FM Code-like value, a flow selected from `NORMAL`, `STRATEGIC`, or `CPT`, and country metadata.

This direction extends [[unified-json-configuration]], but does not establish when validation occurs, whether existing records are revalidated after schema changes, or how schema versions are made compatible with clients.

## Representation inconsistency

The supplied operator-mapping schema defines `value` as a string, yet example values are arrays such as `["=", "!=", "in", "notIn"]`. The proposed generic data model also declares `value` as `VARCHAR`.

Before implementation, the authoritative model must decide whether values are:

- JSON-serialized text in `VARCHAR`;
- native JSON values;
- typed relational columns; or
- a revised schema that permits arrays.

Schemas must validate the persisted representation rather than an incompatible logical representation.