---
type: concept
title: Release Readiness Group-Completion Validation
created: 2026-08-24
updated: 2026-08-24
tags: [release-readiness, cashflow-groups, data-integrity, ratan]
related: [ratan-pss, edmi, cashflow, upstream-cashflow-replay-for-group-completion]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/EG   NP   SAU UBER Roll Out & FXU Business Go-Live Runbook on 04 04.md"]
---
# Release Readiness Group-Completion Validation

Release readiness group-completion validation uses the state of RATAN cashflow groups and group messages as a cutover gate.

For the EG, NP, and SAU scope in this runbook, the expected state is:

- No group joined to the scoped booking entities has a status other than `COMPLETED`.
- No group message for those booking entities has status `PENDING`.
- The EDMI topic and queue have no backlog.

The booking entity IDs specified by the runbook are `401036553`, `400007847`, and `400991880`.

## Validation SQL

```sql
select g.* from ratan_cashflow_group_management_service.ratan_cashflow_group g, ratan_cashflow_group_management_service.ratan_cashflow_group_message gm where gm.booking_entity_id in ('401036553', '400007847', '400991880') and g.status != 'COMPLETED' and g.id = gm.group_id ;

select gm.status, count(status) from ratan_cashflow_group_management_service.ratan_cashflow_group_message gm where gm.booking_entity_id in ('401036553', '400007847', '400991880') group by gm.status ;
```

The source's descriptive label contains `COMPLTED`, but the SQL predicate uses `COMPLETED`. The canonical status vocabulary and whether these queries are authoritative should be confirmed before reuse.

## Evidence boundary

This is a release-specific readiness criterion, not proof that the checks passed. The source provides blank status and evidence fields and does not include query results.
