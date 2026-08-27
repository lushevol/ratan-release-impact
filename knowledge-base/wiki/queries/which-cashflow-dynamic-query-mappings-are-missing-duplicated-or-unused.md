---
type: query
title: Which Cashflow Dynamic Query Mappings Are Missing, Duplicated, or Unused?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, dynamic-query, database-schema, data-quality, mapping]
related: [dynamic-cashflow-query-field-mapping, cashflow-data, cash-settlement-query-cn-cashflow-data, cash-settlement-query-service-graphql-read-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cashflow Query Service - GraghQL schema and DB column mapping for dynamic query.md"]
---
# Which Cashflow Dynamic Query Mappings Are Missing, Duplicated, or Unused?

The mapping inventory flags unresolved entries that prevent it from serving as a clean canonical contract.

## Explicitly missing mappings

- `Instrument_Common.Equity_Instrument_Reference`
- `Instrument_Common.Parent_Trade_Instrument`

## Candidate duplicate or unused columns

The source labels these cashflow columns as candidate duplicates or unused entries:

- `cashflow_cashflow_affirmation_status`
- `cashflow_cashflow_business_version`
- `cashflow_cashflow_version`
- `cashflow_id`
- `cashflow_index`
- `cashflow_minor_version`
- `cashflow_status`
- `cashflow_sub_status`
- `cashflow_sub_status_type`
- `cashflow_sub_status_updater`

It also labels these SSI columns as unused:

- `ssi__is_third_party_payment`
- `ssi__charge_bearer`
- `ssi__nostro_swift_message_type`
- `ssi__swift_payment_method`

## Evidence needed

Compare the proposal against deployed [[cashflow-data]] schema, GraphQL exposure, UI usage, historical compatibility needs, data lineage, and migration plans. A “Duplicate?” or “Unused?” marker is not proof that a column can be removed.