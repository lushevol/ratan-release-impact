---
type: query
title: What Do RATAN FMO Portal Integration Statuses Mean?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, fmo-portal, tenant-status, readiness, open-question]
related: [ratan-fmo-portal-tenant-integration, fmo-portal, stamp-vpa, ssi-plus, fss, ssdr-51507]
sources: ["RATAN/RATAN -Interfaces/Ratan(FMO Portal) and STAMP FSS LOANIQ SSI+ SSDR CES.md"]
---

# What Do RATAN FMO Portal Integration Statuses Mean?

## Question

What are the formal definitions and acceptance criteria for `Technical Online`, `Online`, and `Pending` in the RATAN FMO Portal tenant status table?

## Current evidence

The source lists:

- `Technical Online`: STAMP (VPA)
- `Online`: SSI+, RATAN ONE, LOANIQ.IL, and FSS
- `Pending`: SSDR and FM CES

No status definition, target date, environment, evidence of testing, or ownership is provided.

## Why this remains open

It is unclear whether the statuses apply to entitlement retrieval, request forwarding, the complete FMO Portal integration, or another readiness dimension. `Technical Online` and `Online` should not be treated as equivalent until the status model is confirmed.