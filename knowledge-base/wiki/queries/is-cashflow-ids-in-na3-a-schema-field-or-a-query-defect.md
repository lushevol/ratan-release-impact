---
type: query
title: Is cashflow_ids in NA3 a Schema Field or a Query Defect?
created: 2026-08-24
updated: 2026-08-24
tags: [SSI, SQL, NA3, schema, open-question]
related: [ssi-change-notification-re-stamping, cashflow, schema-evolution-for-cash-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design/SSI Stamping Implementation(SCBML).md"]
---
# Is `cs.cashflow_ids` in NA3 a Schema Field or a Query Defect?

The NA3 exclusion query contains:

```sql
and sna.cashflow_stamping_id = cs.cashflow_ids
```

The other documented queries use `cs.cashflow_id`, including the first NA3 selection query and the join between `cashflow_stamping` and `cashflow_stamping_legacy_exception`.

## Verification required

The database schema and deployed query should be checked to determine whether `cashflow_ids` is an intentional field, a collection-valued field, or a typo for `cashflow_id`. The answer affects whether pending ad-hoc SSI requests are correctly excluded from NA3 re-stamping.