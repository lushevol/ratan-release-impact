---
type: query
title: Is Grouping Management Service the Same as Group Service?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, service-identity, grouping-management, verification]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--27--1wtl90t, grouping-management-service, group-service, grouping-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Grouping Management Service.md"]
---
# Is Grouping Management Service the Same as Group Service?

## Question

Does **Grouping Management Service** refer to the same component as [[entities/group-service]], or are they separate services or architectural layers?

## Current evidence

The available source body is missing. The only evidence is the filename `Grouping Management Service.md` and its location in the Cash Settlement performance technical-design folder.

The supplied wiki index contains [[entities/group-service]] and [[entities/grouping-blotter]], but does not establish an alias relationship with Grouping Management Service.

## Resolution criteria

Resolve this question by confirming:

- Official service names and repository or deployment identifiers.
- Ownership and service boundaries.
- API or event contracts.
- Relationship to the Grouping Blotter.
- Whether performance findings in the source apply to Group Service, Grouping Management Service, or both.

Until confirmed, keep [[entities/grouping-management-service]] separate from [[entities/group-service]].