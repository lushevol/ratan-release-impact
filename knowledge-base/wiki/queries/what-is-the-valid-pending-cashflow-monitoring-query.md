---
type: query
title: What Is the Valid Pending Cashflow Monitoring Query?
created: 2026-08-24
updated: 2026-08-24
tags: [sql, postgresql, monitoring, pending-cashflow, group-management]
related: [cash-settlement-ola-break-monitoring, cash-settlement-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md"]
---
# What Is the Valid Pending Cashflow Monitoring Query?

The source provides this query for groups pending longer than five minutes:

```sql
select * from ratan_cashflow_group_management_service.ratan_cashflow_group where status = 'PENDING' and updated_at < now()-interval'5 M';
```

The interval expression is preserved verbatim but may not be valid PostgreSQL syntax. Before production use, the team should validate syntax, confirm the intended five-minute threshold, assess indexing and query cost, and define whether `updated_at` accurately represents group-arrival delay.