---
type: entity
title: ES Static-Data Layer
created: 2026-08-23
updated: 2026-08-23
tags: [ES, static-data, SSI, replication, SGO, FMRP]
related: [sgo-ssi-replication, ratan, ssi-refresh-exception-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/FMRP SGO Testing.md"]
---
# ES Static-Data Layer

## Role in the testing record

`ES` is the target layer identified for replication of existing `SGD` SSIs as `SGO` records during the FMRP go-live.

The source does not expand the name `ES` or define whether it is a system, service, datastore, or static-data domain. This page therefore uses the neutral term “static-data layer.”

## Observed relationship

The tested flow is:

```text
Existing SGD SSI
→ Replication into ES
→ SGO SSI record
→ SGO cashflow auto-stamping in RATAN
```

The source reports that SGO cashflows could receive replicated SSIs. It also reports a defect where an SGO update event was received after amendment but the SGO cashflow did not reflect the changed SSI value.

## Open identification point

The official product or system name for `ES`, its event contract, and its ownership are not specified in the source. These details should be confirmed before treating this page as a fully identified system entity.
