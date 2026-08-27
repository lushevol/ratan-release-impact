---
type: query
title: What Production Data Window and Reconciliation Acceptance Criteria Apply to Market UDP UAT?
created: 2026-08-24
updated: 2026-08-24
tags: [market-udp, reconciliation, uat, production-data, gdc, indonesia]
related: [market-udp, ratan-indonesia, ratan-gdc, ratan-indonesia-onshoring-2026, what-is-the-approved-ratan-indonesia-data-migration-reconciliation-plan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RATAN ID Cash Settlements Migration - UAT Scope.md"]
---
# What Production Data Window and Reconciliation Acceptance Criteria Apply to Market UDP UAT?

## Open question

What production-data window, dataset composition, reconciliation method, tolerance, exception workflow, and sign-off criteria apply to Market UDP UAT?

## Evidence

The source states that Market UDP needs reconciliation testing using 2–4 weeks of RATAN production data. ID data was initially agreed, while GDC data is preferred and will be followed up. Jerry Bin Feng is to confirm when the production dump can be secured.

The source also states that ID data should be queried with `T-35` to `T+10`, but does not define this period.

## Unresolved points

- Production-dump timing and availability.
- Required ID and GDC datasets, fields, and history.
- Whether GDC data is optional for coverage or only non-blocking for schedule.
- Data masking, access, retention, and handling controls.
- Meaning of `T-35` to `T+10`.
- Reconciliation population, expected results, and permitted tolerances.
- Exception ownership, remediation workflow, and final approval authority.

## Related evidence

[[what-is-the-approved-ratan-indonesia-data-migration-reconciliation-plan]] tracks the broader Indonesia migration reconciliation plan. This query narrows the unresolved requirements to Market UDP UAT.