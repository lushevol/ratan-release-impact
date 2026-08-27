---
type: query
title: What Are the Indonesia RATAN Production NFR Acceptance Criteria?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, nfr, disaster-recovery, sla, ola, production-readiness]
related: [ratan-indonesia-onshoring-2026, production-server-handover-definition-of-done, production-performance-monitoring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia.md"]
---
# What Are the Indonesia RATAN Production NFR Acceptance Criteria?

The Indonesia RATAN plan identifies OLA, SLA, DR testing, ADO pipeline integration, and DB initialization as NFR dependencies. It does not state measurable targets, test scenarios, pass/fail criteria, responsible owners, or approval evidence.

## Questions to resolve

- What OLA and SLA targets apply, including service hours, availability, response times, and incident severity handling?
- What recovery time objective, recovery point objective, DR scenarios, data-validation steps, and DR test schedule apply?
- Does PT mean performance testing? If so, what workloads, volumes, latency thresholds, duration, and success criteria are required?
- What security controls, certificate lifecycle controls, secrets-vaulting validation, access-review requirements, and audit evidence are mandatory?
- What monitoring, alerting, dashboard, ITRS, and operational-support acceptance criteria are required?
- Who signs off each NFR control before the planned 2026-12-05 go-live?

## Why this matters

The stated production-server handover criteria require ITRS configurability and PSS sign-off, but do not establish operational monitoring or resilience outcomes. Measurable acceptance criteria are needed to make the November CPT and final go-live decision auditable.

See [[production-server-handover-definition-of-done]], [[production-performance-monitoring]], and [[ratan-indonesia-onshoring-2026]].