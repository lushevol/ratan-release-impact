---
type: query
title: Is the LMS Entity Filter Fully Removed for All Entities?
created: 2026-08-24
updated: 2026-08-24
tags: [lms, entity-filter, ratan, eligibility, philip-fcu]
related: [lms, ratan, lms-cashflow-feed-eligibility, lms-feed-entity-filter-before-and-after]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/LMS Feed.md"]
---
# Is the LMS Entity Filter Fully Removed for All Entities?

The later requirement states that Ratan must remove the entity filter and send all entities to LMS. However, three pieces of evidence do not align:

1. The user cases still require booking-entity membership in the former 16-entity list.
2. The later change table changes the listed entities from `No` to `Yes`.
3. `PHILIP FCU` is separately marked `No`, with no FMID or branch code.

The current policy should be confirmed as either:

- all entities, including `PHILIP FCU`;
- all entities except `PHILIP FCU`; or
- all entities subject to a revised, centrally maintained exclusion policy.

The user cases should then be updated so that their preconditions match the effective implementation.