---
type: comparison
title: LMS Feed Entity Filter Before and After
created: 2026-08-24
updated: 2026-08-24
tags: [lms, entity-filter, ratan, migration, requirements]
related: [lms, ratan, lms-cashflow-feed-eligibility, is-the-lms-entity-filter-fully-removed-for-all-entities]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/LMS Feed.md"]
---
# LMS Feed Entity Filter Before and After

| Aspect | Original design | Later requirement |
| --- | --- | --- |
| Ratan entity policy | Excluded a hard-coded list of booking entities | Remove the entity filter and send all entities to LMS |
| Affected entities | Listed entities were marked `No`; `Other Manual Entities` was `Yes` | Listed entities changed from `No` to `Yes`; `Other Manual Entities` remains `Yes` |
| Message template | Existing SCBML template | Unchanged |
| Change reference | Historical behavior | ADO Story `10917020`, dated in the 2025-10-28 change table |
| User-case wording | Required membership in the former 16-entity list | Still uses the former wording and is therefore stale or incomplete |
| Exception status | `PHILIP FCU` did not appear in the original list | Later table marks it `No` without FMID or branch code |

## Interpretation

The later requirement should be treated as the current design for ordinary entity filtering, but it does not clearly explain whether `PHILIP FCU` is an intentional exception or an unfinished migration row. The user cases should be updated to reflect the effective policy.