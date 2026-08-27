---
type: query
title: Is ratan_stella_message_event_source_trade_id_idx Misnamed?
tags: [postgresql, index-naming, lifecycle-service, database-schema, deployment-safety]
related: [lifecycle-precheck-database-performance, are-lifecycle-precheck-indexes-proven-by-query-plans, cashflow-lifecycle-service, postgresql, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--56--11z02tq]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/DB High CPU Usage Investigation - Since Feb.16th Midnight.md"]
---
# Is ratan_stella_message_event_source_trade_id_idx Misnamed?

The source defines an index named `ratan_stella_message_event_source_trade_id_idx` on `settlement_date`, not `trade_id`.

```sql
CREATE INDEX if not exists ratan_stella_message_event_source_trade_id_idx ON ratan_cashflow_lifecycle_service.ratan_stella_message_event_source USING btree (settlement_date);
```

## Questions to resolve

- Is `settlement_date` the intended indexed column?
- Is the index name misleading, or does it indicate that the DDL was documented incorrectly?
- Was this exact index created in each environment?
- Does the rollback command identify the intended database object?
- Do Lifecycle Service precheck query plans demonstrate a benefit from this access path?

The answer affects operational diagnosis, migration safety, and the ability to map observed query predicates to the intended index.