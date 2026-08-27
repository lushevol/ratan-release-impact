---
type: entity
title: Market UDP
created: 2026-08-24
updated: 2026-08-24
tags: [market-udp, reconciliation, uat, production-data]
related: [ratan-indonesia, ratan-gdc, ratan-indonesia-onshoring-2026, what-production-data-window-and-reconciliation-acceptance-criteria-apply-to-market-udp-uat]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RATAN ID Cash Settlements Migration - UAT Scope.md"]
---
# Market UDP

Market UDP is a UAT integration and reconciliation consumer in the RATAN Indonesia cash-settlement migration scope.

## Stated testing expectations

- OSV testing is considered adequately covered by SIT according to the source note attributed to Feng and Jerry.
- ID data should be queried for `T-35` to `T+10`; the operational meaning of this period is undefined.
- UAT should use the referenced UAT test cases, which are not included in the source.
- Reconciliation testing requires 2–4 weeks of RATAN production data.
- ID data was initially agreed for provision.
- GDC data is preferred and will be pursued, but is described as non-blocking.

Jerry Bin Feng is identified as the coordinator for confirming production-dump timing. The source does not provide reconciliation controls, expected outcomes, tolerances, exception handling, or sign-off authority.