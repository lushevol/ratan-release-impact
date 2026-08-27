---
type: query
title: What Is the Manual Rounding API Version and Authorization Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, manual-rounding, api, authorization, versioning]
related: [camunda-task-bulk-amend-rounding-api, maker-checker-rounding-workflow, cashflow-versioning, manual-rounding-amendment]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Manual Rounding/Api design.md"]
---
# What Is the Manual Rounding API Version and Authorization Contract?

The source documents the endpoint and example payloads but leaves several implementation and control questions unresolved.

## Questions to resolve

- Must the maker and checker be different users?
- What permissions are required for `AmendRounding`, `Approve`, and `Reject`?
- Is `minorVersion` automatically incremented from `"5"` to `"6"`?
- What is the authoritative version-selection and concurrency-control rule?
- Does rejection restore the prior cashflow amount or only complete the workflow task?
- Can the `/bulk/` endpoint process multiple cashflows atomically, partially, or independently?
- Are `comment`, `amendAmount`, and `currency` mandatory?
- What service is expected at `10.198.199.166:25057`?
- Are the trailing commas in the documented maker payload merely formatting errors?

Deployment records, API implementation details, authorization configuration, and UAT or execution evidence are needed before these questions can be closed.
