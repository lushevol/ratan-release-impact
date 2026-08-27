---
type: query
title: What Is the Authoritative SGO SSI Amendment Propagation Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [SGO, SSI, amendment, propagation, cashflow, event, defect]
related: [sgo-ssi-replication, ssi-refresh-exception-lifecycle, ssi-id-persistence-and-edit-provenance, es-static-data-layer]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/FMRP SGO Testing.md"]
---
# What Is the Authoritative SGO SSI Amendment Propagation Contract?

## Question

Why did the SGO update event arrive without updating the SGO cashflow after the local-agent amendment from `IRVTUS3NIBK` to `CHASGB2LXXX`, while the corresponding SGD cashflow was updated?

## Evidence

Case 5 records:

```text
SGD SSI: 47726687
SGO SSI: 47726687_SGO
SGD cashflow: M01758865047
SGO cashflow: M01758865054
Amendment: IRVTUS3NIBK → CHASGB2LXXX
```

The SGD cashflow reflected the amendment. The SGO update event was received, but the SGO cashflow did not reflect the new value. The source describes this as a BAU issue and indicates that a ticket would be logged.

## Required resolution

Confirm:

- The event producer and consumer for SGO SSI amendments;
- Whether the SGO event payload differs from the SGD payload;
- The cashflow refresh eligibility and matching key;
- Whether the issue is limited to replicated historic SSIs;
- The BAU ticket number, owner, remediation, and regression evidence.

Until resolved, SGD amendment behavior must not be generalized to SGO cashflows.
