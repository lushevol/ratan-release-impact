---
type: concept
title: Cash Settlement Service Landscape
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, service-landscape, microservices, architecture]
related: [cash-settlement-platform, what-do-common-bau-and-cn-mean-in-the-ratan-service-landscape, ratan, orchestration, query-service, cashflow-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design.md"]
---
# Cash Settlement Service Landscape

The source partitions the Cash Settlement Platform inventory into `Frontend`, `Common`, `BAU`, and `CN` classifications.

The `Common` set includes shared capabilities such as authentication, BFFs, an API gateway, configuration, discovery, messaging, static data, and integration ambassadors. The `BAU` set contains RatanOne cashflow, exception, query, settlement orchestration, stamping, SWIFT MX conversion, suppression, and trade services. The `CN` set contains Cash Settlement services for netting, orchestration, query, SSI stamping, lifecycle, exceptions, MXG cashflow adaptation, rules, and group management.

The labels describe an inventory grouping only. The source does not define whether `Common`, `BAU`, and `CN` represent ownership, geography, deployment scope, product generation, migration state, or another boundary. It also supplies no service responsibilities despite including a Responsibility column. Those gaps prevent reliable inference of service ownership, dependencies, and failure boundaries.

Resolve the classifications and service relationships through [[what-do-common-bau-and-cn-mean-in-the-ratan-service-landscape]].