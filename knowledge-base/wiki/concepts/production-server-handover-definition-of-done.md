---
type: concept
title: Production Server Handover Definition of Done
created: 2026-08-24
updated: 2026-08-24
tags: [production-readiness, infrastructure, handover, definition-of-done, ratan, indonesia]
related: [ratan-indonesia-onshoring-2026, ratan, production-performance-monitoring, what-are-the-indonesia-ratan-production-nfr-acceptance-criteria]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia.md"]
---
# Production Server Handover Definition of Done

For the planned [[ratan-indonesia-onshoring-2026]] deployment, production-server handover is a formal readiness gate rather than simple VM delivery. The source schedules it for **2026-07-16**, replacing a struck-through 2026-06-11 date.

## Stated criteria

The project-specific definition of done requires:

- a VM ready with application OS customization requirements, OS version, user group/permission, and storage;
- a ready PostgreSQL database;
- generic network and firewall accessibility;
- ITRS configurability; and
- PSS support permission and sign-off.

## Implications

The gate combines compute, operating-system, identity/access, storage, database, network, monitoring configuration, and support acceptance. PSS sign-off makes operational support readiness an explicit condition for handover.

These criteria are evidence of the Indonesia initiative's intended standard only. They are not established here as a universal enterprise production-handover standard, and the source does not provide completion evidence, named accountable owners, validation procedures, or escalation rules.

ITRS configurability is relevant to [[production-performance-monitoring]], but the source does not specify monitoring counters, alert thresholds, or acceptance tests.