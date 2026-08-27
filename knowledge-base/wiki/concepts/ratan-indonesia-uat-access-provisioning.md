---
type: concept
title: RATAN Indonesia UAT Access Provisioning
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, uat, access-control, gdc, entitlement]
related: [ratan-indonesia, ratan-gdc, fmces, fmces-based-ratan-entitlement-authorization, ratan-indonesia-dual-environment-uat]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RATAN ID Cash Settlements Migration - UAT Scope.md"]
---
# RATAN Indonesia UAT Access Provisioning

RATAN Indonesia UAT requires provisioning access according to operational role and environment:

- Data Ops users are described as requiring both GDC and ID access.
- Settlement Ops access is intentionally split between ID-only, GDC-only, and dual-access users.
- SSDR/FMMIS data visibility requires both FMCES and Indonesia access.

Access provisioning is therefore an UAT entry criterion, not merely an administrative task. Teams should validate that each user can access the intended environment and that reporting visibility is correctly enforced.

## Known ambiguity

The source leaves the explicit access field blank for Data Ops PSID `1528028` (Ramakrishnan, Yogentar). Although the Data Ops narrative implies both GDC and ID access for all Data Ops users, that assignment requires formal confirmation rather than inference.