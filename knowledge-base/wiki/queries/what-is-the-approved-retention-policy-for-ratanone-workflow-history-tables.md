---
type: query
title: What Is the Approved Retention Policy for ratanone Workflow-History Tables?
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, workflow-history, data-retention, truncation, approval]
related: [ratanone, cash-settlement-database-retention-and-housekeeping, chen-yang3]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE DB  Excessive growth in database space.md"]
---
# What Is the Approved Retention Policy for ratanone Workflow-History Tables?

The source proposes an initial truncation followed by monthly truncation for:

- `ratanone.act_hi_detail` — 344,625 MB
- `ratanone.act_hi_varinst` — 135,739 MB
- `ratanone.act_hi_actinst` — 93,896 MB

The documented checker is [[chen-yang3]], but the source does not establish that the proposal has been approved.

## Resolution needed

Confirm whether each table may be truncated and document:

- audit, compliance, and workflow-platform retention requirements;
- process recovery, incident investigation, and reporting dependencies;
- backup and rollback procedures;
- execution ownership, schedule, monitoring, and failure handling.

The source also marks `act_ge_bytearray` and `act_ru_variable` as “Not required at present”; clarify whether that means no current cleanup action or no retention requirement.