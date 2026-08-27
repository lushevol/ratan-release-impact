---
type: query
title: Who Owns Retention for event_record and event_history?
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, data-ownership, data-retention, capacity-management]
related: [ratanone, cash-settlement-database-retention-and-housekeeping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE DB  Excessive growth in database space.md"]
---
# Who Owns Retention for event_record and event_history?

`ratanone.event_record` is listed at 266,549 MB and `ratanone.event_history` at 126,773 MB. The source leaves both the checker and housekeeping-logic fields blank.

Together, these tables represent 393,322 MB of the inventory. Their size makes unassigned ownership and undefined retention treatment a material operational gap.

## Resolution needed

Assign an accountable owner for each schema-qualified table and determine:

- data producers and consumers;
- audit, reconciliation, and debugging dependencies;
- retention, deletion, truncation, or archival requirements;
- approval authority and operational implementation controls.

No deletion or retention policy should be inferred from the policies proposed for the `act_hi_*` tables.