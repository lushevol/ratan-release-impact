---
type: entity
title: ratanone-data-model
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, data-model, tdsx, schema]
related: [tdsx-schema-migration, cashflow-message-parsing-and-enrichment]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratanone-Foundation release note.md"]
---
# ratanone-data-model

`ratanone-data-model` is the RatanOne foundation library containing the TDSX-based data model.

## Release changes

The release note records:

- TDSX proto schema upgrade from `V7.1-RELEASE` to `V7.8-RELEASE`
- Changes to some fields from single values to arrays
- Corrections to internal field value types
- Addition of a new internal field for FXU

## Compatibility impact

The release note does not list the affected fields. Consumers should therefore verify serializers, persistence mappings, XPath mappings, and downstream interfaces before upgrading.

TDSX is distinct from [[tds3]] based on the available evidence; the source does not establish that the two names refer to the same schema or system.

See [[tdsx-schema-migration]] for migration risks and open compatibility questions.
